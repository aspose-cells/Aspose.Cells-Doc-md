---
title: Modifiche all'API pubblica in Aspose.Cells 8.9.2
type: docs
weight: 320
url: /it/net/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.9.1 alla 8.9.2 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

 Si prega di controllare anche il[API pubblica Modifiche introdotte in Aspose.Cells for .NET 8.9.1](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **API aggiunte**
### **Aggiunte classe TextOptions e proprietà FontSettings.TextOptions**
Aspose.Cells for .NET ha esposto la classe TextOptions insieme alla proprietà FontSettings.TextOptions per controllare l'aspetto delle parti testuali di una forma.

Ecco un semplice scenario di utilizzo della proprietà FontSettings.TextOptions.

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


### **Aggiunte le proprietà TextOptions.Fill, Outline e Shadow**
Aspose.Cells for .NET 8.9.2 ha esposto le proprietà TextOptions.Fill, TextOptions.Outline e TextOptions.Shadow che consentono di controllare gli aspetti del contenuto testuale della forma, come rispettivamente riempimento, ombra e contorno.

Ecco un semplice scenario di utilizzo delle proprietà di cui sopra.

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


### **Aggiunta la proprietà Shape.Line**
Aspose.Cells for .NET ha esposto la proprietà Shape.Line che restituisce un'istanza di LineFormat per controllare l'aspetto dei contorni di una Shape.

Ecco un semplice scenario di utilizzo della proprietà Shape.Line.

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


### **Aggiunta la proprietà Shape.Fill**
Aspose.Cells for .NET 8.9.2 ha esposto la proprietà Shape.Fill che restituisce un'istanza di FillFormat per controllare i diversi aspetti dell'area della forma.

Di seguito è riportato il semplice scenario di utilizzo della proprietà Shape.Fill.

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
## **API obsolete**
### **Classe ShapeFont obsoleta**
Utilizzare invece la classe TextOptions.
### **Classe ShapeFormat obsoleta**
Utilizzare direttamente le proprietà Shape.Fill e Shape.Line.
### **Proprietà Shape.Format obsoleta**
Utilizzare direttamente le proprietà Shape.Fill e Shape.Line.
### **Proprietà Shape.LineFormat obsoleta**
Utilizzare invece la proprietà Shape.Line.
### **Proprietà Shape.FillFormat obsoleta**
Utilizzare invece la proprietà Shape.Fill.
### **Proprietà FontSetting.ShapeFont obsoleta**
Utilizzare invece la proprietà FontSetting.TextOptions.
