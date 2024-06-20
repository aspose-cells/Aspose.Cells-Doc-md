---
title: Offentliga API ändringar i Aspose.Cells 8.9.2
type: docs
weight: 320
url: /sv/net/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna i Aspose.Cells API från version 8.9.1 till 8.9.2 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

Vänligen kontrollera även [Offentliga API-ändringar introducerade i Aspose.Cells for .NET 8.9.1](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **Tillagda API:er**
### **Tillagd TextOptions Klass & FontSettings.TextOptions Egendom**
Aspose.Cells for .NET har exponerat TextOptions-klassen tillsammans med FontSettings.TextOptions egenskap för att kontrollera utseendet på textdelarna av en form.

Här är det enkla användningscenariot för FontSettings.TextOptions egendomen.

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


### **Tillagd TextOptions.Fill, Outline & Shadow Egenskaper**
Aspose.Cells for .NET 8.9.2 har exponerat TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow egenskaper som möjliggör kontroll av aspekterna av de textuella innehållen i formen, såsom fyllnad, skugga & kontur.

Här är det enkla användningscenariot för ovanstående egenskaper.

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


### **Tillagd Shape.Line Egendom**
Aspose.Cells for .NET har exponerat Shape.Line-egenskapen som returnerar en instans av LineFormat för att styra utseendet på konturer av en form.

Här är ett enkelt användningsscenariot för Shape.Line-egenskapen.

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


### **Tillagd Shape.Fill Egendom**
Aspose.Cells for .NET 8.9.2 har exponerat Shape.Fill-egenskapen som returnerar en instans av FillFormat för att styra olika aspekter av formområdet.

Följande är det enkla användningscenariot för Shape.Fill egendomen.

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
## **Obsoletterade API:er**
### **Föråldrad ShapeFont Klass**
Använd istället TextOptions-klassen.
### **Föråldrad ShapeFormat Klass**
Använd direkt Shape.Fill- och Shape.Line-egenskaper.
### **Obsolet Shape.Format-egenskap**
Använd direkt Shape.Fill- och Shape.Line-egenskaper.
### **Obsolet Shape.LineFormat-egenskap**
Använd Shape.Line-egenskapen istället.
### **Obsolet Shape.FillFormat-egenskap**
Använd Shape.Fill-egenskapen istället.
### **Obsolet FontSetting.ShapeFont-egenskap**
Använd FontSetting.TextOptions-egenskapen istället.
