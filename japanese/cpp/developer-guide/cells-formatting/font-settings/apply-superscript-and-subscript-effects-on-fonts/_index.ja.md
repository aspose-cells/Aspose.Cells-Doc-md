---
title: C++を使用してフォントに上付きおよび下付き効果を適用する
linktitle: フォントに上付きおよび下付きの効果を適用する
type: docs
weight: 80
url: /ja/cpp/apply-superscript-and-subscript-effects-on-fonts/
description: Aspose.Cells for C++ APIを使用してExcelのテキストに上付きと下付き効果を適用するC++コード。
keywords: Excelの上付き、下付き、上付きおよび下付きのコード、Excelの下付きや上付きの挿入、Excelでの下付きや上付きの追加、Excelでの上付きや下付きの追加、Excelの上付きや下付きの追加、Excelの上付きの追加、Excelの下付きの追加
---

{{% alert color="primary" %}}

Aspose.Cellsは、テキストに上付き（基線の上）および下付き（基線の下）の効果を適用する機能を提供します。

{{% /alert %}}

## **上付きおよび下付きの操作**

上付き文字の効果を適用するには、[**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) オブジェクトの [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) プロパティを **true** に設定します。下付き文字を適用するには、[**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) オブジェクトの [**IsSubscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) プロパティを **true** に設定します。

以下のコード例では、テキストに上付き文字と下付き文字を適用する方法を示しています。

### テキストに上付き効果を適用するC++コード

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Setting the font Superscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSuperscript(true);
    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"Superscript_out.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully with superscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### テキストに下付き効果を適用するC++コード

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Set the font Subscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSubscript(true);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"Subscript_out.xls", SaveFormat::Auto);

    std::cout << "File saved successfully with subscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
