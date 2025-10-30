---
title: C++でExcel 2016のMINIFSおよびMAXIFS関数の計算
description: この記事は、C++を使用してMicrosoft Excel 2016でMINIFSおよびMAXIFS関数を計算するためにAspose.Cellsライブラリを使用する方法を紹介します。
keywords: Aspose.Cells, Excel, 2016, MINIFS関数、MAXIFS関数、計算
type: docs
weight: 300
url: /ja/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **可能な使用シナリオ**
Microsoft Excel 2016はMINIFSおよびMAXIFS関数をサポートしています。これらの関数はExcel 2013以前ではサポートされていません。Aspose.Cellsもこれらの関数の計算をサポートしています。以下のスクリーンショットはこれらの関数の使用例を示しています。スクリーンショット内の赤いコメントを読んで、これらの関数の動作を理解してください。

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Excel 2016のMINIFSおよびMAXIFS関数の計算**
次のサンプルコードは[サンプルExcelファイル](5115149.xlsx)を読み込み、[Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)メソッドを呼び出して数式計算を行い、その結果を[出力PDF](5115154.pdf)に保存します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook containing MINIFS and MAXIFS functions
    Workbook workbook(srcDir + u"sampleMINIFSAndMAXIFS.xlsx");

    // Perform Aspose.Cells formula calculation
    workbook.CalculateFormula();

    // Save the calculations result in pdf format
    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);
    workbook.Save(outDir + u"outputMINIFSAndMAXIFS.pdf", options);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
