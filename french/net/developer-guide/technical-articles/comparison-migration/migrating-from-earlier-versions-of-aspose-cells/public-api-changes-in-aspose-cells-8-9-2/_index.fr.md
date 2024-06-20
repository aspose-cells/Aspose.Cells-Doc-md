---
title: Changements d API public dans Aspose.Cells 8.9.2
type: docs
weight: 320
url: /fr/net/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.9.1 à la 8.9.2 qui pourraient intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, etc., mais aussi une description des changements dans le comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

Veuillez également consulter les [Modifications de l'API publique introduites dans Aspose.Cells for .NET 8.9.1](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **APIs ajoutées**
### **Classe TextOptions ajoutée & Propriété FontSettings.TextOptions ajoutée**
Aspose.Cells for .NET a exposé la classe TextOptions ainsi que la propriété FontSettings.TextOptions afin de contrôler l'apparence des parties textuelles d'une forme.

Voici un scénario d'utilisation simple de la propriété FontSettings.TextOptions.

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


### **Propriétés TextOptions.Fill, Outline & Shadow ajoutées**
Aspose.Cells for .NET 8.9.2 a exposé les propriétés TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow qui permettent de contrôler les aspects du contenu textuel de la forme, tels que le remplissage, l'ombre & le contour respectivement.

Voici un scénario d'utilisation simple des propriétés mentionnées ci-dessus.

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


### **Propriété Shape.Line ajoutée**
Aspose.Cells for .NET a exposé la propriété Shape.Line qui renvoie une instance de LineFormat afin de contrôler l'apparence des contours d'une forme.

Voici un scénario d'utilisation simple de la propriété Shape.Line.

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


### **Propriété Shape.Fill ajoutée**
Aspose.Cells for .NET 8.9.2 a exposé la propriété Shape.Fill qui renvoie une instance de FillFormat afin de contrôler les différents aspects de la zone de la forme.

Voici un exemple d'utilisation simple de la propriété Shape.Fill.

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
