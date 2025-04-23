---
title: HTML と C++
linktitle: HTML
type: docs
weight: 230
url: /ja/cpp/convert-excel-to-html/
description: Aspose.Cells を使用してExcelをHTMLおよびMHTML形式に変換します。その方法を学びましょう。
---

## **ExcelワークブックをHTMLに変換する**
Aspose.Cells APIは、スプレッドシートをHTML形式にエクスポートする機能をサポートしています。これには、出力HTMLの複数の側面を制御する柔軟性を提供する [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions) クラスを使用します。

次のコード例は、C++を使用してワークブックをHTMLファイルとして保存する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"Book1.xlsx");

    // Save file to HTML format
    workbook.Save(u"out.html");

    std::cout << "Workbook saved to HTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ExcelワークブックをMHTMLファイルに変換する**
MHTMLは、通常のHTMLに外部リソース（画像やアニメーション、音声など）を結合し、一つのファイルにまとめたものです。.mht拡張子のメールに使用されます。Aspose.Cellsは、MHTMLファイルの読み書きをサポートしています。

次のコード例は、C++を使用してワークブックをMHTMLファイルとして保存する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    std::unique_ptr<Workbook> workbook = std::make_unique<Workbook>(inputFilePath);

    // Save file to mhtml format
    U16String outputFilePath(u"out.mht");
    workbook->Save(outputFilePath, SaveFormat::MHtml);

    std::cout << "Workbook saved to MHTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [ワークブックにHTMLをロードする際の列と行を自動調整する](/cells/ja/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [HTMLからの大きな数値の指数表記を回避する](/cells/ja/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/)
- [HTMLリンクのターゲットタイプを変更する](/cells/ja/cpp/change-the-html-link-target-type/)
- [ツールチップ付きでExcelをHTMLに変換する](/cells/ja/cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/ja/cpp/create-transparent-image-of-excel-worksheet/)
- [HTMLのインポート時に改行後の余分なスペースを削除する](/cells/ja/cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [HTML への保存時にダウンレベルの表示されたコメントを無効にする](/cells/ja/cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [フレームスクリプトとドキュメントプロパティのエクスポートを無効にする](/cells/ja/cpp/disable-exporting-frame-scripts-and-document-properties/)
- [ExcelをHTMLに変換する際にPresentationPreferenceオプションを使用してレイアウトを向上させる](/cells/ja/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [ExcelからHTMLへの変換時に未使用のスタイルを除外](/cells/ja/cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開](/cells/ja/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Excel を HTML に変換する際の DataBar、ColorScale、および IconSet 条件付き書式をエクスポート](/cells/ja/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [ExcelファイルをHTMLに保存する際にコメントをエクスポート](/cells/ja/cpp/export-comments-while-saving-excel-file-to/)
- [Excel を HTML に変換する際に文書のワークブックとワークシートのプロパティをエクスポート](/cells/ja/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [グリッドライン付きでExcelをHTMLにエクスポートする](/cells/ja/cpp/export-excel-to-html-with-gridlines/)
- [印刷範囲を HTML にエクスポート](/cells/ja/cpp/export-print-area-range-to/)
- [Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする](/cells/ja/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [出力HTMLでワークシートのCSSを別々にエクスポートする](/cells/ja/cpp/export-worksheet-css-separately-in-output/)
- [HTMLに保存する際のボーダースタイルがWebブラウザでサポートされていない場合に似たボーダースタイルをエクスポートする](/cells/ja/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [HtmlSaveOptions.TableCssIdプロパティの使用方法についてのサンプルコードを以下に説明します。参照のために、コードによって生成された[output HTML](60489791.zip)を確認してください。](/cells/ja/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [HTMLに保存する際に非表示のワークシートコンテンツをエクスポートしない](/cells/ja/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [自己終了タグを認識](/cells/ja/cpp/recognise-self-closing-tags/)
- [スプレッドシートをHTMLに変換する際にWordArtのグラデーション塗りをレンダリング](/cells/ja/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [列の幅をemやpercentなどのスケーラブルな単位に設定します](/cells/ja/cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [スプレッドシートをHTMLにレンダリングする際のデフォルトフォントを設定する](/cells/ja/cpp/set-default-font-while-rendering-spreadsheet-to/)
- [出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定](/cells/ja/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [HTMLをエクセルブックにロードする際にDIVタグのレイアウトをサポート](/cells/ja/cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)
- [次のサンプルコードは、{0} 属性の使用例を示しています。このプロパティがTrueに設定されていない場合の効果もスクリーンショットで示しています。[サンプルExcelファイル](50528260.xlsx)と生成された[出力HTML](50528261.zip)をダウンロードして参照してください。](/cells/ja/cpp/enable-css-custom-properties-while-saving-to-html/)
