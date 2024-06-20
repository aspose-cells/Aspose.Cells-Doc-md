---
title: Changements d API publics dans Aspose.Cells 9.0.0
type: docs
weight: 340
url: /fr/java/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.9.2 à la version 9.0.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Propriété Shape.TextOptions ajoutée**
Aspose.Cells for Java a exposé la propriété TextOptions pour la classe Shape afin de contrôler l'apparence des parties textuelles d'une forme.

Voici un scénario d'utilisation simple de la propriété Shape.TextOptions.

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
### **Propriété ChartPoint.IsInSecondaryPlot ajoutée**
Aspose.Cells for Java a exposé la propriété ChartPoint.IsInSecondaryPlot qui peut être utilisée pour détecter si un ChartPoint réside sur un tracé secondaire d'un graphique circulaire ou à barres.

Voici un scénario d'utilisation simple de la propriété Shape.Line.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Trouver un DataPoint résidant sur le deuxième tracé](/cells/fr/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

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
### **Propriété OleObject.ClassIdentifier ajoutée**
Aspose.Cells for Java 9.0.0 a exposé la propriété OleObject.ClassIdentifier qui peut être utilisée pour spécifier le comportement d'application pour charger un OleObject. Par exemple, un fichier PPT peut être incorporé dans une feuille de calcul avec 2 vues différentes, c'est-à-dire la vue de présentation ou la vue de diapositive, alors que les deux vues ont différentes valeurs d'identifiant de classe.

Voici un scénario d'utilisation simple de la propriété OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

Consultez l'article détaillé sur [Utiliser OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

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
## **APIs obsolètes**
### **Méthode Worksheet.setBackground obsolète**
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
### **Méthode Worksheet.copyConditionalFormatting supprimée**
### **Méthode Workbook.checkWriteProtectedPassword supprimée**
## **API renommées**
### **Méthode Workbook.removeDigitallySign renommée**
La méthode Workbook.removeDigitallySign a été renommée en Workbook.removeDigitalSignature.
