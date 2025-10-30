---
title: C++を使用して出力HTMLでの文字列の交差方法をHtmlCrossTypeで指定する
linktitle: 出力HTMLでのHtmlCrossTypeの指定
type: docs
weight: 140
url: /ja/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Aspose.Cells for C++のHtmlCrossTypeを使用して、HTML出力の文字列オーバーフローを制御する方法を学びます。
---

## **可能な使用シナリオ**

セルにテキストまたは文字列が含まれ、その長さがセルの幅を超える場合、次の列のセルがnullまたは空の場合、その文字列ははみ出します。ExcelファイルをHTMLに保存する際、[**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/)列挙体を使用してこのオーバーフローを制御できます。以下の値があります：

- **HtmlCrossType.Default**: MS Excelと同様に表示されます。次のセルによって異なります。次のセルがnullの場合、文字列は交わるか切り捨てられます。

- **HtmlCrossType.MSExport**: 文字列はMS ExcelでHTMLをエクスポートしたように表示されます。

- **HtmlCrossType.Cross**: HTMLクロス文字列が表示され、大きなHTMLファイルの作成に対するパフォーマンスがデフォルトまたはFitToCellに値を設定するよりも10倍以上向上します。

- **HtmlCrossType.FitToCell**: 文字列をセル内の幅に合わせて表示します。

## **出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定**

以下のサンプルコードは、[サンプルExcelファイル](51740732.xlsx)を読み込み、異なる [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/) を指定してHTML形式に保存します。このコードで生成された[出力HTML](51740734.zip)をダウンロードしてください。サンプルExcelファイルには、赤色の枠線で囲まれた画像が含まれています。このスクリーンショットは、[**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/) の値が出力HTMLに与える影響を示しています。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"sampleHtmlCrossStringType.xlsx");
    Workbook wb(inputFilePath);

    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::Default);
    opts.SetHtmlCrossStringType(HtmlCrossType::MSExport);
    opts.SetHtmlCrossStringType(HtmlCrossType::Cross);
    opts.SetHtmlCrossStringType(HtmlCrossType::FitToCell);

    int htmlCrossType = static_cast<int>(opts.GetHtmlCrossStringType());
    std::string numStr = std::to_string(htmlCrossType);
    U16String outputFilePath = U16String(u"out") + U16String(numStr.c_str()) + U16String(u".htm");
    wb.Save(outputFilePath, opts);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
