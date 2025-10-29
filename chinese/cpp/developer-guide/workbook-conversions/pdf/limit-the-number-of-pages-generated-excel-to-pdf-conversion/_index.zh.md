---
title: 限制生成页面数  使用C++将Excel转换为PDF
linktitle: 限制生成页面的数量
type: docs
weight: 180
url: /zh/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: 了解如何在使用Aspose.Cells将Excel转换为PDF时限制生成的页面数。
---

{{% alert color="primary" %}}

有时，您希望将某个范围的页面打印到输出PDF文件中。Aspose.Cells可以在将Excel电子表格转换为PDF文件格式时设置生成的页面数量限制。

{{% /alert %}}

## **限制生成的页面数量**

以下示例显示了如何将Microsoft Excel文件的页面范围（第3页和第4页）呈现为PDF。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"TestBook.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Instantiate the PdfSaveOption
    PdfSaveOptions options;

    // Print only Page 3 and Page 4 in the output PDF
    // Starting page index (0-based index)
    options.SetPageIndex(3);
    // Number of pages to be printed
    options.SetPageCount(2);

    // Path of output PDF file
    U16String outputFilePath = srcDir + u"outPDF1.out.pdf";

    // Save the PDF file
    wb.Save(outputFilePath, options);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

如果电子表格中包含公式，最好在将其呈现为PDF文件之前调用[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)。这样可以确保重新计算公式相关值，并在输出文件中呈现正确的值。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
