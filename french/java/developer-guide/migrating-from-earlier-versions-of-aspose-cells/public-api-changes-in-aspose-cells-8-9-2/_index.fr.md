---
title: Changements d API public dans Aspose.Cells 8.9.2
type: docs
weight: 330
url: /fr/java/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.9.1 à la 8.9.2 qui pourraient intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, etc., mais aussi une description des changements dans le comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

Veuillez également vérifier les [Modifications apportées à l'API publique introduites dans Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **APIs ajoutées**
### **Classe TextOptions ajoutée & Propriété FontSettings.TextOptions ajoutée**
Aspose.Cells for Java a exposé la classe TextOptions ainsi que la propriété FontSettings.TextOptions pour contrôler l'apparence des parties textuelles d'une forme.

Voici un scénario d'utilisation simple de la propriété FontSettings.TextOptions.

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
### **Propriétés TextOptions.Fill, Outline & Shadow ajoutées**
Aspose.Cells for Java 8.9.2 a exposé les propriétés TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow qui permettent de contrôler les aspects des contenus textuels de la forme, tels que le remplissage, l'ombre et le contour respectivement. 

Voici un scénario d'utilisation simple des propriétés mentionnées ci-dessus.

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
### **Propriété Shape.Line ajoutée**
Aspose.Cells for Java a exposé la propriété Shape.Line qui renvoie une instance de LineFormat pour contrôler l'apparence des contours d'une forme.

Voici un scénario d'utilisation simple de la propriété Shape.Line.

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
### **Propriété Shape.Fill ajoutée**
Aspose.Cells for Java 8.9.2 a exposé la propriété Shape.Fill qui renvoie une instance de FillFormat pour contrôler les différents aspects de la zone de la forme.

Voici un exemple d'utilisation simple de la propriété Shape.Fill.

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
## **APIs obsolètes**
### **Classe ShapeFont obsolète**
Veuillez utiliser la classe TextOptions à la place.
### **Classe ShapeFormat obsolète**
Veuillez utiliser directement les propriétés Shape.Fill et Shape.Line.
### **Propriété Shape.Format obsolète**
Veuillez utiliser directement les propriétés Shape.Fill et Shape.Line.
### **Propriété Shape.LineFormat obsolète**
Veuillez utiliser la propriété Shape.Line à la place.
### **Propriété Shape.FillFormat obsolète**
Veuillez utiliser la propriété Shape.Fill à la place.
### **Propriété FontSetting.ShapeFont obsolète**
Veuillez utiliser la propriété FontSetting.TextOptions à la place.
