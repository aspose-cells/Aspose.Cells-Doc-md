---
title: レンダリング時の行自動調整をC++で行う方法
linktitle: 描画用に行を自動調整する
type: docs
weight: 130
url: /ja/cpp/autofit-rows-for-rendering/
description: Aspose.CellsのC++を使用してExcelファイルのレンダリング時に行を自動調整する方法を学びます。
---

通常ビューでセル内の全テキストを表示する場合、Microsoft Excel で 100% ズームで通常ビューで行を自動調整できます。これによりテキストが通常ビューで完全に表示され、印刷やファイルを PDF として保存しても、テキストが正しく表示されます。

ただし、ある場合には、通常ビューで行の自動調整が正常に機能しますが、印刷ビューに切り替えたり、ファイルを PDF として保存すると、テキストが切り取られます。 ソースファイル [Book1.xlsx](Book1.xlsx) とスクリーンショットをご確認ください。

![印刷ビューでテキストが切り取られた場合](text_clipped_in_printview.png)

保存されたPDFファイルでテキストが切り取られるのを防ぎたい場合は、[AutoFitterOptions.GetForRendering()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getforrendering/)オプションを使用して行を自動調整できます。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize workbook instance
    Workbook workbook(u"Book1.xlsx");

    // Set autofit options for rendering
    AutoFitterOptions autoFitterOptions;
    autoFitterOptions.SetForRendering(true);

    // Autofit rows with options
    workbook.GetWorksheets().Get(0).AutoFitRows(autoFitterOptions);

    // Save to PDF
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    Aspose::Cells::Cleanup();
}
```

今、テキストは出力された PDF ファイルで切り取られていません。

![保存した PDF でテキストが切り取られていない場合](text_not_clipped_in_saved_pdf.png)
