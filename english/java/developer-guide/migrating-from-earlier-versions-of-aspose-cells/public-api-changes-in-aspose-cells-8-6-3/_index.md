---
title: Public API Changes in Aspose.Cells 8.6.3
type: docs
weight: 230
url: /java/public-api-changes-in-aspose-cells-8-6-3/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.6.2 to 8.6.3 that may be of interest to module/application developers. It includes not only new and updated public methods and added classes, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 

## **Added APIs**

### **Support for HTML Parsing while Importing Data**

This release of Aspose.Cells for Java API has exposed the `ImportTableOptions.setHtmlString` attribute, which directs the API to parse HTML tags while importing data onto the worksheet and sets the parsed result as the cell value. Please note, Aspose.Cells APIs already provide the `Cell.setHtmlString` attribute to perform this task for a single cell; however, when importing data in bulk, the `ImportTableOptions.setHtmlString` attribute (when set to true) tries to parse all the supported HTML tags and sets the parsed results to the corresponding cells.

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

Aspose.Cells for Java 8.6.3 has exposed the `Workbook.createBuiltinStyle` method that can be used to create an object of the `Style` class that corresponds to one of the [built‑in styles offered by the Excel application](/cells/java/using-built-in-styles/). The `Workbook.createBuiltinStyle` method accepts a constant from the enumeration `BuiltinStyleType`. Please note, with previous releases of the Aspose.Cells APIs, the same task could be accomplished via the `StyleCollection.createBuiltinStyle` method, but as recent releases of Aspose.Cells APIs have removed the `StyleCollection` class, the newly exposed `Workbook.createBuiltinStyle` method can be considered an alternative approach to achieve the same.

Following is a simple usage scenario.

**Java**

{{< highlight csharp >}}
 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built‑in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);
{{< /highlight >}}

### **Added LoadDataOption.OnlyVisibleWorksheet Property**

Aspose.Cells for Java 8.6.3 has exposed the `LoadDataOption.OnlyVisibleWorksheet` property, which, upon setting to true, influences the loading mechanism of the Aspose.Cells for Java API; as a result, only visible worksheets from a given spreadsheet will be loaded.

Following is a simple usage scenario.

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

As an alternative to the `Worksheet.copyConditionalFormatting` method, it is advised to use any of the `Cells.copyRows` or `Range.copy` methods.

### **Obsoleted Cells.End Property**

Please use the `Cells.LastCell` property as an alternative to the `Cells.End` property.

{{< app/cells/assistant language="java" >}}
