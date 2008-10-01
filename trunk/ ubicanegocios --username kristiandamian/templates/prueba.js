/*
	These are global variables that define
	how many items to view at once (itemsPerPage),
	and our current position (curPos).

	"itemsPerPage" is an accurate descriptor only
	within the context of the application, since
	we are not actually browsing "pages".
*/

itemsPerPage = 2;
curPos = 0;

/*
	The next code block is the jQuery implementation
	of the XMLHttpRequest object. The outer function
	specifies that when the page loads we want to
	execute a function:

	$(function() {});

	Now within that function, make a request for an
	XML file, and upon success, execute another
	function. The data we get back is assigned to
	"xmlData". This is only available within the
	scope of this function. By assigning it to
	"xmlDataSet", we can now use the XML data
	throughout the application. Now we call the
	"browseXML()" function, which will manage
	our browse functionality.

	NOTE: In a production environment, you may want
	to account for any instance when the request
	for the XML fails. Please see the jQuery
	documentation on the $.ajax() object.
*/

$(function() {
	$.ajax({
		type: "GET",
		url: "books.xml",
		dataType: "xml",
		success: function(xmlData)
		{
			xmlDataSet = xmlData;
			browseXML();
		}
	});
});

function browseXML()
{
/*
	In jQuery, you can choose an XML data source, and
	then select the name of the node elements you want
	to grab. The results can be assigned to a variable,
	which can further be refined if needed. This is
	demonstrated with the "resultSetLength" variable.

	"strToAppend" will be the sum of our HTML that
	will eventually (re)populate our "widget" DIV when
	a user browses.
*/
	resultSetLength = $("book",xmlDataSet).length;
	strToAppend = "<p>";
/*
	Determine what set of matched results the user is
	currently browsing. Because we started "curPos" at 0,
	we must add 1 to get the actual current position.
*/
	if (curPos + itemsPerPage > resultSetLength)
	{
		showingThrough = resultSetLength;
	}
	else
	{
		showingThrough = parseInt(curPos + itemsPerPage);
	}
	strToAppend += "Showing <b>" + parseInt(curPos + 1) + "</b> through <b>" + showingThrough + "</b> of <b>" + resultSetLength + "</b>";
	strToAppend += " books from the New York Times&reg; Best Sellers List"
	strToAppend += "</p>";
	strToAppend += "<p>Show Me:&nbsp; ";
/*
	Let's give the user a preference for how many results
	they want to view per page. When the user clicks the link,
	we modify the value of "itemsPerPage" to accomplish this task.
	Then we send the user back to the beginning of the result set,
	and call the "browseXML()" function again.
*/
	strToAppend += "<a href='#' onclick='itemsPerPage = 2;curPos = 0;browseXML();return false;'>2 at a time</a> &nbsp;|&nbsp; ";
	strToAppend += "<a href='#' onclick='itemsPerPage = 3;curPos = 0;browseXML();return false;'>3 at a time</a> &nbsp;|&nbsp; ";
	strToAppend += "<a href='#' onclick='itemsPerPage = 4;curPos = 0;browseXML();return false;'>4 at a time</a> &nbsp;|&nbsp; ";
	strToAppend += "<a href='#' onclick='itemsPerPage = " + resultSetLength + ";curPos = 0;browseXML();return false;'>All</a></p>";
	strToAppend += "<p>";
/*
	If the user wants to view all the results, then we
	don't want to give them the capability to browse.
	Show all the results, or display the navigation
	for browsing depending on where the user is at
	within the result set.
*/
	if (itemsPerPage != resultSetLength)
	{
		if (curPos == 0) // First page. Go forward only.
		{
			strToAppend += "<a href='#' onclick='curPos += " + itemsPerPage + ";browseXML();return false;'>Next Items &raquo;</a>";
		}
		if (curPos > 0 && parseInt(curPos + itemsPerPage) < resultSetLength) // Somewhere inbetween.
		{
			strToAppend += "<a href='#' onclick='curPos -= " + itemsPerPage + ";browseXML();return false;'>&laquo; Previous Items</a>";
			strToAppend += " &nbsp;|&nbsp; ";
			strToAppend += "<a href='#' onclick='curPos += " + itemsPerPage + ";browseXML();return false;'>Next Items &raquo;</a>";
		}
		if (parseInt(curPos + itemsPerPage) >= resultSetLength) // Last page. Go back only.
		{
			strToAppend += "<a href='#' onclick='curPos -= " + itemsPerPage + ";browseXML();return false;'>&laquo; Previous Items</a>";
		}
	}

	strToAppend += "</p>";
	strToAppend += "<p> - - - </p>";
/*
	This is the real meat of the jQuery functionality.
	We are performing 3 major tasks:

	1.) Grab each "title" node from our XML data source that
		falls below a certain index. The ":lt" is the expression
		that performs this task.
	2.) Now of those title nodes, filter out those that are
	    greater than a certain index. This will give us our
	    new result set, which is displayed to the user with
		"Showing X through Y of Z". The ":gt" expression is
		used in conjunction with the "filter()" method to
		accomplish this task.
	3.) For each set of results we refined, we now want to
	    execute a function. We know we need the "author",
		"publisher", and the "ISBN" for our book, but we
		only searched for "title". With the "each()" method
		we have access to the index (i), just like in a JavaScript
		"for loop". So we can get each one of those nodes
		that fall at the same index as our "title" nodes.
		However, we always start our results array at 0,
		so we want to add our current position to that
		in order to get the proper node. We use the ":eq"
		expression to accomplish this task.
*/
	$("title:lt(" + parseInt(curPos + itemsPerPage) + ")",xmlDataSet).filter(":gt(" + parseInt(curPos - 1) + ")").each(function(i) {
		strToAppend += "<p><strong>" + $(this).text() + "</strong><br />";
		strToAppend += "by " + $("author:eq(" + parseInt(curPos + i) + ")",xmlDataSet).text() + "</p>";
		strToAppend += "<p>Publisher: " + $("publisher:eq(" + parseInt(curPos + i) + ")",xmlDataSet).text() + "<br />";
		strToAppend += "ISBN-10: " + $("isbn:eq(" + parseInt(curPos + i) + ")",xmlDataSet).text();
		strToAppend += "</p>";
	});

	strToAppend += "<p> - - - </p>";
/*
	Populate our DIV with the HTML we have constructed.
*/
	$("#widget").html(strToAppend);
}
/*
	Obfuscated, and without comments, this script would
	probably only be about 2 KB.
*/