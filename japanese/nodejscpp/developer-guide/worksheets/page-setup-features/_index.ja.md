---
title: ページ設定の機能（Node.js+C++）
linktitle: ページ設定機能
type: docs
weight: 60
url: /ja/nodejs-cpp/page-setup-features/
description: Aspose.Cells for Node.js via C++を使ったページ設定の機能を探求しましょう。ページの寸法、向き、設定の構成方法を学びます。
keywords: ページ設定の機能（Node.js+C++）、ページ寸法の構成（Node.js+C++）、ページの向き設定（Node.js+C++）
---



## **紹介**
Aspose.Cells for Node.js via C++を使用すると、Excelワークブックのさまざまなページ設定を操作できます。ページサイズや向き、マージンなどの設定が可能です。これらの機能を適切に設定することで、印刷や閲覧の体験が向上します。

## **ページサイズと向きの設定**
`PageSetup`クラスを使用して、ワークシートのページサイズと向きを指定できます。さまざまなプロパティでページの寸法やレイアウトを管理します。

### **例のコード**
ページサイズと向きの設定方法のサンプルコード例を示します。

```javascript
const { Workbook } = require("aspose.cells");

// Create a new workbook
let workbook = new Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Set the page size
worksheet.getPageSetup().setPaperSize(0); // A4 size

// Set the page orientation
worksheet.getPageSetup().setOrientation(1); // Landscape orientation

// Save the workbook
workbook.save("PageSetupExample.xlsx");
```

## **マージンの設定**
同じ`PageSetup`クラスを使って余白も設定可能です。左右、上下の余白を調整できます。

### **例のコード**
ワークシートの余白を設定する方法はこちらです。

```javascript
// Set the margins
worksheet.getPageSetup().setLeftMargin(0.5);
worksheet.getPageSetup().setRightMargin(0.5);
worksheet.getPageSetup().setTopMargin(1.0);
worksheet.getPageSetup().setBottomMargin(1.0);

// Save the workbook
workbook.save("PageMarginsExample.xlsx");
```

## **結論**
このドキュメントでは、Excelのページ設定機能をAspose.Cells for Node.js via C++を使用して操作する方法を学びました。`PageSetup`クラスを効果的に使用することで、ワークシートの印刷や表示方法を制御し、情報の全体的なプレゼンテーションを向上させることができます。

---
{{< app/cells/assistant language="nodejs-cpp" >}}
