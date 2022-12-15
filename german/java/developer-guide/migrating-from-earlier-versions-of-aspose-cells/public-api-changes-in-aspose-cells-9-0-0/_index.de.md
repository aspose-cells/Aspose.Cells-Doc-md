---
title: Öffentlich API Änderungen in Aspose.Cells 9.0.0
type: docs
weight: 340
url: /de/java/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.9.2 zu 9.0.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Shape.TextOptions-Eigenschaft hinzugefügt**
Aspose.Cells for Java hat die TextOptions-Eigenschaft für die Shape-Klasse verfügbar gemacht, um das Erscheinungsbild von Textteilen einer Shape zu steuern.

Hier ist ein einfaches Verwendungsszenario der Shape.TextOptions-Eigenschaft.

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
### **ChartPoint.IsInSecondaryPlot-Eigenschaft hinzugefügt**
Aspose.Cells for Java hat die ChartPoint.IsInSecondaryPlot-Eigenschaft verfügbar gemacht, die verwendet werden kann, um zu erkennen, ob sich ein ChartPoint auf einem sekundären Diagramm eines Kreis- oder Balkendiagramms befindet.

Hier ist ein einfaches Verwendungsszenario der Shape.Line-Eigenschaft.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Das Finden eines Datenpunkts befindet sich auf dem zweiten Diagramm](/cells/de/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Laden Sie eine vorhandene Tabelle mit einem Kreisdiagramm

Arbeitsmappenbuch = neue Arbeitsmappe (dir + "PieBar.xlsx");

//Laden Sie das Arbeitsblatt bei Index 0

Arbeitsblatt sheet = book.getWorksheets().get(0);

//Laden Sie das erste Diagramm aus der Sammlung

Diagramm chart = sheet.getCharts().get(0);

//Berechnen Sie das Diagramm, bevor Sie auf seine Eigenschaften zugreifen

chart.calculate();

//Zugriff auf die erste Serie des Diagramms

Serie series = chart.getNSeries().get(0);

//Durchlaufe die ChartPoint-Sammlung

 for(int p = 0 ; p< series.getPoints().getCount(); p++)

{

	ChartPoint point = series.getPoints().get(p);



	//Detect if ChartPoint resides on secondary plot

	System.out.println(point.isInSecondaryPlot());

}

{{< /highlight >}}
### **OleObject.ClassIdentifier-Eigenschaft hinzugefügt**
Aspose.Cells for Java 9.0.0 hat die OleObject.ClassIdentifier-Eigenschaft verfügbar gemacht, die verwendet werden kann, um das Anwendungsverhalten zum Laden eines OleObject anzugeben. Beispielsweise kann eine PPT-Datei in eine Tabellenkalkulation mit 2 verschiedenen Ansichten eingebettet werden, das heißt; Präsentationsansicht oder Folienansicht, wobei beide Ansichten unterschiedliche Klassenkennungswerte haben.

Im Folgenden finden Sie das einfache Verwendungsszenario der OleObject.ClassIdentifier-Eigenschaft.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Verwenden von OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

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
## **Veraltete APIs**
### **Veraltete Worksheet.setBackground-Methode**
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
### **Gelöschte Worksheet.copyConditionalFormatting-Methode**
### **Gelöschte Workbook.checkWriteProtectedPassword-Methode**
## **Umbenannte APIs**
### **Workbook.removeDigitallySign-Methode umbenannt**
Die Workbook.removeDigitallySign-Methode wurde in Workbook.removeDigitalSignature umbenannt.
