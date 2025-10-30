---  
title: Node.jsを通じたC++のスプレッドシート変換時のデフォルトフォント設定  
linktitle: HTMLにスプレッドシートをレンダリングする際のデフォルトフォントを設定する  
type: docs  
weight: 370  
url: /ja/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/  
---  

{{% alert color="primary" %}}  
Aspose.Cellsを使用すると、スプレッドシートをHTMLにレンダリングする際にデフォルトフォントを設定することができます。そのためには、[**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--)を使用してください。このプロパティは、スプレッドシート内に無効または存在しないフォントを持つセルがある場合に役立ちます。その場合、[**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--)プロパティで指定したフォントでセルがレンダリングされます。  
{{% /alert %}}  

## スプレッドシートをHTMLにレンダリングする際のデフォルトフォントの設定  

次のサンプルコードは、ブックを作成し、最初のワークシートのセルB4にテキストを追加し、そのフォントを未知の/存在しないフォントに設定します。それからブックを異なるデフォルトフォント名（Courier New、Arial、Times New Romanなど）でHTML形式で保存します。  

スクリーンショットは、[**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) プロパティを介して異なるデフォルトフォント名を設定した効果を示しています。  

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)  

このコードは、異なる{0}を指定して生成された[出力HTMLファイルとCourier New](5115516)、[Arial](5115518)、[Times New Roman](5115517)を生成します。  

## サンプルコード  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object and access first worksheet.
const wb = new AsposeCells.Workbook();
const ws = wb.getWorksheets().get(0);

// Access cell B4 and add some text inside it.
const cell = ws.getCells().get("B4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell B4 which is unknown.
const st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
cell.setStyle(st);

// Now save the workbook in html format and set the default font to Courier New.
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDefaultFontName("Courier New");
wb.save(path.join(dataDir, "out_courier_new_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Arial.
opts.setDefaultFontName("Arial");
wb.save(path.join(dataDir, "out_arial_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Times New Roman.
opts.setDefaultFontName("Times New Roman");
wb.save(path.join(dataDir, "times_new_roman_out.htm"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
