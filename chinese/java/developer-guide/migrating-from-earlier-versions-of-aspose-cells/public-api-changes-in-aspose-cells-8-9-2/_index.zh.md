---
title: Aspose.Cells 8.9.2 中的公共 API 变更
type: docs
weight: 330
url: /zh/java/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.9.1 到 8.9.2 中 Aspose.Cells API 的变更，这可能对模块/应用程序开发人员感兴趣。其中包括不仅新的和更新的公共方法，添加和删除的类等，还有关 Aspose.Cells 在后台行为变更的描述。

{{% /alert %}} {{% alert color="primary" %}} 

请查看[Aspose.Cells for Java 8.9.1中引入的公共API更改](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **添加的 API**
### **添加了 TextOptions 类和 FontSettings.TextOptions 属性**
Aspose.Cells for Java已经暴露了TextOptions类以及FontSettings.TextOptions属性，以控制形状的文本部分的外观。

以下是 FontSettings.TextOptions 属性的简单使用场景。

**Java**

{{< highlight csharp >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Add text to Shape

shape.setText("Aspose");

//Access TextOptions of Shape

TextOptions textOptions =  ((FontSetting)shape.getCharacters().get(0)).getTextOptions();

{{< /highlight >}}
### **添加了 TextOptions.Fill、Outline 和 Shadow 属性**
Aspose.Cells for Java 8.9.2版本已暴露了TextOptions.Fill、TextOptions.Outline和TextOptions.Shadow属性，允许控制形状文本内容的方面，如填充、阴影和轮廓。 

以下是上述属性的简单使用场景。

**Java**

{{< highlight csharp >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Add text to Shape

shape.setText("Aspose");

//Access TextOptions of Shape

TextOptions textOptions =  ((FontSetting)shape.getCharacters().get(0)).getTextOptions();

//Set shadow 

textOptions.getShadow().setPresetType(PresetShadowType.BELOW);

//Set fill color

textOptions.getFill().setFillType(FillType.SOLID);

textOptions.getFill().getSolidFill().setColor(Color.getRed());

//Set outline color

textOptions.getOutline().setOneColorGradient(Color.getBlue(), 0.3, GradientStyleType.HORIZONTAL, 2);

{{< /highlight >}}
### **添加了 Shape.Line 属性**
Aspose.Cells for Java 公开了 Shape.Line 属性，该属性返回 LineFormat 实例，以便控制形状轮廓的外观。

这里是 Shape.Line 属性的简单使用场景。

**Java**

{{< highlight csharp >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Access LineFormat of Shape

LineFormat line = shape.getLine();

//Set weight of line

line.setWeight(4);

{{< /highlight >}}
### **添加了 Shape.Fill 属性**
Aspose.Cells for Java 8.9.2 公开了 Shape.Fill 属性，该属性返回 FillFormat 实例，以便控制形状区域的不同方面。

以下是 Shape.Fill 属性的简单使用场景。

**Java**

{{< highlight csharp >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Access FillFormat of Shape

FillFormat fill = shape.getFill();

//Set color for fill

fill.setFillType(FillType.SOLID);

fill.getSolidFill().setColor(Color.getBlue());

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
