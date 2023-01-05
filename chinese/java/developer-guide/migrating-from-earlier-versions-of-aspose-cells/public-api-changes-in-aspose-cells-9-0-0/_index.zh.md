---
title: 公共 API Aspose.Cells 9.0.0 的变化
type: docs
weight: 340
url: /zh/java/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.9.2 到 9.0.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **添加了 Shape.TextOptions 属性**
Aspose.Cells for Java 公开了 Shape 类的 TextOptions 属性，以控制 Shape 文本部分的外观。

这是 Shape.TextOptions 属性的简单使用场景。

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
### **添加了 ChartPoint.IsInSecondaryPlot 属性**
Aspose.Cells for Java 公开了 ChartPoint.IsInSecondaryPlot 属性，该属性可用于检测 ChartPoint 是否驻留在饼图或条形图的辅助图上。

下面是 Shape.Line 属性的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[查找数据点驻留在第二个图上](/cells/zh/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

//加载包含饼图的现有电子表格

工作簿 book = new Workbook(dir + "PieBar.xlsx");

//在0索引处加载工作表

工作表 sheet = book.getWorksheets().get(0);

//从集合中加载第一个图表

图表chart = sheet.getCharts().get(0);

//在访问其属性之前计算图表

图表.计算();

//访问图表的第一个系列

系列series = chart.getNSeries().get(0);

//遍历 ChartPoint 集合

对于（整数 p = 0 ; p< series.getPoints().getCount(); p++)

{

	ChartPoint point = series.getPoints().get(p);



	//Detect if ChartPoint resides on secondary plot

	System.out.println(point.isInSecondaryPlot());

}

{{< /highlight >}}
### **添加了 OleObject.ClassIdentifier 属性**
Aspose.Cells for Java 9.0.0 公开了 OleObject.ClassIdentifier 属性，可用于指定加载 OleObject 的应用程序行为。例如，一个 PPT 文件可以嵌入到具有 2 个不同视图的电子表格中，即；演示视图或幻灯片视图，而这两个视图具有不同的类标识符值。

以下是 OleObject.ClassIdentifier 属性的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[使用 OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

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
## **过时的 API**
### **废弃的 Worksheet.setBackground 方法**
请改用 Worksheet.BackgroundImage 属性。
### **废弃的 LineShape.BeginArrowheadStyle 和 ArcShape.BeginArrowheadStyle 属性**
请使用 Shape.Line.BeginArrowheadStyle 属性作为替代。
### **废弃的 LineShape.EndArrowheadStyle 和 ArcShape.EndArrowheadStyle 属性**
请使用 Shape.Line.EndArrowheadStyle 属性作为替代。
### **废弃的 LineShape.BeginArrowheadWidth 和 ArcShape.BeginArrowheadWidth 属性**
请使用 Shape.Line.BeginArrowheadWidth 属性作为替代。
### **废弃的 LineShape.BeginArrowheadLength 和 ArcShape.BeginArrowheadLength 属性**
请改用 Shape.Line.BeginArrowheadLength 属性。
### **废弃的 LineShape.EndArrowheadWidth 和 ArcShape.EndArrowheadWidth 属性**
请改用 Shape.Line.EndArrowheadWidth 属性。
### **废弃的 LineShape.EndArrowheadLength 和 ArcShape.EndArrowheadLength 属性**
请改用 Shape.Line.EndArrowheadLength 属性。
## **已删除的 API**
### **删除了 Worksheet.copyConditionalFormatting 方法**
### **删除了 Workbook.checkWriteProtectedPassword 方法**
## **重命名的 API**
### **重命名 Workbook.removeDigitallySign 方法**
Workbook.removeDigitallySign 方法已重命名为 Workbook.removeDigitalSignature。
