---
title: XLSおよびXLSXフォーマットでサポートされる最大行数と列数をC++で見つける
linktitle: 最大行数と列数を見つける
type: docs
weight: 20
url: /ja/cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: XLSとXLSXフォーマットでサポートされる最大行数と列数の見つけ方をAspose.Cells for C++を使って学ぶ。
---

## **可能な使用シナリオ**

Excelフォーマットでは、サポートされる行数と列数が異なります。例えば、XLSは65536行と256列をサポートし、XLSXは1048576行と16384列をサポートします。特定のフォーマットでサポートされる行数と列数を知りたい場合は、[**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/)と[**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/)プロパティを使用します。

## **XLSおよびXLSX形式がサポートする最大行数および列数を検索する**

次のサンプルコードは、最初にXLS形式でワークブックを作成し、その後XLSX形式で作成します。作成後、[**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/)と[**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/)の値を出力します。以下のコードのコンソール出力をご参照ください。

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Print message about XLS format.
    std::cout << "Maximum Rows and Columns supported by XLS format." << std::endl;

    // Create workbook in XLS format.
    Workbook wb(FileFormatType::Excel97To2003);

    // Print the maximum rows and columns supported by XLS format.
    int maxRows = wb.GetSettings().GetMaxRow() + 1;
    int maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;
    std::cout << std::endl;

    // Print message about XLSX format.
    std::cout << "Maximum Rows and Columns supported by XLSX format." << std::endl;

    // Create workbook in XLSX format.
    wb = Workbook(FileFormatType::Xlsx);

    // Print the maximum rows and columns supported by XLSX format.
    maxRows = wb.GetSettings().GetMaxRow() + 1;
    maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **コンソール出力**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
