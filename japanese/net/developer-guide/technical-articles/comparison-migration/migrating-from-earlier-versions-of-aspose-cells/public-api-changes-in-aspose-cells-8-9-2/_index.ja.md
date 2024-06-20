---
title: Aspose.Cells 8.9.2 でのパブリック API 変更
type: docs
weight: 320
url: /ja/net/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cells API の 8.9.1 から 8.9.2 への変更点をモジュール/アプリケーション開発者にとって興味深いものについて説明しています。新しいおよび更新されたパブリックメソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の内部での動作の変更についても説明しています。

{{% /alert %}} {{% alert color="primary" %}} 

[Aspose.Cells for .NET 8.9.1 で新たに導入された Public API 変更](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1) も参照してください。

{{% /alert %}} 
## **APIの追加**
### **TextOptions クラスと FontSettings.TextOptions プロパティが追加されました**
Aspose.Cells for .NET で TextOptions クラスとそれに伴う FontSettings.TextOptions プロパティを公開し、Shape のテキスト部分の外観を制御するためのものです。

FontSettings.TextOptions プロパティの簡単な使用シナリオは次のとおりです。

**C#**

{{< highlight csharp >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access TextOptions of Shape

var textOptions = shape.TextBody[1].TextOptions;

{{< /highlight >}}


### **TextOptions.Fill、Outline、Shadow プロパティが追加されました**
Aspose.Cells for .NET 8.9.2 で TextOptions.Fill、TextOptions.Outline、TextOptions.Shadow プロパティが公開され、それぞれ形状のテキストコンテンツの塗りつぶし、影、輪郭などの側面を制御できます。

前述のプロパティの簡単な使用シナリオは次のとおりです。

**C#**

{{< highlight csharp >}}

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


### **Shape.Line プロパティが追加されました**
Aspose.Cells for .NET で Shape.Line プロパティが公開され、Shape の輪郭の外観を制御するための LineFormat インスタンスを返します。

以下はShape.Lineプロパティの簡単な使用シナリオです。

**C#**

{{< highlight csharp >}}

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


### **Shape.Fill プロパティが追加されました**
Aspose.Cells for .NET 8.9.2 で Shape.Fill プロパティが公開され、異なる形状領域の側面を制御するための FillFormat インスタンスを返します。

Shape.Fill プロパティの簡単な使用シナリオは次のとおりです。

**C#**

{{< highlight csharp >}}

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
## **非推奨API**
### **非推奨のShapeFontクラス**
代わりにTextOptionsクラスを使用してください。
### **非推奨のShapeFormatクラス**
代わりにShape.FillおよびShape.Lineプロパティを直接使用してください。
### **非推奨のShape.Formatプロパティ**
代わりにShape.FillおよびShape.Lineプロパティを直接使用してください。
### **非推奨のShape.LineFormatプロパティ**
代わりにShape.Lineプロパティを使用してください。
### **非推奨のShape.FillFormatプロパティ**
代わりにShape.Fillプロパティを使用してください。
### **非推奨のFontSetting.ShapeFontプロパティ**
代わりにFontSetting.TextOptionsプロパティを使用してください。
