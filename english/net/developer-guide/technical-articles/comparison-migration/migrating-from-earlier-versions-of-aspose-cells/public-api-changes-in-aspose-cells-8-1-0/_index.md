---
title: Public API Changes in Aspose.Cells 8.1.0
type: docs
weight: 40
url: /net/public-api-changes-in-aspose-cells-8-1-0/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes changes to the Aspose.Cells API from version 8.0.2 to 8.1.0 that may be of interest to module/application developers. It includes not only new and updated public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added HtmlSaveOptions.ExportHiddenWorksheet Property**
The HtmlSaveOptions class has exposed the ExportHiddenWorksheet property which can be used to specify if hidden worksheets are exported to HTML format. The default value is true, whereas if set to false, Aspose.Cells will not export hidden worksheet contents.

{{% alert color="primary" %}} 

Please check the detailed article on [Prevent Exporting Hidden Worksheet](/cells/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Added Cell.StringValueWithoutFormat Property**
StringValueWithoutFormat property has been added to the Cell class, in order to facilitate developers retrieving the cell value without any formatting applied.

Below provided code snippet demonstrates the usage of the Cell.StringValueWithoutFormat property compared to the cell.DisplayStringValue, by creating a spreadsheet from scratch and applying the number format to one of the cells.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.Worksheets[0];

//Access A1 cell

Cell cell = sheet.Cells["A1"];

//Put a value cell and convert it to number

cell.PutValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

Style style = book.Styles[book.Styles.Add()];

//Set Number format for Style object

style.Number = 3;

//Set the style of A1 cell

cell.SetStyle(style, new StyleFlag() { NumberFormat = true });

//Get formatted string value 

string formatted = cell.DisplayStringValue;

Console.WriteLine(formatted);

//Get un-formatted string value

string unformatted = cell.StringValueWithoutFormat;

Console.WriteLine(unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

Output of the above code is as follows

123,456

123456

{{% /alert %}}
## **Obsolete Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs Properties**
Many properties from BuiltInDocumentPropertyCollection class have been marked obsolete starting from Aspose.Cells for .NET 8.1.0. These properties include Bytes, Characters, CharactersWithSpaces, Lines & Paragraphs. The reason is that these properties are of no use in preserving Excel spreadsheets because Excel omits them. Whereas these properties were originally intended for Word documents and PowerPoint presentations.
{{< app/cells/assistant language="csharp" >}}
