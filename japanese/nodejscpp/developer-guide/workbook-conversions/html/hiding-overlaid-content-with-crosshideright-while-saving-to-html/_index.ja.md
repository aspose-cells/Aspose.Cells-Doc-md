---
title: Node.js経由でC++を使用したHTML保存時のオーバーレイコンテンツをCrossHideRightで隠す
linktitle: HTMLで保存する際のCrossHideRightでオーバーレイされたコンテンツを非表示にする
type: docs
weight: 100
url: /ja/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---


## **可能な使用シナリオ**

ExcelファイルをHTMLに保存する際、セル文字列に対して異なるクロスタイプを指定できます。デフォルトでは、Aspose.CellsはMicrosoft Excelに従ってHTMLを生成しますが、[**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)にクロスタイプを設定すると、セルの右側に重ね合わされたり重複したセル文字列がある場合、その文字列を非表示にします。

## **CrossHideRightを使用してオーバーレイコンテンツを非表示にする**

次のサンプルコードは、[サンプルExcelファイル](64716894.xlsx)を読み込み、[**HtmlSaveOptions.getHtmlCrossStringType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getHtmlCrossStringType--)を[**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)に設定した後、[出力HTML](64716893.zip)に保存します。スクリーンショットは、[**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)がどのように出力に影響するかを示しています。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.CrossHideRight);

// Save to HTML with HtmlSaveOptions
workbook.save(path.join(dataDir, "outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html"), opts);
``` 
