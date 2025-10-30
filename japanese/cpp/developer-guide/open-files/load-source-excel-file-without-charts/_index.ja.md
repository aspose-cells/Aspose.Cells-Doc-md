---
title: チャートなしのExcelファイルをC++で読み込む方法
linktitle: グラフを含まないソースエクセルファイルを読み込む
type: docs
weight: 420
url: /ja/cpp/load-source-excel-file-without-charts/
description: Aspose.Cellsを使用してチャートなしのExcelファイルをロードする方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsでは、チャートのないExcelファイルを読み込むことが可能です。これには[**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/)プロパティを使用してください。

{{% /alert %}}

## **グラフを含まないスプレッドシートを読み込む**

以下のサンプルコードは、チャートなしのExcelファイルを読み込み、それを出力PDF形式で保存します。

```c++
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

    // Specify the load options and filter the data
    LoadOptions options;

    // Include everything except charts
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xlsx";

    // Load the workbook with specified load options
    Workbook workbook(inputFilePath, options);

    // Path of output PDF file
    U16String outputFilePath = outDir + u"ResultWithoutChart.pdf";

    // Save the workbook in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully without charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
