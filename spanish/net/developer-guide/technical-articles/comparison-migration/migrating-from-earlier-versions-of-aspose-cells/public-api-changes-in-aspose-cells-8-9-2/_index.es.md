---
title: Cambios en la API pública en Aspose.Cells 8.9.2
type: docs
weight: 320
url: /es/net/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.9.1 hasta la 8.9.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento en segundo plano de Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

Por favor también revise los [Cambios en la API Pública introducidos en Aspose.Cells for .NET 8.9.1](http://aspose.com/docs/display/cellsnet/Cambios+en+la+API+Pública+en+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **APIs Añadidas**
### **Clase TextOptions y propiedad FontSettings.TextOptions agregadas**
Aspose.Cells for .NET ha expuesto la clase TextOptions junto con la propiedad FontSettings.TextOptions para controlar la apariencia de las partes textuales de una Forma.

Aquí hay un escenario de uso simple de la propiedad FontSettings.TextOptions.

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


### **Propiedad de relleno, contorno y sombra TextOptions agregadas**
Aspose.Cells for .NET 8.9.2 ha expuesto las propiedades TextOptions.Fill, TextOptions.Outline y TextOptions.Shadow que permiten controlar los aspectos de los contenidos textuales de la forma, como el relleno, la sombra y el contorno respectivamente.

Aquí hay un escenario de uso simple de las propiedades mencionadas.

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


### **Propiedad Shape.Line agregada**
Aspose.Cells for .NET ha expuesto la propiedad Shape.Line que devuelve una instancia de LineFormat para controlar la apariencia de los contornos de una forma.

Aquí hay un escenario de uso simple de la propiedad Shape.Line.

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


### **Propiedad Shape.Fill agregada**
Aspose.Cells for .NET 8.9.2 ha expuesto la propiedad Shape.Fill que devuelve una instancia de FillFormat para controlar los diferentes aspectos del área de la forma.

A continuación se muestra el escenario de uso simple de la propiedad Shape.Fill.

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
## **APIs obsoletas**
### **Clase ShapeFont obsoleta**
Por favor, utilice la clase TextOptions en su lugar.
### **Clase ShapeFormat obsoleta**
Por favor, utilice directamente las propiedades Shape.Fill y Shape.Line.
### **Propiedad Shape.Format obsoleta**
Por favor, utilice directamente las propiedades Shape.Fill y Shape.Line.
### **Propiedad Shape.LineFormat obsoleta**
Por favor, utilice la propiedad Shape.Line en su lugar.
### **Propiedad Shape.FillFormat obsoleta**
Por favor, utilice la propiedad Shape.Fill en su lugar.
### **Propiedad FontSetting.ShapeFont obsoleta**
Por favor, utilice la propiedad FontSetting.TextOptions en su lugar.
{{< app/cells/assistant language="csharp" >}}
