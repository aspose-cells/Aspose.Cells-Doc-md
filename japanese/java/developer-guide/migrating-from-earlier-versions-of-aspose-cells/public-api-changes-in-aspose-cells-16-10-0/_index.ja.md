---
title: パブリック API Aspose.Cells 16.10.0 の変更点
type: docs
weight: 350
url: /ja/java/public-api-changes-in-aspose-cells-16-10-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 9.0.0 から 16.10.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **反射効果のサポート**
Aspose.Cells 16.10.0 は、Shape オブジェクトの反射効果を制御するために、Shape.Reflection プロパティとともに ReflectionEffect クラスを公開しました。 ReflectionEffect クラスには、次のプロパティがあります。

- ReflectionEffect.Blur: ぼかし半径をポイント単位で取得/設定します。
- ReflectionEffect.Direction: シェイプ自体に対するアルファ グラディエント ランプの方向を取得/設定します。
- ReflectionEffect.Distance: 反射の距離をポイント単位で取得/設定します。
- ReflectionEffect.FadeDirection: 反射をオフセットする方向を取得または設定します。
- ReflectionEffect.RotWithShape: 反射が形状と共に回転するかどうかを取得/設定します。
- ReflectionEffect.Size: 終了アルファ値の終了位置 (アルファ グラディエント ランプに沿った) をパーセンテージ単位で取得/設定します。
- ReflectionEffect.Transparency: 開始時の反射の透明度を 0.0 (不透明) から 1.0 (クリア) の値として取得/設定します。
- ReflectionEffect.Type: プリセットの反射効果を取得/設定します。

Shape.Reflection プロパティの簡単な使用シナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[反射効果の操作](/cells/ja/java/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ReflectionEffect from the Shape object

ReflectionEffect reflection = shape.getReflection();

//Set its Blur, Size, Transparency and Distance properties

reflection.setBlur(30);

reflection.setSize(90);

reflection.setTransparency(0.5);

reflection.setDistance(80);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **影効果のサポート**
Aspose.Cells 16.10.0 は、ShadowEffect クラスと共に Shape.ShadowEffect プロパティを公開しました。これにより、Shadow オブジェクトに影の効果を設定できます。 ShadowEffect クラスには次のプロパティがあります。

- ShadowEffect.Angle: 0 ～ 359.9 度の照明角度を取得/設定します。
- ShadowEffect.Blur: 0 ～ 100 ポイントの範囲の影のぼかしを取得および設定します。
- ShadowEffect.Color: 影の色を取得/設定します。
- ShadowEffect.Distance: 影の距離を 0 ～ 200 ポイントの範囲で取得または設定します。
- ShadowEffect.PresetType: シャドウのプリセット シャドウ タイプを取得/設定します。
- ShadowEffect.Size: 影のサイズを 0 から 2.0 の範囲で取得/設定します。内側の影の場合は意味がありません。
- ShadowEffect.Transparency: 影の透明度を 0.0 (不透明) から 1.0 (透明) の範囲で取得/設定します。

前述のプロパティの簡単な使用シナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[シャドウ効果の操作](/cells/ja/java/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ShadowEffect from the Shape object

ShadowEffect shadow = shape.getShadowEffect();

//Set its Angle, Blur, Size, Transparency and Distance properties

shadow.setAngle(150);

shadow.setBlur(30);

shadow.setSize(90);

shadow.setTransparency(0.5);

shadow.setDistance(80);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **グロー効果のサポート**
Aspose.Cells 16.10.0 では、Shape オブジェクトのグロー効果を設定できる GlowEffect クラスと共に Shape.Glow プロパティが公開されました。 GlowEffect クラスはグロー効果を指定します。グロー効果では、次のプロパティを使用して、オブジェクトのエッジの外側に色のぼやけたアウトラインが追加されます。

- GlowEffect.Size: グローの半径をポイント単位で取得/設定します。
- GlowEffect.Transparency: グロー効果の透明度を 0.0 (不透明) から 1.0 (透明) の範囲で取得/設定します。

Shape.Glow プロパティの簡単な使用シナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[グロー効果の操作](/cells/ja/java/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of GlowEffect from the Shape object

GlowEffect glow = shape.getGlow();

//Set its Size & Transparency properties

glow.setSize(90);

glow.setTransparency(0.5);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **3D フォーマットのサポート**
Aspose.Cells 16.10.0 は、Shape オブジェクトの 3D フォーマットを制御するために一緒に使用できる ThreeDFormat クラスと共に Shape.ThreeDFormat プロパティを公開しました。 ThreeDFormat クラスは、図形の 3 次元の書式設定を表し、次のプロパティがあります。

- ThreeDFormat.BottomBevelHeight: 下部ベベルの高さ、または適用される形状の深さをポイント単位で取得/設定します。
- ThreeDFormat.BottomBevelType: 下部ベベルのタイプ、またはそれが適用されるシェイプの深さをポイント単位で取得/設定します。
- ThreeDFormat.BottomBevelWidth: 下部ベベルの幅、またはそれが適用される形状の深さをポイント単位で取得/設定します。
- ThreeDFormat.ContourColor: 形状の輪郭の色を取得/設定します。
- ThreeDFormat.ContourWidth: 形状の輪郭の幅をポイント単位で取得/設定します。
- ThreeDFormat.ExtrusionColor: 形状の押し出し色を取得します。
- ThreeDFormat.ExtrusionHeight: 形状に適用される押し出しの高さをポイント単位で取得/設定します。
- ThreeDFormat.LightAngle: 押し出しライトの角度を取得/設定します。
- ThreeDFormat.Lighting: ライト リグのタイプを取得/設定します。
- ThreeDFormat.LightingDirection: シーンに対するライト リグの方向を取得/設定します。
- ThreeDFormat.Material: 照明プロパティと組み合わせて形状の最終的なルック アンド フィールを与えるプリセット マテリアルを表します。
- ThreeDFormat.Perspective: ThreeDFormat オブジェクトを表示できる角度を取得/設定します。
- ThreeDFormat.PresetCameraType: 押し出しプリセット カメラを取得/設定します。
- ThreeDFormat.RotationX: X 軸を中心とした押し出された形状の回転を度単位で取得/設定します。
- ThreeDFormat.RotationY: Y 軸を中心とした押し出された形状の回転を度単位で取得/設定します。
- ThreeDFormat.RotationZ: Z 軸を中心とした押し出された形状の回転を度単位で取得/設定します。
- ThreeDFormat.TopBevelHeight: 上部のベベルの高さ、または適用される形状の深さをポイント単位で取得/設定します。
- ThreeDFormat.TopBevelType: 上部のベベルのタイプ、または適用されるシェイプの深さをポイント単位で取得/設定します。
- ThreeDFormat.TopBevelWidth: 上部のベベルの幅、または適用される形状の深さをポイント単位で取得/設定します。
- ThreeDFormat.Z: 3D 形状の地面からの距離を定義します。

以下は、Shape.ThreeDFormat プロパティの簡単な使用シナリオです。

{{% alert color="primary" %}} 

の詳細記事をチェック[3D フォーマットの操作](/cells/ja/java/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ThreeDFormat from the Shape object

ThreeDFormat threeD = shape.getThreeDFormat();

//Set its ContourWidth & ExtrusionHeight properties

threeD.setContourWidth(15);

threeD.setExtrusionHeight(30);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **図形のテキストでのワードアート スタイルのサポート**
Aspose.Cells 16.10.0 は、プリセットのワードアート スタイルを Shape オブジェクトのテキストに設定するために、FontSettingCollection.SetWordArtStyle および FontSetting.SetWordArtStyle メソッドを公開しました。

前述の方法の簡単な使用シナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[ワードアート スタイルの操作](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Create a TextBox with some text

int index = sheet.getTextBoxes().add(0, 0, 100, 700);

TextBox textBox = (TextBox)sheet.getShapes().get(index);

textBox.setText("Aspose File Format APIs");

textBox.getFont().setSize(44);

//Set preset WordArt style to the text of the shape

FontSetting fntSetting = (FontSetting)textBox.getCharacters().get(0);

fntSetting.setWordArtStyle(PresetWordArtStyle.WORD_ART_STYLE_15);

{{< /highlight >}}
### **ワードアートの組み込みスタイルのサポート**
Aspose.Cells 16.10.0 は、Excel 2007 以降のプリセット ワードアート オブジェクトの追加をサポートするために、PresetWordArtStyle 列挙と共に ShapeCollection.AddWordArt メソッドを公開しました。

ここでは、ShapeCollection.AddWordArt メソッドの簡単な使用シナリオを示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[組み込みのスタイルでワードアートを追加する](/cells/ja/java/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access ShapeCollection of first worksheet

ShapeCollection shapes = sheet.getShapes();

//Add WordArt with built-in styles

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_1, "Aspose File Format APIs", 00, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **XmlMapCollection.Add メソッドを追加**
Aspose.Cells は、スプレッドシートに Xml マップを追加できる XmlMapCollection.Add メソッドを公開しました。 XmlMapCollection.Add メソッドの簡単な使用シナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[XML マップをスプレッドシートに追加](/cells/ja/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Cells.LinkToXmlMap メソッドを追加**
Aspose.Cells は、セルを XML マップ要素にリンクするために Cells.LinkToXmlMap メソッドを公開しました。 Cells.LinkToXmlMap メソッドの簡単な使用シナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[Cells を XML マップ要素にリンク](/cells/ja/java/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook("sample.xlsx");

//Access the XML Map from the spreadsheet

XmlMap map = book.getWorksheets().getXmlMaps().get(0);

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Map FIELD1 and FIELD2 to cell A1 and B2

sheet.getCells().linkToXmlMap(map.getName(), 0, 0, "/root/row/FIELD1");

sheet.getCells().linkToXmlMap(map.getName(), 1, 1, "/root/row/FIELD2");

//Map FIELD4 and FIELD5 to cell C3 and D4

sheet.getCells().linkToXmlMap(map.getName(), 2, 2, "/root/row/FIELD4");

sheet.getCells().linkToXmlMap(map.getName(), 3, 3, "/root/row/FIELD5");

//Map FIELD7 and FIELD8 to cell E5 and F6

sheet.getCells().linkToXmlMap(map.getName(), 4, 4, "/root/row/FIELD7");

sheet.getCells().linkToXmlMap(map.getName(), 5, 5, "/root/row/FIELD8");

{{< /highlight >}}
### **ListColumn.Formula プロパティを追加**
Aspose.Cells 16.10.0 では、新たに挿入された行に式を自動的に伝達するために、ListColumn.Formula プロパティが公開されました。

ListColumn.Formula プロパティの簡単な使用シナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[リスト オブジェクトに数式を自動的に適用する](/cells/ja/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add column headings in cell A1 and B1

sheet.getCells().get(0, 0).putValue("Column A");

sheet.getCells().get(0, 1).putValue("Column B");

//Add list object, set its name and style

ListObject listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));

listObject.setTableStyleType(TableStyleType.TABLE_STYLE_MEDIUM_14);

listObject.setDisplayName("Table");

//Set the formula of second column so that it could automatically propagate to new rows while entering data

listObject.getListColumns().get(1).setFormula("=[Column A]+ 1");

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
