---
title: Aspose.Cells 8.9.2中的公共API更改
type: docs
weight: 330
url: /zh/java/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.9.1到8.9.2的Aspose.Cells API的变化，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、已添加和删除的类等，还包括Aspose.Cells背后行为的任何更改描述。

{{% /alert %}} {{% alert color="primary" %}} 

还要检查一下[Aspose.Cells for Java 8.9.1中引入的公共API更改](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)。

{{% /alert %}} 
## **已添加API**
### **已添加TextOptions类和FontSettings.TextOptions属性**
Aspose.Cells for Java 还公开了 TextOptions 类以及 FontSettings.TextOptions 属性，以控制形状的文本部分的外观。

以下是FontSettings.TextOptions属性的简单用法场景。

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
### **已添加TextOptions.Fill、Outline和Shadow属性**
Aspose.Cells for Java 8.9.2 公开了 TextOptions.Fill、TextOptions.Outline 和 TextOptions.Shadow 属性，允许控制形状文本内容的填充、阴影和轮廓等方面。 

以下是上述属性的简单用法场景。

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
### **已添加Shape.Line属性**
Aspose.Cells for Java 公开了 Shape.Line 属性，它返回一个 LineFormat 实例，以控制形状轮廓的外观。

以下是Shape.Line属性的简单用法场景。

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
### **已添加Shape.Fill属性**
Aspose.Cells for Java 8.9.2 公开了 Shape.Fill 属性，它返回一个 FillFormat 实例，以控制形状区域的不同方面。

以下是Shape.Fill属性的简单用法场景。

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
