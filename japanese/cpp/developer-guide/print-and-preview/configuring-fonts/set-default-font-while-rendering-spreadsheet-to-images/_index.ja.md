---
title: C++でスプレッドシートを画像にレンダリングする際にデフォルトフォントを設定する
linktitle: デフォルトフォントの設定
type: docs
weight: 360
url: /ja/cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Aspose.Cellsを使用してC++でスプレッドシートを画像にレンダリングするときのデフォルトフォント設定方法を学びます。
---

{{% alert color="primary" %}}

スプレッドシートを画像にレンダリングする際に、デフォルトのフォントを設定するには、[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) プロパティを使用してください。このプロパティは、ワークブックのデフォルトのフォントが文字をレンダリングできない場合にのみ有効です。[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) プロパティで指定されたデフォルトのフォントは、無効または存在しないフォントを持つすべてのセルに使用されます。

{{% /alert %}}

## スプレッドシートを画像にレンダリングする際のデフォルトフォントの設定

次のサンプルコードでは、ワークブックを作成し、最初のワークシートのセルA4にテキストを追加し、そのフォントを無効または存在しないフォントに設定します。その後、ワークシートの2つの画像を取得します。最初の画像は[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) プロパティを*Courier New*に設定して取得し、2番目の画像は[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)プロパティを*Times New Roman*に設定して取得します。

これは、[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) プロパティを *Courier New* に設定した後の出力画像です。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

これは、[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) プロパティを *Times New Roman* に設定した後の出力画像です。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## サンプルコード

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Set default font of the workbook to none
    Style s = wb.GetDefaultStyle();
    s.GetFont().SetName(u"");
    wb.SetDefaultStyle(s);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A4 and add some text inside it
    Cell cell = ws.GetCells().Get(u"A4");
    cell.PutValue(u"This text has some unknown or invalid font which does not exist.");

    // Set the font of cell A4 which is unknown
    Style st = cell.GetStyle();
    st.GetFont().SetName(u"UnknownNotExist");
    st.GetFont().SetSize(20);
    st.SetIsTextWrapped(true);
    cell.SetStyle(st);

    // Set first column width and fourth column height
    ws.GetCells().SetColumnWidth(0, 80);
    ws.GetCells().SetRowHeight(3, 60);

    // Create image or print options
    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    // Render worksheet image with Courier New as default font
    opts.SetDefaultFont(u"Courier New");
    SheetRender sr(ws, opts);
    sr.ToImage(0, outDir + u"out_courier_new_out.png");

    // Render worksheet image again with Times New Roman as default font
    opts.SetDefaultFont(u"Times New Roman");
    SheetRender sr2(ws, opts);
    sr2.ToImage(0, outDir + u"times_new_roman_out.png");

    Aspose::Cells::Cleanup();
    return 0;
}
```
