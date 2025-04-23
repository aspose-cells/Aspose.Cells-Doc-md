---
title: Aspose.Cells 9.0.0 中的公共 API 更改
type: docs
weight: 340
url: /zh/java/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.9.2 到 9.0.0 的 Aspose.Cells API 变化，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加和删除的类等，还描述了在 Aspose.Cells 后台行为中的任何更改。

{{% /alert %}} 
## **添加的 API**
### **添加了 Shape.TextOptions 属性**
Aspose.Cells for Java 为 Shape 类公开了 TextOptions 属性，以便控制形状的文本部分的外观。

这里是 Shape.TextOptions 属性的简单使用场景。

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
### **添加了 ChartPoint.IsInSecondaryPlot 属性**
Aspose.Cells for Java 公开了 ChartPoint.IsInSecondaryPlot 属性，可用于检测 ChartPoint 是否位于饼图或条形图的次要绘图区域。

这里是 Shape.Line 属性的简单使用场景。

{{% alert color="primary" %}} 

查看[在饼图和画的饼图上找到数据点](/cells/zh/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-chart/)的详细文章

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
### **添加了OleObject.ClassIdentifier属性**
Aspose.Cells for Java 9.0.0 公开了 OleObject.ClassIdentifier 属性，可用于指定加载 OleObject 的应用程序行为。例如，PPT 文件可以嵌入到带有两个不同视图的电子表格中，即演示文稿视图或幻灯片视图，而这两个视图具有不同的类标识值。

以下是OleObject.ClassIdentifier属性的简单使用场景。

{{% alert color="primary" %}} 

查看[使用OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)的详细文章

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
## **已弃用的API**
### **已废弃Worksheet.setBackground方法**
请使用Worksheet.BackgroundImage属性代替。
### **已废弃LineShape.BeginArrowheadStyle & ArcShape.BeginArrowheadStyle 属性**
请使用Shape.Line.BeginArrowheadStyle属性作为替代。
### **已废弃LineShape.EndArrowheadStyle & ArcShape.EndArrowheadStyle 属性**
请使用Shape.Line.EndArrowheadStyle属性作为替代。
### **已废弃LineShape.BeginArrowheadWidth & ArcShape.BeginArrowheadWidth 属性**
请使用Shape.Line.BeginArrowheadWidth属性作为替代。
### **已废弃LineShape.BeginArrowheadLength & ArcShape.BeginArrowheadLength 属性**
请使用Shape.Line.BeginArrowheadLength属性代替。
### **已废弃LineShape.EndArrowheadWidth & ArcShape.EndArrowheadWidth 属性**
请使用Shape.Line.EndArrowheadWidth属性代替。
### **已废弃LineShape.EndArrowheadLength & ArcShape.EndArrowheadLength 属性**
请使用Shape.Line.EndArrowheadLength属性代替。
## **删除的API**
### **已删除Worksheet.copyConditionalFormatting方法**
### **已删除工作簿 checkWriteProtectedPassword 方法**
## **重命名的API**
### **已重命名工作簿 removeDigitallySign 方法**
Workbook.removeDigitallySign 方法已重命名为 Workbook.removeDigitalSignature。
{{< app/cells/assistant language="java" >}}
