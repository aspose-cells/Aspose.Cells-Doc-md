---
title: パブリック API Aspose.Cells 9.0.0 の変更点
type: docs
weight: 340
url: /ja/java/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.9.2 から 9.0.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **Shape.TextOptions プロパティを追加**
Aspose.Cells for Java は、Shape のテキスト部分の外観を制御するために、Shape クラスの TextOptions プロパティを公開しました。

Shape.TextOptions プロパティの簡単な使用シナリオを次に示します。

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
### **ChartPoint.IsInSecondaryPlot プロパティを追加**
Aspose.Cells for Java は ChartPoint.IsInSecondaryPlot プロパティを公開しました。このプロパティを使用して、ChartPoint が円グラフまたは棒グラフの二次プロットにあるかどうかを検出できます。

Shape.Line プロパティの簡単な使用シナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[2 番目のプロットに存在する DataPoint を見つける](/cells/ja/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

//円グラフを含む既存のスプレッドシートを読み込みます

Workbook book = new Workbook(dir + "PieBar.xlsx");

// ワークシートをインデックス 0 にロードします

ワークシート シート = book.getWorksheets().get(0);

//コレクションから最初のチャートをロード

チャート chart = sheet.getCharts().get(0);

//プロパティにアクセスする前にチャートを計算します

chart.calculate();

//チャートの最初のシリーズへのアクセス

シリーズ series = chart.getNSeries().get(0);

//ChartPoint コレクションをループします

for(int p = 0 ; p< series.getPoints().getCount(); p++)

{

	ChartPoint point = series.getPoints().get(p);



	//Detect if ChartPoint resides on secondary plot

	System.out.println(point.isInSecondaryPlot());

}

{{< /highlight >}}
### **OleObject.ClassIdentifier プロパティを追加しました**
Aspose.Cells for Java 9.0.0 は、OleObject をロードするアプリケーションの動作を指定するために使用できる OleObject.ClassIdentifier プロパティを公開しました。たとえば、PPT ファイルは 2 つの異なるビューを持つスプレッドシートに埋め込むことができます。どちらのビューも異なるクラス識別子の値を持っていますが、プレゼンテーション ビューまたはスライド ビューです。

以下は、OleObject.ClassIdentifier プロパティの簡単な使用シナリオです。

{{% alert color="primary" %}} 

の詳細記事をチェック[OleObject.ClassIdentifier の使用](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

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
## **廃止された API**
### **廃止された Worksheet.setBackground メソッド**
代わりに Worksheet.BackgroundImage プロパティを使用してください。
### **廃止された LineShape.BeginArrowheadStyle および ArcShape.BeginArrowheadStyle プロパティ**
代わりに Shape.Line.BeginArrowheadStyle プロパティを使用してください。
### **廃止された LineShape.EndArrowheadStyle および ArcShape.EndArrowheadStyle プロパティ**
代わりに Shape.Line.EndArrowheadStyle プロパティを使用してください。
### **廃止された LineShape.BeginArrowheadWidth および ArcShape.BeginArrowheadWidth プロパティ**
代わりに Shape.Line.BeginArrowheadWidth プロパティを使用してください。
### **廃止された LineShape.BeginArrowheadLength および ArcShape.BeginArrowheadLength プロパティ**
代わりに Shape.Line.BeginArrowheadLength プロパティを使用してください。
### **廃止された LineShape.EndArrowheadWidth および ArcShape.EndArrowheadWidth プロパティ**
代わりに Shape.Line.EndArrowheadWidth プロパティを使用してください。
### **廃止された LineShape.EndArrowheadLength および ArcShape.EndArrowheadLength プロパティ**
代わりに Shape.Line.EndArrowheadLength プロパティを使用してください。
## **削除された API**
### **Worksheet.copyConditionalFormatting メソッドの削除**
### **削除された Workbook.checkWriteProtectedPassword メソッド**
## **名前が変更された API**
### **名前が変更された Workbook.removeDigitallySign メソッド**
Workbook.removeDigitallySign メソッドの名前が Workbook.removeDigitalSignature に変更されました。
