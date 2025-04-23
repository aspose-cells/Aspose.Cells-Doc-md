---
title: 改行とテキストの折り返し（C++）
description: Aspose.Cellsライブラリを使用して、C++でテキスト折り返しと語句折り返しを実装する方法。Aspose.Cellsライブラリを使用すると、セルにテキストを簡単に挿入でき、手動の語句折り返しや自動折り返しなどのテキスト折り返し方法を設定できます。これらの機能を実装する方法とサンプルコードを示します。
keywords: Aspose.Cells, 改行, テキストの折り返し, テキストレイアウト
type: docs
weight: 60
url: /ja/cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

セル内のテキストが読み取れるようにするために、明示的な改行とテキストの折り返しを適用することができます。テキストの折り返しは、セル内の一行を複数行に変換し、明示的な改行は望む場所に改行を挿入します。

{{% /alert %}}

## **セル内でテキストを折り返す**

 セルのテキストを折り返すには、[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) プロパティを使用します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of the first column
    cell.SetColumnWidth(0, 35);

    // Increase the height of the first row
    cell.SetRowHeight(0, 36);

    // Add text to the first cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make the cell's text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(srcDir + u"WrappingText.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **明示的な改行を使用する**

 C++では、‘\n’を使用してセル内に明示的な改行を挿入できます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create Workbook Object
    Workbook workbook;

    // Open first Worksheet in the workbook
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Aspose::Cells::Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 65);

    // Add Text to the First Cell with Explicit Line Breaks
    cell.Get(0, 0).PutValue(u"I am using\nthe latest version of \nAspose.Cells to \ntest this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    U16String outputFilePath = u"WrappingText.out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
