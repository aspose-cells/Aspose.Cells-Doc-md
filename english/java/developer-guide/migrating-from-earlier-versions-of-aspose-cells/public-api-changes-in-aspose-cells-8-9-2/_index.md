---
title: Public API Changes in Aspose.Cells 8.9.2
type: docs
weight: 330
url: /java/public-api-changes-in-aspose-cells-8-9-2/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.9.1 to 8.9.2 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

Please also check the [Public API Changes introduced in Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **Added APIs**
### **Added TextOptions Class & FontSettings.TextOptions Property**
Aspose.Cells for Java has exposed the TextOptions class along with FontSettings.TextOptions property in order to control the appearance of textual parts of a Shape.

Here is a simple usage scenario of FontSettings.TextOptions property.

**Java**

{{< highlight java >}}

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
### **Added TextOptions.Fill, Outline & Shadow Properties**
Aspose.Cells for Java 8.9.2 has exposed the TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow properties which allow to control the aspects of textual content of the shape, such as fill, shadow & outline respectively. 

Here is a simple usage scenario of the aforementioned properties.

**Java**

{{< highlight java >}}

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
### **Added Shape.Line Property**
Aspose.Cells for Java has exposed the Shape.Line property which returns an instance of LineFormat in order to control the appearance of outlines of a Shape.

Here is a simple usage scenario of Shape.Line property.

**Java**

{{< highlight java >}}

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
### **Added Shape.Fill property**
Aspose.Cells for Java 8.9.2 has exposed the Shape.Fill property which returns an instance of FillFormat in order to control the different aspects of shape area.

Following is a simple usage scenario of Shape.Fill property.

**Java**

{{< highlight java >}}

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
## **Obsoleted APIs**
### **Obsoleted ShapeFont Class**
Please use TextOptions class instead.
### **Obsoleted ShapeFormat Class**
Please directly use Shape.Fill and Shape.Line properties.
### **Obsoleted Shape.Format Property**
Please directly use Shape.Fill and Shape.Line properties.
### **Obsoleted Shape.LineFormat Property**
Please use Shape.Line property instead.
### **Obsoleted Shape.FillFormat Property**
Please use Shape.Fill property instead.
### **Obsoleted FontSetting.ShapeFont Property**
Please use FontSetting.TextOptions property instead.
{{< app/cells/assistant language="java" >}}
