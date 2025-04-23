---
title: Изменения в публичном API в Aspose.Cells 8.9.2
type: docs
weight: 330
url: /ru/java/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.9.1 до 8.9.2, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные открытые методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

Также ознакомьтесь с [Изменениями в общем API, введенными в Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **Добавленные API**
### **Добавлен класс TextOptions и свойство FontSettings.TextOptions**
Aspose.Cells for Java представил класс TextOptions вместе со свойством FontSettings.TextOptions для управления видом текстовых частей формы.

Вот простой сценарий использования свойства FontSettings.TextOptions.

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
### **Добавлены свойства TextOptions.Fill, Outline и Shadow**
Aspose.Cells for Java 8.9.2 представил свойства TextOptions.Fill, TextOptions.Outline и TextOptions.Shadow, которые позволяют контролировать аспекты текстового содержимого формы, такие как заливка, тень и контур соответственно. 

Вот простой сценарий использования вышеперечисленных свойств.

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
### **Добавлено свойство Shape.Line**
Aspose.Cells for Java представил свойство Shape.Line, которое возвращает экземпляр LineFormat для управления отображением контуров формы.

Вот простой сценарий использования свойства Shape.Line.

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
### **Добавлено свойство Shape.Fill**
Aspose.Cells for Java 8.9.2 представил свойство Shape.Fill, которое возвращает экземпляр FillFormat для управления различными аспектами области формы.

Ниже приведен простой сценарий использования свойства Shape.Fill.

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
## **Устаревшие API**
### **Устаревший класс ShapeFont**
Пожалуйста, используйте класс TextOptions вместо.
### **Устаревший класс ShapeFormat**
Пожалуйста, непосредственно используйте свойства Shape.Fill и Shape.Line.
### **Устаревшее свойство Shape.Format**
Пожалуйста, непосредственно используйте свойства Shape.Fill и Shape.Line.
### **Устаревшее свойство Shape.LineFormat.**
Пожалуйста, используйте свойство Shape.Line вместо него.
### **Устаревшее свойство Shape.FillFormat.**
Пожалуйста, используйте свойство Shape.Fill вместо него.
### **Устаревшее свойство FontSetting.ShapeFont.**
Пожалуйста, используйте свойство FontSetting.TextOptions вместо него.
{{< app/cells/assistant language="java" >}}
