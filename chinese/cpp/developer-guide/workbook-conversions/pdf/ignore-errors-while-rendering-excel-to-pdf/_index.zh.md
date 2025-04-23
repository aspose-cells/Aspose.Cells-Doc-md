---
title: 使用C++在将Excel转换为PDF时忽略错误
linktitle: 在将Excel渲染为PDF时忽略错误
type: docs
weight: 80
url: /zh/cpp/ignore-errors-while-rendering-excel-to-pdf/
description: 了解如何在将Excel转换为PDF时使用Aspose.Cells for C++忽略错误。
---

## **可能的使用场景**

有时在将您的Excel文件转换为PDF时，会发生错误或异常并终止转换过程。您可以在转换过程中使用[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)属性忽略所有此类错误。这样，转换过程将顺利完成而不会抛出任何错误或异常，但可能会丢失数据。因此，仅当数据丢失对您不关键时才使用此属性。

## **在将Excel渲染为PDF时忽略错误**

以下代码加载了[示例Excel文件](55541778.xlsx)，但该Excel文件存在错误，在[转换为PDF](55541779.pdf)的17.11中会抛出错误，但由于我们使用了[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)属性，不会抛出错误。然而，如此截图所示，一个*圆角红色箭头形状*会丢失。

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **示例代码**

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
    U16String inputFilePath = srcDir + u"sampleErrorExcel2Pdf.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"outputErrorExcel2Pdf.pdf";

    // Load the Sample Workbook that throws Error on Excel2Pdf conversion
    Workbook wb(inputFilePath);

    // Specify Pdf Save Options - Ignore Error
    PdfSaveOptions opts;
    opts.SetIgnoreError(true);

    // Save the Workbook in Pdf with Pdf Save Options
    wb.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully with error ignored!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
