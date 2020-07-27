+++
title = "Public API Changes in Aspose.Cells 8.4.0" 
description = "" 
weight = 12299 
+++

Aspose.Cells for Java : Public API Changes in Aspose.Cells 8.4.0  

# Aspose.Cells for Java : Public API Changes in Aspose.Cells 8.4.0


This document describes the changes to the Aspose.Cells API from version 8.3.2 to 8.4.0 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](https://docs2.aspose.com/cells/java/developerguide/migratingfromearlierversionsofasposecells/public+api+changes+in+aspose.cells+8.4.0) and [removed classes etc.](https://docs2.aspose.com/cells/java/developerguide/migratingfromearlierversionsofasposecells/public+api+changes+in+aspose.cells+8.4.0), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Mechanism to Modify the VBA/Macro Code in Spreadsheets

In order to provide the feature of [VBA/Macro Code Manipulation](https://docs2.aspose.com/cells/java/developerguide/workbookvbaproject/modifying+vba+or+macro+code+using+aspose.cells), the Aspose.Cells for Java 8.4.0 has exposed a series of new classes and properties in the `com.aspose.cells.Vba` package. A few of the important details of these new classes are as follow.

*   `VbaProject` class can be used to fetch the VBA project from a given spreadsheet.
*   `VbaModuleCollection` class represents the collection of VBA modules that are part of a given `VbaProject`.
*   `VbaModule` class represents a single module from the `VbaModuleCollection`.

The following code snippet shows how to dynamically modify the VBA code segments.

**Java**

{{< code lang="java" >}}
Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code
VbaModuleCollection modules = workbook.getVbaProject().getModules();

for(int i=0; i < modules.getCount(); i++)
{
	VbaModule module = modules.get(i);
    String code = module.getCodes();

    //Replace the original message with the modified message
    if (code.contains("This is test message."))
    {
        code = code.replace("This is test message.", "This is Aspose.Cells message.");
        module.setCodes(code);
    }
}

//Save the output Excel file
workbook.save("output.xlsm");
{{< /code >}}

### Ability to Remove Pivot Table

Aspose.Cells for Java 8.4.0 has exposed two methods for the `PivotTableCollection` to provide the feature of Pivot Table removal from a given spreadsheet. The details of aforesaid methods are as follow.

*   `PivotTableCollection.remove` method accepts an object of PivotTable, and removes it from the collection.
*   `PivotTableCollection.removeAt` method accepts a zero index based integer value and removes the particular PivotTable from the collection.

The following code snippet shows how to remove the PivotTable using both above mentioned methods.

**Java**

{{< code lang="java" >}}
//Create workbook object from source Excel file
Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first pivot table object
PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Remove pivot table using pivot table object
worksheet.getPivotTables().remove(pivotTable);

//Remove pivot table using pivot table position
worksheet.getPivotTables().removeAt(0);

//Save the workbook
workbook.save("output.xlsx");
{{< /code >}}

### Support for Different Pivot Table Layouts

Aspose.Cells for Java 8.4.0 provides the support for different predefined layouts for Pivot Tables. In order to provide this feature, the Aspose.Cells APIs have exposed three methods for the `PivotTable` class as detailed below.

*   `PivotTable.showInCompactForm` method renders the Pivot Table in Compact layout.
*   `PivotTable.showInOutlineForm` method renders the Pivot Table in Outline layout.
*   `PivotTable.showInTabularForm` method renders the Pivot Table in Tabular layout.

It is important to call the `PivotTable.refreshData` & `PivotTable.calculateData` after setting any of the above mentioned layouts.

The following sample code sets different layouts for a Pivot Table and stores the result on disc.

**Java**

{{< code lang="java" >}}
//Create workbook object from source excel file
Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table
PivotTable pivotTable = worksheet.getPivotTables().get(0);

//1 - Show the pivot table in compact form
pivotTable.showInCompactForm();

//Refresh the pivot table
pivotTable.refreshData();
pivotTable.calculateData();

//Save the output
workbook.save("CompactForm.xlsx");

//2 - Show the pivot table in outline form
pivotTable.showInOutlineForm();

//Refresh the pivot table
pivotTable.refreshData();
pivotTable.calculateData();

//Save the output
workbook.save("OutlineForm.xlsx");

//3 - Show the pivot table in tabular form
pivotTable.showInTabularForm();

//Refresh the pivot table
pivotTable.refreshData();
pivotTable.calculateData();

//Save the output
workbook.save("TabularForm.xlsx");
{{< /code >}}

### Class TxtLoadStyleStrategy & Property TxtLoadOptions.LoadStyleStrategy Added

Aspose.Cells for Java 8.4.0 has exposed the `TxtLoadStyleStrategy` class and `TxtLoadOptions.LoadStyleStrategy` property in order to specify the strategy to format the parsed values while converting string value to number or date time.

### Method DataBar.ToImage Added

With the release of v8.4.0, the Aspose.Cells API has provided the `DataBar.toImage` method to save the conditionally formatted DataBar in image format. The {DataBar.toImage}} method accepts two parameters as detailed below.

*   The first parameter is of type `com.aspose.cells.Cell` on which conditional formatting has been applied.
*   The second parameter is of type `com.aspose.cells.rendering.ImageOrPrintOptions` in order to set different parameters of the resultant image.

The following sample code demonstrates the use of `DataBar.toImage` method to render the DataBar in image format.

**Java**

{{< code lang="java" >}}
//Create workbook object from source excel file
Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cell which contains conditional formatting databar
Cell cell = worksheet.getCells().get("C1");

//Get the conditional formatting of the cell
FormatConditionCollection fcc = cell.getFormatConditions();

//Access the conditional formatting databar
DataBar dbar = fcc.get(0).getDataBar();

//Create image or print options
ImageOrPrintOptions opts = new ImageOrPrintOptions();
opts.setImageFormat(ImageFormat.getPng());

//Get the image bytes of the databar
byte[] imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk
FileOutputStream out = new FileOutputStream("databar.png");
out.write(imgBytes);
out.close();
{{< /code >}}

### Property Border.ThemeColor Added

Aspose.Cells APIs allow to extract theme related data from the spreadsheets. With the release of Aspose.Cells for Java 8.4.0, the API has exposed the `Border.ThemeColor` property that can be used to retrieve the theme color attributes of `Cell` borders.

### Property DrawObject.ImageBytes Added

Aspose.Cells for Java 8.4.0 has exposed the `DrawObject.ImageBytes` property to get the image data from Chart or Shape.

### Property HtmlSaveOptions.ExportBogusRowData Added

Aspose.Cells for Java 8.4.0 has provided the {HtmlSaveOptions.ExportBogusRowData}} property. The Boolean type property determines if API will inject bogus bottom row data while exporting spreadsheet to HTML format.

The default value is `true`.

The following sample code illustrates the use of aforesaid property.

**Java**

{{< code lang="java" >}}
//Create an object of HtmlSaveOptions class
HtmlSaveOptions options = new HtmlSaveOptions();
//Set the ExportBogusRowData to true
options.ExportBogusRowData = true;

//Create workbook object from source excel file
Workbook workbook = new Workbook("source.xlsx");

//Save the workbook
workbook.save("output.xlsx");
{{< /code >}}

### Property HtmlSaveOptions.CellCssPrefix Added

Newly added property `HtmlSaveOptions.CellCssPrefix` allows to set the prefix for the CSS files while exporting spreadsheets to HTML format.

The default value is "" (empty string).

## Obseleted APIs

### Methods Cells.getCellByIndex & Row.getCellByIndex Obsoleted

Use the `getEnumerator` method to iterate all cells instead.

### Property DrawObject.Image Obsoleted

Use the `DrawObject.ImageBytes` property to get image data instead.

