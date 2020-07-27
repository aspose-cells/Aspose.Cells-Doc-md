+++
title = "Public API Changes in Aspose.Cells 8.8.0" 
description = "" 
weight = 12312 
+++

Aspose.Cells for Java : Public API Changes in Aspose.Cells 8.8.0  

# Aspose.Cells for Java : Public API Changes in Aspose.Cells 8.8.0


This document describes the changes to the Aspose.Cells API from version 8.7.2 to 8.8.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Get Cell References for External Connection

Aspose.Cells for Java 8.8.0 has exposed the following new properties that are helpful in retrieving the target & output cell references for external connections stored in the spreadsheet.

1.  `QueryTable.ConnectionId`: Gets the connection Id of the query table.
2.  `ExternalConnection.Id`: Gets the Id of the external connection.
3.  `ListObject.QueryTable`: Gets the linked QueryTable.

For more details on this feature, please review the detailed article on [Find Query Tables and List Objects related to External Data Connections](http://www.aspose.com/docs/display/cellsjava/Find+Query+Tables+and+List+Objects+related+to+External+Data+Connections)

### Added HTMLLoadOptions.KeepPrecision Property

Aspose.Cells for Java 8.8.0 has added the `HTMLLoadOptions.KeepPrecision` property in order to control the conversion of long numeric values to exponential notation while importing HTML files. By default, any value longer than 15 digits gets converted to exponential notation if the data is being imported from HTML string or file. However, now the users can control this behaviour with the help of `HTMLLoadOptions.KeepPrecision` property. If the said property is set to true, the values will be imported as they are in the source.

For more details on this feature, please review the detailed article on [Avoid the Conversion of Large Numeric Values to Exponential Notation](http://www.aspose.com/docs/display/cellsjava/Avoid+exponential+notation+of+large+numbers+while+importing+from+Html)

Following is the simple usage scenario.

**Java**

{{< code lang="java" >}}
//Sample Html containing large number with digits greater than 15
String html = "<html>"
		+ "<body>"
		+ "<p>1234567890123456</p>"
		+ "</body>"
		+ "</html>";

//Convert Html to byte array
byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true
HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);
loadOptions.setKeepPrecision(true);

//Convert byte array into stream
java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options
Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns
worksheet.autoFitColumns();

//Save the workbook
workbook.save(dataDir + "output.xlsx", SaveFormat.XLSX);
{{< /code >}}

### Added HTMLLoadOptions.DeleteRedundantSpaces Property

Aspose.Cells for Java 8.8.0 has exposed the `HTMLLoadOptions.DeleteRedundantSpaces` property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The `HTMLLoadOptions.DeleteRedundantSpaces` property has the default value as false that means, all extra spaces will be preserved and imported to the `Workbook` object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

For more details on this feature, please review the detailed article on [Delete Redundant Spaces from HTML](http://www.aspose.com/docs/display/cellsjava/Delete+redundant+spaces+after+line+break+while+importing+Html)

Simple usage scenario looks as follow.

**Java**

{{< code lang="java" >}}
//Sample Html containing redundant spaces after <br> tag
String html = "<html>"
		+ "<body>"
			+ "<table>"
				+ "<tr>"
					+ "<td>"
						+ "<br>    This is sample data"
						+ "<br>    This is sample data"
						+ "<br>    This is sample data"
					+ "</td>"
				+ "</tr>"
			+ "</table>"
		+ "</body>"
	+ "</html>";

//Convert Html to byte array
byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true
HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);
loadOptions.setDeleteRedundantSpaces(true);

//Convert byte array into stream
java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options
Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns
worksheet.autoFitColumns();

//Save the workbook
workbook.save(dataDir + "output-" + loadOptions.getDeleteRedundantSpaces() + ".xlsx", SaveFormat.XLSX);
{{< /code >}}

### Added Style.QuotePrefix Property

Aspose.Cells for Java 8.8.0 has exposed the `Style.QuotePrefix` property in order to detect if a cell value starts with a single quote symbol.

For more details on this feature, please review the detailed article on [Detect Single Quote at the Start of Cell Value](http://www.aspose.com/docs/display/cellsjava/Find+if+the+cell+value+starts+with+single+quote+mark)

Simple usage scenario looks as follow.

**Java**

{{< code lang="java" >}}
//Create an instance of workbook
Workbook workbook = new Workbook();

//Access first worksheet from the collection
Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells A1 and A2
Cell a1 = worksheet.getCells().get("A1");
Cell a2 = worksheet.getCells().get("A2");

//Add simple text to cell A1 and text with quote prefix to cell A2
a1.putValue("sample");
a2.putValue("'sample");

//Print their string values, A1 and A2 both are same
System.out.println("String value of A1: " + a1.getStringValue());
System.out.println("String value of A2: " + a2.getStringValue());

//Access styles of cells A1 and A2
Style s1 = a1.getStyle();
Style s2 = a2.getStyle();

System.out.println();

//Check if A1 and A2 has a quote prefix
System.out.println("A1 has a quote prefix: " + s1.getQuotePrefix());
System.out.println("A2 has a quote prefix: " + s2.getQuotePrefix());
{{< /code >}}

## Obsoleted APIs

### Obsoleted LoadOptions.ConvertNumericData Property

Aspose.Cells 8.8.0 has marked the `LoadOptions.ConvertNumericData` property as obsoleted. Please use the corresponding property from the `HTMLLoadOptions` or `TxtLoadOptions` classes.

