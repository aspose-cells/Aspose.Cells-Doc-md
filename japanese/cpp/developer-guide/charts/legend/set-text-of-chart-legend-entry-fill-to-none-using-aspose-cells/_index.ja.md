---
title: C++でチャートの凡例エントリの塗りつぶし文字を「なし」に設定
linktitle: チャート凡例エントリの塗りつぶし文字を「なし」に設定
description: Aspose.Cells for C++を使って、Microsoft Excelのチャートの凡例エントリの塗りつぶしを「なし」に設定する方法を学びましょう。ガイドは、凡例エントリの塌色を改善し、視覚化とカスタマイズを向上させる方法を示します。
keywords: Aspose.Cells for C++、チャート凡例エントリの塗りつぶし、Microsoft Excel、視覚化、カスタマイズ。
type: docs
weight: 320
url: /ja/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

チャートの凡例エントリの塗りつぶしのテキストを表示しないようにするには、[**LegendEntry.IsTextNoFill**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legendentry/istextnofill/)を**true**に設定してください。

{{% /alert %}}

次のサンプルコードは、チャートの2番目の凡例エントリの塗りつぶしのテキストを無効に設定します。このコードで使用される [サンプルExcelファイル](5115219.xlsx) とその生成される [出力Excelファイル](5115217.xlsx) をダウンロードして参照してください。

次のスクリーンショットは、このコードが[sample excel file](5115219.xlsx)に与える影響を示しています。

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ChartLegendEntry_out.xlsx";

    // Open the template file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = sheet.GetCharts().Get(0);

    // Set text of second legend entry fill to none
    chart.GetLegend().GetLegendEntries().Get(1).SetIsTextNoFill(true);

    // Save the workbook in xlsx format
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Chart legend entry modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
