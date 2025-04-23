---
title: C++を使用してスプレッドシートをHTMLにレンダリングする際のデフォルトフォントを設定する
linktitle: HTMLにスプレッドシートをレンダリングする際のデフォルトフォントを設定する
type: docs
weight: 370
url: /ja/cpp/set-default-font-while-rendering-spreadsheet-to/
description: Aspose.Cells for C++を使用して、HTMLにスプレッドシートをレンダリングする際のデフォルトフォント設定方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsでは、スプレッドシートをHTMLにレンダリングする際にデフォルトフォントを設定できます。これには [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/) を使用してください。このプロパティは、スプレッドシート内のセルに無効または存在しないフォントがある場合に便利です。そのセルは [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/) プロパティで指定されたフォントでレンダリングされます。

{{% /alert %}}

## スプレッドシートをHTMLにレンダリングする際のデフォルトフォントの設定

次のサンプルコードは、ブックを作成し、最初のワークシートのセルB4にテキストを追加し、そのフォントを未知の/存在しないフォントに設定します。それからブックを異なるデフォルトフォント名（Courier New、Arial、Times New Romanなど）でHTML形式で保存します。

スクリーンショットは、[**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/) プロパティを介して異なるデフォルトフォント名を設定した効果を示しています。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

このコードは、異なる{0}を指定して生成された[出力HTMLファイルとCourier New](5115516)、[Arial](5115518)、[Times New Roman](5115517)を生成します。

## サンプルコード

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object and access first worksheet
    Workbook wb;
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B4 and add some text inside it
    Cell cell = ws.GetCells().Get(u"B4");
    cell.PutValue(u"This text has some unknown or invalid font which does not exist.");

    // Set the font of cell B4 which is unknown
    Style st = cell.GetStyle();
    st.GetFont().SetName(u"UnknownNotExist");
    st.GetFont().SetSize(20);
    cell.SetStyle(st);

    // Now save the workbook in html format and set the default font to Courier New
    HtmlSaveOptions opts;
    opts.SetDefaultFontName(u"Courier New");
    wb.Save(outDir + u"out_courier_new_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Arial
    opts.SetDefaultFontName(u"Arial");
    wb.Save(outDir + u"out_arial_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Times New Roman
    opts.SetDefaultFontName(u"Times New Roman");
    wb.Save(outDir + u"times_new_roman_out.htm", opts);

    Aspose::Cells::Cleanup();
}
```
