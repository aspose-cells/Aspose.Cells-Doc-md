---
title: Öffentliche API Änderungen in Aspose.Cells 8.9.2
type: docs
weight: 320
url: /de/net/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 8.9.1 auf 8.9.2, die für Modul-/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

Bitte überprüfen Sie auch die [Öffentlichen API-Änderungen, die in Aspose.Cells for .NET 8.9.1 eingeführt wurden](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Hinzugefügte TextOptions-Klasse & FontSettings.TextOptions-Eigenschaft**
Aspose.Cells for .NET hat die TextOptions-Klasse zusammen mit der FontSettings.TextOptions-Eigenschaft freigegeben, um das Aussehen von Textteilen einer Form zu steuern.

Hier ist ein einfaches Anwendungsszenario der FontSettings.TextOptions-Eigenschaft.

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


### **Hinzugefügte TextOptions.Fill, Outline & Shadow-Eigenschaften**
Aspose.Cells for .NET 8.9.2 hat die TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow-Eigenschaften freigegeben, die es ermöglichen, Aspekte des Textinhalts der Form zu steuern, wie z.B. Füllung, Schatten & Kontur.

Hier ist ein einfaches Anwendungsszenario der genannten Eigenschaften.

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


### **Hinzugefügte Shape.Line-Eigenschaft**
Aspose.Cells for .NET hat die Shape.Line-Eigenschaft freigegeben, die eine Instanz von LineFormat zurückgibt, um das Erscheinungsbild der Umrisse einer Form zu steuern.

Hier ist ein einfaches Anwendungsbeispiel der Shape.Line Eigenschaft.

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


### **Hinzugefügte Shape.Fill-Eigenschaft**
Aspose.Cells for .NET 8.9.2 hat die Shape.Fill-Eigenschaft freigegeben, die eine Instanz von FillFormat zurückgibt, um die verschiedenen Aspekte des Formbereichs zu steuern.

Nachfolgend finden Sie das einfache Anwendungsszenario der Shape.Fill-Eigenschaft.

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
## **Veraltete APIs**
### **Veraltete ShapeFont-Klasse**
Bitte verwenden Sie stattdessen die TextOptions-Klasse.
### **Veraltete ShapeFormat-Klasse**
Bitte verwenden Sie direkt die Shape.Fill und Shape.Line Eigenschaften.
### **Veraltete Shape.Format Eigenschaft**
Bitte verwenden Sie direkt die Shape.Fill und Shape.Line Eigenschaften.
### **Veraltete Shape.LineFormat Eigenschaft**
Bitte verwenden Sie die Shape.Line Eigenschaft stattdessen.
### **Veraltete Shape.FillFormat Eigenschaft**
Bitte verwenden Sie die Shape.Fill Eigenschaft stattdessen.
### **Veraltete FontSetting.ShapeFont Eigenschaft**
Bitte verwenden Sie stattdessen die FontSetting.TextOptions Eigenschaft.
