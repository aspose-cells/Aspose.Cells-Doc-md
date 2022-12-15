---
title: Offentlig API Ändringar i Aspose.Cells 8.9.2
type: docs
weight: 320
url: /sv/net/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.9.1 till 8.9.2 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

 Kontrollera också[Offentlig API Ändringar införda i Aspose.Cells for .NET 8.9.1](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **Lade till API:er**
### **Lagt till TextOptions Class & FontSettings.TextOptions Property**
Aspose.Cells for .NET har exponerat TextOptions-klassen tillsammans med FontSettings.TextOptions-egenskapen för att kontrollera utseendet på textdelar av en Shape.

Här är ett enkelt användningsscenario för FontSettings.TextOptions-egenskapen.

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


### **Lade till TextOptions.Fill, Outline & Shadow Properties**
Aspose.Cells for .NET 8.9.2 har exponerat egenskaperna TextOptions.Fill, TextOptions.Outline och TextOptions.Shadow som gör det möjligt att kontrollera aspekterna av textinnehållet i formen, såsom fyllning, skugga och kontur respektive.

Här är ett enkelt användningsscenario för ovannämnda egenskaper.

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


### **Lade till Shape.Line-egenskap**
Aspose.Cells for .NET har exponerat egenskapen Shape.Line som returnerar en instans av LineFormat för att kontrollera utseendet på konturerna av en Shape.

Här är ett enkelt användningsscenario för Shape.Line-egenskapen.

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


### **Lade till egenskapen Shape.Fill**
Aspose.Cells for .NET 8.9.2 har exponerat egenskapen Shape.Fill som returnerar en instans av FillFormat för att kontrollera de olika aspekterna av formområdet.

Följande är det enkla användningsscenariot för Shape.Fill-egenskapen.

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
## **Föråldrade API:er**
### **Föråldrad ShapeFont Class**
Använd TextOptions-klassen istället.
### **Föråldrad ShapeFormat Class**
Använd egenskaperna Shape.Fill och Shape.Line direkt.
### **Föråldrad Shape.Format Property**
Använd egenskaperna Shape.Fill och Shape.Line direkt.
### **Föråldrad Shape.LineFormat-egenskap**
Använd egenskapen Shape.Line istället.
### **Föråldrad Shape.FillFormat-egenskap**
Använd Shape.Fill-egenskapen istället.
### **Föråldrad FontSetting.ShapeFont-egenskap**
Använd egenskapen FontSetting.TextOptions istället.
