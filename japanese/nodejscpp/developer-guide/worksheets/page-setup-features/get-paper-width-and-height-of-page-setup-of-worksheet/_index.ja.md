---
title: ページ設定の用紙幅と高さをNode.jsとC++を使って取得。
linktitle: ワークシートのページ設定の用紙幅と用紙高さを取得する方法
type: docs
weight: 50
url: /ja/nodejs-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Node.jsとC++を使ってExcelのページ設定の用紙幅と高さをプログラム的に取得する方法を学びます。
keywords: Excelのページ設定の用紙幅と高さをNode.jsとC++で取得。
---

## **可能な使用シナリオ**

シートのページ設定に設定された用紙幅と高さを知る必要がある場合、このために[**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--)と[**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--)のプロパティを使用してください。

## **ワークシートのページ設定の用紙の幅と高さを取得**

次のサンプルコードは、[**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--)と[**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--)の使い方を例示しています。最初に用紙サイズを*A2*に設定し、その後用紙の幅と高さを取得します。次に*A3*、*A4*、*Letter*に変更し、それぞれの用紙の幅と高さを取得します。

### **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook class
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Set paper size to A2 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA2);
console.log("PaperA2: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A3 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);
console.log("PaperA3: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A4 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);
console.log("PaperA4: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to Letter and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperLetter);
console.log("PaperLetter: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());
```

### **コンソール出力**

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
