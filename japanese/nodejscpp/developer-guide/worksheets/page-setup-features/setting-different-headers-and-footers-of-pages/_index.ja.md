---
title: Node.jsをC++経由で使用して、異なるページに異なるヘッダーとフッターを設定する方法
linktitle: 異なるページ用に異なるヘッダーとフッターの設定
type: docs
weight: 35
url: /ja/nodejs-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: このサンプルコードは、Aspose.Cells for Node.js via C++を使ってExcelワークシートのページ設定のヘッダーとフッターをプログラム的に設定する方法を示しています。最初のページ、奇数ページ、偶数ページのヘッダーとフッターを設定します。
keywords: C++を経由したNode.jsでのExcelのヘッダーとフッターの設定、FitToPagesWideとFitToPagesTallの追加方法、Excelでの設定、クリア方法、全体を一ページに印刷する方法
---

{{% alert color="primary" %}}

 MS Excelは、Excel 2007以降、最初のページ、奇数ページ、偶数ページの異なるヘッダーとフッターの設定をサポートしています。
Aspose.Cells for Node.js via C++も同じ機能をサポートしています。

{{% /alert %}}

## **MS Excelで異なるヘッダーとフッターの設定**

**![異なるヘッダーとフッターの設定](difpage.png)**

1. **ページレイアウト > 印刷タイトル > ヘッダー/フッター**をクリックします。
1. **奇数ページと偶数ページを異なる設定にする**または**最初のページだけ異なる設定にする**を確認してください。
1. 異なるヘッダーとフッターを入力します。

## **Aspose.Cells for Node.js via C++を使用した異なるヘッダーとフッターの設定例**

Aspose.CellsはExcelと同じように動作します。
1. [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffOddEven--)と[PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffFirst--)のフラグを設定します。 
1. 異なるヘッダーとフッターを入力します。
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Gets the setting of page setup.
const pageSetup = wb.getWorksheets().get(0).getPageSetup();
// Sets different odd and even pages
pageSetup.setIsHFDiffOddEven(true);
pageSetup.setHeader(1, "I am the header of the Odd page.");
pageSetup.setEvenHeader(1, "I am the header of the Even page.");
// Sets different first page
pageSetup.setIsHFDiffFirst(true);
pageSetup.setFirstPageHeader(1, "I am the header of the First page.");
```
