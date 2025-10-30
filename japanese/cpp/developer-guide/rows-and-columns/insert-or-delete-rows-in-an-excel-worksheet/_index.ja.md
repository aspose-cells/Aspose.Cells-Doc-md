---
title: C++でExcelワークシートに行を挿入または削除
linktitle: 行の挿入と削除
type: docs
weight: 20
url: /ja/cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: この記事ではC++を使ったExcelワークシートでの行の挿入と削除のC++コードを提供します。
keywords: C++でExcelワークシートに行を挿入または削除、Excelに行を挿入、Excelの行を削除、C++を使った行の挿入や削除、Excelの行をC++で挿入または削除
---

{{% alert color="primary" %}}

新しいワークシートを作成するか、既存のワークシートを操作する際に、データを収容するために余分な行または列を追加することがあります。別の時には、ワークシート内の指定された位置から行または列を削除する必要があります。

{{% /alert %}}

Aspose.Cellsでは、行を挿入したり削除するための2つのメソッドが提供されています: [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) と [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)。これらのメソッドはパフォーマンスが最適化されており、非常に迅速に作業を行います。

行を挿入または削除する場合、[**Cells.InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) や [**DeleteRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterow/) のメソッドをループ内で使用する代わりに、常に [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) と [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) のメソッドを使用することをお勧めします。

Aspose.CellsはMicrosoft Excelと同様に動作します。行または列が追加されると、ワークシートの内容は下方向や右方向にシフトされます。行または列が削除されると、ワークシートの内容は上方向や左方向にシフトされます。行が追加または削除された場合、他のワークシートやセル内の参照が更新されます。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_book1.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows at row index 2 (insertion starts at 3rd row)
    sheet.GetCells().InsertRows(2, 10);

    // Delete 5 rows now. (8th row - 12th row)
    sheet.GetCells().DeleteRows(7, 5);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted and deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
