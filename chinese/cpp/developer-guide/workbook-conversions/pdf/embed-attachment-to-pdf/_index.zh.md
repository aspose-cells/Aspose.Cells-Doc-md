---
title: 使用C++将附件嵌入到PDF中
linktitle: 将附件嵌入到PDF中
type: docs
weight: 380
url: /zh/cpp/embed-attachment-to-pdf/
description: 学习如何用C++结合Aspose.Cells将附件嵌入到PDF中。
---

在Excel中，您可以插入带有源数据的Ole对象（[embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)）。双击Ole对象，嵌入的文件将被打开。

通常，在转换为PDF时，Ole对象将作为图标或缩略图渲染，而不显示Ole对象的源数据。使用选项[PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getembedattachments/)，您可以将Ole对象的源数据作为附件嵌入到PDF中。在PDF中双击图标或缩略图即可打开Ole对象的源文件。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template file
    Workbook workbook(u"embedded-attachments-example.xlsx");

    // Set to embed Ole Object attachment.
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetEmbedAttachments(true);

    // Save the pdf file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF saved successfully with embedded attachments!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="cpp" >}}
