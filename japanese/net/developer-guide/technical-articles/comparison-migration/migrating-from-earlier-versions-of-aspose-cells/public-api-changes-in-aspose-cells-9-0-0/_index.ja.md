---
title: パブリック API Aspose.Cells 9.0.0 の変更点
type: docs
weight: 330
url: /ja/net/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.9.2 から 9.0.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **Shape.TextOptions プロパティを追加**
Aspose.Cells for .NET は、Shape のテキスト部分の外観を制御するために、Shape クラスの TextOptions プロパティを公開しました。

Shape.TextOptions プロパティの簡単な使用シナリオを次に示します。

**C#**

{{< highlight "csharp" >}}

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


### **LoadOptions.CultureInfo プロパティを追加**
Aspose.Cells for .NET 9.0.0 は LoadOptions.CultureInfo プロパティを公開しました。これにより、Workbook のインスタンスにドキュメントをロードするときに CultureInfo のインスタンスを挿入できます。

前述のプロパティの簡単な使用シナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[特定の CultureInfo を含むスプレッドシートの読み込み](/cells/ja/net/load-the-workbook-with-specific-system-culture-info/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **ChartPoint.IsInSecondaryPlot プロパティを追加**
Aspose.Cells for .NET は ChartPoint.IsInSecondaryPlot プロパティを公開しました。このプロパティを使用して、ChartPoint が円グラフまたは棒グラフの二次プロットにあるかどうかを検出できます。

Shape.Line プロパティの簡単な使用シナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[2 番目のプロットに存在する DataPoint を見つける](/cells/ja/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **OleObject.ClassIdentifier プロパティを追加しました**
Aspose.Cells for .NET 9.0.0 は、OleObject をロードするアプリケーションの動作を指定するために使用できる OleObject.ClassIdentifier プロパティを公開しました。たとえば、PPT ファイルは 2 つの異なるビューを持つスプレッドシートに埋め込むことができます。どちらのビューも異なるクラス識別子の値を持っていますが、プレゼンテーション ビューまたはスライド ビューです。

以下は、OleObject.ClassIdentifier プロパティの簡単な使用シナリオです。

{{% alert color="primary" %}} 

の詳細記事をチェック[OleObject.ClassIdentifier の使用](/cells/ja/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load a spreadsheet containing a presentation as OleObject

var book = new Workbook(dir + "embeddedPresentation.xls");

// Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[]imageData = null;

int x = 0;

int y = 0;

byte[]objData = null;

string progID = "";

FileFormatType fileFormatType = FileFormatType.Unknown;

string sourceFullName = "";

bool isDisplayAsIcon = false;

byte[]classId = null;

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
## **廃止された API**
### **廃止された Worksheet.SetBackground メソッド**
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
### **削除された Worksheet.CopyConditionalFormatting メソッド**
### **Workbook.CheckWriteProtectedPassword メソッドを削除しました**
## **名前が変更された API**
### **名前が変更された Workbook.RemoveDigitallySign メソッド**
Workbook.RemoveDigitallySign メソッドの名前が Workbook.RemoveDigitalSignature に変更されました。
