---
title: Node.js経由でC++を使用したHTMLのテーブル要素スタイルの接頭辞にHtmlSaveOptions.TableCssIdプロパティを付与
linktitle: HtmlSaveOptions.TableCssIdプロパティでテーブル要素スタイルをプレフィックス
type: docs
weight: 110
url: /ja/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Aspose.Cells for Node.js via C++を使ったHTMLのテーブル要素スタイルのプレフィックスの設定方法について学びます。 
---

## **可能な使用シナリオ**

Aspose.Cellsは、[**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--)プロパティを設定することでテーブル要素のスタイルにプレフィックスを付けることを可能にします。例えば、このプロパティに**MyTest_TableCssId**などの値を設定すると、次のようなスタイルになります。

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

以下のスクリーンショットは、[**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--)プロパティの使用による出力HTMLに対する効果を示しています。

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **HtmlSaveOptions.TableCssIdプロパティの使用方法についてのサンプルコードを以下に説明します。参照のために、コードによって生成された[output HTML](60489791.zip)を確認してください。**

次のサンプルコードは、[**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--)プロパティを使用する方法を示しています。コードによって生成された[output HTML](60489790.zip)の参照用です。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - specify table css id
const opts = new AsposeCells.HtmlSaveOptions();
opts.setTableCssId("MyTest_TableCssId");

// Save the workbook in html
wb.save("outputTableCssId.html", opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
