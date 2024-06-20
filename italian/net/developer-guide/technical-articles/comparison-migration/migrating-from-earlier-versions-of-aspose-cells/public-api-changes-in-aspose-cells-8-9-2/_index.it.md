---
title: Modifiche dell API pubblica in Aspose.Cells 8.9.2
type: docs
weight: 320
url: /it/net/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.9.1 a 8.9.2 che possono interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte e rimosse, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

Si prega di controllare anche le [Modifiche dell'API pubblica introdotte in Aspose.Cells for .NET 8.9.1](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **API aggiunte**
### **Aggiunta la classe TextOptions e la proprietà FontSettings.TextOptions**
Aspose.Cells for .NET ha esposto la classe TextOptions insieme alla proprietà FontSettings.TextOptions al fine di controllare l'aspetto delle parti testuali di una forma.

Ecco un semplice scenario d'uso della proprietà FontSettings.TextOptions.

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


### **Aggiunte le proprietà TextOptions.Fill, Outline e Shadow**
Aspose.Cells for .NET 8.9.2 ha esposto le proprietà TextOptions.Fill, TextOptions.Outline e TextOptions.Shadow che consentono di controllare gli aspetti dei contenuti testuali della forma, come riempimento, ombra e contorno rispettivamente.

Ecco un semplice scenario di utilizzo delle proprietà sopra menzionate.

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


### **Aggiunta la proprietà Shape.Line**
Aspose.Cells for .NET ha esposto la proprietà Shape.Line che restituisce un'istanza di LineFormat al fine di controllare l'aspetto degli elementi di contorno di una forma.

Ecco un semplice scenario d'uso della proprietà Shape.Line.

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


### **Aggiunta la proprietà Shape.Fill**
Aspose.Cells for .NET 8.9.2 ha esposto la proprietà Shape.Fill che restituisce un'istanza di FillFormat al fine di controllare diversi aspetti dell'area della forma.

Di seguito è riportato un semplice scenario d'uso della proprietà Shape.Fill.

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
## **API deprecate**
### **Classe ShapeFont obsoleta**
Si prega di utilizzare la classe TextOptions al suo posto.
### **Classe ShapeFormat deprecata**
Si prega di utilizzare direttamente le proprietà Shape.Fill e Shape.Line.
### **Proprietà Shape.Format deprecata**
Si prega di utilizzare direttamente le proprietà Shape.Fill e Shape.Line.
### **Proprietà Shape.LineFormat deprecata**
Si prega di utilizzare la proprietà Shape.Line invece.
### **Proprietà Shape.FillFormat deprecata**
Si prega di utilizzare la proprietà Shape.Fill invece.
### **Proprietà FontSetting.ShapeFont deprecata**
Si prega di utilizzare la proprietà FontSetting.TextOptions invece.
