---
title: Modifiche dell API pubblica in Aspose.Cells 8.9.2
type: docs
weight: 330
url: /it/java/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.9.1 a 8.9.2 che possono interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte e rimosse, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

Si prega inoltre di verificare le [Modifiche dell'API pubblica introdotte in Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **API aggiunte**
### **Aggiunta la classe TextOptions e la proprietà FontSettings.TextOptions**
Aspose.Cells for Java ha esposto la classe TextOptions insieme alla proprietà FontSettings.TextOptions al fine di controllare l'aspetto delle parti testuali di una Forma.

Ecco un semplice scenario d'uso della proprietà FontSettings.TextOptions.

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
### **Aggiunte le proprietà TextOptions.Fill, Outline e Shadow**
Aspose.Cells for Java 8.9.2 ha esposto le proprietà TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow che consentono di controllare gli aspetti dei contenuti testuali della forma, come riempimento, ombreggiatura & contorno rispettivamente. 

Ecco un semplice scenario di utilizzo delle proprietà sopra menzionate.

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
### **Aggiunta la proprietà Shape.Line**
Aspose.Cells for Java ha esposto la proprietà Shape.Line che restituisce un'istanza di LineFormat al fine di controllare l'aspetto dei contorni di una Forma.

Ecco un semplice scenario d'uso della proprietà Shape.Line.

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
### **Aggiunta la proprietà Shape.Fill**
Aspose.Cells for Java 8.9.2 ha esposto la proprietà Shape.Fill che restituisce un'istanza di FillFormat al fine di controllare gli aspetti diversi dell'area della forma.

Di seguito è riportato un semplice scenario d'uso della proprietà Shape.Fill.

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
