---
title: 使用 C++ 在 ODF 1.1、1.2 和 1.3 规格下保存 ODS 文件
linktitle: 以 ODF 1.1、1.2 和 1.3 版本保存
description: 使用 Aspose.Cells 和 C++ 将 Excel 转换为符合 ODF 1.1、1.2 和 1.3 规范的文件。
type: docs
weight: 230
url: /zh/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

 Aspose.Cells 支持将 ODS 文件（**OpenDocument Spreadsheet**）保存为符合 ODF（**OpenDocument Format**） 1.1、1.2 和 1.3 规格的文件。Aspose.Cells 有 [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells/odssaveoptions/getodfstrictversion/) 属性，用于指定保存 ODS 文件的 ODF 版本。该属性默认值为 [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/)，因此未设置此属性保存的 ODS 文件默认使用 1.2 规范。

{{% /alert %}}

 以下示例代码创建了一个工作簿对象，向第一个工作表的单元格 A1 添加了一些值，然后以 ODF 1.1、1.2 和 1.3 规范保存 ODS 文件。默认情况下，ODS 文件以 ODF 1.2 规范保存。

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

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some value in cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Welcome to Aspose!");

    // Save ODS in ODF 1.2 version which is default
    OdsSaveOptions options;
    workbook.Save(outDir + u"ODF1.2_out.ods", options);

    // Save ODS in ODF 1.1 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf11);
    workbook.Save(outDir + u"ODF1.1_out.ods", options);

    // Save ODS in ODF 1.3 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf13);
    workbook.Save(outDir + u"ODF1.3_out.ods", options);

    std::cout << "ODS files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
