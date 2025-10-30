---
title: Anhänge in PDF mit C++ einbetten
linktitle: Anhang in PDF einbetten
type: docs
weight: 380
url: /de/cpp/embed-attachment-to-pdf/
description: Erfahren Sie, wie Sie Anhänge mit Aspose.Cells in C++ in PDFs einbetten.
---

In Excel können Sie ein Ole-Objekt mit Quelldaten einfügen ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Doppelklicken Sie auf das Ole-Objekt, um die eingebettete Datei zu öffnen.

Im Allgemeinen wird beim Konvertieren in PDF das Ole-Objekt als Symbol oder Miniaturbild ohne Quelldaten des Ole-Objekts dargestellt. Mit der Option [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getembedattachments/) können Sie die Quelldaten des Ole-Objekts als Anhang im PDF einbetten. Durch Doppelklick auf das Symbol oder die Miniaturansicht im PDF können Sie die Quelldatei des Ole-Objekts öffnen.

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
