---
title: Aspose.Cells 16.10.0の公開APIの変更
type: docs
weight: 340
url: /ja/net/public-api-changes-in-aspose-cells-16-10-0/
---

{{% alert color="primary" %}} 

このドキュメントは、モジュール/アプリケーション開発者に興味があるかもしれない、Aspose.Cells APIのバージョン9.0.0から16.10.0への変更点について説明しています。新しいおよび更新された公開メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cellsの裏側での挙動の変更の説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **反射効果のサポート**
Aspose.Cells 16.10.0では、Shapeオブジェクトの反射効果を制御するためにReflectionEffectクラスとShape.Reflectionプロパティが公開されました。ReflectionEffectクラスには以下のプロパティがあります。

- ReflectionEffect.Blur: ポイント単位のぼかし半径を取得/設定します。
- ReflectionEffect.Direction: 形状自体に対するアルファグラデーションランプの方向を取得/設定します。
- ReflectionEffect.Distance: リフレクションの距離（ポイント単位）を取得/設定します。
- ReflectionEffect.FadeDirection: リフレクションのオフセット方向を取得/設定します。
- ReflectionEffect.RotWithShape: リフレクションを図形とともに回転させるかどうかを取得/設定します。
- ReflectionEffect.Size: 終了アルファ値までの終了位置（アルファグラデーションランプに沿って）をパーセンテージ単位で取得/設定します。
- ReflectionEffect.Transparency: 開始リフレクションの透明度を0.0（不透明）から1.0（透明）の値で取得/設定します。
- ReflectionEffect.Type: プリセットのリフレクション効果を取得/設定します。

Shape.Reflection プロパティの簡単な使用シナリオを以下に示します。

{{% alert color="primary" %}} 

[反射効果の取り扱い](/cells/ja/net/working-with-the-reflection-effect-of-shape-or-chart/) の詳細な記事をチェックしてください。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ReflectionEffect from the Shape object

var reflection = shape.Reflection;

// Set its Blur, Size, Transparency and Distance properties

reflection.Blur = 30;

reflection.Size = 90;

reflection.Transparency = 0.5;

reflection.Distance = 80;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **シャドウ効果のサポート**
Aspose.Cells 16.10.0 では、Shape.ShadowEffect プロパティが公開され、ShadowEffect クラスと共に、Shape オブジェクトにシャドウ効果を設定することが可能となりました。 ShadowEffect クラスには、以下のプロパティがあります。

- ShadowEffect.Angle: 0から359.9度までの照明角度を取得/設定します。
- ShadowEffect.Blur: 0から100ポイントまでのシャドウのぼかしを取得および設定します。
- ShadowEffect.Color: シャドウの色を取得/設定します。
- ShadowEffect.Distance: 0から200ポイントまでのシャドウの距離を取得/設定します。
- ShadowEffect.PresetType: シャドウのプリセットタイプを取得/設定します。
- ShadowEffect.Size: 0 から 2.0 までのシャドウのサイズを取得/設定します。内部シャドウの場合は無意味です。
- ShadowEffect.Transparency: 0.0（不透明）から 1.0（透明）の透明度を取得/設定します。

上記のプロパティの簡単な使用シナリオを以下に示します。

{{% alert color="primary" %}} 

[形状やチャートにシャドウエフェクトを利用](/cells/ja/net/working-with-the-shadow-effect-of-shape-or-chart/)の詳細な記事をチェックしてください。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ShadowEffect from the Shape object

var shadow = shape.ShadowEffect;

// Set its Angle, Blur, Size, Transparency and Distance properties

shadow.Angle = 150;

shadow.Blur = 30;

shadow.Size = 90;

shadow.Transparency = 0.5;

shadow.Distance = 80;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **グローエフェクトのサポート**
Aspose.Cells 16.10.0 では、Shape.Glow プロパティが公開され、GlowEffect クラスと共に、Shape オブジェクトのグローエフェクトを設定できるようになりました。 GlowEffect クラスは、以下のプロパティを使用してグローエフェクトを指定します。

- GlowEffect.Size: グローの半径（ポイント単位）を取得/設定します。
- GlowEffect.Transparency: 0.0（不透明）から 1.0（透明）の透明度を取得/設定します。

Shape.Glow プロパティの簡単な使用シナリオを以下に示します。

{{% alert color="primary" %}} 

[形状やチャートにグローエフェクトを利用](/cells/ja/net/working-with-the-glow-effect-of-shape-or-chart/)の詳細な記事をチェックしてください。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of GlowEffect from the Shape object

var glow = shape.Glow;

// Set its Size & Transparency properties

glow.Size = 90;

glow.Transparency = 0.5;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **3D形式のサポート**
Aspose.Cells 16.10.0 では、Shape.ThreeDFormat プロパティが公開され、ThreeDFormat クラスと共に、Shape オブジェクトの3Dの書式設定を制御するために使用できます。 ThreeDFormat クラスは、以下のプロパティを持っています。

- ThreeDFormat.BottomBevelHeight: 下部面取りの高さまたは形状内に適用される距離をポイント単位で取得/設定します。
- ThreeDFormat.BottomBevelType: 下部面取りのタイプまたは形状内に適用される距離をポイント単位で取得/設定します。
- ThreeDFormat.BottomBevelWidth: 下部面取りの幅または形状内に適用される距離をポイント単位で取得/設定します。
- ThreeDFormat.ContourColor: シェイプの輪郭色を取得/設定します。
- ThreeDFormat.ContourWidth: シェイプ上の輪郭の幅をポイント単位で取得/設定します。
- ThreeDFormat.ExtrusionColor: シェイプ上の突出色を取得します。
- ThreeDFormat.ExtrusionHeight: シェイプに適用される突出の高さをポイント単位で取得/設定します。
- ThreeDFormat.LightAngle: 突出光の角度を取得/設定します。
- ThreeDFormat.Lighting: ライト リグのタイプを取得/設定します。
- ThreeDFormat.LightingDirection: シーンに対するライト リグの向きを取得/設定します。
- ThreeDFormat.Material: シェイプの最終的な外観と感触を与えるために照明プロパティと組み合わされるプリセット素材を表します。
- ThreeDFormat.Perspective: ThreeDFormat オブジェクトが表示できる角度を取得/設定します。
- ThreeDFormat.PresetCameraType: 突出のプリセットカメラを取得/設定します。
- ThreeDFormat.RotationX: X 軸を中心にした突出形状の回転を度単位で取得/設定します。
- ThreeDFormat.RotationY: Y 軸を中心にした突出形状の回転を度単位で取得/設定します。
- ThreeDFormat.RotationZ: Z 軸を中心にした突出形状の回転を度単位で取得/設定します。
- ThreeDFormat.TopBevelHeight: 上面面取りの高さをポイント単位で取得/設定します。
- ThreeDFormat.TopBevelType: 上面面取りのタイプをポイント単位で取得/設定します。
- ThreeDFormat.TopBevelWidth: 上面面取りの幅をポイント単位で取得/設定します。
- ThreeDFormat.Z: 3D シェイプの地面からの距離を定義します。

Shape.ThreeDFormat プロパティの単純な使用シナリオは次のとおりです。

{{% alert color="primary" %}} 

[3Dフォーマットとの作業] (/cells/ja/net/working-with-the-threedformat-of-shape-or-chart/)の詳細な記事を確認してください

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ThreeDFormat from the Shape object

var threeD = shape.ThreeDFormat;

// Set its ContourWidth & ExtrusionHeight properties

threeD.ContourWidth = 15;

threeD.ExtrusionHeight = 30;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Shape のテキストに WordArt スタイルのサポート**
Aspose.Cells 16.10.0 では、Shape オブジェクトのテキストにプリセットの WordArt スタイルを設定するための FontSettingCollection.SetWordArtStyle および FontSetting.SetWordArtStyle メソッドが公開されています。

上記のメソッドのシンプルな使用シナリオは次のとおりです。

{{% alert color="primary" %}} 

[WordArtスタイルとの作業] (/cells/ja/net/set-preset-wordart-style-to-the-text-of-the-shape/) の詳細な記事を確認してください

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create workbook object

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Create a TextBox with some text

var textBox = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 700);

textBox.Text = "Aspose File Format APIs";

textBox.Font.Size = 44;

// Set preset WordArt style to the text of the shape

FontSetting fntSetting = textBox.GetCharacters()[0] as FontSetting;

fntSetting.SetWordArtStyle(PresetWordArtStyle.WordArtStyle3);

{{< /highlight >}}


### **WordArt の組み込みスタイルのサポート**
Aspose.Cells 16.10.0 では、Excel 2007 以降でのプリセット WordArt オブジェクトの追加のサポートを提供するために、ShapeCollection.AddWordArt メソッドと PresetWordArtStyle 列挙型を公開しています。

ShapeCollection.AddWordArt メソッドの単純な使用シナリオは次のとおりです。

{{% alert color="primary" %}} 

[組み込みスタイルのWordArtを追加する] (/cells/ja/net/add-word-art-text-with-built-in-styles/) の詳細な記事を確認してください

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access ShapeCollection of first worksheet

var shapes = sheet.Shapes;

// Add WordArt with built-in styles

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 00, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **XmlMapCollection.Add メソッドが追加されました**
Aspose.Cells は、スプレッドシートに Xml マップを追加する XmlMapCollection.Add メソッドを公開しました。XmlMapCollection.Add メソッドの単純な使用シナリオは次のとおりです。

{{% alert color="primary" %}} 

[スプレッドシートにXMLマップを追加] (/cells/ja/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/) の詳細な記事を確認してください

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **Cells.LinkToXmlMap メソッドを追加しました**
Aspose.Cellsは、新たに追加された行に自動的に式を伝播するためのCells.LinkToXmlMapメソッドを公開しました。 以下はCells.LinkToXmlMapメソッドのシンプルな使用シナリオです。

[セルをXMLマップ要素にリンク] (/cells/ja/net/link-cells-to-xml-map-elements/)の詳細な記事を確認してください

{{% alert color="primary" %}} 

[リンクセルをXMLマップ要素に接続する](/cells/ja/net/link-cells-to-xml-map-elements/)の詳細な記事をチェックしてください

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook("sample.xlsx");

// Access the XML Map from the spreadsheet

var map = book.Worksheets.XmlMaps[0];

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Map FIELD1 and FIELD2 to cell A1 and B2

sheet.Cells.LinkToXmlMap(map.Name, 0, 0, "/root/row/FIELD1");

sheet.Cells.LinkToXmlMap(map.Name, 1, 1, "/root/row/FIELD2");

// Map FIELD4 and FIELD5 to cell C3 and D4

sheet.Cells.LinkToXmlMap(map.Name, 2, 2, "/root/row/FIELD4");

sheet.Cells.LinkToXmlMap(map.Name, 3, 3, "/root/row/FIELD5");

// Map FIELD7 and FIELD8 to cell E5 and F6

sheet.Cells.LinkToXmlMap(map.Name, 4, 4, "/root/row/FIELD7");

sheet.Cells.LinkToXmlMap(map.Name, 5, 5, "/root/row/FIELD8");

{{< /highlight >}}


### **ListColumn.Formula プロパティを追加しました**
Aspose.Cells 16.10.0 は、新しく挿入された行に自動的に式を伝達するために ListColumn.Formula プロパティを公開しました。

ListColumn.Formula プロパティの簡単な使用シナリオは次のとおりです。

{{% alert color="primary" %}} 

[テーブルまたはリストオブジェクトへのデータの入力時に、自動的に式を伝播] (/cells/ja/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/) の詳細な記事を確認してください

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add column headings in cell A1 and B1

sheet.Cells[0, 0].PutValue("Column A");

sheet.Cells[0, 1].PutValue("Column B");

// Add list object, set its name and style

var listObject = sheet.ListObjects[sheet.ListObjects.Add(0, 0, 1, sheet.Cells.MaxColumn, true)];

listObject.TableStyleType = TableStyleType.TableStyleMedium2;

listObject.DisplayName = "Table";

// Set the formula of second column so that it could automatically propagate to new rows while entering data

listObject.ListColumns[1].Formula = "=[Column A] + 1";

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **GridWebでのカスタム関数の計算をサポート**
Aspose.Cells.GridWeb 16.10.0では、GridWeb.CustomCalculationEngineプロパティとGridAbstractCalculationEngineクラスを公開しました。 これらをすべて使用することで、GridWebコンポーネント内からカスタム関数を定義および計算できます。

上記のAPIのシンプルな使用シナリオは次のとおりです。

{{% alert color="primary" %}} 

[GridWebでのカスタム関数の計算] (/cells/ja/net/calculate-custom-functions-in-gridweb/) の詳細な記事を確認してください

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 private class GridWebCustomCalculationEngine : GridAbstractCalculationEngine

{

    public override void Calculate(GridCalculationData data)

    {

        //  Calculate MYTESTFUNC() with your own logic.

        //For example, you can multiply MYTESTFUNC() parameter with 2 so

        // MYTESTFUNC(3.0) will return 6

        // MYTESTFUNC(4.0) will return 8

        // MYTESTFUNC(5.0) will return 10

        if ("MYTESTFUNC".Equals(data.FunctionName.ToUpper()))

        {

            data.CalculatedValue = (decimal)(2.0 * (double)data.GetParamValue(0));

        }

    }

}


if (Page.IsPostBack == false && GridWeb1.IsPostBack == false)

{

    // Assign your own custom calculation engine to GridWeb

    GridWeb1.CustomCalculationEngine = new GridWebCustomCalculationEngine();

    // Access the active worksheet and add your custom function in cell B3

    GridWorksheet sheet = GridWeb1.ActiveSheet;

    GridCell cell = sheet.Cells["B3"];

    cell.Formula = "=MYTESTFUNC(9.0)";

    // Calculate the GridWeb formula

    GridWeb1.CalculateFormula();

}

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
