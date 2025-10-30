---
title: C++でページ設定のスケーリング係数を計算する方法：1ページ(横)×nページ(縦)に合わせるオプションを使用してExcelワークシートをプログラム的に調整するサンプルコードを提供します。
linktitle: ページ設定スケーリングファクターを計算します
type: docs
weight: 300
url: /ja/cpp/calculate-page-setup-scaling-factor/
description: この文章は、C++ APIまたはライブラリを使用してExcelワークシートのページ設定の縮尺係数をプログラム的に計算する方法を説明したサンプルコードを提供します。
keywords: フィット横nページ縦mページのExcel C++、ページ設定のスケーリング係数を計算するC++コード
---

{{% alert color="primary" %}}

**ページの幅 n ページ、高さ m ページに合わせる** オプションを使用してページ設定のスケーリングを設定すると、Microsoft Excel はページ設定のスケーリングファクターを計算します。同様の計算は [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/) プロパティを使用して行うことができます。このプロパティは、パーセンテージ値に変換可能な double 値を返します。たとえば、0.5 を返すと、スケーリングファクターが 50％であることを意味します。

{{% /alert %}}

次のサンプルコードは、[**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/) プロパティを使用してページ設定のスケーリングファクターを計算する方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some data in these cells
    worksheet.GetCells().Get(u"A4").PutValue(u"Test");
    worksheet.GetCells().Get(u"S4").PutValue(u"Test");

    // Set paper size
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Set fit to pages wide as 1
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Calculate page scale via sheet render
    ImageOrPrintOptions options;
    SheetRender sr(worksheet, options);

    // Convert page scale double value to percentage
    double pageScale = sr.GetPageScale();
    std::wstring strPageScale = std::to_wstring(pageScale * 100) + L"%";

    // Write the page scale value
    std::wcout << strPageScale << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
