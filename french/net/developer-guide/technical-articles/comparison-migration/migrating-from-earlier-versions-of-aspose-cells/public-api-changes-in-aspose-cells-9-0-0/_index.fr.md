---
title: Changements d API publics dans Aspose.Cells 9.0.0
type: docs
weight: 330
url: /fr/net/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.9.2 à la version 9.0.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Propriété Shape.TextOptions ajoutée**
Aspose.Cells for .NET a exposé la propriété TextOptions pour la classe Shape afin de contrôler l'apparence des parties textuelles d'une forme.

Voici un scénario d'utilisation simple de la propriété Shape.TextOptions.

**C#**

{{< highlight csharp >}}

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


### **Propriété LoadOptions.CultureInfo ajoutée**
Aspose.Cells for .NET 9.0.0 a exposé la propriété LoadOptions.CultureInfo qui permet d'injecter une instance de CultureInfo au moment du chargement d'un document dans une instance de Workbook.

Voici un scénario d'utilisation simple des propriétés mentionnées ci-dessus.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Chargement de feuilles de calcul avec une culture spécifique](/cells/fr/net/load-the-workbook-with-specific-system-culture-info/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Propriété ChartPoint.IsInSecondaryPlot ajoutée**
Aspose.Cells for .NET a exposé la propriété ChartPoint.IsInSecondaryPlot qui peut être utilisée pour détecter si un ChartPoint réside sur un tracé secondaire d'un graphique circulaire ou à barres.

Voici un scénario d'utilisation simple de la propriété Shape.Line.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Trouver un DataPoint qui réside sur le Second Plot](/cells/fr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Propriété OleObject.ClassIdentifier ajoutée**
Aspose.Cells for .NET 9.0.0 a exposé la propriété OleObject.ClassIdentifier qui peut être utilisée pour spécifier le comportement de l'application pour charger un OleObject. Par exemple, un fichier PPT peut être incorporé dans une feuille de calcul avec 2 vues différentes, à savoir la vue de présentation ou la vue de diapositive, chaque vue ayant des valeurs de classe d'identifiant différentes.

Voici un scénario d'utilisation simple de la propriété OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Using OleObject.ClassIdentifier](/cells/fr/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet containing a presentation as OleObject

var book = new Workbook(dir + "embeddedPresentation.xls");

// Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[] imageData = null;

int x = 0;

int y = 0;

byte[] objData = null;

string progID = "";

FileFormatType fileFormatType = FileFormatType.Unknown;

string sourceFullName = "";

bool isDisplayAsIcon = false;

byte[] classId = null;

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
## **APIs obsolètes**
### **Méthode Worksheet.SetBackground obsolète**
Veuillez utiliser la propriété Worksheet.BackgroundImage à la place.
### **Propriétés LineShape.BeginArrowheadStyle & ArcShape.BeginArrowheadStyle obsolètes**
Veuillez utiliser la propriété Shape.Line.BeginArrowheadStyle comme alternative.
### **Propriétés LineShape.EndArrowheadStyle & ArcShape.EndArrowheadStyle obsolètes**
Veuillez utiliser la propriété Shape.Line.EndArrowheadStyle comme alternative.
### **Propriétés LineShape.BeginArrowheadWidth et ArcShape.BeginArrowheadWidth obsolètes**
Veuillez utiliser la propriété Shape.Line.BeginArrowheadWidth comme alternative.
### **Propriétés LineShape.BeginArrowheadLength et ArcShape.BeginArrowheadLength obsolètes**
Veuillez utiliser la propriété Shape.Line.BeginArrowheadLength à la place.
### **Propriétés LineShape.EndArrowheadWidth et ArcShape.EndArrowheadWidth obsolètes**
Veuillez utiliser la propriété Shape.Line.EndArrowheadWidth à la place.
### **Propriétés LineShape.EndArrowheadLength et ArcShape.EndArrowheadLength obsolètes**
Veuillez utiliser la propriété Shape.Line.EndArrowheadLength à la place.
## **APIs supprimées**
### **Méthode Worksheet.CopyConditionalFormatting supprimée**
### **Méthode Workbook.CheckWriteProtectedPassword supprimée**
## **API renommées**
### **Méthode Workbook.RemoveDigitallySign renommée**
La méthode Workbook.RemoveDigitallySign a été renommée en Workbook.RemoveDigitalSignature.
{{< app/cells/assistant language="csharp" >}}
