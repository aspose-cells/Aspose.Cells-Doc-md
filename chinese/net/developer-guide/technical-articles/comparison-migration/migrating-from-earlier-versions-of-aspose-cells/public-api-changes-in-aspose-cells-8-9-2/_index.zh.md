---
title: Aspose.Cells 8.9.2中的公共API更改
type: docs
weight: 320
url: /zh/net/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.9.1到8.9.2的Aspose.Cells API的变化，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、已添加和删除的类等，还包括Aspose.Cells背后行为的任何更改描述。

{{% /alert %}} {{% alert color="primary" %}} 

还请查看[Aspose.Cells for .NET 8.9.1中引入的公共API更改](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **已添加API**
### **已添加TextOptions类和FontSettings.TextOptions属性**
Aspose.Cells for .NET现已公开TextOptions类以及FontSettings.TextOptions属性，以便控制形状的文本部分的外观。

以下是FontSettings.TextOptions属性的简单用法场景。

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


### **已添加TextOptions.Fill、Outline和Shadow属性**
Aspose.Cells for .NET 8.9.2现已公开TextOptions.Fill、TextOptions.Outline和TextOptions.Shadow属性，允许控制形状文本内容的方面，如填充、阴影和轮廓。

以下是上述属性的简单用法场景。

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


### **已添加Shape.Line属性**
Aspose.Cells for .NET现已公开Shape.Line属性，返回LineFormat实例以控制形状轮廓的外观。

以下是Shape.Line属性的简单用法场景。

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


### **已添加Shape.Fill属性**
Aspose.Cells for .NET 8.9.2现已公开Shape.Fill属性，返回FillFormat实例以控制形状区域的不同方面。

以下是Shape.Fill属性的简单用法场景。

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
## **已废弃的API**
### **已废弃ShapeFont类**
请改用TextOptions类。
### **已废弃ShapeFormat类**
请直接使用Shape.Fill和Shape.Line属性。
### **已废弃Shape.Format属性**
请直接使用Shape.Fill和Shape.Line属性。
### **已废弃Shape.LineFormat属性**
请使用Shape.Line属性。
### **不推荐使用Shape.FillFormat属性**
请改用Shape.Fill属性。
### **已过时的FontSetting.ShapeFont属性**
请改用FontSetting.TextOptions属性。
