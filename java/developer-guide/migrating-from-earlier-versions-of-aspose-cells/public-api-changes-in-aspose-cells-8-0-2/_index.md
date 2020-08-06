---
title: Public API Changes in Aspose.Cells 8.0.2
type: docs
weight: 40
url: /java/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

This document describes changes to the Aspose.Cells API from version 8.0.1 to 8.0.2, that may be of interest to module/application developers. It includes not only new and updated public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
### **Added TextDirection Property to Shape Class**
The Shape class has exposed TextDirection property which can be used get or set the direction of the text flow for the Shape object. The TextDirection property can also be used to set the desired text direction for the comments in a spreadsheet as demonstrated below.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Adding a comment to "F5" cell

int commentIndex = sheet.getComments().add("F5");

Comment comment = sheet.getComments().get(commentIndex);

//Set its vertical alignment setting            

comment.getCommentShape().setTextVerticalAlignment(TextAlignmentType.CENTER);

//Set its horizontal alignment setting

comment.getCommentShape().setTextHorizontalAlignment(TextAlignmentType.RIGHT);

//Set the Text Direction - Right-to-Left

comment.getCommentShape().setTextDirection(TextDirectionType.RIGHT_TO_LEFT);

//Set the Comment note

comment.setNote("This is my Comment Text. This is test");

//Save the Excel file

book.save(myDir + "output.xlsx");

{{< /highlight >}}
### **Added ConvertFormulasData Property to HTMLLoadOptions Class**
ConvertFormulasData property has been added to the HTMLLoadOptions Class, in order to facilitate the developers to load Excel formulas from HTML files. The boolean ConvertFormulasData property indicates whether or not to convert the string to a formula when the string value starts with character '='.

**Java**

{{< highlight csharp >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.setConvertFormulasData(true);

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

The default value of ConvertFormulasData property is false.

{{% /alert %}}
### **Added ImageOptions Property to HtmlSaveOptions Class**
ImageOptions property has been added to the HtmlSaveOptions Class. Exposing the ImageOptions property has enabled the developers to set the preferences for the images embedded in the HTML while exporting spreadsheets. 
### **Obsoleted HtmlSaveOptions.ExportChartImageFormat Property**
HtmlSaveOptions.ExportChartImageFormat has been marked obsolete starting from Aspose.Cells for .NET 8.0.2. It is advised to use HtmlSaveOptions.ImageOptions instead for image format settings while exporting spreadsheets to HTML format.
