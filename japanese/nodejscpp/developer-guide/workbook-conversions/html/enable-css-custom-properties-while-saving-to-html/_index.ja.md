---
title: Node.js経由でC++を使用して、HTMLに保存するときにCSSカスタムプロパティを有効にする
linktitle: HTML保存時にCSSカスタムプロパティを有効にする方法を学びます。
type: docs
weight: 320
url: /ja/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/
description: Microsoft ExcelファイルをHTMLに保存する際にCSSカスタムプロパティを有効にする方法についてAspose.Cells for Node.js via C++を使用して学びましょう。 
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存するとき、特定のBase64画像について複数の出現箇所がある場合に、カスタムプロパティを使用して画像データを一度だけ保存し、結果のHTMLのパフォーマンスを向上させることができます。[**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--)プロパティを使用し、**true**に設定して保存してください。
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **次のサンプルコードは、{0} 属性の使用例を示しています。このプロパティがTrueに設定されていない場合の効果もスクリーンショットで示しています。[サンプルExcelファイル](50528260.xlsx)と生成された[出力HTML](50528261.zip)をダウンロードして参照してください。**

以下のサンプルコードは[**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--)プロパティの使い方を示しており、設定されていない場合の効果もスクリーンショットで表示しています。このコードで使用されるサンプルExcelファイル（50528260.xlsx）と、生成された出力HTML（50528261.zip）も参考としてダウンロードしてください。



## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleEnableCssCustomProperties.xlsx"));

const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportImagesAsBase64(true);

// Enable EnableCssCustomProperties
opts.setEnableCssCustomProperties(true);

// Save the workbook in HTML
workbook.save(path.join(dataDir, "outputEnableCssCustomProperties.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
