---
title: Общедоступный API Изменения в Aspose.Cells 9.0.0
type: docs
weight: 340
url: /ru/java/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.9.2 до 9.0.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Добавлено свойство Shape.TextOptions**
Aspose.Cells for Java предоставил свойство TextOptions для класса Shape, чтобы управлять внешним видом текстовых частей Shape.

Вот простой сценарий использования свойства Shape.TextOptions.

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
### **Добавлено свойство ChartPoint.IsInSecondaryPlot**
Aspose.Cells for Java предоставил свойство ChartPoint.IsInSecondaryPlot, которое можно использовать для определения того, находится ли ChartPoint на вторичном графике круговой или гистограммы.

Вот простой сценарий использования свойства Shape.Line.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Поиск DataPoint находится на втором графике](/cells/ru/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Загрузить существующую электронную таблицу, содержащую круговую диаграмму

Книга рабочей книги = новая рабочая книга (каталог + "PieBar.xlsx");

//Загрузить рабочий лист с индексом 0

Рабочий лист = book.getWorksheets().get(0);

//Загружаем первый график из коллекции

Диаграмма Диаграмма = лист.getCharts().get(0);

//Рассчитываем график перед доступом к его свойствам

диаграмма.вычислить();

//Доступ к первой серии графика

Серии серий = chart.getNSeries().get(0);

//Перебираем коллекцию ChartPoint

 for(int p = 0 ; p< series.getPoints().getCount(); p++)

{

	ChartPoint point = series.getPoints().get(p);



	//Detect if ChartPoint resides on secondary plot

	System.out.println(point.isInSecondaryPlot());

}

{{< /highlight >}}
### **Добавлено свойство OleObject.ClassIdentifier.**
Aspose.Cells for Java 9.0.0 предоставило свойство OleObject.ClassIdentifier, которое можно использовать для указания поведения приложения при загрузке OleObject. Например, файл PPT может быть встроен в электронную таблицу с двумя разными представлениями, то есть; представление презентации или представление слайдов, тогда как оба представления имеют разные значения идентификатора класса.

Ниже приведен простой сценарий использования свойства OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Использование OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

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
## **Устаревшие API**
### **Устаревший метод Worksheet.setBackground**
Вместо этого используйте свойство Worksheet.BackgroundImage.
### **Устаревшие свойства LineShape.BeginArrowheadStyle и ArcShape.BeginArrowheadStyle**
В качестве альтернативы используйте свойство Shape.Line.BeginArrowheadStyle.
### **Устаревшие свойства LineShape.EndArrowheadStyle и ArcShape.EndArrowheadStyle**
В качестве альтернативы используйте свойство Shape.Line.EndArrowheadStyle.
### **Устаревшие свойства LineShape.BeginArrowheadWidth и ArcShape.BeginArrowheadWidth**
В качестве альтернативы используйте свойство Shape.Line.BeginArrowheadWidth.
### **Устаревшие свойства LineShape.BeginArrowheadLength и ArcShape.BeginArrowheadLength**
Вместо этого используйте свойство Shape.Line.BeginArrowheadLength.
### **Устаревшие свойства LineShape.EndArrowheadWidth и ArcShape.EndArrowheadWidth**
Вместо этого используйте свойство Shape.Line.EndArrowheadWidth.
### **Устаревшие свойства LineShape.EndArrowheadLength и ArcShape.EndArrowheadLength**
Вместо этого используйте свойство Shape.Line.EndArrowheadLength.
## **Удаленные API**
### **Удаленный метод Worksheet.copyConditionalFormatting**
### **Удаленный метод Workbook.checkWriteProtectedPassword**
## **Переименованные API**
### **Метод Workbook.removeDigitallySign переименован.**
Метод Workbook.removeDigitallySign был переименован в Workbook.removeDigitalSignature.
