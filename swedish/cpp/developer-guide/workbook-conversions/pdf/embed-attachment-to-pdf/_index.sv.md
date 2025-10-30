---
title: Bifoga bilaga till PDF med C++
linktitle: Inbädda bilaga till PDF
type: docs
weight: 380
url: /sv/cpp/embed-attachment-to-pdf/
description: Lär dig hur man bifogar bilagor till PDF med Aspose.Cells i C++.
---

I Excel kan du infoga ett Ole-objekt med källdata ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Dubbelklicka på Ole-objektet, det inbäddade filen öppnas.

Generellt sett kommer Ole-objektet att renderas som en ikon eller miniatyrbild utan Ole-objektets källdata vid konvertering till PDF. Med alternativet [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getembedattachments/) kan du bädda in Ole-objektets källdata som en bilaga i PDF:en. Dubbelklicka på ikonen eller miniatyrbilden i PDF:n för att öppna källdatan för Ole-objektet.

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
