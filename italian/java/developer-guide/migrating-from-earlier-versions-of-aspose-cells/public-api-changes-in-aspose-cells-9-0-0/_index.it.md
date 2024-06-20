---
title: Modifiche dell API pubblica in Aspose.Cells 9.0.0
type: docs
weight: 340
url: /it/java/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.9.2 a 9.0.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici aggiornati, classi aggiunte e rimosse, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Aggiunta proprietà Shape.TextOptions**
Aspose.Cells for Java ha esposto la proprietà TextOptions per la classe Shape al fine di controllare l'aspetto delle parti testuali di una Forma.

Ecco un semplice scenario di utilizzo della proprietà Shape.TextOptions.

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
### **Aggiunta proprietà ChartPoint.IsInSecondaryPlot**
Aspose.Cells for Java ha esposto la proprietà ChartPoint.IsInSecondaryPlot che può essere utilizzata per rilevare se un ChartPoint risiede su un secondo tracciato di un grafico a torta o a barre.

Ecco un semplice scenario d'uso della proprietà Shape.Line.

{{% alert color="primary" %}} 

Consultare l'articolo dettagliato su [Individuare se un punto dati risiede nel secondo tracciato](/cells/it/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

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
### **Aggiunta la proprietà OleObject.ClassIdentifier.**
Aspose.Cells for Java 9.0.0 ha esposto la proprietà OleObject.ClassIdentifier che può essere utilizzata per specificare il comportamento dell'applicazione per caricare un OleObject. Ad esempio, un file PPT può essere incorporato in un foglio di calcolo con 2 visualizzazioni diverse, ovvero; visualizzazione di presentazione o visualizzazione di diapositiva, mentre entrambe le visualizzazioni hanno valori di identificatore di classe diversi.

Ecco il semplice scenario d'uso della proprietà OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

Consultare l'articolo dettagliato su [Utilizzo di OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

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
## **API deprecate**
### **Metodo Worksheet.setBackground obsoleto**
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
### **Metodo Worksheet.copyConditionalFormatting eliminato**
### **Metodo Workbook.checkWriteProtectedPassword eliminato**
## **API Rinominate**
### **Il Metodo Workbook.removeDigitallySign è stato Rinominato**
Il metodo Workbook.removeDigitallySign è stato rinominato in Workbook.removeDigitalSignature.
