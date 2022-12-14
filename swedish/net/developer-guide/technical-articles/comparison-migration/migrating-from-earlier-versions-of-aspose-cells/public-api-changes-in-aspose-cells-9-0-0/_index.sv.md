---
title: Offentliga API-ändringar i Aspose.Cells 9.0.0
type: docs
weight: 330
url: /sv/net/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna av Aspose.Cells API från version 8.9.2 till 9.0.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Lade till Shape.TextOptions-egenskap**
Aspose.Cells för .NET har exponerat egenskapen TextOptions för Shape-klassen för att kontrollera utseendet på textdelar av en Shape.

Här är ett enkelt användningsscenario för Shape.TextOptions-egenskapen.

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


### **Lade till egenskapen LoadOptions.CultureInfo**
Aspose.Cells för .NET 9.0.0 har avslöjat egenskapen LoadOptions.CultureInfo som tillåter injicera en instans av CultureInfo vid tidpunkten för inläsning av ett dokument i en instans av Workbook.

Här är ett enkelt användningsscenario för ovannämnda egenskaper.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Laddar kalkylblad med specifik kulturinformation](/cells/sv/net/load-the-workbook-with-specific-system-culture-info/).

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


### **Lade till egenskapen ChartPoint.IsInSecondaryPlot**
Aspose.Cells för .NET har exponerat egenskapen ChartPoint.IsInSecondaryPlot som kan användas för att upptäcka om en ChartPoint finns på en sekundär plot av ett cirkel- eller stapeldiagram.

Här är ett enkelt användningsscenario för Shape.Line-egenskapen.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Att hitta en DataPoint ligger på den andra plotten](/cells/sv/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

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


### **Lade till egenskapen OleObject.ClassIdentifier**
Aspose.Cells för .NET 9.0.0 har avslöjat egenskapen OleObject.ClassIdentifier som kan användas för att specificera programmets beteende för att ladda ett OleObject. Till exempel kan en PPT-fil bäddas in i ett kalkylblad med 2 olika vyer, det vill säga; presentationsvy eller bildvy, medan båda vyerna har olika klassidentifieringsvärden.

Följande är det enkla användningsscenariot för egenskapen OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Använder OleObject.ClassIdentifier](/cells/sv/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

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
## **Föråldrade API:er**
### **Föråldrat arbetsblad.Setbakgrundsmetod**
Använd egenskapen Worksheet.BackgroundImage istället.
### **Föråldrad LineShape.BeginArrowheadStyle & ArcShape.BeginArrowheadStyle-egenskaper**
Använd egenskapen Shape.Line.BeginArrowheadStyle som ett alternativ.
### **Föråldrad LineShape.EndArrowheadStyle & ArcShape.EndArrowheadStyle-egenskaper**
Använd egenskapen Shape.Line.EndArrowheadStyle som ett alternativ.
### **Föråldrad LineShape.BeginArrowheadWidth & ArcShape.BeginArrowheadWidth egenskaper**
Använd egenskapen Shape.Line.BeginArrowheadWidth som ett alternativ.
### **Föråldrad LineShape.BeginArrowheadLength & ArcShape.BeginArrowheadLength Egenskaper**
Använd egenskapen Shape.Line.BeginArrowheadLength istället.
### **Föråldrad LineShape.EndArrowheadWidth & ArcShape.EndArrowheadWidth egenskaper**
Använd egenskapen Shape.Line.EndArrowheadWidth istället.
### **Föråldrad LineShape.EndArrowheadLength & ArcShape.EndArrowheadLength egenskaper**
Använd egenskapen Shape.Line.EndArrowheadLength istället.
## **Borttagna API:er**
### **Borttaget arbetsblad.CopyConditionalFormatting Method**
### **Borttagen Workbook.CheckWriteProtectedPassword Method**
## **Omdöpta API:er**
### **Byt namn på Workbook.RemoveDigitallySign Method**
Metoden Workbook.RemoveDigitalSign har bytt namn till Workbook.RemoveDigitalSignature.
