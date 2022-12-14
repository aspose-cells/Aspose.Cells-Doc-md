---
title: Public API Changements dans Aspose.Cells 8.9.2
type: docs
weight: 320
url: /fr/net/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.9.1 à 8.9.2 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

 Veuillez également vérifier le[Public API Modifications introduites dans Aspose.Cells for .NET 8.9.1](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **API ajoutées**
### **Ajout de la classe TextOptions et de la propriété FontSettings.TextOptions**
Aspose.Cells for .NET a exposé la classe TextOptions avec la propriété FontSettings.TextOptions afin de contrôler l'apparence des parties textuelles d'une forme.

Voici un scénario d'utilisation simple de la propriété FontSettings.TextOptions.

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


### **Ajout de TextOptions.Fill, propriétés de contour et d'ombre**
Aspose.Cells for .NET 8.9.2 a exposé les propriétés TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow qui permettent de contrôler les aspects du contenu textuel de la forme, tels que le remplissage, l'ombre et le contour respectivement.

Voici un scénario d'utilisation simple des propriétés susmentionnées.

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


### **Ajout de la propriété Shape.Line**
Aspose.Cells for .NET a exposé la propriété Shape.Line qui renvoie une instance de LineFormat afin de contrôler l'apparence des contours d'une forme.

Voici un scénario d'utilisation simple de la propriété Shape.Line.

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


### **Ajout de la propriété Shape.Fill**
Aspose.Cells for .NET 8.9.2 a exposé la propriété Shape.Fill qui renvoie une instance de FillFormat afin de contrôler les différents aspects de la zone de forme.

Voici le scénario d'utilisation simple de la propriété Shape.Fill.

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
