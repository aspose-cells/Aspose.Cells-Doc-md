---
title: Public API Changes in Aspose.Cells 8.1.0
type: docs
weight: 50
url: /java/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

This document describes changes to the Aspose.Cells API from version 8.0.2 to 8.1.0, that may be of interest to module/application developers. It includes not only new and updated public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
### **Added HtmlSaveOptions.ExportHiddenWorksheet Property**
The HtmlSaveOptions class has exposed ExportHiddenWorksheet property which can be used to specify if hidden worksheets are exported to HTML format. The default value is true. whereas if set to false, the Aspose.Cells will not export hidden worksheet contents.

{{% alert color="primary" %}} 

Please check the detailed article on [Prevent Exporting Hidden Worksheet](/cells/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
### **Added Cell.StringValueWithoutFormat Property**
StringValueWithoutFormat property has been added to the Cell Class, in order to facilitate the developers to retrieve the cell value without any formatting applied. 

Below provided code snippet demonstrate the usage of Cell.getStringValueWithoutFormat method as compared to the cell.getDisplayStringValue by creating a spreadsheet from scratch and applying the number format to one of the cells. 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access A1 cell

Cell cell = sheet.getCells().get("A1");

//Put a value cell and convert it to number

cell.putValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

int index = book.getStyles().add();

Style style = book.getStyles().get(index);

//Set Number format for Style object

style.setNumber(3);

//Create an instance of StyleFlag class

//and set NumberFormat to true

StyleFlag flag = new StyleFlag();

flag.setNumberFormat(true);

//Set the style of A1 cell

cell.setStyle(style, flag);

//Get formatted string value 

String formatted = cell.getDisplayStringValue();

System.out.println("Formatted String Value: " +formatted);

//Get un-formatted string value

String unformatted = cell.getStringValueWithoutFormat();

System.out.println("Un-formatted String Value: " + unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

Output of above code is as follow

Formatted String Value: 123,456
Un-formatted String Value: 123456

{{% /alert %}}
### **Obsoleted Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs Properties**
Many properties from BuiltInDocumentPropertyCollection class have been marked obsolete starting from Aspose.Cells for .NET 8.1.0. These properties include Bytes, Characters, CharactersWithSpaces, Lines & Paragraphs. Reason being, the aforesaid properties are of no use in preservative of Excel spreadsheets because Excel omits them. Where as these properties were originally written for Word documents & PowerPoint presentations. 
