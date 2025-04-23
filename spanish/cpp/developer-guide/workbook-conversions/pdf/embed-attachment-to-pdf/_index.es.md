---
title: Incrustar adjunto en PDF con C++
linktitle: Agregar adjunto a PDF
type: docs
weight: 380
url: /es/cpp/embed-attachment-to-pdf/
description: Aprende cómo incrustar archivos adjuntos en PDF usando Aspose.Cells con C++.
---

En Excel, puedes insertar un Objeto OLE con datos de origen ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Haz doble clic en el Objeto OLE y el archivo incrustado se abrirá.

Por lo general, al convertir a PDF, el Objeto OLE se renderiza como un icono o una miniatura sin los datos del origen del Objeto OLE. Con la opción [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getembedattachments/), puedes incrustar los datos del origen del Objeto OLE como un adjunto en el PDF. Puedes hacer doble clic en el icono o la miniatura en el PDF para abrir el archivo fuente del Objeto OLE.

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
