---
title: Offentlig API Ändringar i Aspose.Cells 8.9.2
type: docs
weight: 330
url: /sv/java/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.9.1 till 8.9.2 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

 Kontrollera också[Offentlig API Ändringar införda i Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **Lade till API:er**
### **Lagt till TextOptions Class & FontSettings.TextOptions Property**
Aspose.Cells for Java har exponerat TextOptions-klassen tillsammans med FontSettings.TextOptions-egenskapen för att kontrollera utseendet på textdelar av en Shape.

Här är ett enkelt användningsscenario för FontSettings.TextOptions-egenskapen.

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
### **Lade till TextOptions.Fill, Outline & Shadow Properties**
 Aspose.Cells for Java 8.9.2 har exponerat egenskaperna TextOptions.Fill, TextOptions.Outline och TextOptions.Shadow som gör det möjligt att kontrollera aspekterna av textinnehållet i formen, såsom fyllning, skugga och kontur respektive.

Här är ett enkelt användningsscenario för ovannämnda egenskaper.

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
### **Lade till Shape.Line-egenskap**
Aspose.Cells for Java har exponerat egenskapen Shape.Line som returnerar en instans av LineFormat för att kontrollera utseendet på konturerna av en Shape.

Här är ett enkelt användningsscenario för Shape.Line-egenskapen.

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
### **Lade till egenskapen Shape.Fill**
Aspose.Cells for Java 8.9.2 har exponerat egenskapen Shape.Fill som returnerar en instans av FillFormat för att kontrollera de olika aspekterna av formområdet.

Följande är det enkla användningsscenariot för Shape.Fill-egenskapen.

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
