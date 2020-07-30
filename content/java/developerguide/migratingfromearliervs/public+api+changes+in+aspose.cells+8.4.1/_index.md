---
title : "Public API Changes in Aspose.Cells 8.4.1" 
description : "" 
weight : 12300 
toc : false
type: docs
url: /java/developerguide/migratingfromearliervs/public+api+changes+in+aspose.cells+8.4.1/
---

# Aspose.Cells for Java : Public API Changes in Aspose.Cells 8.4.1


This document describes the changes to the Aspose.Cells API from version 8.4.0 to 8.4.1 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](https://docs2.aspose.com/cells/java/developerguide/migratingfromearliervs/public+api+changes+in+aspose.cells+8.4.1) and [removed classes etc.](https://docs2.aspose.com/cells/java/developerguide/migratingfromearliervs/public+api+changes+in+aspose.cells+8.4.1), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Mechanism to Modify Database Connection

The `com.aspose.cells.ExternalConnection` class already contained the method & properties that could be used to inspect the database connection details stored in a spreadsheet. Most of the properties associated with `ExternalConnection` class were read only until the release of Aspose.Cells for Java 8.4.1. With this release, the API has provided the support to manipulate the database connection settings as well.

The following code snippet shows how to dynamically modify database connection settings.

**Java**

{{< code lang="java" >}}
//Create workbook object
com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first data connection
com.aspose.cells.ExternalConnection conn = workbook.getDataConnections().get(0);

//Change a few properties
conn.setName("MyConnectionName");
conn.setOdcFile("MyDefaulConnection.odc");
conn.setConnectionDescription("Test Connection");
conn.setCredentials(com.aspose.cells.CredentialsMethodType.PROMPT);

//Save the workbook
workbook.save(output);
{{< /code >}}

Here are a few most important properties exposed by the {ExternalConnection}} class.

{{< table style="table-striped" >}}
|Property Name|Description|
|:----|:----|
|BackgroundRefresh|Indicates whether the connection can be refreshed in the background (asynchronously).  true if preferred usage of the connection is to refresh asynchronously in the background;  false if preferred usage of the connection is to refresh synchronously in the foreground.|
|ConnectionDescription|Specifies the user description for this connection|
|ConnectionId|Specifies The unique identifier of this connection.|
|Credentials|Specifies the authentication method to be used when establishing (or re-establishing) the connection.|
|IsDeleted|Indicates whether the associated workbook connection has been deleted. true if the  connection has been deleted; otherwise, false.|
|IsNew|True if the connection has not been refreshed for the first time; otherwise, false. This  state can happen when the user saves the file before a query has finished returning.|
|KeepAlive|True when the spreadsheet application should make efforts to keep the connection  open. When false, the application should close the connection after retrieving the  information.|
|Name|Specifies the name of the connection. Each connection must have a unique name.|
|OdcFile|Specifies the full path to external connection file from which this connection was  created. If a connection fails during an attempt to refresh data, and reconnectionMethod=1,  then the spreadsheet application will try again using information from the external connection file  instead of the connection object embedded within the workbook.|
|OnlyUseConnectionFile|Indicates whether the spreadsheet application should always and only use the  connection information in the external connection file indicated by the odcFile attribute  when the connection is refreshed. If false, then the spreadsheet application  should follow the procedure indicated by the reconnectionMethod attribute|
|Parameters|Gets ConnectionParameterCollection for an ODBC or web query.|
|ReConnectionMethod|Specify reconnectionMethod type|
|RefreshInternal|Specifies the number of minutes between automatic refreshes of the connection.|
|RefreshOnLoad|True if this connection should be refreshed when opening the file; otherwise, false.|
|SaveData|True if the external data fetched over the connection to populate a table is to be saved  with the workbook; otherwise, false.|
|SavePassword|True if the password is to be saved as part of the connection string; otherwise, False.|
|SourceFile|Used when the external data source is file-based. When a connection to such a data  source fails, the spreadsheet application attempts to connect directly to this file. May be  expressed in URI or system-specific file path notation.|
|SSOId|Identifier for Single Sign On (SSO) used for authentication between an intermediate  spreadsheetML server and the external data source.|
|Type|Specifies the data source type.|
{{< /table >}}

  

### Ability to Format Sub-String of DataLabels' Text

Aspose.Cells for Java 8.4.1 has exposed the `DataLabels.characters` method to retrieve an instance of `FontSetting` class that corresponds to the sub-string of a `ChartPoints.DataLabels`. In turn, the instance of `FontSetting` class can be used to format the sub-string of the DataLabels with different font settings & color.

The following code snippet shows how to use the `DataLabels.characters` method.

**Java**

{{< code lang="java" >}}
//Create a workbook from source Excel file
com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet
com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first chart inside the sheet
com.aspose.cells.Chart chart = worksheet.getCharts().get(0);

//Access the data label of first series first point
com.aspose.cells.DataLabels labels = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

//Set data label text
labels.setText("Rich Text Label");

//Set the font setting of the first 10 characters
com.aspose.cells.FontSetting settings = labels.characters(0, 10);
settings.getFont().setColor(com.aspose.cells.Color.getRed());
settings.getFont().setBold(true);

//Save the workbook
workbook.save(output);
{{< /code >}}

  

### Ability to Set Desired Image Dimensions for Spreadsheet & Chart Export

Aspose.Cells for Java 8.4.1 has exposed the `ImageOrPrintOptions.setDesiredSize` method to set the dimensions of the resultant image while exporting spreadsheets & charts to images. The `ImageOrPrintOptions.setDesiredSize` method accepts two integer type parameters, where first is the desired width and second is desired height.

The following code snippet shows how to set the desired dimensions while exporting worksheet to PNG.

**Java**

{{< code lang="java" >}}
com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet
com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions
com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();
//Set resultant image format
options.setImageFormat(com.aspose.cells.ImageFormat.getPng());

//Set desired dimensions as 400x400
options.setDesiredSize(400, 400);

//Render sheet to image
com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);
renderer.toImage(0, "output.png");
{{< /code >}}

Same method can also be used for converting charts to images.

  

### Rendering Comments to PDF

With the release of v8.4.1, the Aspose.Cells API has provided the `PageSetup.PrintComments` property & `PrintCommentsType` enumeration in order to facilitate the rendering of comments while converting spreadsheets to PDF format. The `PrintCommentsType` enumeration has the following constants.

*   `PrintCommentsType.PRINT_NO_COMMENTS`: Comments are not to be rendered.
*   `PrintCommentsType.PRINT_IN_PLACE`: Comments are to be rendered where they are placed.
*   `PrintCommentsType.PRINT_SHEET_END`: Comments are to be rendered at the end of worksheet.

The following sample code demonstrates the use of `PageSetup.PrintComments` property to render the comments using all possible `PrintCommentsType` enumeration values.

**Java**

{{< code lang="java" >}}
//Create an instance of workbook
com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet
com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Print no comments
worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_NO_COMMENTS);

//Save workbook in PDF format without comments
workbook.save("nocomments.pdf");

//Print the comments as displayed on sheet
worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_IN_PLACE);

//Save workbook in PDF format while rendering comments in place
workbook.save("printinplace.pdf");

//Print the comments at the end of sheet
worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_SHEET_END);

//Save workbook in PDF format while rendering comments at the end of worksheet
workbook.save("printsheetend.pdf");
{{< /code >}}

  

### Added Workbook.isLicensed Property

Aspose.Cells for Java 8.4.1 has exposed the `Workbook.isLicensed` which could be of great help in determining if the license has been successfully loaded or not. If you access this property before setting the license, it will return false and vise versa, however, the license should be valid.

The following sample code demonstrates the usage of `Workbook.isLicensed` property.

**Java**

{{< code lang="java" >}}
//Create workbook object before setting a license
com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook();

//Check if the license is loaded or not
if (!workbook.isLicensed())
{
	//Set license
	com.aspose.cells.License license = new com.aspose.cells.License();
	lic.SetLicense(licPath);
}
else
{
  //do process
}
{{< /code >}}

  

### Added ImageOrPrintOptions.SVGFitToViewPort Property

Aspose.Cells for Java 8.4.1 has exposed the `SVGFitToViewPort` property for the `ImageOrPrintOptions` class that can be used to turn on the viewBox attribute for the SVG file format while exporting spreadsheets or charts to SVG format. The default value of this property is false therefore the base XML for SVG file generated without setting the aforesaid property will not include the viewBox attribute.

The following sample code demonstrates the usage of `ImageOrPrintOptions.SVGFitToViewPort` property.

**Java**

{{< code lang="java" >}}
//Create workbook object from source file
com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet
com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions
com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();
//Set image format to SVG
options.setSaveFormat(com.aspose.cells.SaveFormat.SVG);
//Set the SVGFitToViewPort to true
options.setSVGFitToViewPort(true);

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions
com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);
renderer.toImage(0, "output.svg");
{{< /code >}}

## Obsoleted APIs

### Method Workbook.validateFormula Obsoleted

Use the `Cell.Formula` property to validate the formula.

