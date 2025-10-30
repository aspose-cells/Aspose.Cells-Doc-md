---  
title: Node.jsを使ってC++経由でExcelファイルに画像やシェイプを挿入する  
linktitle: シェイプ  
type: docs  
weight: 140  
url: /ja/nodejs-cpp/insert-shapes/  
description: Excelファイル内の画像、OLEオブジェクト、シェイプの管理には、Aspose.Cells for Node.js via C++を使用します。  
---  

{{% alert color="primary" %}}  
必要に応じてワークシートにシェイプを挿入する必要がある場合があります。同じシェイプを異なる位置に挿入したり、バッチで複数のシェイプを挿入したりすることもあります。  
心配しないでください！[Aspose.Cells](https://products.aspose.com/cells/)はこれらの操作をすべてサポートしています。  
{{% /alert %}}  

Excelのシェイプは主に次のタイプに分類されます：  
- **写真**  
- **OLEオブジェクト**  
- **直線**  
- **四角形**  
- **基本図形**  
- **ブロック矢印**  
- **数式図形**  
- **フローチャート**  
- **星とバナー**  
- **吹き出し**  

このガイドドキュメントでは、各タイプから1つまたは2つのシェイプを選び、サンプルを作成します。これらの例を通じて、[Aspose.Cells](https://products.aspose.com/cells/)を使用して指定されたシェイプをワークシートに挿入する方法を学びます。  

## **Node.jsを使用したExcelワークシートへの画像追加**  

スプレッドシートに写真を追加するのは非常に簡単です。わずかなコード行だけで済みます:  
[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)オブジェクトのコレクションの[**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection)メソッドの[**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-)を呼び出すだけです。[**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-)メソッドは以下のパラメータを取ります：  

- **左上の行インデックス**、左上の行のインデックス。  
- **左上の列インデックス**、左上の列のインデックス。  
- **画像ファイル名**、パスを含む画像ファイルの名前。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Node.jsを使ったExcelワークシートへのOLEオブジェクト挿入**  

Aspose.Cellsは、ワークシートへのOLEオブジェクトの追加、抽出、および操作をサポートします。そのため、コレクションリストに新しいOLEオブジェクトを追加するために使用される[**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection)クラスと、OLEオブジェクトを表す[**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject)クラスがあります。重要なメンバーは次の通りです：  

- `[**OleObject.getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--)`プロパティは、イメージ（アイコン）のデータをバイト配列型で指定します。この画像は、ワークシート内のOLEオブジェクトを表示するために使われます。  
- `[**OleObject.getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--)`プロパティは、オブジェクトのデータをバイト配列の形式で指定します。このデータは、ダブルクリックによって関連付けられたプログラムで表示されます。  

以下の例は、ワークシートにOLEオブジェクトを追加する方法を示しています。  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const excelFilePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(excelFilePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Node.jsを使用したExcelワークシートへのライン挿入**  

ラインの形状は**lines**カテゴリに属します。  

***Microsoft Excel（例: 2007年）***  

- 線を挿入するセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- それから、『最近使ったシェイプ』または『ライン』からラインを選択します。  

![](line.png)  

***Aspose.Cells を使用***  

ワークシートに線を挿入するために以下の方法を使用できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
このメソッドは、[LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape)オブジェクトを返します。  
{{% /alert %}}  

以下の例では、ワークシートにラインを挿入する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line to the worksheet
sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// sheet.getShapes().addAutoShape(AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// sheet.getShapes().addShape(MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// Save. You can check your line in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

上記のコードを実行すると、次の結果が得られます。  

![](line2.png)  

## **Node.jsを使ったExcelワークシートへの矢印ライン挿入**  

矢印ラインの形状は**Lines**カテゴリに属しており、ラインの特殊なケースです。  

***Microsoft Excel（例: 2007年）***  

- 矢印を挿入するセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- それから、『最近使ったシェイプ』または『ライン』から矢印ラインを選択します。  

![](line_arrow1.png)  

***Aspose.Cells を使用***  

ワークシートに直線矢印を挿入するために以下の方法を使用できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
このメソッドは、[LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape)オブジェクトを返します。  
{{% /alert %}}  

以下の例では、ワークシートに矢印ラインを挿入する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line arrow to the worksheet
let s = sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// let s = sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// let s = sheet.getShapes().addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// add a arrow at the line begin
s.getLine().setBeginArrowheadStyle(AsposeCells.MsoArrowheadStyle.Arrow); // arrow type
s.getLine().setBeginArrowheadWidth(AsposeCells.MsoArrowheadWidth.Wide); // arrow width
s.getLine().setBeginArrowheadLength(AsposeCells.MsoArrowheadLength.Short); // arrow length

// add a arrow at the line end
s.getLine().setEndArrowheadStyle(AsposeCells.MsoArrowheadStyle.ArrowOpen); // arrow type
s.getLine().setEndArrowheadWidth(AsposeCells.MsoArrowheadWidth.Narrow); // arrow width
s.getLine().setEndArrowheadLength(AsposeCells.MsoArrowheadLength.Long); // arrow length

// Save. You can check your arrow in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

上記のコードを実行すると、次の結果が得られます。  

![](line_arrow2.png)  

## **Node.jsを使ったExcelワークシートへの四角形挿入**  

四角形の形状は**Rectangles**カテゴリに属します。  

***Microsoft Excel（例: 2007年）***  

- 長方形を挿入するセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- それから、『最近使ったシェイプ』または『四角形』から選択します。  

![](rectangle.png)  

***Aspose.Cells を使用***  

ワークシートに長方形を挿入するには、次のメソッドを使用できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
このメソッドは、[RectangleShape](https://reference.aspose.com/cells/nodejs-cpp/rectangleshape)オブジェクトを返します。  
{{% /alert %}}  

以下の例では、ワークシートに四角形を挿入する方法を示しています。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the rectangle to the worksheet
sheet.getShapes().addRectangle(2, 0, 2, 0, 100, 300);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

上記のコードを実行すると、次の結果が得られます。  

![](rectangle2.png)  

## **Node.jsを使ってExcelシートにキューブを挿入する**  

キューブの形状は**基本図形**カテゴリに属します。  

***Microsoft Excel（例: 2007年）***  

- キューブを挿入したいセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- その後、**基本図形**からキューブを選択します  

![](cube.png)  

***Aspose.Cells を使用***  

ワークシートにキューブを挿入するには、次のメソッドを使用できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
このメソッドは[Shape](https://reference.aspose.com/cells/nodejs-cpp/shape)オブジェクトを返します。  
{{% /alert %}}  

例は、ワークシートにキューブを挿入する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the cube to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

// Save. You can check your cube in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

上記のコードを実行すると、次の結果が得られます。  

![](cube2.png)  

## **Node.jsを使ったExcelシートへのコールアウトクアッドアローの挿入**  

コールアウトクアッドアローの形状は**ブロック矢印**カテゴリに属します。  

***Microsoft Excel（例: 2007年）***  

- コールアウト四角矢印を挿入したいセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- その後、**ブロック矢印**からコールアウトクアッドアローを選びます  

![](callout_quad_arrow.png)  

***Aspose.Cells を使用***  

ワークシートにコールアウト四角矢印を挿入するには、次のメソッドを使用できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
このメソッドは[Shape](https://reference.aspose.com/cells/nodejs-cpp/shape)オブジェクトを返します。  
{{% /alert %}}  

例は、ワークシートにコールアウトクアッドアローを挿入する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the callout quad arrow to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

//Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

上記のコードを実行すると、次の結果が得られます。  

![](callout_quad_arrow2.png)  

## **Node.jsを使ったExcelシートへの掛け算記号の挿入**  

掛け算記号の形状は**式図形**カテゴリに属します。  

***Microsoft Excel（例: 2007年）***  

- 乗算記号を挿入したいセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- その後、**式図形**から掛け算記号を選択します  

![](multiplication_sign.png)  

***Aspose.Cells を使用***  

次の方法を使用してワークシートに乗算記号を挿入できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
このメソッドは[Shape](https://reference.aspose.com/cells/nodejs-cpp/shape)オブジェクトを返します。  
{{% /alert %}}  

例は、ワークシートに掛け算記号を挿入する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multiplication sign to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

// Save. You can check your multiplication in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

上記のコードを実行すると、次の結果が得られます。  

![](multiplication_sign2.png)  

## **Node.jsを使ったExcelシートへの多ドキュメントの挿入**  

多ドキュメントの形状は**フローチャート**カテゴリに属します。  

***Microsoft Excel（例: 2007年）***  

- 多重ドキュメントを挿入するセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- その後、多ドキュメントを**フローチャート**から選択します  

![](multidocument.png)  

***Aspose.Cells を使用***  

次の方法を使用してワークシートに多重ドキュメントを挿入できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
このメソッドは[Shape](https://reference.aspose.com/cells/nodejs-cpp/shape)オブジェクトを返します。  
{{% /alert %}}  

例は、多ドキュメントをワークシートに挿入する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multidocument to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

上記のコードを実行すると、次の結果が得られます。  

![](multidocument2.png)  

## **Node.jsを使用してExcelワークシートに五芒星を挿入する**  

五芒星の形状は**星とバナー**カテゴリに属しています。  

***Microsoft Excel（例: 2007年）***  

- 五角星を挿入したいセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- その後、**星とバナー**から五芒星を選択します  

![](star_5_points.png)  

***Aspose.Cells を使用***  

この方法は [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
このメソッドは[Shape](https://reference.aspose.com/cells/nodejs-cpp/shape)オブジェクトを返します。  
{{% /alert %}}  

次の例は、ワークシートに五芒星を挿入する方法を示しています。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the Five-pointed star to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

// Save. You can check your icon in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

上記のコードを実行すると、次の結果が得られます。  

![](star_5_points2.png)  

## **Node.jsを使用してExcelワークシートに思考バブル雲を挿入する**  

思考バブル雲の形状は**コールアウト**カテゴリに属しています。  

***Microsoft Excel（例: 2007年）***  

- 思考バブルクラウドを挿入したいセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- その後、**コールアウト**から思考バブル雲を選択します  

![](thought_bubble_cloud.png)  

***Aspose.Cells を使用***  

ワークシートに思考バブルクラウドを挿入するために次の方法を使用できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
このメソッドは[Shape](https://reference.aspose.com/cells/nodejs-cpp/shape)オブジェクトを返します。  
{{% /alert %}}  

次の例は、ワークシートに思考バブル雲を挿入する方法を示しています。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the thought bubble cloud to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

上記のコードを実行すると、次の結果が得られます。  

![](thought_bubble_cloud2.png)  

## **高度なトピック**  
- [図形の調整値を変更](/cells/ja/nodejs-cpp/change-adjustment-values-of-the-shape/)  
- [ワークシート間で図形をコピーする](/cells/ja/nodejs-cpp/copy-shapes-between-worksheets/)  
- [非プリミティブ形状のデータ](/cells/ja/nodejs-cpp/data-in-non-primitive-shape/)  
- [ワークシート内の形状の絶対位置を検索する](/cells/ja/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [形状から接続ポイントを取得する](/cells/ja/nodejs-cpp/get-connection-points-from-shape/)  
- [コントロールの管理](/cells/ja/nodejs-cpp/managing-controls/)  
- [ワークシートにアイコンを追加する](/cells/ja/nodejs-cpp/insert-svg-to-excel/)  
- [OLE オブジェクトの管理](/cells/ja/nodejs-cpp/managing-ole-objects/)  
- [画像の管理](/cells/ja/nodejs-cpp/managing-pictures/)  
- [Smart Art の管理](/cells/ja/nodejs-cpp/managing-smartart/)  
- [テキストボックスの管理](/cells/ja/nodejs-cpp/managing-textbox-of-excel/)  
- [Aspose.Cells にワードアートウォーターマークを追加](/cells/ja/nodejs-cpp/add-wordart-watermark-to-worksheet/)  
- [リンクされた図形の値を更新する](/cells/ja/nodejs-cpp/refresh-values-of-linked-shapes/)  
- [ワークシート内でShape FrontまたはBackを送信する](/cells/ja/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [形状オプションを管理する](/cells/ja/nodejs-cpp/managing-shape-options/)  
- [形状テキストオプションの管理](/cells/ja/nodejs-cpp/managing-shape-text-options/)  
- [Web拡張 - Office アドイン](/cells/ja/nodejs-cpp/web-extensions-office-add-ins/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
