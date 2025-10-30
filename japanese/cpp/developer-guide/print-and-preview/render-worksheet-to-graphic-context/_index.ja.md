---
title: ワークシートをグラフィックコンテキストにレンダリング（C++）
linktitle: グラフィックコンテキストにワークシートをレンダリングする
type: docs
weight: 300
url: /ja/cpp/render-worksheet-to-graphic-context/
description: Aspose.Cells for C++を使ってワークシートをグラフィックコンテキストにレンダリングする方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsは現在、ワークシートをグラフィックコンテキストにレンダリングできます。グラフィックコンテキストは画像ファイルや画面、プリンタなど何でも可能です。ワークシートをグラフィックコンテキストにレンダリングするには以下の2つの方法のいずれかを使用してください。

- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)
- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)

{{% /alert %}}

以下のコードは、Aspose.Cellsを使ってワークシートをグラフィックコンテキストにレンダリングする方法を示しています。コードを実行すると、ワークシート全体が印刷され、残りの空白部分が青色に塗られ、画像として**OutputImage_out_.png**に保存されます。どのExcelファイルでも試すことが可能です。コード内のコメントも参照してください。

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleBook.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outDir + u"OutputImage_out.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
