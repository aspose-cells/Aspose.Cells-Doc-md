---
title: 行と列の自動調整（AutoFit）をC++で実行
linktitle: 行と列の自動調整
type: docs
weight: 20
url: /ja/cpp/autofit-rows-and-columns/
description: この記事は、Aspose.Cells for C++ APIを使用して、セル範囲の行、列、結合セルの行、およびセル範囲内の行の自動調整 方法を紹介します。
keywords: 行を自動調整、列を自動調整、セル範囲内の行を自動調整、結合されたセルの行を自動調整
---

{{% alert color="primary" %}}

Microsoft Excel では、セルの内容に応じてセルの幅と高さを自動的に調整することができます。この機能は Aspose.Cells でも利用可能で、開発者はRuntimeでセルの寸法を自動調整できます。

{{% /alert %}}

## **自動調整**

Aspose.Cells は、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスは、Excelファイル内の各ワークシートにアクセスできる [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) コレクションを含んでいます。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスはワークシートの管理に役立つ多くのメソッドを提供します。この記事では、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスを使用した行または列の自動調整について説明します。

### **行の自動調整 - シンプル**

行の幅と高さを自動調整する最も簡単な方法は、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)メソッドを呼び出すことです。[**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)メソッドは調整対象の行のインデックスをパラメータとして受け取ります。

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

    // Auto-fit the 2nd row (index 1) of the worksheet
    worksheet.AutoFitRow(1);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **セル範囲内の行を自動調整する方法**

行は多くの列で構成されます。Aspose.Cellsでは、行内のセル範囲の内容に基づいて行を自動調整できるように、[**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)メソッドのオーバーロード版を呼び出すことが可能です。引数は次の通りです。

- **行インデックス**：自動調整される行のインデックス。
- **最初の列インデックス**：行の最初の列のインデックス。
- **最後の列インデックス**：行の最後の列のインデックス。

[**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)メソッドは、行内のすべての列の内容をチェックし、その後行を自動調整します。

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fitting the 3rd row of the worksheet
    worksheet.AutoFitRow(1, 0, 5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **セル範囲内の列を自動調整する方法**

列は多くの行で構成されています。列のセル範囲の内容に基づいて列を自動調整するには、[**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) メソッドのオーバーロード版を呼び出し、以下のパラメータを渡します：

- **列インデックス**：自動調整される列のインデックス。
- **最初の行インデックス**：列の最初の行のインデックス。
- **最後の行インデックス**：列の最後の行のインデックス。

[**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/)メソッドは、列内のすべての行の内容をチェックし、その後列を自動調整します。

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

    // Auto-fit the 5th column (index 4) from row 4 to 6
    worksheet.AutoFitColumn(4, 4, 6);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **結合セルの行を自動調整する方法**

Aspose.Cells を使用すると、[**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) APIを利用して結合されたセルの行の自動調整も可能です。[**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) クラスは、結合セルの行を自動調整するための [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) プロパティを提供します。[**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/)は、以下のメンバーを持つ [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitmergedcellstype/) 列挙体を受け入れます：

- なし: 結合セルを無視します。
- 最初の行のみ: 最初の行の高さのみ拡張します。
- 最終行のみ: 最後の行の高さのみ拡張します。
- 各行: 各行の高さのみ拡張します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook wb;

    // Get the first (default) worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Create a range A1:B1
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 2);

    // Merge the cells
    range.Merge();

    // Insert value to the merged cell A1
    worksheet.GetCells().Get(0, 0).SetValue(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

    // Create a style object
    Style style = worksheet.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style.SetIsTextWrapped(true);

    // Apply the style to the cell
    worksheet.GetCells().Get(0, 0).SetStyle(style);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options;

    // Set auto-fit for merged cells
    options.SetAutoFitMergedCellsType(AutoFitMergedCellsType::EachLine);

    // Autofit rows in the sheet (including the merged cells)
    worksheet.AutoFitRows(options);

    // Save the Excel file
    wb.Save(outDir + u"AutofitRowsforMergedCells.xlsx");

    std::cout << "Autofit rows for merged cells completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

また、範囲の行／列と `[**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/)` のインスタンスを受け入れる [**AutoFitRows**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrows/) および [**AutoFitColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumns/) メソッドのオーバーロード版を使用して、選択した行または列の高さや幅を希望の [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) に自動調整することも試せます。

上記メソッドのシグニチャは次の通りです：

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)
1. AutoFitColumns（最初の列、最後の列、[**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/)オプション）

{{% /alert %}}

## **重要なこと**

{{% alert color="primary" %}}

セルが結合されている場合、AutoFitメソッドは適用されません。これはMicrosoft Excelと同じ動作です。これを回避するには、オートフィルターAPIを使用できます。さらに、セル内のテキストが折り返されている場合も、[**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/)メソッドは適用されません。もう一つ知っておくべきことは、*AutoFit*メソッドは時間がかかるということです。したがって、アプリケーションの効率性を保つために、これらのメソッドの呼び出しはできるだけ控えるべきです。

{{% /alert %}}

## ** 高度なトピック**
- [結合されたセルの行のAutoFit](/cells/ja/cpp/autofit-rows-for-merged-cells/)
