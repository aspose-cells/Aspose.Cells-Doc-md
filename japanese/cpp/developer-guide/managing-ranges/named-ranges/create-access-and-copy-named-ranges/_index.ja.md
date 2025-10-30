---
title: C++で名前付き範囲を作成、アクセス、コピー
linktitle: 名前付き範囲を作成、アクセス、コピー
type: docs
weight: 200
url: /ja/cpp/create-access-and-copy-named-ranges/
description: Aspose.Cellsを使用してExcelファイル内の名前付き範囲を作成、アクセス、コピーする方法を学びます（C++版）。
---

## **紹介**

通常、列および行のラベルは個々のセルを指すために使用されます。セル、セル範囲、数式、または定数値を表すための説明的な名前を作成することも可能です。 **名前** という言葉は、セル、範囲、数式、または定数値を表す文字列を指す場合があります。範囲に名前を割り当てることは、その範囲のセルを名前で参照できることを意味します。理解しやすい名前（例：Products）を使用して、Sales!C20:C30のように理解しにくい範囲を表現します。ラベルは同じワークシート上のデータを参照する数式にも使用できます。別のワークシートの範囲を表す場合は、名前を使用することができます。*名前付き範囲はMicrosoft Excelの最も強力な機能の一つであり、リストコントロール、ピボットテーブル、グラフなどのソース範囲として使用されると特に便利です。

## **Microsoft Excelを使用した名前付き範囲の操作**

### **名前付き範囲を作成します**

次のステップは、**MS Excel**を使用してセルまたはセル範囲に名前を付ける方法を説明します。この方法は**Microsoft Office Excel 2003**、**Microsoft Excel 97**、2000、2002に適用されます。

1. 名前を付けたいセルまたはセル範囲を選択します。
1. フォーミュラバーの左端にある**名前ボックス**をクリックします。
1. セルに名前を入力します。
1. ENTER キーを押します。

{{% alert color="primary" %}}

セルの内容を変更しているときにはセルに名前を付けることはできません。

{{% /alert %}}

## **Aspose.Cellsを使用した名前付き範囲の操作**

ここでは、Aspose.Cells API を使用してタスクを実行します。
Aspose.Cellsは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)を提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを提供します。

### **名前付き範囲の作成**

{0}コレクションの{1}メソッドを呼び出して、スプレッドシート内のすべての名前付き範囲を取得します。{2}メソッドは、{3}コレクション内のすべての名前付き範囲の配列を返します。

- 左上のセルの名前、範囲内の左上のセルの名前。
- 右下のセルの名前、範囲内の右下のセルの名前。

[**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/)メソッドを呼び出すと、[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)クラスのインスタンスとして新しく作成された範囲が返されます。この[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)オブジェクトを使用して、名前付き範囲を構成します。たとえば、[**GetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getname/)プロパティを使用して範囲の名前を設定します。次の例は、B4:G14を拡張するセルの名前付き範囲を作成する方法を示しています。

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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating a named range
    Range range = worksheet.GetCells().CreateRange(u"B4", u"G14");

    // Setting the name of the named range
    range.SetName(u"TestRange");

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Named range created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **名前付き範囲内のセルにデータを入力する**

範囲の個々のセルにデータを挿入できます。

- **C++**: Range(row, column)

名前付き範囲がA1:C4にまたがるとします。この範囲は4 * 3 = 12個のセルを形成します。個々の範囲セルは順次配置されています：Range(0, 0)、Range(0, 1)、Range(0, 2)、Range(1, 0)、Range(1, 1)、Range(1, 2)、Range(2, 0)、Range(2, 1)、Range(2, 2)、Range(3, 0)、Range(3, 1)、Range(3, 2)。

範囲内のセルを特定するには、次のプロパティを使用します:

- FirstRowは、名前付き範囲内の最初の行のインデックスを返します。
- FirstColumnは、名前付き範囲内の最初の列のインデックスを返します。
- RowCountは、名前付き範囲内の総行数を返します。
- ColumnCountは、名前付き範囲内の総列数を返します。

次の例では、指定された範囲のセルに値を入力する方法を示しています。

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Create a range of cells based on H1:J4
    Range range = worksheet1.GetCells().CreateRange(u"H1", u"J4");

    // Name the range
    range.SetName(u"MyRange");

    // Input some data into cells in the range
    range.Get(0, 0).PutValue(u"USA");
    range.Get(0, 1).PutValue(u"SA");
    range.Get(0, 2).PutValue(u"Israel");
    range.Get(1, 0).PutValue(u"UK");
    range.Get(1, 1).PutValue(u"AUS");
    range.Get(1, 2).PutValue(u"Canada");
    range.Get(2, 0).PutValue(u"France");
    range.Get(2, 1).PutValue(u"India");
    range.Get(2, 2).PutValue(u"Egypt");
    range.Get(3, 0).PutValue(u"China");
    range.Get(3, 1).PutValue(u"Philipine");
    range.Get(3, 2).PutValue(u"Brazil");

    // Save the excel file
    workbook.Save(outDir + u"rangecells.out.xls");

    std::cout << "Range cells created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **名前付き範囲内のセルを特定する**

範囲の個々のセルにデータを挿入できます。

- **C++**: Range(row, column)

A1:C4にまたがる名前付き範囲を持つ場合。範囲は4 * 3 = 12のセルを形成します。個々の範囲セルは順次配置されています：Range(0, 0)、Range(0, 1)、Range(0, 2)、Range(1, 0)、Range(1, 1)、Range(1, 2)、Range(2, 0)、Range(2, 1)、Range(2, 2)、Range(3, 0)、Range(3, 1)、Range(3, 2)。

範囲内のセルを特定するには、次のプロパティを使用します:

- FirstRowは、名前付き範囲内の最初の行のインデックスを返します。
- FirstColumnは、名前付き範囲内の最初の列のインデックスを返します。
- RowCountは、名前付き範囲内の総行数を返します。
- ColumnCountは、名前付き範囲内の総列数を返します。

次の例では、指定された範囲のセルに値を入力する方法を示しています。

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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    // Identify range cells
    std::cout << "First Row : " << range.GetFirstRow() << std::endl;
    std::cout << "First Column : " << range.GetFirstColumn() << std::endl;
    std::cout << "Row Count : " << range.GetRowCount() << std::endl;
    std::cout << "Column Count : " << range.GetColumnCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **名前付き範囲へのアクセス**

#### **特定の名前付き範囲にアクセスする**

指定された名前で範囲にアクセスするために、[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションの[**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/)メソッドを呼び出します。典型的な[**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/)メソッドは、名前付き範囲の名前を取り、[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)クラスのインスタンスとして指定された名前付き範囲を返します。次の例は、名前で指定された範囲にアクセスする方法を示しています。

```c++
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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Getting the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    if (range)
    {
        std::cout << "Named Range : " << range.GetRefersTo().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

#### **スプレッドシート内のすべての名前付き範囲にアクセス**

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションの[**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/)メソッドを呼び出して、スプレッドシート内のすべての名前定義範囲を取得します。 [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/)メソッドは、[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクション内のすべての名前定義範囲の配列を返します。

次の例は、ワークブック内のすべての名前付き範囲にアクセスする方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    WorksheetCollection sheets = workbook.GetWorksheets();
    Vector<Range> ranges = sheets.GetNamedRanges();

    std::cout << "Total Number of Named Ranges: " << ranges.GetLength() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **名前付き範囲をコピー**

Aspose.Cellsはセル範囲をフォーマット付きでコピーするための[**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/)メソッドを提供します。

次の例では、ソース範囲のセルを別の名前付き範囲にコピーする方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Range range1 = worksheet.GetCells().CreateRange(u"E12", u"I12");
    range1.SetName(u"MyRange");

	Color borderColor = Color{ 0,0, 0, 128 };
    range1.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Medium, borderColor);

    range1.Get(0, 0).PutValue(u"Test");
    range1.Get(0, 4).PutValue(u"123");

    Range range2 = worksheet.GetCells().CreateRange(u"B3", u"F3");
    range2.SetName(u"testrange");
    range2.Copy(range1);

    workbook.Save(outDir + u"copyranges.out.xls");

    std::cout << "Ranges copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
