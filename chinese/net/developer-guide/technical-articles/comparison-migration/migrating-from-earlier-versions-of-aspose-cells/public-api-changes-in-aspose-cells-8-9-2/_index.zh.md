---
title: Aspose.Cells 8.9.2 中的公共 API 变更
type: docs
weight: 320
url: /zh/net/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.9.1 到 8.9.2 中 Aspose.Cells API 的变更，这可能对模块/应用程序开发人员感兴趣。其中包括不仅新的和更新的公共方法，添加和删除的类等，还有关 Aspose.Cells 在后台行为变更的描述。

{{% /alert %}} {{% alert color="primary" %}} 

请还要查看[在 Aspose.Cells for .NET 8.9.1 中引入的公共 API 变更](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **添加的 API**
### **添加了 TextOptions 类和 FontSettings.TextOptions 属性**
Aspose.Cells for .NET 已经公开了 TextOptions 类及 FontSettings.TextOptions 属性，用于控制形状文本部分的外观。

以下是 FontSettings.TextOptions 属性的简单使用场景。

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


### **添加了 TextOptions.Fill、Outline 和 Shadow 属性**
Aspose.Cells for .NET 8.9.2 已经公开了 TextOptions.Fill、TextOptions.Outline 和 TextOptions.Shadow 属性，允许控制形状文本内容的不同方面，如填充、阴影和轮廓。

以下是上述属性的简单使用场景。

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


### **添加了 Shape.Line 属性**
Aspose.Cells for .NET 已经公开了 Shape.Line 属性，返回 LineFormat 的实例，以控制形状外观的轮廓。

这里是 Shape.Line 属性的简单使用场景。

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


### **添加了 Shape.Fill 属性**
Aspose.Cells for .NET 8.9.2 已经公开了 Shape.Fill 属性，返回 FillFormat 的实例，以及控制形状区域的不同方面。

以下是 Shape.Fill 属性的简单使用场景。

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
## **已弃用的API**
### **ShapeFont 类已过时**
请使用 TextOptions 类代替。
### **ShapeFormat 类已过时**
请直接使用 Shape.Fill 和 Shape.Line 属性。
### **Shape.Format 属性已过时**
请直接使用 Shape.Fill 和 Shape.Line 属性。
### **Shape.LineFormat 属性已过时**
请使用 Shape.Line 属性代替。
### **Shape.FillFormat 属性已过时**
请使用 Shape.Fill 属性代替。
### **FontSetting.ShapeFont 属性已过时**
请使用 FontSetting.TextOptions 属性代替。
{{< app/cells/assistant language="csharp" >}}
