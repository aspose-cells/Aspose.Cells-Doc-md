---
title: Öffentliche API Änderungen in Aspose.Cells 8.9.2
type: docs
weight: 330
url: /de/java/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 8.9.1 auf 8.9.2, die für Modul-/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

Bitte prüfen Sie auch die [Öffentliche API-Änderungen in Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Hinzugefügte TextOptions-Klasse & FontSettings.TextOptions-Eigenschaft**
Aspose.Cells for Java hat die TextOptions-Klasse zusammen mit der FontSettings.TextOptions-Eigenschaft freigegeben, um das Erscheinungsbild textueller Teile einer Form zu steuern.

Hier ist ein einfaches Anwendungsszenario der FontSettings.TextOptions-Eigenschaft.

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
### **Hinzugefügte TextOptions.Fill, Outline & Shadow-Eigenschaften**
Aspose.Cells for Java 8.9.2 hat die Eigenschaften TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow freigegeben, die es ermöglichen, die Aspekte des textuellen Inhalts der Form, wie Füllung, Schatten & Umrandung, zu steuern. 

Hier ist ein einfaches Anwendungsszenario der genannten Eigenschaften.

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
### **Hinzugefügte Shape.Line-Eigenschaft**
Aspose.Cells for Java hat die Eigenschaft Shape.Line freigegeben, die eine Instanz von LineFormat zurückgibt, um das Erscheinungsbild der Umrisse einer Form zu steuern.

Hier ist ein einfaches Anwendungsbeispiel der Shape.Line Eigenschaft.

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
### **Hinzugefügte Shape.Fill-Eigenschaft**
Aspose.Cells for Java 8.9.2 hat die Eigenschaft Shape.Fill freigegeben, die eine Instanz von FillFormat zurückgibt, um die verschiedenen Aspekte des Formbereichs zu steuern.

Nachfolgend finden Sie das einfache Anwendungsszenario der Shape.Fill-Eigenschaft.

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
