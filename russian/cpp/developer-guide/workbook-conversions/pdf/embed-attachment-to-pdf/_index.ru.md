---
title: Встроить вложение в PDF на C++
linktitle: Встроить вложение в PDF
type: docs
weight: 380
url: /ru/cpp/embed-attachment-to-pdf/
description: Узнайте, как вставлять вложения в PDF с помощью Aspose.Cells на C++.
---

В Excel вы можете вставить Ole Object с исходными данными ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Дважды щелкните по Ole Object, и встроенный файл откроется.

Обычно при преобразовании в PDF Ole Object отображается как иконка или миниатюра без исходных данных Ole Object. Используя опцию [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getembedattachments/), вы можете встроить исходные данные Ole Object в качестве вложения в PDF. Дважды щелкнув по значку или миниатюре в PDF, вы можете открыть исходный файл Ole Object.

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
