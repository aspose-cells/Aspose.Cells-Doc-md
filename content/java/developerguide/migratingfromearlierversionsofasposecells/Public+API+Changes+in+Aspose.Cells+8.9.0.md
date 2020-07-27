+++
title = "Public API Changes in Aspose.Cells 8.9.0" 
description = "" 
weight = 12316 
+++

Aspose.Cells for Java : Public API Changes in Aspose.Cells 8.9.0  

# Aspose.Cells for Java : Public API Changes in Aspose.Cells 8.9.0


This document describes the changes to the Aspose.Cells API from version 8.8.3 to 8.9.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Added HtmlSaveOptions.DefaultFontName Property

Aspose.Cells for Java 8.9.0 has exposed the `DefaultFontName` property for the `HtmlSaveOptions` class that allows to specify the default font name while rendering spreadsheets to HTML format. The default font will be used only when the font of style does not exist. The default value of `HtmlSaveOptions.DefaultFontName` property is null that means, Aspose.Cells for Java API will use the universal font which has the same family with the original font.

For more details on this feature, please review the article on [Setting Default Font for Rendering Spreadsheets to HTML Format](http://www.aspose.com/docs/display/cellsjava/Set+Default+Font+while+rendering+spreadsheet+to+HTML).

Following is the simple usage scenario.

**Java**

{{< code lang="java" >}}
//Create an instance of HtmlSaveOptions
HtmlSaveOptions options = new HtmlSaveOptions();
//Set default font name for Html rendering
options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook
Workbook book = new Workbook(dir + "sample.xlsx");
//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions
book.save(dir + "output.html", options);
{{< /code >}}

### Added ImageOrPrintOptions.DefaultFont Property

Aspose.Cells for Java 8.9.0 allows to set the default font name for the `ImageOrPrintOptions` class by exposing the `DefaultFont` property. The said property can be used when Unicode characters in the spreadsheet are not set with correct font in cell style therefore such characters may appear as blocks in the resultant images.

Set the `DefaultFont` property to MingLiu or MS Gothic to show Unicode characters. If the said property is not set, Aspose.Cells will use the system's default font to show Unicode characters.

For more details on this feature, please review the article on [Setting Default Font for Rendering Spreadsheets in Image Formats](http://www.aspose.com/docs/display/cellsjava/Set+Default+Font+while+rendering+spreadsheet+to+images).

Following is the simple usage scenario.

**Java**

{{< code lang="java" >}}
//Create an instance of ImageOrPrintOptions
ImageOrPrintOptions options = new ImageOrPrintOptions();
//Set default font name for image rendering
options.setDefaultFont("Arial");

//Load a spreadsheet in an instance of Workbook
Workbook book = new Workbook(dir + "sample.xlsx");
//Access the worksheet to be rendered
Worksheet sheet = book.getWorksheets().get(0);

//Create an instance of SheetRender
SheetRender render = new SheetRender(sheet, options);
//Save spreadsheet to image
render.toImage(0, dir + "output.png");
{{< /code >}}

### Added PivotTable.Excel2003Compatible Property

Aspose.Cells for Java API has exposed the Boolean type `Excel2003Compatible` property for the `PivotTable` class which allows to specify if the `PivotTable` is Excel 2003 compatible for refreshing purposes. The default value of `Excel2003Compatible` property is true, that means a string must be less than or equal to 255 characters. If the string is greater than 255 characters, it will be truncated. If false, the aforementioned restriction will not be imposed.

For more details on this feature, please review the article on [Compatibility for Excel 2003 for Refreshing Pivot Tables](http://www.aspose.com/docs/display/cellsjava/Specify+whether+the+PivotTable+is+compatible+for+Excel2003+while+refreshing+PivotTable).

Following is the simple usage scenario.

**Java**

{{< code lang="java" >}}
//Load a spreadsheet in an instance of Workbook
Workbook book = new Workbook(dir + "sample.xlsx");

//Access the desired Pivot Table from the spreadsheet
PivotTable pivot = book.getWorksheets().get(0).getPivotTables().get(0);

//Set Excel 2003 compatibility to false
pivot.setExcel2003Compatible(false);

//Refresh & recalculate Pivot Table
pivot.refreshData();
pivot.calculateData();
{{< /code >}}

