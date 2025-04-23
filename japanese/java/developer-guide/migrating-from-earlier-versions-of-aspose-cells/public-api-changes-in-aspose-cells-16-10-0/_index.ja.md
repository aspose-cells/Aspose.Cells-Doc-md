---
title: Aspose.Cells 16.10.0の公開APIの変更
type: docs
weight: 350
url: /ja/java/public-api-changes-in-aspose-cells-16-10-0/
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

[形状またはグラフのリフレクション効果の使用](/cells/ja/java/working-with-the-reflection-effect-of-shape-or-chart/)に関する詳細な記事をご確認ください。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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

[形状またはグラフのシャドウ効果の使用](/cells/ja/java/working-with-the-shadow-effect-of-shape-or-chart/)に関する詳細な記事をご確認ください。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **グローエフェクトのサポート**
Aspose.Cells 16.10.0 では、Shape.Glow プロパティが公開され、GlowEffect クラスと共に、Shape オブジェクトのグローエフェクトを設定できるようになりました。 GlowEffect クラスは、以下のプロパティを使用してグローエフェクトを指定します。

- GlowEffect.Size: グローの半径（ポイント単位）を取得/設定します。
- GlowEffect.Transparency: 0.0（不透明）から 1.0（透明）の透明度を取得/設定します。

Shape.Glow プロパティの簡単な使用シナリオを以下に示します。

{{% alert color="primary" %}} 

[グローエフェクトの使用](/cells/ja/java/working-with-the-glow-effect-of-shape-or-chart/)に関する詳細な記事をご確認ください。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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

[3D フォーマットの使用](/cells/ja/java/working-with-the-threedformat-of-shape-or-chart/)に関する詳細な記事をチェックしてください。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **Shape のテキストに WordArt スタイルのサポート**
Aspose.Cells 16.10.0 では、Shape オブジェクトのテキストにプリセットの WordArt スタイルを設定するための FontSettingCollection.SetWordArtStyle および FontSetting.SetWordArtStyle メソッドが公開されています。

上記のメソッドのシンプルな使用シナリオは次のとおりです。

{{% alert color="primary" %}} 

[WordArt スタイルの使用](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)に関する詳細な記事をチェックしてください。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **WordArt の組み込みスタイルのサポート**
Aspose.Cells 16.10.0 では、Excel 2007 以降でのプリセット WordArt オブジェクトの追加のサポートを提供するために、ShapeCollection.AddWordArt メソッドと PresetWordArtStyle 列挙型を公開しています。

ShapeCollection.AddWordArt メソッドの単純な使用シナリオは次のとおりです。

{{% alert color="primary" %}} 

[組み込みスタイルの WordArt の追加](/cells/ja/java/add-word-art-text-with-built-in-styles/)に関する詳細な記事をチェックしてください。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **XmlMapCollection.Add メソッドが追加されました**
Aspose.Cells は、スプレッドシートに Xml マップを追加する XmlMapCollection.Add メソッドを公開しました。XmlMapCollection.Add メソッドの単純な使用シナリオは次のとおりです。

{{% alert color="primary" %}} 

[スプレッドシートに XML マップを追加](/cells/ja/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)に関する詳細な記事をチェックしてください。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Cells.LinkToXmlMap メソッドを追加しました**
Aspose.Cells は、セルを XML マップ要素にリンクするために Cells.LinkToXmlMap メソッドを公開しました。Cells.LinkToXmlMap メソッドの簡単な使用シナリオは次のとおりです。

{{% alert color="primary" %}} 

[セルを XML マップ要素にリンク](/cells/ja/java/link-cells-to-xml-map-elements/)する詳細な記事を確認してください

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **ListColumn.Formula プロパティを追加しました**
Aspose.Cells 16.10.0 は、新しく挿入された行に自動的に式を伝達するために ListColumn.Formula プロパティを公開しました。

ListColumn.Formula プロパティの簡単な使用シナリオは次のとおりです。

{{% alert color="primary" %}} 

[テーブルまたはリスト オブジェクトに新しい行にデータを入力する際に自動的に式を伝達](/cells/ja/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)する詳細な記事を確認してください

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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

listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
