---
title: Öffentlich API Änderungen in Aspose.Cells 9.0.0
type: docs
weight: 330
url: /de/net/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.9.2 zu 9.0.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Shape.TextOptions-Eigenschaft hinzugefügt**
Aspose.Cells for .NET hat die TextOptions-Eigenschaft für die Shape-Klasse verfügbar gemacht, um das Erscheinungsbild von Textteilen einer Shape zu steuern.

Hier ist ein einfaches Verwendungsszenario der Shape.TextOptions-Eigenschaft.

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


### **LoadOptions.CultureInfo-Eigenschaft hinzugefügt**
Aspose.Cells for .NET 9.0.0 hat die LoadOptions.CultureInfo-Eigenschaft verfügbar gemacht, die es ermöglicht, eine Instanz von CultureInfo zum Zeitpunkt des Ladens eines Dokuments in eine Instanz von Workbook einzufügen.

Hier ist ein einfaches Nutzungsszenario der oben genannten Eigenschaften.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Laden der Tabelle mit spezifischen CultureInfo](/cells/de/net/load-the-workbook-with-specific-system-culture-info/).

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


### **ChartPoint.IsInSecondaryPlot-Eigenschaft hinzugefügt**
Aspose.Cells for .NET hat die ChartPoint.IsInSecondaryPlot-Eigenschaft verfügbar gemacht, die verwendet werden kann, um zu erkennen, ob sich ein ChartPoint auf einem sekundären Diagramm eines Kreis- oder Balkendiagramms befindet.

Hier ist ein einfaches Verwendungsszenario der Shape.Line-Eigenschaft.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Das Finden eines Datenpunkts befindet sich auf dem zweiten Plot](/cells/de/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

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


### **OleObject.ClassIdentifier-Eigenschaft hinzugefügt**
Aspose.Cells for .NET 9.0.0 hat die OleObject.ClassIdentifier-Eigenschaft verfügbar gemacht, die verwendet werden kann, um das Anwendungsverhalten zum Laden eines OleObject anzugeben. Beispielsweise kann eine PPT-Datei in eine Tabellenkalkulation mit 2 verschiedenen Ansichten eingebettet werden, das heißt; Präsentationsansicht oder Folienansicht, wobei beide Ansichten unterschiedliche Klassenkennungswerte haben.

Im Folgenden finden Sie das einfache Verwendungsszenario der OleObject.ClassIdentifier-Eigenschaft.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Verwenden von OleObject.ClassIdentifier](/cells/de/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

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
## **Veraltete APIs**
### **Veraltete Worksheet.SetBackground-Methode**
Bitte verwenden Sie stattdessen die Worksheet.BackgroundImage-Eigenschaft.
### **Veraltete LineShape.BeginArrowheadStyle- und ArcShape.BeginArrowheadStyle-Eigenschaften**
Bitte verwenden Sie alternativ die Eigenschaft Shape.Line.BeginArrowheadStyle.
### **Veraltete LineShape.EndArrowheadStyle- und ArcShape.EndArrowheadStyle-Eigenschaften**
Bitte verwenden Sie alternativ die Eigenschaft Shape.Line.EndArrowheadStyle.
### **Veraltete LineShape.BeginArrowheadWidth- und ArcShape.BeginArrowheadWidth-Eigenschaften**
Bitte verwenden Sie alternativ die Eigenschaft Shape.Line.BeginArrowheadWidth.
### **Veraltete LineShape.BeginArrowheadLength- und ArcShape.BeginArrowheadLength-Eigenschaften**
Bitte verwenden Sie stattdessen die Eigenschaft Shape.Line.BeginArrowheadLength.
### **Veraltete LineShape.EndArrowheadWidth- und ArcShape.EndArrowheadWidth-Eigenschaften**
Bitte verwenden Sie stattdessen die Eigenschaft Shape.Line.EndArrowheadWidth.
### **Veraltete LineShape.EndArrowheadLength- und ArcShape.EndArrowheadLength-Eigenschaften**
Bitte verwenden Sie stattdessen die Eigenschaft Shape.Line.EndArrowheadLength.
## **Gelöschte APIs**
### **Gelöschte Worksheet.CopyConditionalFormatting-Methode**
### **Gelöschte Workbook.CheckWriteProtectedPassword-Methode**
## **Umbenannte APIs**
### **Workbook.RemoveDigitallySign-Methode umbenannt**
Die Workbook.RemoveDigitallySign-Methode wurde in Workbook.RemoveDigitalSignature umbenannt.
