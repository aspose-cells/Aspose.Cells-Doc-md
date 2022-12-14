---
title: Общедоступный API Изменения в Aspose.Cells 8.9.2
type: docs
weight: 320
url: /ru/net/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.9.1 до 8.9.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

 Пожалуйста, также проверьте[Общедоступный API Изменения, внесенные в Aspose.Cells for .NET 8.9.1](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **Добавлены API**
### **Добавлен класс TextOptions и свойство FontSettings.TextOptions.**
Aspose.Cells for .NET предоставил класс TextOptions вместе со свойством FontSettings.TextOptions для управления внешним видом текстовых частей формы.

Вот простой сценарий использования свойства FontSettings.TextOptions.

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


### **Добавлены свойства TextOptions.Fill, Outline и Shadow.**
Aspose.Cells for .NET 8.9.2 предоставляет свойства TextOptions.Fill, TextOptions.Outline и TextOptions.Shadow, которые позволяют управлять аспектами текстового содержимого фигуры, такими как заливка, тень и контур соответственно.

Вот простой сценарий использования вышеупомянутых свойств.

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


### **Добавлено свойство Shape.Line**
Aspose.Cells for .NET предоставил свойство Shape.Line, которое возвращает экземпляр LineFormat для управления внешним видом контуров фигуры.

Вот простой сценарий использования свойства Shape.Line.

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


### **Добавлено свойство Shape.Fill**
Aspose.Cells for .NET 8.9.2 предоставляет свойство Shape.Fill, которое возвращает экземпляр FillFormat для управления различными аспектами области формы.

Ниже приведен простой сценарий использования свойства Shape.Fill.

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
