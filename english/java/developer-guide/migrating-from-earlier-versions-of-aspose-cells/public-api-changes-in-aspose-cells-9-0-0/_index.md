---
title: Public API Changes in Aspose.Cells 9.0.0
type: docs
weight: 340
url: /java/public-api-changes-in-aspose-cells-9-0-0/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.9.2 to 9.0.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Added Shape.TextOptions Property**
Aspose.Cells for Java has exposed the TextOptions property for the Shape class in order to control the appearance of textual parts of a Shape.

Here is simple usage scenario of Shape.TextOptions property.

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
### **Added ChartPoint.IsInSecondaryPlot Property**
Aspose.Cells for Java has exposed the ChartPoint.IsInSecondaryPlot property which can be used to detect if a ChartPoint resides on a secondary plot of a Pie or Bar chart.

Here is simple usage scenario of Shape.Line property.

{{% alert color="primary" %}} 

Check the detailed article on [Finding a DataPoint resides on the Second Plot](/cells/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

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
### **Added OleObject.ClassIdentifier property**
Aspose.Cells for Java 9.0.0 has exposed the OleObject.ClassIdentifier property which can be used to specify the application behavior to load an OleObject. For instance, a PPT file can be embedded in a spreadsheet with 2 different views, that is; presentation view or slide view, whereas both views have different class identifier values.

Following is the simple usage scenario of OleObject.ClassIdentifier property.

{{% alert color="primary" %}} 

Check the detailed article on [Using OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

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
## **Obsoleted APIs**
### **Obsoleted Worksheet.setBackground Method**
Please use Worksheet.BackgroundImage property instead.
### **Obsoleted LineShape.BeginArrowheadStyle & ArcShape.BeginArrowheadStyle Properties**
Please use Shape.Line.BeginArrowheadStyle property as an alternative.
### **Obsoleted LineShape.EndArrowheadStyle & ArcShape.EndArrowheadStyle Properties**
Please use Shape.Line.EndArrowheadStyle property as an alternative.
### **Obsoleted LineShape.BeginArrowheadWidth & ArcShape.BeginArrowheadWidth Properties**
Please use Shape.Line.BeginArrowheadWidth property as an alternative.
### **Obsoleted LineShape.BeginArrowheadLength & ArcShape.BeginArrowheadLength Properties**
Please use Shape.Line.BeginArrowheadLength property instead.
### **Obsoleted LineShape.EndArrowheadWidth & ArcShape.EndArrowheadWidth Properties**
Please use Shape.Line.EndArrowheadWidth property instead.
### **Obsoleted LineShape.EndArrowheadLength & ArcShape.EndArrowheadLength Properties**
Please use Shape.Line.EndArrowheadLength property instead.
## **Deleted APIs**
### **Deleted Worksheet.copyConditionalFormatting Method**
### **Deleted Workbook.checkWriteProtectedPassword Method**
## **Renamed APIs**
### **Renamed Workbook.removeDigitallySign Method**
The Workbook.removeDigitallySign method has been renamed to Workbook.removeDigitalSignature.
{{< app/cells/assistant language="java" >}}
