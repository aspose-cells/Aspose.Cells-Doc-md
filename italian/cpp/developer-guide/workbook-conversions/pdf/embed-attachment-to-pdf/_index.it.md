---
title: Allega allegati in PDF con C++
linktitle: Incorpora allegato in PDF
type: docs
weight: 380
url: /it/cpp/embed-attachment-to-pdf/
description: Impara come incorporare allegati nei PDF utilizzando Aspose.Cells con C++.
---

In Excel, puoi inserire un Oggetto Ole con dati di origine ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Fai doppio clic sull’Ole Object, il file incorporato si aprirà.

In generale, durante la conversione in PDF, l’Ole Object verrà rappresentato come un’icona o una miniatura senza i dati di origine dell’Ole Object stesso. Con l’opzione [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getembedattachments/), puoi incorporare i dati di origine dell’Ole Object come allegato nel PDF. Puoi fare doppio clic sull’icona o sulla miniatura nel PDF per aprire il file di origine dell’Ole Object.

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
