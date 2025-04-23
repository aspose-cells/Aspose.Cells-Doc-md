---
title: Offentliga API ändringar i Aspose.Cells 9.0.0
type: docs
weight: 330
url: /sv/net/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.9.2 till 9.0.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser osv., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Tillagd Shape.TextOptions-egenskap**
Aspose.Cells for .NET har exponerat TextOptions-egenskapen för Shape-klassen för att styra utseendet på textdelar av en form.

Här är ett enkelt användningsscenariot för Shape.TextOptions-egenskapen.

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


### **Tillagd LoadOptions.CultureInfo-egenskap**
Aspose.Cells for .NET 9.0.0 har exponerat LoadOptions.CultureInfo-egenskapen som möjliggör att injicera en instans av CultureInfo vid laddning av ett dokument i en instans av Workbook.

Här är det enkla användningscenariot för ovanstående egenskaper.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Laddning av kalkylblad med specifik CultureInfo](/cells/sv/net/load-the-workbook-with-specific-system-culture-info/).

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


### **Tillagd ChartPoint.IsInSecondaryPlot-egenskap**
Aspose.Cells for .NET har expons ChartPoint.IsInSecondaryPlot-egenskapen som kan användas för att upptäcka om en ChartPoint finns på en sekundär plott av en Pie- eller Bar-diagram.

Här är ett enkelt användningsscenariot för Shape.Line-egenskapen.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Att hitta en datapunkt som finns på den andra kartan](/cells/sv/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

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


### **Tillagd OleObject.ClassIdentifier-egenskap**
Aspose.Cells for .NET 9.0.0 har exponerat OleObject.ClassIdentifier-egenskapen som kan användas för att ange applikationsbeteendet för att ladda en OleObject. Till exempel kan en PPT-fil bäddas in i ett kalkylblad med 2 olika vyer, det vill säga presentationsvy eller bildvy, medan båda vyerna har olika klassidentifierarvärden.

Följande är det enkla användningsscenarioet för OleObject.ClassIdentifier-egenskapen.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Att använda OleObject.ClassIdentifier](/cells/sv/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

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
## **Obsoletterade API:er**
### **Föråldrat Worksheet.SetBackground-metoden**
Använd istället Worksheet.BackgroundImage-egenskapen.
### **Obsoletterade LineShape.BeginArrowheadStyle- och ArcShape.BeginArrowheadStyle-egenskaper**
Använd Shape.Line.BeginArrowheadStyle-egenskapen som ett alternativ.
### **Obsoletterade LineShape.EndArrowheadStyle- och ArcShape.EndArrowheadStyle-egenskaper**
Använd Shape.Line.EndArrowheadStyle-egenskapen som ett alternativ.
### **Obsoletterade LineShape.BeginArrowheadWidth- och ArcShape.BeginArrowheadWidth-egenskaper**
Använd Shape.Line.BeginArrowheadWidth-egenskapen som ett alternativ.
### **Obsoletad LineShape.BeginArrowheadLength och ArcShape.BeginArrowheadLength Egenskaper**
Använd istället Shape.Line.BeginArrowheadLength egenskapen.
### **Obsoletad LineShape.EndArrowheadWidth och ArcShape.EndArrowheadWidth Egenskaper**
Använd istället Shape.Line.EndArrowheadWidth egenskapen.
### **Obsoletad LineShape.EndArrowheadLength och ArcShape.EndArrowheadLength Egenskaper**
Använd istället Shape.Line.EndArrowheadLength egenskapen.
## **Raderade API:er**
### **Raderad Worksheet.CopyConditionalFormatting-metoden**
### **Raderad Workbook.CheckWriteProtectedPassword-metoden**
## **Namnändrade API:er**
### **Ändrad namn på Workbook.RemoveDigitallySign-metoden**
Workbook.RemoveDigitallySign-metoden har ändrats namn till Workbook.RemoveDigitalSignature.
{{< app/cells/assistant language="csharp" >}}
