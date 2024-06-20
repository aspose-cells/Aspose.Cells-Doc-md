---
title: Aspose.Cells 9.0.0での公開API変更
type: docs
weight: 330
url: /ja/net/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cells APIのバージョン8.9.2から9.0.0への変更点について、モジュール／アプリケーション開発者に興味を引くかもしれない情報を記載しています。新しいおよび更新された公開メソッド、追加および削除されたクラス等についてだけでなく、Aspose.Cellsの内部動作の変更についても記載しています。

{{% /alert %}} 
## **APIの追加**
### **Shape.TextOptionsプロパティが追加されました**
Aspose.Cells for .NETでは、ShapeクラスのTextOptionsプロパティが公開され、Shapeのテキスト部分の外観を制御するために使用できます。

以下はShape.TextOptionsプロパティの簡単な使用シナリオです。

**C#**

{{< highlight csharp >}}

 // Initialize an instance of Workbook

var book = new Workbook();

// Get the default Worksheet from the Workbook

var sheet = book.Worksheets[0];

// Add a TextBox to the collection

var textboxIndex = sheet.TextBoxes.Add(2, 1, 160, 200);

// Get the TextBox object

var textbox = sheet.TextBoxes[textboxIndex];

// Add text to the TextBox

textbox.Text = "Hello Aspose!";

// Format the textual contents

textbox.TextOptions.Color = System.Drawing.Color.Red;

textbox.TextOptions.IsItalic = true;

{{< /highlight >}}


### **LoadOptions.CultureInfoプロパティが追加されました。**
Aspose.Cells for .NET 9.0.0では、LoadOptions.CultureInfoプロパティが公開され、Workbookのインスタンスでドキュメントをロードする際にCultureInfoのインスタンスを注入することができます。

前述のプロパティの簡単な使用シナリオは次のとおりです。

{{% alert color="primary" %}} 

[特定のCultureInfoでスプレッドシートをロード](/cells/ja/net/load-the-workbook-with-specific-system-culture-info/)する詳細な記事をご覧ください。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of CultureInfo and populate its properties

var culture = new CultureInfo("en-GB");

culture.NumberFormat.NumberDecimalSeparator = ",";

culture.DateTimeFormat.DateSeparator = "-";

culture.DateTimeFormat.ShortDatePattern = "dd-MM-yyyy";

// Create an instance of LoadOptions and set the CultureInfo property

var options = new LoadOptions(LoadFormat.Html);

options.CultureInfo = culture;

// Load a HTML or TXT file in an instance of Workbook with instance of  LoadOptions

var book = new Workbook(dir + "input.html", options);

{{< /highlight >}}


### **ChartPoint.IsInSecondaryPlotプロパティが追加されました**
Aspose.Cells for .NETでは、ChartPoint.IsInSecondaryPlotプロパティが公開され、PieやBarのチャートのセカンダリープロットにChartPointが存在するかどうかを検出するために使用できます。

以下はShape.Lineプロパティの簡単な使用シナリオです。

{{% alert color="primary" %}} 

[データポイントがセカンダリプロットに存在するかどうかを見つける](/cells/ja/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)詳細な記事をご覧ください。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load an existing spreadsheet containing a Pie chart

var book = new Workbook(dir + "PieBar.xlsx");

// Load the Worksheet at 0 index

var sheet = book.Worksheets[0];

// Load the first chart from the collection

var chart = sheet.Charts[0];

// Calculate the chart before accessing its properties

chart.Calculate();

// Accessing chart's first series

var series = chart.NSeries[0];

// Loop over the ChartPoint collection

foreach (ChartPoint point in series.Points)

{

    // Detect if ChartPoint resides on secondary plot

    Console.WriteLine(point.IsInSecondaryPlot);

}

{{< /highlight >}}


### **OleObject.ClassIdentifierプロパティが追加されました**
Aspose.Cells for .NET 9.0.0では、OleObject.ClassIdentifierプロパティが公開され、オートエレメントをロードするためのアプリケーションの動作を指定するために使用できます。たとえば、PPTファイルをスプレッドシートに埋め込む場合、プレゼンテーションビューまたはスライドビューの2つの異なるビューがあり、両方のビューに異なるクラス識別子の値があります。

以下はOleObject.ClassIdentifierプロパティの簡単な使用シナリオです。

{{% alert color="primary" %}} 

[OleObject.ClassIdentifierの使用](/cells/ja/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)に関する詳細な記事をご覧ください。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet containing a presentation as OleObject

var book = new Workbook(dir + "embeddedPresentation.xls");

// Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[] imageData = null;

int x = 0;

int y = 0;

byte[] objData = null;

string progID = "";

FileFormatType fileFormatType = FileFormatType.Unknown;

string sourceFullName = "";

bool isDisplayAsIcon = false;

byte[] classId = null;

// Get the first worksheet from the collection

var sheet = book.Worksheets[0];

// Get the first OleObject from the collection

var frame = sheet.OleObjects[0];

// Store the properties in variables

upperLeftRow = frame.UpperLeftRow;

upperLeftColumn = frame.UpperLeftColumn;

height = frame.Height;

width = frame.Width;

imageData = frame.ImageData;

x = frame.X;

y = frame.Y;

objData = frame.ObjectData;

progID = frame.ProgID;

fileFormatType = frame.FileFormatType;

sourceFullName = frame.ObjectSourceFullName;

isDisplayAsIcon = frame.DisplayAsIcon;

classId = frame.ClassIdentifier;

// Initialize a new Workbook instance

book = new Workbook();

// Access first worksheet from the collection

sheet = book.Worksheets[0];

// Insert the OleObject to the worksheet

int oleNumber = sheet.OleObjects.Add(upperLeftRow, upperLeftColumn, height, width, imageData);

// Access newly inserted OleObject

var embeddedObject = sheet.OleObjects[oleNumber];

// Assign previously stored properties to new OleObject

embeddedObject.X = x;

embeddedObject.Y = y;

embeddedObject.ObjectData = objData;

embeddedObject.ProgID = progID;

embeddedObject.FileFormatType = fileFormatType;

embeddedObject.DisplayAsIcon = isDisplayAsIcon;

embeddedObject.ObjectSourceFullName = sourceFullName;

embeddedObject.IsAutoSize = false;

if (classId != null)

{

    embeddedObject.ClassIdentifier = classId;

}

// Save the resultant spreadsheet

book.Save(dir  + "output.xls");

{{< /highlight >}}
## **非推奨API**
### **非推奨のWorksheet.SetBackgroundメソッド**
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
### **削除されたWorksheet.CopyConditionalFormattingメソッド**
### **削除されたWorkbook.CheckWriteProtectedPasswordメソッド**
## **改名されたAPI**
### **Workbook.RemoveDigitallySignメソッドの名前が変更されました**
Workbook.RemoveDigitallySignメソッドはWorkbook.RemoveDigitalSignatureに名前が変更されました。
