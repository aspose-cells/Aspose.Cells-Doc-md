---
title: 使用 C++ 将 Excel 工作簿转换为 Ods、Sxc 和 Fods（OpenOffice / LibreOffice Calc）
linktitle: Ods
type: docs
weight: 20
url: /zh/cpp/convert-excel-to-ods/
description: 如何使用 Aspose.Cells 和 C++ 将 Excel 转换为 Ods（OpenOffice / LibreOffice Calc）或将 Ods（OpenOffice / LibreOffice Calc）转换为 Excel。
---

## **关于OpenDocument**
[OpenDocument format (ODF)](https://en.wikipedia.org/wiki/OpenDocument)是一种免费开放的用于电子办公文档的文件格式，最初由Sun开发用于Open Office套件。 OpenDocument Spreadsheet (ODS)是Excel文档的文件格式。 OpenDocument目前是OASIS和ISO标准。

## **将Ods（OpenOffice / LibreOffice calc）转换为Excel**
 Aspose.Cells 支持加载 OpenOffice / LibreOffice Calc 支持的 Ods、Sxc 和 Fods，并将 [Ods](book1.ods)、[Sxc](book1.sxc) 和 [Fods](book1.fods) 转换为 Excel 文件。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source ods file
    U16String odsFilePath(u"book1.ods");
    std::shared_ptr<Workbook> workbook = std::make_shared<Workbook>(odsFilePath);

    // Save as xlsx file
    U16String xlsxOutputPath(u"ods_out.xlsx");
    workbook->Save(xlsxOutputPath);

    // Load your source sxc file
    U16String sxcFilePath(u"book1.sxc");
    workbook = std::make_shared<Workbook>(sxcFilePath);

    // Save as xls file
    U16String xlsOutputPath(u"sxc_out.xls");
    workbook->Save(xlsOutputPath);

    // Load your source fods file
    U16String fodsFilePath(u"book1.fods");
    workbook = std::make_shared<Workbook>(fodsFilePath);

    // Save as xlsb file
    U16String xlsbOutputPath(u"fods_out.xlsb");
    workbook->Save(xlsbOutputPath);

    std::cout << "Files converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将Excel转换为Ods（OpenOffice / LibreOffice Calc）**
 Aspose.Cells 支持将 Excel 文件转换为 Ods、Sxc 和 Fods 文件。以下代码示例演示了如何将 [模板](book1.xlsx) 转换为 Ods、Sxc 和 Fods 文件。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file 
    workbook.Save(u"Out.ods");

    // Save as sxc file 
    workbook.Save(u"Out.sxc");

    // Save as fods file 
    workbook.Save(u"Out.fods");

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [按照ODF 1.1和1.2规范保存ODS文件](/cells/zh/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [在ODS文件中处理背景](/cells/zh/cpp/working-with-background-in-ods-files/)
