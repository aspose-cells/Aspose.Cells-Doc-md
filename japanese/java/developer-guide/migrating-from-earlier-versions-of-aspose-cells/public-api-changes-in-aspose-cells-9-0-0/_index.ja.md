---
title: Aspose.Cells 9.0.0での公開API変更
type: docs
weight: 340
url: /ja/java/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cells APIのバージョン8.9.2から9.0.0への変更点について、モジュール／アプリケーション開発者に興味を引くかもしれない情報を記載しています。新しいおよび更新された公開メソッド、追加および削除されたクラス等についてだけでなく、Aspose.Cellsの内部動作の変更についても記載しています。

{{% /alert %}} 
## **APIの追加**
### **Shape.TextOptionsプロパティが追加されました**
Aspose.Cells for Javaは、ShapeクラスのTextOptionsプロパティを公開し、Shapeのテキスト部分の外観を制御するために使用できるようにしました。

以下はShape.TextOptionsプロパティの簡単な使用シナリオです。

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
### **ChartPoint.IsInSecondaryPlotプロパティが追加されました**
Aspose.Cells for Javaは、ChartPoint.IsInSecondaryPlotプロパティを公開し、PieやBarチャートのセカンダリプロット上にChartPointが存在するかどうかを検出するために使用できるようにしました。

以下はShape.Lineプロパティの簡単な使用シナリオです。

{{% alert color="primary" %}} 

[データポイントがセカンドプロットに存在するかどうかの詳細については、この詳細記事を参照してください](/cells/ja/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

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
### **OleObject.ClassIdentifierプロパティが追加されました**
Aspose.Cells for Java 9.0.0では、OleObject.ClassIdentifierプロパティを公開し、OleObjectを読み込むためのアプリケーションの動作を指定するために使用できるようにしました。たとえば、PPTファイルをスプレッドシートに埋め込む場合、プレゼンテーションビューまたはスライドビューのいずれかを指定できます。両方のビューは異なるクラス識別子の値を持っています。

以下はOleObject.ClassIdentifierプロパティの簡単な使用シナリオです。

{{% alert color="primary" %}} 

[OleObject.ClassIdentifierを使用する詳細記事はこちらをご覧ください](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

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
## **非推奨API**
### **非推奨のWorksheet.setBackgroundメソッド**
代わりにWorksheet.BackgroundImageプロパティを使用してください。
### **非推奨のLineShape.BeginArrowheadStyleおよびArcShape.BeginArrowheadStyleプロパティ**
代替としてShape.Line.BeginArrowheadStyleプロパティを使用してください。
### **LineShape.EndArrowheadStyleおよびArcShape.EndArrowheadStyleプロパティは廃止されました**
代替としてShape.Line.EndArrowheadStyleプロパティを使用してください。
### **LineShape.BeginArrowheadWidthおよびArcShape.BeginArrowheadWidthプロパティは廃止されました**
代替としてShape.Line.BeginArrowheadWidthプロパティを使用してください。
### **LineShape.BeginArrowheadLengthおよびArcShape.BeginArrowheadLengthプロパティは廃止されました**
代わりにShape.Line.BeginArrowheadLengthプロパティを使用してください。
### **LineShape.EndArrowheadWidthおよびArcShape.EndArrowheadWidthプロパティは廃止されました**
代わりにShape.Line.EndArrowheadWidthプロパティを使用してください。
### **LineShape.EndArrowheadLengthおよびArcShape.EndArrowheadLengthプロパティは廃止されました**
代わりにShape.Line.EndArrowheadLengthプロパティを使用してください。
## **削除されたAPI**
### **削除されたWorksheet.copyConditionalFormattingメソッド**
### **削除されたWorkbook.checkWriteProtectedPasswordメソッド**
## **改名されたAPI**
### **Workbook.removeDigitallySignメソッドが名前変更されました**
Workbook.removeDigitallySignメソッドはWorkbook.removeDigitalSignatureに名前が変更されました。
{{< app/cells/assistant language="java" >}}
