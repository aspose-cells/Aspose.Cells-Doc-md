---
title: Modifiche dell API pubblica in Aspose.Cells 9.0.0
type: docs
weight: 330
url: /it/net/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.9.2 a 9.0.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici aggiornati, classi aggiunte e rimosse, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Aggiunta proprietà Shape.TextOptions**
Aspose.Cells for .NET ha esposto la proprietà TextOptions per la classe Shape al fine di controllare l'aspetto delle parti testuali di una forma.

Ecco un semplice scenario di utilizzo della proprietà Shape.TextOptions.

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


### **Aggiunta proprietà LoadOptions.CultureInfo**
Aspose.Cells for .NET 9.0.0 ha esposto la proprietà LoadOptions.CultureInfo che consente di iniettare un'istanza di CultureInfo al momento del caricamento di un documento in un'istanza di Workbook.

Ecco un semplice scenario di utilizzo delle proprietà sopra menzionate.

{{% alert color="primary" %}} 

Consulta l'articolo dettagliato su [Caricamento del foglio di calcolo con CultureInfo specifica](/cells/it/net/load-the-workbook-with-specific-system-culture-info/).

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


### **Aggiunta proprietà ChartPoint.IsInSecondaryPlot**
Aspose.Cells for .NET ha esposto la proprietà ChartPoint.IsInSecondaryPlot che può essere utilizzata per rilevare se un ChartPoint risiede su un tracciato secondario di un grafico a torta o a barre.

Ecco un semplice scenario d'uso della proprietà Shape.Line.

{{% alert color="primary" %}} 

Controlla l'articolo dettagliato su [Ricerca di un DataPoint residente sul Secondo Plot](/cells/it/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

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


### **Aggiunta la proprietà OleObject.ClassIdentifier.**
Aspose.Cells for .NET 9.0.0 ha esposto la proprietà OleObject.ClassIdentifier che può essere utilizzata per specificare il comportamento dell'applicazione per caricare un OleObject. Ad esempio, un file PPT può essere incorporato in un foglio di calcolo con 2 visualizzazioni diverse, cioè; visualizzazione presentazione o visualizzazione diapositiva, mentre entrambe le visualizzazioni hanno valori di identificatore di classe diversi.

Ecco il semplice scenario d'uso della proprietà OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

Controlla l'articolo dettagliato su [Utilizzo di OleObject.ClassIdentifier](/cells/it/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

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
## **API deprecate**
### **Metodo Worksheet.SetBackground reso obsoleto**
Si prega di utilizzare invece la proprietà Worksheet.BackgroundImage.
### **Proprietà LineShape.BeginArrowheadStyle & ArcShape.BeginArrowheadStyle rese obsolete**
Si prega di utilizzare la proprietà Shape.Line.BeginArrowheadStyle come alternativa.
### **Proprietà LineShape.EndArrowheadStyle & ArcShape.EndArrowheadStyle rese obsolete**
Si prega di utilizzare la proprietà Shape.Line.EndArrowheadStyle come alternativa.
### **Proprietà LineShape.BeginArrowheadWidth & ArcShape.BeginArrowheadWidth rese obsolete**
Si prega di utilizzare la proprietà Shape.Line.BeginArrowheadWidth come alternativa.
### **Proprietà LineShape.BeginArrowheadLength & ArcShape.BeginArrowheadLength rese obsolete**
Si prega di utilizzare la proprietà Shape.Line.BeginArrowheadLength invece.
### **Proprietà LineShape.EndArrowheadWidth & ArcShape.EndArrowheadWidth rese obsolete**
Si prega di utilizzare la proprietà Shape.Line.EndArrowheadWidth invece.
### **Proprietà Obsoleta LineShape.EndArrowheadLength & ArcShape.EndArrowheadLength**
Si prega di utilizzare la proprietà Shape.Line.EndArrowheadLength.
## **API eliminate**
### **Metodo Worksheet.CopyConditionalFormatting cancellato**
### **Metodo Workbook.CheckWriteProtectedPassword cancellato**
## **API Rinominate**
### **Metodo Workbook.RemoveDigitallySign rinominato**
Il metodo Workbook.RemoveDigitallySign è stato rinominato in Workbook.RemoveDigitalSignature.
