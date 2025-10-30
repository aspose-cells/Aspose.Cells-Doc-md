---  
title: Node.jsとC++を使った写真の管理  
linktitle: 画像の管理  
type: docs  
weight: 10  
url: /ja/nodejs-cpp/managing-pictures/  
description: Aspose.Cells for Node.js via C++を使用して、スプレッドシートに画像を追加し配置する方法を学びます。  
---  

Aspose.Cellsを使用すると、開発者は実行時にスプレッドシートに画像を追加できます。さらに、これらの画像の位置を実行時に制御することができます。これについては後のセクションで詳しく説明します。

この資料では、画像の追加方法や特定のセルの内容を示す画像の挿入方法について解説します。

## **画像の追加**

スプレッドシートに写真を追加するのは非常に簡単です。わずかなコード行だけで済みます:  
[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)オブジェクトのコレクションの[**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection)メソッドの[**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-)を呼び出すだけです。[**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-)メソッドは以下のパラメータを取ります：

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

## **写真の位置合わせ**

Aspose.Cellsを使用して写真の位置合わせを制御する方法には2つの方法があります:

- 比例位置合わせ：行の高さと幅に比例した位置を定義します。
- 絶対位置指定：画像を挿入するページ上の正確な位置を定義します。例：セルの縁から左に40ピクセル、下に20ピクセル。

### **比例位置合わせ**

開発者は、[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)オブジェクトの[**getUpperDeltaX()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaX--)と[**getUpperDeltaY()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaY--)のプロパティを使用して、行の高さと列の幅に比例した画像の位置を設定できます。[**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection)コレクションから画像のインデックスを渡すことで、[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)オブジェクトを取得できます。この例では、F6セルに画像を配置しています。

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
const pictureIndex = worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Positioning the picture proportional to row height and column width
picture.setUpperDeltaX(200);
picture.setUpperDeltaY(200);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **絶対位置づけ**

開発者は、[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)オブジェクトの[**getLeft()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeft--)と[**getTop()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTop--)のプロパティを使用して、画像を絶対位置に配置することも可能です。この例では、セルF6に画像を配置し、左から60ピクセル、上から10ピクセルの位置にあります。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "logo.jpg");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, filePath);

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Absolute positioning of the picture in unit of pixels
picture.setLeft(60);
picture.setTop(10);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **セル参照に基づいて画像を挿入**

Aspose.Cellsを使用すると、ワークシートのセルの内容を画像形状で表示できます。画像は、データを表示したいセルにリンクされています。セルまたはセル範囲がグラフィックオブジェクトにリンクされているため、そのセルまたはセル範囲のデータを変更すると、自動的にグラフィックオブジェクトに変更が反映されます。

[**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection)コレクションの[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)オブジェクトの[**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-)メソッドを呼び出して、ワークシートに画像を追加します。セル範囲は、[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)オブジェクトの[**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--)属性を使用して指定します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

const picts = workbook.getWorksheets().get(0).getPictures();
// Add a blank picture to the D1 cell
const picIndex = picts.add(0, 3, 10, 6, null);
const pic = picts.get(picIndex);

// Specify the formula that refers to the source range of cells

pic.setFormula("A1:C10");

// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **高度なトピック**
- [セルのテキストと条件付きアイコンセットの追加](/cells/ja/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/)
- [Webアドレスからリンクされた画像の挿入](/cells/ja/nodejs-cpp/insert-a-linked-picture-from-web-address/)
- [セル参照に基づく画像の挿入](/cells/ja/nodejs-cpp/insert-a-picture-based-on-cell-reference/)
- [Web画像のURLをExcelワークシートに読み込む](/cells/ja/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="nodejs-cpp" >}}
