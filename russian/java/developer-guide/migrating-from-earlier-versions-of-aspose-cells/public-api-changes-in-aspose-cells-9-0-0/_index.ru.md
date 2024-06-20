---
title: Изменения в общедоступном API в Aspose.Cells 9.0.0
type: docs
weight: 340
url: /ru/java/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.9.2 по 9.0.0, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные открытые методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Добавлено свойство Shape.TextOptions.**
Aspose.Cells for Java добавило свойство TextOptions для класса Shape для управления внешним видом текстовых частей фигуры.

Вот простой сценарий использования свойства Shape.TextOptions.

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
### **Добавлено свойство ChartPoint.IsInSecondaryPlot.**
Aspose.Cells for Java добавило свойство ChartPoint.IsInSecondaryPlot, которое позволяет определить, находится ли объект ChartPoint на вторичном графике круговой или столбчатой диаграммы.

Вот простой сценарий использования свойства Shape.Line.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Обнаружению расположения точки данных на втором графике](/cells/ru/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

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
### **Добавлено свойство OleObject.ClassIdentifier.**
Aspose.Cells for Java 9.0.0 добавило свойство OleObject.ClassIdentifier, которое можно использовать для указания поведения при загрузке объекта OleObject. Например, файл PPT можно встроить в электронную таблицу с 2 разными видами, презентационным или отображением слайдов, при этом у обоих видов различные значения идентификатора класса.

Ниже приведен простой сценарий использования свойства OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Использованию OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

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
## **Устаревшие API**
### **Устаревший метод Worksheet.setBackground**
Вместо этого используйте свойство Worksheet.BackgroundImage.
### **Свойства LineShape.BeginArrowheadStyle и ArcShape.BeginArrowheadStyle устарели**
В качестве альтернативы используйте свойство Shape.Line.BeginArrowheadStyle.
### **Свойства LineShape.EndArrowheadStyle и ArcShape.EndArrowheadStyle устарели**
В качестве альтернативы используйте свойство Shape.Line.EndArrowheadStyle.
### **Свойства LineShape.BeginArrowheadWidth и ArcShape.BeginArrowheadWidth устарели**
В качестве альтернативы используйте свойство Shape.Line.BeginArrowheadWidth.
### **Свойства LineShape.BeginArrowheadLength и ArcShape.BeginArrowheadLength устарели**
Используйте свойство Shape.Line.BeginArrowheadLength вместо.
### **Свойства LineShape.EndArrowheadWidth и ArcShape.EndArrowheadWidth устарели**
Используйте свойство Shape.Line.EndArrowheadWidth вместо.
### **Свойства LineShape.EndArrowheadLength и ArcShape.EndArrowheadLength устарели**
Используйте свойство Shape.Line.EndArrowheadLength вместо.
## **Удаленные API**
### **Метод Worksheet.copyConditionalFormatting удален**
### **Метод Workbook.checkWriteProtectedPassword удален**
## **Переименованные API**
### **Метод Workbook.removeDigitallySign переименован**
Метод Workbook.removeDigitallySign переименован в Workbook.removeDigitalSignature.
