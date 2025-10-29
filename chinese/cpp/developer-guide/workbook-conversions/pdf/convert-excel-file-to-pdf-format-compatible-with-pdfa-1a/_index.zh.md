---
title: 使用C++将Excel文件转换为兼容PDFA 1a的PDF格式
linktitle: 将Excel文件转换为与PDFA 1a兼容的PDF格式
type: docs
weight: 130
url: /zh/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: 了解如何使用Aspose.Cells的C++将Excel文件转换为符合PDF/A 1a标准的PDF文件。
---

## **可能的使用场景**

 PDF/A是一种特殊的PDF版本，旨在文件的长期保存。PDF/A是ISO标准化的PDF格式，它在PDF中嵌入了所有使用的字体以实现存档，且禁止某些功能，如字体链接（而非嵌入）和加密。Aspose.Cells支持将Excel文件保存为符合PDF/A标准的PDF文件（支持PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab 和 PDF/A-3u）。本主题介绍如何将Excel工作簿保存为符合PDF/A（PDF/A-1a）标准的PDF文件。

## **将Excel文件转换为与PDF/A-1a兼容的PDF格式**

 开发者可以使用[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)类设置转换的不同属性。设置[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)类的不同属性，可以控制输出PDF的打印、字体、安全性和压缩设置。最重要的属性是[**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/)，它允许你将Excel文件保存为符合PDF/A标准的PDF文件。

以下示例代码解释了如何将Excel文件转换为与PDF/A-1a兼容的PDF格式。请参阅其[输出PDF](outputCompliancePdfA1a.pdf)以及屏幕截图作为参考。

## **屏幕截图**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and add some message inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This PDF format is compatible with PDFA-1a.");

    // Create pdf save options and set its compliance to PDFA-1a
    PdfSaveOptions opts;
    opts.SetCompliance(PdfCompliance::PdfA1a);

    // Save the output pdf
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputCompliancePdfA1a.pdf", opts);

    std::cout << "PDF created successfully with PDFA-1a compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
