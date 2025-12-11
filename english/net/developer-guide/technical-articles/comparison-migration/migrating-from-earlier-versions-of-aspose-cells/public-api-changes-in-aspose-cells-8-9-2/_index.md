---
title: Public API Changes in Aspose.Cells 8.9.2
type: docs
weight: 320
url: /net/public-api-changes-in-aspose-cells-8-9-2/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.9.1 to 8.9.2 that may be of interest to module and application developers. It includes not only new and updated public methods, added and removed classes, etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

Please also check the [Public API Changes introduced in Aspose.Cells for .NET 8.9.1](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **Added APIs**
### **Added TextOptions Class & FontSettings.TextOptions Property**
Aspose.Cells for .NET has exposed the TextOptions class along with the FontSettings.TextOptions property in order to control the appearance of the textual parts of a shape.

Here is a simple usage scenario of the FontSettings.TextOptions property.

**C#**

{{< highlight csharp >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access TextOptions of Shape

var textOptions = shape.TextBody[1].TextOptions;

{{< /highlight >}}


### **Added TextOptions.Fill, Outline & Shadow Properties**
Aspose.Cells for .NET 8.9.2 has exposed the TextOptions.Fill, TextOptions.Outline, and TextOptions.Shadow properties, which allow you to control aspects of the textual contents of the shape, such as fill, shadow, and outline respectively.

Here is a simple usage scenario of the aforementioned properties.

**C#**

{{< highlight csharp >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Set text for TextBox

shape.Text = "Aspose";

// Access TextOptions of Shape

var textOptions = shape.TextBody[1].TextOptions;

// Set shadow 

textOptions.Shadow.PresetType = PresetShadowType.Below;

// Set fill color

textOptions.Fill.FillType = FillType.Solid;

textOptions.Fill.SolidFill.Color = Color.Red;

// Set outline color

textOptions.Outline.SetOneColorGradient(Color.Blue, 0.3, GradientStyleType.Horizontal, 2);

{{< /highlight >}}


### **Added Shape.Line Property**
Aspose.Cells for .NET has exposed the Shape.Line property, which returns an instance of LineFormat in order to control the appearance of the outline of a shape.

Here is a simple usage scenario of the Shape.Line property.

**C#**

{{< highlight csharp >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access LineFormat of Shape

var line = shape.Line;

// Set weight of line

line.Weight = 1;

{{< /highlight >}}


### **Added Shape.Fill Property**
Aspose.Cells for .NET 8.9.2 has exposed the Shape.Fill property, which returns an instance of FillFormat in order to control the different aspects of a shape's area.

The following is a simple usage scenario of the Shape.Fill property.

**C#**

{{< highlight csharp >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access FillFormat of Shape

var fill = shape.Fill;

// Set color for fill

fill.SetOneColorGradient(Color.Red, 0.1, GradientStyleType.Horizontal, 2);

{{< /highlight >}}
## **Obsoleted APIs**
### **Obsoleted ShapeFont Class**
Please use the TextOptions class instead.

### **Obsoleted ShapeFormat Class**
Please directly use the Shape.Fill and Shape.Line properties.

### **Obsoleted Shape.Format Property**
Please directly use the Shape.Fill and Shape.Line properties.

### **Obsoleted Shape.LineFormat Property**
Please use the Shape.Line property instead.

### **Obsoleted Shape.FillFormat Property**
Please use the Shape.Fill property instead.

### **Obsoleted FontSetting.ShapeFont Property**
Please use the FontSettings.TextOptions property instead.
{{< app/cells/assistant language="csharp" >}}
