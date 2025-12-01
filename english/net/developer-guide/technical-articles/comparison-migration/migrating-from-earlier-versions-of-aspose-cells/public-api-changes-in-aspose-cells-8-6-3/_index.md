---
title: Public API Changes in Aspose.Cells 8.6.3
type: docs
weight: 220
url: /net/public-api-changes-in-aspose-cells-8-6-3/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.6.2 to 8.6.3 that may be of interest to module/application developers. It includes not only new and updated public methods, added classes, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for HTML Parsing while Importing Data**
This release of Aspose.Cells for .NET API has exposed the ImportTableOptions.IsHtmlString property which directs the API to parse the HTML tags while importing data onto the Worksheet and set the parsed result as cell value. Please note, Aspose.Cells APIs already provide the Cell.HtmlString to perform this task for a single cell, however, while importing data in bulk such as from a DataTable, the ImportTableOptions.IsHtmlString property (when set to true) tries to parse all the supported HTML tags and sets the parsed results to the corresponding cells.

Here is the simplest usage scenario.

**C#**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Added Workbook.CreateBuiltinStyle Method**
Aspose.Cells for .NET 8.6.3 has exposed the Workbook.CreateBuiltinStyle method that can be used to create an object of the Style class that corresponds to one of the [built-in styles offered by the Excel application](/cells/net/using-built-in-styles/). The Workbook.CreateBuiltinStyle method accepts a constant from the enumeration BuiltinStyleType. Please note, with previous releases of the Aspose.Cells APIs, same task could be accomplished via StyleCollection.CreateBuiltinStyle method but as the recent releases of Aspose.Cells APIs have removed the StyleCollection class therefore the newly exposed Workbook.CreateBuiltinStyle method can be considered as an alternative approach to achieve the same.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Added Cells.ImportGridView Method**
Aspose.Cells for .NET 8.6.3 has exposed an overloaded version of the Cells.ImportGridView that can now accept an instance of ImportTableOptions to give more control over the import process.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions & set its various properties

var importOptions = new ImportTableOptions();

importOptions.IsHtmlString = true;

importOptions.IsFieldNameShown = true;

//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **Added ImportTableOptions.ConvertGridStyle Property**
In reference the above mentioned enhancements, the latest version of Aspose.Cells for .NET API has also exposed the ImportTableOptions.ConvertGridStyle property. This Boolean type property allows the developers to control the appearance of the imported data, where setting the ImportTableOptions.ConvertGridStyle property to true indicates that the API will apply the style of the GridView to the cells where data has been imported.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set ConvertGridStyle property to true

importOptions.ConvertGridStyle = true;



//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **Property LoadDataOption.OnlyVisibleWorksheet Added**
Aspose.Cells for .NET 8.6.3 has exposed the LoadDataOption.OnlyVisibleWorksheet property which upon setting to true will influence the loading mechanism of Aspose.Cells for .NET API, as a result only visible worksheets from a given spreadsheet will be loaded. Please check the [detailed article](/cells/net/different-ways-to-open-files/) on this subject.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadDataOption

var loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.OnlyVisibleWorksheet = true;

//Create an instance of LoadOptions

var loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.LoadDataOptions = loadDataOptions;



//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

var book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **Obsoleted APIs**
### **Obsoleted Worksheet.CopyConditionalFormatting Method**
As an alternative to the Worksheet.CopyConditionalFormatting method, it is advised to use any of the Cells.CopyRows or Range.Copy methods.
### **Obsoleted Cells.End Property**
Please use Cells.LastCell property as an alternative to the Cells.End property.
{{< app/cells/assistant language="csharp" >}}
