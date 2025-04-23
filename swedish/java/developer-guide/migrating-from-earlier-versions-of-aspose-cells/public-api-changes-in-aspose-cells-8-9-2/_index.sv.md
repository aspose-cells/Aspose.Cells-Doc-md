---
title: Offentliga API ändringar i Aspose.Cells 8.9.2
type: docs
weight: 330
url: /sv/java/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna i Aspose.Cells API från version 8.9.1 till 8.9.2 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

Vänligen kontrollera även [Offentliga API-ändringar som introducerades i Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **Tillagda API:er**
### **Tillagd TextOptions Klass & FontSettings.TextOptions Egendom**
Aspose.Cells for Java har exponerat TextOptions-klassen tillsammans med FontSettings.TextOptions egendomen för att styra utseendet på textdelar av en form.

Här är det enkla användningscenariot för FontSettings.TextOptions egendomen.

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
### **Tillagd TextOptions.Fill, Outline & Shadow Egenskaper**
Aspose.Cells for Java 8.9.2 har exponerat TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow egenskaperna som tillåter att styra aspekterna av textinnehållet i formen, såsom fyllning, skugga & kontur respektive. 

Här är det enkla användningscenariot för ovanstående egenskaper.

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
### **Tillagd Shape.Line Egendom**
Aspose.Cells for Java har exponerat Shape.Line egendomen som returnerar en instans av LineFormat för att styra utseendet på konturerna av en form.

Här är ett enkelt användningsscenariot för Shape.Line-egenskapen.

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
### **Tillagd Shape.Fill Egendom**
Aspose.Cells for Java 8.9.2 har exponerat Shape.Fill egendomen som returnerar en instans av FillFormat för att styra olika aspekter av formområdet.

Följande är det enkla användningscenariot för Shape.Fill egendomen.

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
{{< app/cells/assistant language="java" >}}
