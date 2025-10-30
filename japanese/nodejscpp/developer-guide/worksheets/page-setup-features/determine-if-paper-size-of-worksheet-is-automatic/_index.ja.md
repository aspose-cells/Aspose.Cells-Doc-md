---
title: ワークシートの用紙サイズが自動かどうかをNode.jsとC++を使用して判定。
linktitle: ワークシートの用紙サイズが自動かどうかを判定する
type: docs
weight: 90
url: /ja/nodejs-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: この資料では、Node.js APIとC++アドオンを使い、ワークシートの用紙サイズが自動設定になっているかどうかをプログラム的に判定する方法を説明します。
keywords: Node.jsとC++を使用して、ワークシートの用紙サイズが自動かを判定します。
---

## **可能な使用シナリオ**

多くの場合、ワークシートの用紙サイズは自動設定になっています。自動の場合、多くは*Letter*になっています。ユーザが必要に応じて用紙サイズを設定することもあります。この場合、用紙サイズは自動ではありません。[**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isAutomaticPaperSize--)プロパティを使って、用紙サイズが自動かどうかを判定できます。

## **ワークシートの用紙サイズが自動かどうかを判断する**

以下のサンプルコードは、次の2つのExcelファイルをロードし

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

その最初のワークシートの用紙サイズが自動かどうかを確認します。Microsoft Excelでは、このスクリーンショットに示すように、ページ設定ウィンドウで用紙サイズが自動かどうかを確認できます。

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const wb1 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-False.xlsx"));
const wb2 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-True.xlsx"));

// Access first worksheet of both workbooks
const ws11 = wb1.getWorksheets().get(0);
const ws12 = wb2.getWorksheets().get(0);

// Print the PageSetup.IsAutomaticPaperSize property of both worksheets
console.log("First Worksheet of First Workbook - IsAutomaticPaperSize: " + ws11.getPageSetup().isAutomaticPaperSize());
console.log("First Worksheet of Second Workbook - IsAutomaticPaperSize: " + ws12.getPageSetup().isAutomaticPaperSize());
```

## **コンソール出力**

上記のサンプルコードを指定されたサンプルExcelファイルで実行したときのコンソール出力は次の通りです。

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
