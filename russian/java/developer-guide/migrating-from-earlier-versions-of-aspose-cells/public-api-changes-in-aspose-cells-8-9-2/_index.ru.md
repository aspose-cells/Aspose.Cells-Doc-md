---
title: Общедоступный API Изменения в Aspose.Cells 8.9.2
type: docs
weight: 330
url: /ru/java/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.9.1 до 8.9.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

 Пожалуйста, также проверьте[Общедоступный API Изменения, внесенные в Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **Добавлены API**
### **Добавлен класс TextOptions и свойство FontSettings.TextOptions.**
Aspose.Cells for Java предоставил класс TextOptions вместе со свойством FontSettings.TextOptions для управления внешним видом текстовых частей формы.

Вот простой сценарий использования свойства FontSettings.TextOptions.

**Java**

{{< highlight "csharp" >}}

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
### **Добавлены свойства TextOptions.Fill, Outline и Shadow.**
 Aspose.Cells for Java 8.9.2 предоставляет свойства TextOptions.Fill, TextOptions.Outline и TextOptions.Shadow, которые позволяют управлять аспектами текстового содержимого фигуры, такими как заливка, тень и контур соответственно.

Вот простой сценарий использования вышеупомянутых свойств.

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells for Java предоставил свойство Shape.Line, которое возвращает экземпляр LineFormat для управления внешним видом контуров фигуры.

Вот простой сценарий использования свойства Shape.Line.

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells for Java 8.9.2 предоставляет свойство Shape.Fill, которое возвращает экземпляр FillFormat для управления различными аспектами области формы.

Ниже приведен простой сценарий использования свойства Shape.Fill.

**Java**

{{< highlight "csharp" >}}

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
Вместо этого используйте класс TextOptions.
### **Устаревший класс ShapeFormat**
Пожалуйста, используйте свойства Shape.Fill и Shape.Line напрямую.
### **Устаревшее свойство Shape.Format**
Пожалуйста, используйте свойства Shape.Fill и Shape.Line напрямую.
### **Устаревшее свойство Shape.LineFormat**
Вместо этого используйте свойство Shape.Line.
### **Устаревшее свойство Shape.FillFormat**
Вместо этого используйте свойство Shape.Fill.
### **Устаревшее свойство FontSetting.ShapeFont**
Вместо этого используйте свойство FontSetting.TextOptions.
