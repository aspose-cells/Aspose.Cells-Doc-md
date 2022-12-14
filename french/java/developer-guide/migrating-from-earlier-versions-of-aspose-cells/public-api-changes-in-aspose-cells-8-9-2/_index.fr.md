---
title: Public API Changements dans Aspose.Cells 8.9.2
type: docs
weight: 330
url: /fr/java/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.9.1 à 8.9.2 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

 Veuillez également vérifier le[Public API Modifications introduites dans Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **API ajoutées**
### **Ajout de la classe TextOptions et de la propriété FontSettings.TextOptions**
Aspose.Cells for Java a exposé la classe TextOptions avec la propriété FontSettings.TextOptions afin de contrôler l'apparence des parties textuelles d'une forme.

Voici un scénario d'utilisation simple de la propriété FontSettings.TextOptions.

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
### **Ajout de TextOptions.Fill, propriétés de contour et d'ombre**
 Aspose.Cells for Java 8.9.2 a exposé les propriétés TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow qui permettent de contrôler les aspects du contenu textuel de la forme, tels que le remplissage, l'ombre et le contour respectivement.

Voici un scénario d'utilisation simple des propriétés susmentionnées.

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
### **Ajout de la propriété Shape.Line**
Aspose.Cells for Java a exposé la propriété Shape.Line qui renvoie une instance de LineFormat afin de contrôler l'apparence des contours d'une forme.

Voici un scénario d'utilisation simple de la propriété Shape.Line.

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
### **Ajout de la propriété Shape.Fill**
Aspose.Cells for Java 8.9.2 a exposé la propriété Shape.Fill qui renvoie une instance de FillFormat afin de contrôler les différents aspects de la zone de forme.

Voici le scénario d'utilisation simple de la propriété Shape.Fill.

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
## **API obsolètes**
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
