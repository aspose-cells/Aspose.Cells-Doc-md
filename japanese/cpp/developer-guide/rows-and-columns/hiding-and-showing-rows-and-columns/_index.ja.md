---
title: C++で行と列の非表示と再表示
linktitle: 行と列の非表示および表示
type: docs
weight: 60
url: /ja/cpp/hiding-and-showing-rows-and-columns/
description: Aspose.Cellsを使ってExcelファイル内の行と列をプログラムで非表示および表示させる方法を学びます。
---

{{% alert color="primary" %}}

ワークシートで特定の行や列を非表示にし、後で再表示させることは理にかなっています。Microsoft ExcelやAspose.Cellsもこの機能を提供しています。

{{% /alert %}}

## **行と列の可視性の制御**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには[**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)が含まれており、Excelファイルの各ワークシートにアクセスできるように開発者に提供します。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションは、ワークシートの行または列を管理するためのいくつかのメソッドを提供します。そのうちのいくつかについては以下で説明します。

### **行と列の非表示**

開発者は、[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/)および[**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/)メソッドを呼び出すことで、特定の行または列を非表示にすることができます。両方のメソッドは、非表示にする特定の行または列のインデックスを取ります。

```c++
#include <iostream>
#include <memory>
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully. File saved to: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

また、行または列を非表示にすることもできます。その際は、行の高さまたは列の幅をそれぞれ0に設定することができます。

{{% /alert %}}

### **行と列の表示**

開発者は、[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/)および[**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/)メソッドを呼び出すことで、非表示になっている任意の行または列を表示することができます。両方のメソッドは2つのパラメーターを取ります。

- **行または列のインデックス** - 特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅** - 非表示にする行または列に割り当てられた行の高さまたは列の幅。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhide the 3rd row and set its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhide the 2nd column and set its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File modified and saved successfully!" << std::endl;

    return 0;
}
```

{{% alert color="primary" %}}

非表示の列を表示状態に戻す場合、以前の幅に復元したり、元の幅に戻す必要がある場合は、負の幅で列を非表示解除します。例：`worksheet.Cells.UnhideColumn(5, -1)`

{{% /alert %}}

### **複数の行および列の非表示**

開発者は、[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/)および[**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/)メソッドを呼び出すことで、一度に複数の行または列を非表示にすることができます。両方のメソッドは、非表示にする開始行または列のインデックスと非表示にする行または列の数をパラメーターとして取ります。

```cpp
#include <iostream>
#include <memory>
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet (zero-based index)
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet (zero-based index)
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

また、複数の行と列を表示するために[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)クラスの[**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/)および[**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/)メソッドを使用することもできます。

{{% /alert %}}
