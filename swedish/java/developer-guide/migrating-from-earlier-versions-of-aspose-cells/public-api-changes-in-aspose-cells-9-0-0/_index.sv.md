---
title: Offentliga API ändringar i Aspose.Cells 9.0.0
type: docs
weight: 340
url: /sv/java/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.9.2 till 9.0.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser osv., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Tillagd Shape.TextOptions-egenskap**
Aspose.Cells for Java har exponerat TextOptions-egenskapen för Shape-klassen för att styra utseendet på textdelar av en Shape.

Här är ett enkelt användningsscenariot för Shape.TextOptions-egenskapen.

**Java**

{{< highlight csharp >}}

 //Initialize an instance of Workbook

Workbook book = new Workbook();

//Get the default Worksheet from the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the collection

int textboxIndex = sheet.getTextBoxes().add(2, 1, 160, 200);

//Get the TextBox object

TextBox textbox = sheet.getTextBoxes().get(textboxIndex);

//Add text to the TextBox

textbox.setText("Hello Aspose!");

//Format the textual contents

textbox.getTextOptions().setColor(Color.getRed());

textbox.getTextOptions().setItalic(true);

textbox.getTextOptions().setBold(true);

{{< /highlight >}}
### **Tillagd ChartPoint.IsInSecondaryPlot-egenskap**
Aspose.Cells for Java har exponerat ChartPoint.IsInSecondaryPlot-egenskapen som kan användas för att upptäcka om en ChartPoint finns på en sekundär plot av en Pie- eller Bar-chart.

Här är ett enkelt användningsscenariot för Shape.Line-egenskapen.

{{% alert color="primary" %}} 

Kolla in den detaljerade artikeln om [Att hitta en datapunkt som finns på den andra plotten](/cells/sv/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load an existing spreadsheet containing a Pie chart

Workbook book = new Workbook(dir + "PieBar.xlsx");

//Load the Worksheet at 0 index

Worksheet sheet = book.getWorksheets().get(0);

//Load the first chart from the collection

Chart chart = sheet.getCharts().get(0);

//Calculate the chart before accessing its properties

chart.calculate();

//Accessing chart's first series

Series series = chart.getNSeries().get(0);

//Loop over the ChartPoint collection

for(int p = 0 ; p < series.getPoints().getCount(); p++)

{

	ChartPoint point = series.getPoints().get(p);



	//Detect if ChartPoint resides on secondary plot

	System.out.println(point.isInSecondaryPlot());

}

{{< /highlight >}}
### **Tillagd OleObject.ClassIdentifier-egenskap**
Aspose.Cells for Java 9.0.0 har exponerat OleObject.ClassIdentifier-egenskapen som kan användas för att specificera beteendet för att ladda en OleObject. Till exempel kan en PPT-fil bäddas in i en kalkylblad med 2 olika vyer, det vill säga presentationsvy eller bildvy, medan båda vyerna har olika klassidentifieringsvärden.

Följande är det enkla användningsscenarioet för OleObject.ClassIdentifier-egenskapen.

{{% alert color="primary" %}} 

Kolla in den detaljerade artikeln om [Användning av OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet containing a presentation as OleObject

Workbook book = new Workbook(dir + "embeddedPresentation.xls");

//Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[] imageData = null;

int x = 0;

int y = 0;

byte[] objData = null;

String progID = "";

int fileFormatType = 0;

String sourceFullName = "";

Boolean isDisplayAsIcon = false;

byte[] classId = null;

//Get the first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Get the first OleObject from the collection

OleObject frame = sheet.getOleObjects().get(0);

//Store the properties in variables

upperLeftRow = frame.getUpperLeftRow();

upperLeftColumn = frame.getUpperLeftColumn();

height = frame.getHeight();

width = frame.getWidth();

imageData = frame.getImageData();

x = frame.getX();

y = frame.getY();

objData = frame.getObjectData();

progID = frame.getProgID();

fileFormatType = frame.getFileFormatType();

sourceFullName = frame.getObjectSourceFullName();

isDisplayAsIcon = frame.getDisplayAsIcon();

classId = frame.getClassIdentifier();

//Initialize a new Workbook instance

book = new Workbook();

//Access first worksheet from the collection

sheet = book.getWorksheets().get(0);

//Insert the OleObject to the worksheet

int oleNumber = sheet.getOleObjects().add(upperLeftRow, upperLeftColumn, height, width, imageData);

//Access newly inserted OleObject

OleObject embeddedObject = sheet.getOleObjects().get(oleNumber);

//Assign previously stored properties to new OleObject

embeddedObject.setX(x);

embeddedObject.setY(y);

embeddedObject.setObjectData(objData);

embeddedObject.setProgID(progID);

embeddedObject.setFileFormatType(fileFormatType);

embeddedObject.setDisplayAsIcon(isDisplayAsIcon);

embeddedObject.setObjectSourceFullName(sourceFullName);

embeddedObject.setAutoSize(false);

if (classId != null)

{

	embeddedObject.setClassIdentifier(classId);

}

{{< /highlight >}}
## **Obsoletterade API:er**
### **Obsolet Worksheet.setBackground-metod**
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
### **Tabort Worksheet.copyConditionalFormatting Metoden**
### **Tabort Workbook.checkWriteProtectedPassword Metoden**
## **Namnändrade API:er**
### **Bytt namn på Workbook.removeDigitallySign Metoden**
Workbook.removeDigitallySign metoden har bytt namn till Workbook.removeDigitalSignature.
