---
title: C++を使用してチャートのデータラベルの折り返しを無効にする
linktitle: データラベルの折り返しを無効にする
description: Aspose.Cells for C++を使用して、チャートのデータラベルの折り返しを無効にする方法を学びます。長いラベルが重なるのを防ぎ、より見やすくクリアなチャート表示を実現する方法を示します。
keywords: Aspose.Cells for C++、チャート作成、データラベル、折り返し、重なり、可読性、表示。
type: docs
weight: 70
url: /ja/cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013では、ユーザーはチャートのデータラベル内のテキストを折り返すか折り返さないかを選択できます。デフォルトでは、チャートのデータラベル内のテキストは折り返し状態になっています。

Aspose.Cellsでは、チャートのデータラベルのテキスト折り返しを有効または無効にするための[**DataLabels.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/istextwrapped/)プロパティを提供しています。

{{% /alert %}}

次のコードサンプルは、チャートのデータラベルのテキスト折り返しを無効にする方法を示しています。

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Load the sample Excel file inside the workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Disable the Text Wrapping of Data Labels in all Series
    chart.GetNSeries().Get(0).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(1).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(2).GetDataLabels().SetIsTextWrapped(false);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Text wrapping disabled successfully in data labels!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
