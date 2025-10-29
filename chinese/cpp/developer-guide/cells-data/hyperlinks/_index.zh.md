---
title: 在Excel或OpenOffice中插入超链接的C++方法
linktitle: 管理超链接
type: docs
weight: 45
url: /zh/cpp/insert-hyperlinks-to-excel/
description: 学习如何在不使用MS Excel的情况下，用Aspose.Cells库向Excel文件插入超链接。
keywords: 在 Excel 中插入超链接，添加或插入超链接，添加或插入到 URL 的链接，在单元格中添加或插入链接，向外部文件添加链接
---

{{% alert color="primary" %}} 

超链接用于在两个实体之间创建链接。每个人都熟悉超链接的使用，特别是在网站上。
使用Aspose.Cells，开发人员可以在Microsoft Excel文件中创建不同类型的超链接。本主题讨论了Aspose.Cells支持哪些类型的超链接以及如何在我们的Excel文件中使用它们。

{{% /alert %}} 

## **添加超链接**
Aspose.Cells允许开发者使用API或设计表格（手动创建超链接并由Aspose.Cells导入到其他表格中）向Excel文件中添加超链接。

Aspose.Cells 提供了一个类 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，代表一个Microsoft Excel文件。 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类包含一个 [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)，允许访问Excel文件中的每个工作表。一个工作表由 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 提供不同的方法，用以向Excel文件添加不同的超链接。

## **添加指向URL的链接**
[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类包含一个 [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/) 集合。每个 [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/) 集合中的项表示一个 [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink)。通过调用 [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) 集合的 [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) 方法，向URL添加超链接。 [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) 方法接受以下参数：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，URL地址。

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a hyperlink to cell "A1"
    worksheet.GetHyperlinks().Add(u"A1", 1, 1, u"http://www.aspose.com");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

在上述示例中，在空单元格**A1**中添加了一个超链接。在这种情况下，如果单元格为空，则URL地址也会作为其值添加到该空单元格。如果单元格不为空并添加了超链接，则单元格的值看起来像普通文本。要使其看起来像超链接，请在该单元格上应用适当的格式设置。

{{% /alert %}} 

## **将链接添加到同一文件中的单元格**
可以通过调用 [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) 集合的 [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) 方法，为相同Excel文件中的单元格添加超链接。该 [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) 方法适用于内部和外部超链接。重载方法的一个版本接受以下参数：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标单元格的地址。

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

    // Adding a new worksheet to the Workbook object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in
    // The same Excel file
    worksheet.GetHyperlinks().Add(u"B3", 1, 1, u"Sheet2!B9");

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **向外部文件添加链接**
可以通过调用 [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) 集合的 [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) 方法，为外部Excel文件添加超链接。该方法接受以下参数：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标外部Excel文件的地址。

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Add an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
    worksheet.GetHyperlinks().Add(U16String(u"A5"), 1, 1, srcDir + U16String(u"book1.xls"));

    // Save the Excel file
    workbook.Save(outDir + U16String(u"output.out.xls"));

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [添加图像超链接](/cells/zh/cpp/add-image-hyperlinks/)
- [检测超链接类型](/cells/zh/cpp/detect-hyperlink-type/)
- [编辑工作表的超链接](/cells/zh/cpp/editing-hyperlinks-of-worksheet/)
- [获取范围内的超链接](/cells/zh/cpp/get-hyperlinks-in-range/)
{{< app/cells/assistant language="cpp" >}}
