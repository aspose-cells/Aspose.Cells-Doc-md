---
title: Public API Changements dans Aspose.Cells 9.0.0
type: docs
weight: 330
url: /fr/net/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.9.2 à 9.0.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Ajout de la propriété Shape.TextOptions**
Aspose.Cells for .NET a exposé la propriété TextOptions pour la classe Shape afin de contrôler l'apparence des parties textuelles d'un Shape.

Voici un scénario d'utilisation simple de la propriété Shape.TextOptions.

**C#**

{{< highlight "csharp" >}}

 // Initialize an instance of Workbook

var book = new Workbook();

// Get the default Worksheet from the Workbook

var sheet = book.Worksheets[0];

// Add a TextBox to the collection

var textboxIndex = sheet.TextBoxes.Add(2, 1, 160, 200);

// Get the TextBox object

var textbox = sheet.TextBoxes[textboxIndex];

// Add text to the TextBox

textbox.Text = "Hello Aspose!";

// Format the textual contents

textbox.TextOptions.Color = System.Drawing.Color.Red;

textbox.TextOptions.IsItalic = true;

{{< /highlight >}}


### **Ajout de la propriété LoadOptions.CultureInfo**
Aspose.Cells for .NET 9.0.0 a exposé la propriété LoadOptions.CultureInfo qui permet d'injecter une instance de CultureInfo au moment du chargement d'un document dans une instance de Workbook.

Voici un scénario d'utilisation simple des propriétés susmentionnées.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Chargement d'une feuille de calcul avec CultureInfo spécifique](/cells/fr/net/load-the-workbook-with-specific-system-culture-info/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of CultureInfo and populate its properties

var culture = new CultureInfo("en-GB");

culture.NumberFormat.NumberDecimalSeparator = ",";

culture.DateTimeFormat.DateSeparator = "-";

culture.DateTimeFormat.ShortDatePattern = "dd-MM-yyyy";

// Create an instance of LoadOptions and set the CultureInfo property

var options = new LoadOptions(LoadFormat.Html);

options.CultureInfo = culture;

// Load a HTML or TXT file in an instance of Workbook with instance of  LoadOptions

var book = new Workbook(dir + "input.html", options);

{{< /highlight >}}


### **Ajout de la propriété ChartPoint.IsInSecondaryPlot**
Aspose.Cells for .NET a exposé la propriété ChartPoint.IsInSecondaryPlot qui peut être utilisée pour détecter si un ChartPoint réside sur un tracé secondaire d'un graphique à secteurs ou à barres.

Voici un scénario d'utilisation simple de la propriété Shape.Line.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Trouver un point de données réside sur le deuxième tracé](/cells/fr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load an existing spreadsheet containing a Pie chart

var book = new Workbook(dir + "PieBar.xlsx");

// Load the Worksheet at 0 index

var sheet = book.Worksheets[0];

// Load the first chart from the collection

var chart = sheet.Charts[0];

// Calculate the chart before accessing its properties

chart.Calculate();

// Accessing chart's first series

var series = chart.NSeries[0];

// Loop over the ChartPoint collection

foreach (ChartPoint point in series.Points)

{

    // Detect if ChartPoint resides on secondary plot

    Console.WriteLine(point.IsInSecondaryPlot);

}

{{< /highlight >}}


### **Ajout de la propriété OleObject.ClassIdentifier**
Aspose.Cells for .NET 9.0.0 a exposé la propriété OleObject.ClassIdentifier qui peut être utilisée pour spécifier le comportement de l'application pour charger un OleObject. Par exemple, un fichier PPT peut être intégré dans une feuille de calcul avec 2 vues différentes, c'est-à-dire ; vue de présentation ou vue de diapositive, alors que les deux vues ont des valeurs d'identificateur de classe différentes.

Voici le scénario d'utilisation simple de la propriété OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

 Consultez l'article détaillé sur[Utilisation d'OleObject.ClassIdentifier](/cells/fr/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load a spreadsheet containing a presentation as OleObject

var book = new Workbook(dir + "embeddedPresentation.xls");

// Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[]imageData = null;

int x = 0;

int y = 0;

byte[]objData = null;

string progID = "";

FileFormatType fileFormatType = FileFormatType.Unknown;

string sourceFullName = "";

bool isDisplayAsIcon = false;

byte[]classId = null;

// Get the first worksheet from the collection

var sheet = book.Worksheets[0];

// Get the first OleObject from the collection

var frame = sheet.OleObjects[0];

// Store the properties in variables

upperLeftRow = frame.UpperLeftRow;

upperLeftColumn = frame.UpperLeftColumn;

height = frame.Height;

width = frame.Width;

imageData = frame.ImageData;

x = frame.X;

y = frame.Y;

objData = frame.ObjectData;

progID = frame.ProgID;

fileFormatType = frame.FileFormatType;

sourceFullName = frame.ObjectSourceFullName;

isDisplayAsIcon = frame.DisplayAsIcon;

classId = frame.ClassIdentifier;

// Initialize a new Workbook instance

book = new Workbook();

// Access first worksheet from the collection

sheet = book.Worksheets[0];

// Insert the OleObject to the worksheet

int oleNumber = sheet.OleObjects.Add(upperLeftRow, upperLeftColumn, height, width, imageData);

// Access newly inserted OleObject

var embeddedObject = sheet.OleObjects[oleNumber];

// Assign previously stored properties to new OleObject

embeddedObject.X = x;

embeddedObject.Y = y;

embeddedObject.ObjectData = objData;

embeddedObject.ProgID = progID;

embeddedObject.FileFormatType = fileFormatType;

embeddedObject.DisplayAsIcon = isDisplayAsIcon;

embeddedObject.ObjectSourceFullName = sourceFullName;

embeddedObject.IsAutoSize = false;

if (classId != null)

{

    embeddedObject.ClassIdentifier = classId;

}

// Save the resultant spreadsheet

book.Save(dir  + "output.xls");

{{< /highlight >}}
## **API obsolètes**
### **Méthode Worksheet.SetBackground obsolète**
Veuillez utiliser la propriété Worksheet.BackgroundImage à la place.
### **Propriétés obsolètes de LineShape.BeginArrowheadStyle et ArcShape.BeginArrowheadStyle**
Veuillez utiliser la propriété Shape.Line.BeginArrowheadStyle comme alternative.
### **Propriétés obsolètes de LineShape.EndArrowheadStyle et ArcShape.EndArrowheadStyle**
Veuillez utiliser la propriété Shape.Line.EndArrowheadStyle comme alternative.
### **Propriétés obsolètes de LineShape.BeginArrowheadWidth et ArcShape.BeginArrowheadWidth**
Veuillez utiliser la propriété Shape.Line.BeginArrowheadWidth comme alternative.
### **Propriétés obsolètes de LineShape.BeginArrowheadLength et ArcShape.BeginArrowheadLength**
Veuillez utiliser la propriété Shape.Line.BeginArrowheadLength à la place.
### **Propriétés obsolètes de LineShape.EndArrowheadWidth et ArcShape.EndArrowheadWidth**
Veuillez utiliser la propriété Shape.Line.EndArrowheadWidth à la place.
### **Propriétés obsolètes de LineShape.EndArrowheadLength et ArcShape.EndArrowheadLength**
Veuillez utiliser la propriété Shape.Line.EndArrowheadLength à la place.
## **API supprimées**
### **Méthode Worksheet.CopyConditionalFormatting supprimée**
### **Méthode Workbook.CheckWriteProtectedPassword supprimée**
## **API renommées**
### **Méthode Workbook.RemoveDigitallySign renommée**
La méthode Workbook.RemoveDigitallySign a été renommée Workbook.RemoveDigitalSignature.
