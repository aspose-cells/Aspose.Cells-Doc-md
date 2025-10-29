---
title: 在使用C++进行写保护时指定作者
linktitle: 在写保护工作簿时指定作者
type: docs
weight: 40
url: /zh/cpp/specify-author-while-write-protecting-workbook/
description: 学习如何在用Aspose.Cells for C++写保护工作簿时指定作者名称。
---

## **可能的使用场景**

您可以在用Aspose.Cells API进行写保护时指定作者名称。请使用[**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/)属性实现此功能。

## **在保护工作簿时指定作者**

以下示例代码演示了 [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/) 属性的用法。该代码创建一个空工作簿，设置写保护密码，指定作者名字，并将其保存为[输出Excel文件](67338582.xlsx)。下方截图展示了示例代码对输出Excel文件的影响，供您参考。

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create empty workbook
    Workbook wb;

    // Write protect workbook with password
    wb.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Specify author while write protecting workbook
    wb.GetSettings().GetWriteProtection().SetAuthor(u"SimonAspose");

    // Save the workbook in XLSX format
    wb.Save(outDir + u"outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx");

    std::cout << "Workbook write protected with author specified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
