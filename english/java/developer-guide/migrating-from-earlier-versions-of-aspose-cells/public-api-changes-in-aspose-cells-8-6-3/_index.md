---
title: Public API Changes in Aspose.Cells 8.6.3
type: docs
weight: 230
url: /java/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.6.2 to 8.6.3 that may be of interest to module/application developers. It includes not only new and updated public methods, added classes, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for HTML Parsing while Importing Data**
This release of Aspose.Cells for Java API has exposed the ImportTableOptions.setHtmlString attribute which directs the API to parse the HTML tags while importing data onto the Worksheet and set the parsed result as cell value. Please note, Aspose.Cells APIs already provide the Cell.setHtmlString attribute to perform this task for a single cell, however, while importing data in bulk, the ImportTableOptions.setHtmlString attribute (when set to true) tries to parse all the supported HTML tags and sets the parsed results to the corresponding cells.

Here is the simplest usage scenario.

**Java**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Added Workbook.createBuiltinStyle Method**
Aspose.Cells for Java 8.6.3 has exposed the Workbook.createBuiltinStyle method that can be used to create an object of the Style class that corresponds to one of the [built-in styles offered by the Excel application](/cells/java/using-built-in-styles/). The Workbook.createBuiltinStyle method accepts a constant from the enumeration BuiltinStyleType. Please note, with previous releases of the Aspose.Cells APIs, same task could be accomplished via StyleCollection.createBuiltinStyle method but as the recent releases of Aspose.Cells APIs have removed the StyleCollection class therefore the newly exposed Workbook.createBuiltinStyle method can be considered as an alternative approach to achieve the same.

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Added LoadDataOption.OnlyVisibleWorksheet Property**
Aspose.Cells for Java 8.6.3 has exposed the LoadDataOption.OnlyVisibleWorksheet property which upon setting to true will influence the loading mechanism of Aspose.Cells for Java API, as a result only visible worksheets from a given spreadsheet will be loaded.

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadDataOption

LoadDataOption loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.setOnlyVisibleWorksheet(true);

//Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.setLoadDataOptions(loadDataOptions);

//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

Workbook book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **Obsoleted APIs**
### **Obsoleted Worksheet.copyConditionalFormatting Method**
As an alternative to the Worksheet.copyConditionalFormatting method, it is advised to use any of the Cells.copyRows or Range.copy methods.
### **Obsoleted Cells.End Property**
Please use Cells.LastCell property as an alternative to the Cells.End property.
{{< app/cells/assistant language="java" >}}