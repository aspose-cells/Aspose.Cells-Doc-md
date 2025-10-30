---
title: HtmlSaveOptions.TableCssIdプロパティを使用してテーブル要素のスタイルにプリフィックスを付ける（C++）
linktitle: HtmlSaveOptions.TableCssIdプロパティを使用してテーブル要素のスタイルにプレフィックスを付ける
type: docs
weight: 110
url: /ja/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Aspose.Cells for C++の[TableCSSid](https //reference.aspose.com/cells/cpp/aspose.cells.html.saveoptions/tablecssid/)プロパティを使用して、テーブル要素のスタイルにプレフィックスを付ける方法を学びます。
---

## **可能な使用シナリオ**

Aspose.Cellsには、ワークシートのCSSを[**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/)プロパティで接頭辞としてエクスポートする機能があります。このような値として**MyTest_TableCssId**などの値を設定すると、以下に示すようなテーブル要素のスタイルが見つかります。

```cpp
table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
```

以下のスクリーンショットは、[**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/)プロパティの使用による出力HTMLに対する効果を示しています。

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **HtmlSaveOptions.TableCssIdプロパティを使用してテーブル要素のスタイルにプレフィックスを付ける**

次のサンプルコードは、[**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/)プロパティを使用する方法を示しています。コードによって生成された[output HTML](60489790.zip)の参照用です。

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and put value inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This is some text.");

    // Set the style of the cell - font color is Red
    Style st = cell.GetStyle();
    st.GetFont().SetColor(Color::Red());
    cell.SetStyle(st);

    // Specify html save options - specify table css id
    HtmlSaveOptions opts;
    opts.SetTableCssId(u"MyTest_TableCssId");

    // Save the workbook in html
    wb.Save(u"outputTableCssId.html", opts);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
