---
title: Node.jsを使用したセルのマージとアンマージ
linktitle: セルの結合と解除
description: Aspose.Cellsは、セルのマージとアンマージをサポートするスプレッドシートファイル操作用Node.jsライブラリです。この記事では、Aspose.Cellsライブラリを使ったセルのマージとアンマージの方法と、マージセルのスタイルカスタマイズオプションについて紹介します。
keywords: Aspose.Cells、Node.jsライブラリ、スプレッドシート、セルの結合、アンマージ、スタイル設定、カスタムスタイル
type: docs
weight: 190
url: /ja/nodejs-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cellsはこの機能をサポートし、ワークシート内でセルを結合することもできます。 結合されたセルは解除することもできます。 結合されたセルのセル参照は、元の選択範囲の左上のセルの参照です。

{{% /alert %}} 
## **紹介**
すべての行や列に常に同じ数のセルを必ずしも欲しいわけではありません。 たとえば、複数の列にまたがるタイトルを置きたい場合があります。 または、請求書を作成する場合、合計に対して少ない列を望むことがあります。 セルを1つに結合してみてください。 Microsoft Excelは、ユーザーがファイルを選択して自分の望むようにスプレッドシートの構造を結合できます。

{{% alert color="primary" %}} 

セルをマージすると、左上のセルのデータだけが保持されます。範囲内の他のセルにデータがある場合は、そのデータは削除されます。書式設定も参照セルの基準に基づいて行われ、セルのマージ時には範囲内の左上セルの書式設定が適用されます。セルの分割時には、新しいセルは元の書式設定を保持します。

{{% /alert %}} 
## **ワークシート内でセルを結合する**
### **Microsoft Excelでセルを結合する**
以下の手順では、MS Excelを使用してワークシート内のセルを結合する方法について説明します。

1. 範囲内で左上のセルにデータをコピーします。
1. 結合したいセルを選択します。
1. 行または列内のセルを結合してセルの内容を中央に配置するには、**書式設定**ツールバーの**結合して中央配置**アイコンをクリックします。

### **Aspose.Cellsでセルの結合**
Aspose.Cells.Cellsクラスにはこの作業に役立つ便利なメソッドがあります。例えば、merge()メソッドは特定の範囲内のセルを1つのセルに結合します。

以下の例は、ワークシート内のセル(C6:E7)を結合する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
const wbk = new AsposeCells.Workbook();

// Create a Worksheet and get the first sheet.
const worksheet = wbk.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Merge some Cells (C6:E7) into a single C6 Cell.
cells.merge(5, 2, 2, 3);

// Input data into C6 Cell.
cells.get(5, 2).putValue("This is my value");

// Create a Style object to fetch the Style of C6 Cell.
const style = cells.get(5, 2).getStyle();

// Create a Font object
const font = style.getFont();

// Set the name.
font.setName("Times New Roman");

// Set the font size.
font.setSize(18);

// Set the font color
font.setColor(AsposeCells.Color.Blue);

// Bold the text
font.setIsBold(true);

// Make it italic
font.setIsItalic(true);

// Set the background color of C6 Cell to Red
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);

// Apply the Style to C6 Cell.
cells.get(5, 2).setStyle(style);

// Save the Workbook.
wbk.save(path.join(dataDir, "mergingcells.out.xls"));
```

## **結合されたセルの結合解除（分割）**
### **Microsoft Excel の使用**
以下の手順では、Microsoft Excelを使用して結合されたセルを分割する方法について説明します。

1. 結合されたセルを選択します。
   セルが結合されている場合、**結合して中央配置**が**書式設定**ツールバーで選択されます。
1. **書式設定**ツールバーで**結合して中央配置**をクリックします。

### **Aspose.Cellsの使用**
Aspose.Cells.Cellsクラスには、セルを元の状態に分割する`unmerge()`メソッドもあります。これはセルの参照を使用してセルを分割します。

以下の例は、結合されたセル(C6)を分割する方法を示しています。 この例では、前の例で作成されたファイルを使用し、結合されたセルを分割しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
// Open the excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "mergingcells.xls"));

// Create a Worksheet and get the first sheet.
const worksheet = workbook.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Unmerge the cells.
cells.unMerge(5, 2, 2, 3);

// Save the file.
workbook.save(path.join(dataDir, "unmergingcells.out.xls"));
```

## **高度なトピック**
- [ワークシート内の結合セルを検出する](/cells/ja/nodejs-cpp/detect-merged-cells-in-a-worksheet/)
{{< app/cells/assistant language="nodejs-cpp" >}}
