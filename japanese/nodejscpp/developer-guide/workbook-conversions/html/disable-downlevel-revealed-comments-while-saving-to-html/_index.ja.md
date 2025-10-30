---
title: Node.js経由でC++を使用して、HTMLに保存する際のDownlevel Revealed Commentsを無効にする
linktitle: HTMLへの保存時にDownlevel表示されたコメントを無効にする
type: docs
weight: 20
url: /ja/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: ExcelファイルをHTMLに保存する際にDownlevel revealed commentsを無効にする方法についてAspose.Cells for Node.js via C++を使用して学びましょう。
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存するとき、Aspose.CellsはDownlevel Conditional Commentsを表示します。これらの条件付きコメントは主に古いバージョンのInternet Explorerに関連しており、現代のWebブラウザには関係ありません。詳細は以下のリンクで確認できます。

- [条件付きコメント - Downlevel-revealed条件付きコメント](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for Node.js via C++では、[**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--)プロパティを**true**に設定することで、これらのDownlevel Revealed Commentsを排除できます。

## **HTML への保存時にダウンレベルの表示されたコメントを無効にする**

以下のサンプルコードは[**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--)プロパティの使い方を示しており、設定されていない場合の効果もスクリーンショットで示しています。このコードで使用されるサンプルExcelファイル（50528257.xlsx）と、生成された出力HTML（50528258.zip）も参考としてダウンロードしてください。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableDownlevelRevealedComments.xlsx"));

// Disable DisableDownlevelRevealedComments
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableDownlevelRevealedComments(true);

// Save the workbook in html
workbook.save(path.join(outputDir, "outputDisableDownlevelRevealedComments_true.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
