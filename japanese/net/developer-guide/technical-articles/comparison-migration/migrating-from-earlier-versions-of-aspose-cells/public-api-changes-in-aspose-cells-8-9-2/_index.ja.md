---
title: パブリック API Aspose.Cells 8.9.2 の変更点
type: docs
weight: 320
url: /ja/net/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.9.1 から 8.9.2 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} {{% alert color="primary" %}} 

こちらもご確認ください[Public API Aspose.Cells for .NET 8.9.1 で導入された変更](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **追加された API**
### **TextOptions クラスと FontSettings.TextOptions プロパティを追加**
Aspose.Cells for .NET は、Shape のテキスト部分の外観を制御するために、FontSettings.TextOptions プロパティと共に TextOptions クラスを公開しました。

FontSettings.TextOptions プロパティの簡単な使用シナリオを次に示します。

**C#**

{{< highlight "csharp" >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access TextOptions of Shape

var textOptions = shape.TextBody[1].TextOptions;

{{< /highlight >}}


### **TextOptions.Fill、Outline、Shadow プロパティを追加**
Aspose.Cells for .NET 8.9.2 では、TextOptions.Fill、TextOptions.Outline、TextOptions.Shadow プロパティが公開されており、それぞれ塗りつぶし、影、アウトラインなど、形状のテキスト コンテンツの側面を制御できます。

前述のプロパティの簡単な使用シナリオを次に示します。

**C#**

{{< highlight "csharp" >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Set text for TextBox

shape.Text = "Aspose";

// Access TextOptions of Shape

var textOptions = shape.TextBody[1].TextOptions;

// Set shadow 

textOptions.Shadow.PresetType = PresetShadowType.Below;

// Set fill color

textOptions.Fill.FillType = FillType.Solid;

textOptions.Fill.SolidFill.Color = Color.Red;

// Set outline color

textOptions.Outline.SetOneColorGradient(Color.Blue, 0.3, GradientStyleType.Horizontal, 2);

{{< /highlight >}}


### **Shape.Line プロパティを追加**
Aspose.Cells for .NET は、Shape のアウトラインの外観を制御するために LineFormat のインスタンスを返す Shape.Line プロパティを公開しました。

Shape.Line プロパティの簡単な使用シナリオを次に示します。

**C#**

{{< highlight "csharp" >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access LineFormat of Shape

var line = shape.Line;

// Set weight of line

line.Weight = 1;

{{< /highlight >}}


### **Shape.Fill プロパティを追加**
Aspose.Cells for .NET 8.9.2 は、形状領域のさまざまな側面を制御するために、FillFormat のインスタンスを返す Shape.Fill プロパティを公開しました。

以下は、Shape.Fill プロパティの簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access FillFormat of Shape

var fill = shape.Fill;

// Set color for fill

fill.SetOneColorGradient(Color.Red, 0.1, GradientStyleType.Horizontal, 2);

{{< /highlight >}}
## **廃止された API**
### **廃止された ShapeFont クラス**
代わりに TextOptions クラスを使用してください。
### **廃止された ShapeFormat クラス**
Shape.Fill および Shape.Line プロパティを直接使用してください。
### **廃止された Shape.Format プロパティ**
Shape.Fill および Shape.Line プロパティを直接使用してください。
### **廃止された Shape.LineFormat プロパティ**
代わりに Shape.Line プロパティを使用してください。
### **廃止された Shape.FillFormat プロパティ**
代わりに Shape.Fill プロパティを使用してください。
### **廃止された FontSetting.ShapeFont プロパティ**
代わりに FontSetting.TextOptions プロパティを使用してください。
