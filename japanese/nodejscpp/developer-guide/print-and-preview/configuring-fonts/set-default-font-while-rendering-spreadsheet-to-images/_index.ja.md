---
title: Node.js でのスプレッドシートの画像変換中のデフォルトフォント設定（C++ 経由）
linktitle: スプレッドシートを画像にレンダリングする際にデフォルトフォントを設定する
type: docs
weight: 360
url: /ja/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Aspose.Cells for Node.js via C++ を使用して、スプレッドシートを画像にレンダリングする際のデフォルトフォントの設定方法を学びます。 
---

{{% alert color="primary" %}}

スプレッドシートを画像にレンダリングする際に、デフォルトのフォントを設定するには、[**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) プロパティを使用してください。このプロパティは、ワークブックのデフォルトのフォントが文字をレンダリングできない場合にのみ有効です。[**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) プロパティで指定されたデフォルトのフォントは、無効または存在しないフォントを持つすべてのセルに使用されます。

{{% /alert %}}

## スプレッドシートを画像にレンダリングする際のデフォルトフォントの設定

以下のサンプルコードは、Excelファイルを開きます。最初のワークシートのセル A4 に "Christmas Time Font text" のテキストを設定し、フォント名はインストールされていない "Christmas Time Personal Use" にします。次に、そのワークシートの画像を2枚取得します。1枚目は [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) プロパティを *Courier New* に設定して取得し、2枚目は [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) プロパティを *Times New Roman* に設定して取得します。

これが [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) プロパティを *Courier New* に設定した後の出力画像です。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

これが [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) プロパティを *Times New Roman* に設定した後の出力画像です。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## サンプルコード

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Set default font of the workbook to none
let s = wb.getDefaultStyle();
s.getFont().setName("");
wb.setDefaultStyle(s);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access cell A4 and add some text inside it.
const cell = ws.getCells().get("A4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell A4 which is unknown.
let st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
st.setIsTextWrapped(true);
cell.setStyle(st);

// Set first column width and fourth column height
ws.getCells().setColumnWidth(0, 80);
ws.getCells().setRowHeight(3, 60);

// Create image or print options.
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);

// Render worksheet image with Courier New as default font.
opts.setDefaultFont("Courier New");
let sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "out_courier_new_out.png");

// Render worksheet image again with Times New Roman as default font.
opts.setDefaultFont("Times New Roman");
sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "times_new_roman_out.png");
```
