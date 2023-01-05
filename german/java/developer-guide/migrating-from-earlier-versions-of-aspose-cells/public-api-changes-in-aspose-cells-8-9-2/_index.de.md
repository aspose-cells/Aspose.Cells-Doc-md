---
title: Öffentlich API Änderungen in Aspose.Cells 8.9.2
type: docs
weight: 330
url: /de/java/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.9.1 zu 8.9.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

 Bitte prüfen Sie auch die[Öffentlich API Änderungen eingeführt in Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **APIs hinzugefügt**
### **TextOptions-Klasse und FontSettings.TextOptions-Eigenschaft hinzugefügt**
Aspose.Cells for Java hat die TextOptions-Klasse zusammen mit der FontSettings.TextOptions-Eigenschaft verfügbar gemacht, um die Darstellung von Textteilen einer Form zu steuern.

Hier ist ein einfaches Verwendungsszenario der Eigenschaft FontSettings.TextOptions.

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
### **TextOptions.Fill, Outline & Shadow Properties hinzugefügt**
 Aspose.Cells for Java 8.9.2 hat die TextOptions.Fill-, TextOptions.Outline- und TextOptions.Shadow-Eigenschaften verfügbar gemacht, mit denen die Aspekte des Textinhalts der Form gesteuert werden können, z. B. Füllung, Schatten und Umriss.

Hier ist ein einfaches Nutzungsszenario der oben genannten Eigenschaften.

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
### **Shape.Line-Eigenschaft hinzugefügt**
Aspose.Cells for Java hat die Shape.Line-Eigenschaft verfügbar gemacht, die eine Instanz von LineFormat zurückgibt, um das Erscheinungsbild der Konturen einer Form zu steuern.

Hier ist ein einfaches Verwendungsszenario der Shape.Line-Eigenschaft.

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
### **Shape.Fill-Eigenschaft hinzugefügt**
Aspose.Cells for Java 8.9.2 hat die Shape.Fill-Eigenschaft verfügbar gemacht, die eine Instanz von FillFormat zurückgibt, um die verschiedenen Aspekte des Formbereichs zu steuern.

Im Folgenden finden Sie das einfache Verwendungsszenario der Shape.Fill-Eigenschaft.

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
## **Veraltete APIs**
### **Veraltete ShapeFont-Klasse**
Bitte verwenden Sie stattdessen die TextOptions-Klasse.
### **Veraltete ShapeFormat-Klasse**
Bitte verwenden Sie direkt die Shape.Fill- und Shape.Line-Eigenschaften.
### **Veraltete Shape.Format-Eigenschaft**
Bitte verwenden Sie direkt die Shape.Fill- und Shape.Line-Eigenschaften.
### **Veraltete Shape.LineFormat-Eigenschaft**
Bitte verwenden Sie stattdessen die Shape.Line-Eigenschaft.
### **Veraltete Shape.FillFormat-Eigenschaft**
Bitte verwenden Sie stattdessen die Shape.Fill-Eigenschaft.
### **Veraltete FontSetting.ShapeFont-Eigenschaft**
Bitte verwenden Sie stattdessen die Eigenschaft FontSetting.TextOptions.
