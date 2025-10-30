---  
title: レンダリング用にワークシートのカスタム用紙サイズを設定する方法（Node.jsとC++を使用）。  
linktitle: レンダリング用のワークシートのカスタム用紙サイズを実装する  
type: docs  
weight: 70  
url: /ja/nodejs-cpp/implement-custom-paper-size-of-worksheet-for-rendering/  
description: この資料では、Node.js APIとC++を用いて、ExcelファイルをPDFにレンダリングする際にカスタム用紙サイズを設定する方法を解説します。  
keywords: ExcelをPDFにレンダリングする際にカスタム用紙サイズを設定する（Node.jsとC++）。  
---  

## **可能な使用シナリオ**  

MS Excelには直接カスタム用紙サイズを作成するオプションはありませんが、ExcelファイルをPDFにレンダリングする際に希望のワークシートのカスタム用紙サイズを設定できます。このドキュメントでは、Aspose.Cells APIを使ったワークシートのカスタム用紙サイズの設定方法を説明します。  

## **レンダリングのためのワークシートのカスタム用紙サイズを実装する**  

Aspose.Cellsを使えば、目的の用紙サイズを設定できます。`[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/)`クラスの[**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#customPaperSize-number-number-)メソッドを使ってカスタムページサイズを指定してください。以下のサンプルコードは、ブック内の最初のワークシートにカスタム用紙サイズを指定する例です。参考用に、次のコードで生成された[出力PDF](45056028.pdf)もご覧ください。  

## **スクリーンショット**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Set custom paper size in unit of inches
ws.getPageSetup().customPaperSize(6, 4);

// Access cell B4
const b4 = ws.getCells().get("B4");

// Add the message in cell B4
b4.putValue("Pdf Page Dimensions: 6.00 x 4.00 in");

// Save the workbook in pdf format
wb.save(path.join(dataDir, "outputCustomPaperSize.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
