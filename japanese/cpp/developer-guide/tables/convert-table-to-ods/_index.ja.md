---
title: TableをODSに変換（C++使用）
linktitle: テーブルをODSに変換
type: docs
weight: 70
url: /ja/cpp/convert-table-to-ods/
description: Aspose.Cellsを使用して、Tableを持つExcelファイルをODSファイル形式に変換します。
---

Aspose.Cellsは、テーブルを含むExcelファイルをODSファイルに変換することをサポートしています。ファイルをODS形式で保存すると、機能するテーブルを持つODSファイルが生成されます。

## サンプルコード

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C++

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an existing file that contains a table/list object in it
    U16String inputFilePath = sourceDir + u"SampleTable.xlsx";
    Workbook workbook(inputFilePath);

    // Save the file in ODS format
    workbook.Save(outputDir + u"ConvertTableToOds_out.ods");

    std::cout << "Conversion to ODS completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

サンプルコードによって生成された出力ODSファイルが添付されています。

[**Output ODS File**](ConvertTableToOds_out.ods)
