---
title: 公共 API Aspose.Cells 8.9.2 的变化
type: docs
weight: 320
url: /zh/net/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.9.1 到 8.9.2 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} {{% alert color="primary" %}} 

另请检查[公共 API Aspose.Cells for .NET 8.9.1 中引入的更改](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **添加的 API**
### **添加了 TextOptions 类和 FontSettings.TextOptions 属性**
Aspose.Cells for .NET 公开了 TextOptions 类以及 FontSettings.TextOptions 属性，以控制 Shape 文本部分的外观。

这是 FontSettings.TextOptions 属性的简单使用场景。

**C#**

{{< highlight "csharp" >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access TextOptions of Shape

var textOptions = shape.TextBody[1].TextOptions;

{{< /highlight >}}


### **添加了 TextOptions.Fill、Outline 和 Shadow 属性**
Aspose.Cells for .NET 8.9.2 公开了 TextOptions.Fill、TextOptions.Outline 和 TextOptions.Shadow 属性，这些属性允许分别控制形状文本内容的各个方面，例如填充、阴影和轮廓。

这是上述属性的简单使用场景。

**C#**

{{< highlight "csharp" >}}

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


### **添加了 Shape.Line 属性**
Aspose.Cells for .NET 公开了 Shape.Line 属性，该属性返回 LineFormat 的实例以控制 Shape 轮廓的外观。

下面是 Shape.Line 属性的简单使用场景。

**C#**

{{< highlight "csharp" >}}

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


### **添加了 Shape.Fill 属性**
Aspose.Cells for .NET 8.9.2 公开了返回 FillFormat 实例的 Shape.Fill 属性，以控制形状区域的不同方面。

以下是 Shape.Fill 属性的简单使用场景。

**C#**

{{< highlight "csharp" >}}

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
## **过时的 API**
### **废弃的 ShapeFont 类**
请改用 TextOptions 类。
### **废弃的 ShapeFormat 类**
请直接使用 Shape.Fill 和 Shape.Line 属性。
### **废弃的 Shape.Format 属性**
请直接使用 Shape.Fill 和 Shape.Line 属性。
### **废弃的 Shape.LineFormat 属性**
请改用 Shape.Line 属性。
### **废弃的 Shape.FillFormat 属性**
请改用 Shape.Fill 属性。
### **废弃的 FontSetting.ShapeFont 属性**
请改用 FontSetting.TextOptions 属性。
