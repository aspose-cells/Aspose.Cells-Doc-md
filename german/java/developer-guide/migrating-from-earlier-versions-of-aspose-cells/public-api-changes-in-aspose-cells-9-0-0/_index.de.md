---
title: Öffentliche API Änderungen in Aspose.Cells 9.0.0
type: docs
weight: 340
url: /de/java/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 8.9.2 auf 9.0.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Hinzugefügte Shape.TextOptions Eigenschaft**
Aspose.Cells for Java hat die TextOptions Eigenschaft für die Shape-Klasse freigelegt, um das Erscheinungsbild textueller Teile einer Shape zu steuern.

Hier ist ein einfaches Anwendungsbeispiel der Shape.TextOptions Eigenschaft.

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
### **Hinzugefügte ChartPoint.IsInSecondaryPlot Eigenschaft**
Aspose.Cells for Java hat die ChartPoint.IsInSecondaryPlot Eigenschaft freigelegt, die verwendet werden kann, um festzustellen, ob ein ChartPoint in einem sekundären Plot eines Kuchen- oder Balkendiagramms liegt.

Hier ist ein einfaches Anwendungsbeispiel der Shape.Line Eigenschaft.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Ermitteln eines Datenpunkts im zweiten Plot](/cells/de/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

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
### **Hinzugefügte OleObject.ClassIdentifier Eigenschaft**
Aspose.Cells for Java 9.0.0 hat die OleObject.ClassIdentifier Eigenschaft freigelegt, die verwendet werden kann, um das Anwendungsverhalten beim Laden eines OleObject anzugeben. Beispielsweise kann eine PPT-Datei in einer Tabelle mit 2 verschiedenen Ansichten eingebettet werden, nämlich die Präsentationsansicht oder die Foliensicht, wobei beide Ansichten unterschiedliche Klassenidentifikatorwerte aufweisen.

Im Folgenden finden Sie das einfache Anwendungsszenario der OleObject.ClassIdentifier Eigenschaft.

{{% alert color="primary" %}} 

Lesen Sie den ausführlichen Artikel über [Die Verwendung von OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

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
## **Veraltete APIs**
### **Veraltete Worksheet.setBackground Methode**
Bitte verwenden Sie stattdessen die Worksheet.BackgroundImage Eigenschaft.
### **Veraltete LineShape.BeginArrowheadStyle & ArcShape.BeginArrowheadStyle Eigenschaften**
Bitte verwenden Sie die Shape.Line.BeginArrowheadStyle Eigenschaft als Alternative.
### **Veraltete LineShape.EndArrowheadStyle & ArcShape.EndArrowheadStyle Eigenschaften**
Bitte verwenden Sie die Shape.Line.EndArrowheadStyle Eigenschaft als Alternative.
### **Veraltete LineShape.BeginArrowheadWidth & ArcShape.BeginArrowheadWidth Eigenschaften**
Bitte verwenden Sie die Shape.Line.BeginArrowheadWidth Eigenschaft als Alternative.
### **Veraltete LineShape.BeginArrowheadLength & ArcShape.BeginArrowheadLength Eigenschaften**
Bitte verwenden Sie stattdessen die Shape.Line.BeginArrowheadLength Eigenschaft.
### **Veraltete LineShape.EndArrowheadWidth & ArcShape.EndArrowheadWidth Eigenschaften**
Bitte verwenden Sie stattdessen die Shape.Line.EndArrowheadWidth Eigenschaft.
### **Veraltete LineShape.EndArrowheadLength & ArcShape.EndArrowheadLength Eigenschaften**
Bitte verwenden Sie stattdessen die Shape.Line.EndArrowheadLength Eigenschaft.
## **Gelöschte APIs**
### **Gelöschte Worksheet.copyConditionalFormatting Methode**
### **Gelöschte Workbook.checkWriteProtectedPassword Methode**
## **Umbenannte APIs**
### **Die Methode Workbook.removeDigitallySign wurde umbenannt**
Die Methode Workbook.removeDigitallySign wurde in Workbook.removeDigitalSignature umbenannt
{{< app/cells/assistant language="java" >}}
