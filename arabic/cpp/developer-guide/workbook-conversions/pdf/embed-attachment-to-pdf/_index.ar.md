---
title: دمج المرفقات في PDF باستخدام C++
linktitle: تضمين مرفق في ملف PDF
type: docs
weight: 380
url: /ar/cpp/embed-attachment-to-pdf/
description: تعلم كيفية دمج المرفقات في PDF باستخدام Aspose.Cells مع C++.
---

في Excel، يمكنك إدراج كائن Ole ببيانات مصدر ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). بالنقر المزدوج على كائن Ole، سيتم فتح الملف المضمّن.

بشكل عام، أثناء التحويل إلى PDF، سيتم عرض كائن Ole كرمز أو صورة مصغرة بدون بيانات مصدر الكائن Ole. مع خيار [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getembedattachments/)، يمكنك دمج بيانات مصدر الكائن Ole كمرفق في PDF. يمكنك النقر المزدوج على الرمز أو الصورة المصغرة في PDF لفتح الملف المصدر للكائن Ole.

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
