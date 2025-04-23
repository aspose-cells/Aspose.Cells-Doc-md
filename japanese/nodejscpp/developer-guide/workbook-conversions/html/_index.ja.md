---
title: HTMLをNode.js経由でC++で操作
linktitle: HTML
type: docs
weight: 230
url: /ja/nodejs-cpp/convert-excel-to-html/
---

## **ExcelワークブックをHTMLに変換する**
Aspose.Cells APIは、スプレッドシートをHTML形式にエクスポートする機能をサポートしています。これには、出力HTMLの複数の側面を制御する柔軟性を提供する [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) クラスを使用します。

以下のコード例は、Node.jsを使ってワークブックをHTMLファイルとして保存する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to HTML format
workbook.save("out.html");
```


## **ExcelワークブックをMHTMLファイルに変換する**
MHTMLは、通常のHTMLに外部リソース（画像やアニメーション、音声など）を結合し、一つのファイルにまとめたものです。.mht拡張子のメールに使用されます。Aspose.Cellsは、MHTMLファイルの読み書きをサポートしています。

以下のコード例は、Node.jsを使ってワークブックをMHTMLファイルとして保存する方法を示しています。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```

## **高度なトピック**
- [ワークブックにHTMLをロードする際の列と行を自動調整する](/cells/ja/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [HTMLからの大きな数値の指数表記を回避する](/cells/ja/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [HTMLリンクのターゲットタイプを変更する](/cells/ja/nodejs-cpp/change-the-html-link-target-type/)
- [ツールチップ付きでExcelをHTMLに変換する](/cells/ja/nodejs-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/ja/nodejs-cpp/create-transparent-image-of-excel-worksheet/)
- [HTMLのインポート時に改行後の余分なスペースを削除する](/cells/ja/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [HTML への保存時にダウンレベルの表示されたコメントを無効にする](/cells/ja/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [フレームスクリプトとドキュメントプロパティのエクスポートを無効にする](/cells/ja/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [ExcelをHTMLに変換する際にPresentationPreferenceオプションを使用してレイアウトを向上させる](/cells/ja/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [ExcelからHTMLへの変換時に未使用のスタイルを除外](/cells/ja/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開](/cells/ja/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Excel を HTML に変換する際の DataBar、ColorScale、および IconSet 条件付き書式をエクスポート](/cells/ja/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [ExcelファイルをHTMLに保存する際にコメントをエクスポート](/cells/ja/nodejs-cpp/export-comments-while-saving-excel-file-to/)
- [Excel を HTML に変換する際に文書のワークブックとワークシートのプロパティをエクスポート](/cells/ja/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [グリッドライン付きでExcelをHTMLにエクスポートする](/cells/ja/nodejs-cpp/export-excel-to-html-with-gridlines/)
- [印刷範囲を HTML にエクスポート](/cells/ja/nodejs-cpp/export-print-area-range-to/)
- [Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする](/cells/ja/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [出力HTMLでワークシートのCSSを別々にエクスポートする](/cells/ja/nodejs-cpp/export-worksheet-css-separately-in-output/)
- [HTMLに保存する際のボーダースタイルがWebブラウザでサポートされていない場合に似たボーダースタイルをエクスポートする](/cells/ja/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [HtmlSaveOptions.TableCssIdプロパティの使用方法についてのサンプルコードを以下に説明します。参照のために、コードによって生成された[output HTML](60489791.zip)を確認してください。](/cells/ja/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [HTMLに保存する際に非表示のワークシートコンテンツをエクスポートしない](/cells/ja/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [IFilePathProviderインターフェースを介してエクスポートされたワークシートのhtmlファイルパスを提供](/cells/ja/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [自己終了タグを認識](/cells/ja/nodejs-cpp/recognise-self-closing-tags/)
- [スプレッドシートをHTMLに変換する際にWordArtのグラデーション塗りをレンダリング](/cells/ja/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [列の幅をemやpercentなどのスケーラブルな単位に設定します](/cells/ja/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [スプレッドシートをHTMLにレンダリングする際のデフォルトフォントを設定する](/cells/ja/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定](/cells/ja/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [HTMLをエクセルブックにロードする際にDIVタグのレイアウトをサポート](/cells/ja/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [次のサンプルコードは、{0} 属性の使用例を示しています。このプロパティがTrueに設定されていない場合の効果もスクリーンショットで示しています。[サンプルExcelファイル](50528260.xlsx)と生成された[出力HTML](50528261.zip)をダウンロードして参照してください。](/cells/ja/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/)
