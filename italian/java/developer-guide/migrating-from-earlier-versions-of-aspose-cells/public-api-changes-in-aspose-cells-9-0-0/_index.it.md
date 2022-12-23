---
title: Pubblico API Modifiche in Aspose.Cells 9.0.0
type: docs
weight: 340
url: /it/java/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.9.2 alla 9.0.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Proprietà Shape.TextOptions aggiunta**
Aspose.Cells for Java ha esposto la proprietà TextOptions per la classe Shape per controllare l'aspetto delle parti testuali di una Shape.

Ecco un semplice scenario di utilizzo della proprietà Shape.TextOptions.

**Java**

{{< highlight "csharp" >}}

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
### **Proprietà ChartPoint.IsInSecondaryPlot aggiunta**
Aspose.Cells for Java ha esposto la proprietà ChartPoint.IsInSecondaryPlot che può essere utilizzata per rilevare se un ChartPoint si trova su un grafico secondario di un grafico a torta oa barre.

Ecco un semplice scenario di utilizzo della proprietà Shape.Line.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[La ricerca di un punto dati risiede nel secondo grafico](/cells/it/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Carica un foglio di calcolo esistente contenente un grafico a torta

Libro della cartella di lavoro = nuova cartella di lavoro (dir + "PieBar.xlsx");

//Carica il foglio di lavoro all'indice 0

Foglio di lavoro = book.getWorksheets().get(0);

//Carica il primo grafico dalla raccolta

Grafico chart = sheet.getCharts().get(0);

//Calcola il grafico prima di accedere alle sue proprietà

grafico.calcola();

//Accesso alla prima serie del grafico

Serie serie = chart.getNSeries().get(0);

//Ripeti la collezione ChartPoint

 for(int p = 0 ; p< series.getPoints().getCount(); p++)

{

	ChartPoint point = series.getPoints().get(p);



	//Detect if ChartPoint resides on secondary plot

	System.out.println(point.isInSecondaryPlot());

}

{{< /highlight >}}
### **Aggiunta proprietà OleObject.ClassIdentifier**
Aspose.Cells for Java 9.0.0 ha esposto la proprietà OleObject.ClassIdentifier che può essere utilizzata per specificare il comportamento dell'applicazione per caricare un OleObject. Ad esempio, un file PPT può essere incorporato in un foglio di calcolo con 2 viste diverse, ovvero; vista presentazione o vista diapositiva, mentre entrambe le viste hanno valori di identificatore di classe diversi.

Di seguito è riportato il semplice scenario di utilizzo della proprietà OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

 Controlla l'articolo dettagliato su[Utilizzo di OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet containing a presentation as OleObject

Workbook book = new Workbook(dir + "embeddedPresentation.xls");

//Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[]imageData = null;

int x = 0;

int y = 0;

byte[]objData = null;

String progID = "";

int fileFormatType = 0;

String sourceFullName = "";

Boolean isDisplayAsIcon = false;

byte[]classId = null;

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
## **API obsolete**
### **Metodo Worksheet.setBackground obsoleto**
Utilizzare invece la proprietà Worksheet.BackgroundImage.
### **Proprietà LineShape.BeginArrowheadStyle e ArcShape.BeginArrowheadStyle obsolete**
Utilizzare la proprietà Shape.Line.BeginArrowheadStyle come alternativa.
### **Proprietà LineShape.EndArrowheadStyle e ArcShape.EndArrowheadStyle obsolete**
Utilizzare la proprietà Shape.Line.EndArrowheadStyle come alternativa.
### **Proprietà LineShape.BeginArrowheadWidth e ArcShape.BeginArrowheadWidth obsolete**
Utilizzare la proprietà Shape.Line.BeginArrowheadWidth come alternativa.
### **Proprietà LineShape.BeginArrowheadLength e ArcShape.BeginArrowheadLength obsolete**
Utilizzare invece la proprietà Shape.Line.BeginArrowheadLength.
### **Proprietà LineShape.EndArrowheadWidth e ArcShape.EndArrowheadWidth obsolete**
Utilizzare invece la proprietà Shape.Line.EndArrowheadWidth.
### **Proprietà LineShape.EndArrowheadLength e ArcShape.EndArrowheadLength obsolete**
Utilizzare invece la proprietà Shape.Line.EndArrowheadLength.
## **API eliminate**
### **Metodo Worksheet.copyConditionalFormatting eliminato**
### **Metodo Workbook.checkWriteProtectedPassword eliminato**
## **API rinominate**
### **Metodo Workbook.removeDigitallySign rinominato**
Il metodo Workbook.removeDigitallySign è stato rinominato in Workbook.removeDigitalSignature.
