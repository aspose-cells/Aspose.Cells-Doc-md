---
title: C++でExcelファイルの行と列を挿入・削除する
linktitle: Excelファイルの行と列の挿入と削除
type: docs
weight: 70
url: /ja/cpp/inserting-and-deleting-rows-and-columns/
description: この資料は、Aspose.Cells for C++ APIを使用して行と列の挿入・削除方法を示しています。
keywords: Aspose.Cells C++で行と列を管理し、行と列を挿入・削除します。
---

## **紹介**

ワークシートをゼロから作成するか、既存のワークシートで作業する場合、さらなるデータを収容するために追加の行や列を必要とする場合があります。逆に、ワークシート内の特定の位置から行や列を削除する必要がある場合もあります。
これらの要件を満たすために、Aspose.Cellsは以下の非常にシンプルなクラスとメソッドのセットを提供しています。

### **行と列の管理**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシート内のすべてのセルを表す[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)コレクションを提供します。

[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)コレクションは、ワークシート内の行と列を管理するためのいくつかのメソッドを提供します。いくつかの例を以下に示します。

{{% alert color="primary" %}}

行や列を追加すると、ワークシート内の内容が下または右にシフトされ、削除すると上または左にシフトされます。

{{% /alert %}}

## **行と列の挿入**

### **行の挿入方法**

任意の位置に行を挿入するには、[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)コレクションの[**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)メソッドを呼び出します。[**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)メソッドは、新しい行を挿入する位置のインデックスを取ります。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Instantiating a Workbook object
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRow(2);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **複数の行を挿入する方法**

ワークシートに複数の行を挿入するには、[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)コレクションの[**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)メソッドを呼び出します。[**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)メソッドは2つのパラメータを取ります：

- 行インデックス、新しい行が挿入される行のインデックス。
- 行数、挿入する必要がある行の合計数。

```c++
#include <iostream>
#include <fstream>
#include <memory>
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

    // Insert 10 rows into the worksheet starting from 3rd row
    worksheet.GetCells().InsertRows(2, 10);

    // Path of output excel file
    U16String outputFilePath = srcDir + u"output.out.xls";

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **書式付きで行を挿入する方法**

書式設定オプション付きの行を挿入するには、引数に[**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/)を取る[**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)のオーバーロードを使用します。[**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/)クラスの[**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/)プロパティを[**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/)列挙型で設定します。[**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/)列挙型には以下の3つのメンバーがあります。

- SameAsAbove: 上の行と同じフォーマット。
- SameAsBelow: 下の行と同じフォーマット。
- Clear: 書式をクリアします。

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"InsertingARowWithFormatting_out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting Formatting options
    InsertOptions insertOptions;
    insertOptions.SetCopyFormatType(CopyFormatType::SameAsAbove);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRows(2, 1, insertOptions);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully with formatting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **列の挿入方法**

開発者は、任意の場所に列を挿入することもできます。[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)コレクションの[**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)メソッドを呼び出します。[**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)メソッドは、挿入する列のインデックスを受け取ります。

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a column into the worksheet at 2nd position
    worksheet.GetCells().InsertColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Column inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **行と列の削除**

### **複数の行を削除する方法**

複数行を削除するには、[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)コレクションの[**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)メソッドを呼び出します。[**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)メソッドは2つのパラメータを取ります：

- 行インデックス、削除される行のインデックス。
- 行数、削除する必要がある行の合計数。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete 10 rows from the worksheet starting from 3rd row
    worksheet.GetCells().DeleteRows(2, 10);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Rows deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **列を削除する方法**

任意の場所で列を削除するには、[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)コレクションの[**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)メソッドを呼び出します。[**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)メソッドは削除する列のインデックスを受け取ります。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete a column from the worksheet at 5th position (index 4)
    worksheet.GetCells().DeleteColumn(4);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
