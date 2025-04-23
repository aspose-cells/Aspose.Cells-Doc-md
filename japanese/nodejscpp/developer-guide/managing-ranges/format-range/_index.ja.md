---  
title: Node.jsとC++を使用した範囲の書式設定  
linktitle: 範囲の書式設定  
type: docs  
weight: 105  
url: /ja/nodejs-cpp/how-to-format-a-range/  
description: Aspose.Cells for Node.js via C++を使ったExcelのセル範囲の書式設定方法を学びましょう。  
---  

## **可能な使用シナリオ**  
範囲にスタイルを適用する必要がある場合は、範囲の書式設定を使用できます。  

## **Excelでの範囲の書式設定方法**  

Excelで範囲の書式を設定するには、Excelが提供する組み込みの書式設定オプションを使用します。Excelで範囲の書式を設定する方法は以下の通りです:  

1. Excelを開き、書式を設定したい範囲が含まれているワークブックを開きます。  

2. 書式を設定したい範囲を選択します。範囲を選択するには、範囲をクリックしてドラッグするか、ショートカットキーであるシフト+矢印キーを使用して選択を拡張することができます。  

3. 範囲が選択されたら、選択した範囲を右クリックし、コンテキストメニューから「セルの書式設定」を選択します。または、Excelリボンのホームタブに移動し、「セル」グループの「書式」ドロップダウンをクリックし、「セルの書式設定」を選択します。  

4. 「セルの書式設定」ダイアログボックスが表示されます。ここで、選択した範囲に適用するさまざまな書式設定オプションを選択できます。たとえば、フォントスタイル、フォントサイズ、フォント色、数値形式、罫線、背景色などを変更できます。 ダイアログボックス内の異なるタブを探索して、さまざまな書式設定オプションにアクセスできます。  

5.所望の書式設定を行った後、選択した範囲に書式を適用するには、「OK」ボタンをクリックします。  

## **Node.jsを使った範囲の書式設定方法**  

Aspose.Cells for Node.js via C++を使用して範囲を書式設定するには、次の方法を使用できます：  
1. [Range.applyStyle(style, flag)](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  
3. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  

## **サンプルコード**  
この例では、Excelワークブックを作成し、サンプルデータを追加し、最初のワークシートにアクセスし、2つの範囲("A1:C3"および"A4:C5")を定義します。次に、新しいスタイルを作成し、さまざまな書式設定オプション(たとえば、フォントの色、太字)を設定し、範囲にスタイルを適用します。最後に、ワークブックを新しいファイルとして保存します。  
<br>  
![todo:image_alt_text](format-range.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = workbook.getWorksheets().get(0);

const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Access the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Define the range
const range = worksheet.getCells().createRange("A1:C3");

// Apply formatting to the range
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Red);
style.getFont().setIsBold(true);

const flag = new AsposeCells.StyleFlag();
flag.setFont(true);
range.applyStyle(style, flag);

// Define the range
const range2 = worksheet.getCells().createRange("A4:C5");

// Apply formatting to the range
const style2 = workbook.createStyle();
style2.getFont().setColor(AsposeCells.Color.Blue);
style2.getFont().setIsItalic(true);
range2.setStyle(style2);

// Save the modified workbook
workbook.save("output.xlsx");
```  

