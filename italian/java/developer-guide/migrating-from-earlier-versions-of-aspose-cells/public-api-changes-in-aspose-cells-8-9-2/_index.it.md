---
title: Modifiche all'API pubblica in Aspose.Cells 8.9.2
type: docs
weight: 330
url: /it/java/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.9.1 alla 8.9.2 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

 Si prega di controllare anche il[API pubblica Modifiche introdotte in Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **API aggiunte**
### **Aggiunte classe TextOptions e proprietà FontSettings.TextOptions**
Aspose.Cells for Java ha esposto la classe TextOptions insieme alla proprietà FontSettings.TextOptions per controllare l'aspetto delle parti testuali di una forma.

Ecco un semplice scenario di utilizzo della proprietà FontSettings.TextOptions.

**Giava**

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
### **Aggiunte le proprietà TextOptions.Fill, Outline e Shadow**
 Aspose.Cells for Java 8.9.2 ha esposto le proprietà TextOptions.Fill, TextOptions.Outline e TextOptions.Shadow che consentono di controllare gli aspetti del contenuto testuale della forma, come rispettivamente riempimento, ombra e contorno.

Ecco un semplice scenario di utilizzo delle proprietà di cui sopra.

**Giava**

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
### **Aggiunta la proprietà Shape.Line**
Aspose.Cells for Java ha esposto la proprietà Shape.Line che restituisce un'istanza di LineFormat per controllare l'aspetto dei contorni di una Shape.

Ecco un semplice scenario di utilizzo della proprietà Shape.Line.

**Giava**

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
### **Aggiunta la proprietà Shape.Fill**
Aspose.Cells for Java 8.9.2 ha esposto la proprietà Shape.Fill che restituisce un'istanza di FillFormat per controllare i diversi aspetti dell'area della forma.

Di seguito è riportato il semplice scenario di utilizzo della proprietà Shape.Fill.

**Giava**

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
