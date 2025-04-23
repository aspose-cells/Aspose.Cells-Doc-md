---
title: Incorporer une pièce jointe dans un PDF avec C++
linktitle: Intégrer la pièce jointe dans le PDF
type: docs
weight: 380
url: /fr/cpp/embed-attachment-to-pdf/
description: Découvrez comment incorporer des pièces jointes dans un PDF en utilisant Aspose.Cells avec C++.
---

Dans Excel, vous pouvez insérer un objet OLE avec des données source ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Double-cliquez sur l'objet OLE, le fichier incorporé s'ouvrira.

En général, lors de la conversion en PDF, l'objet OLE sera rendu sous forme d'icône ou de vignette sans ses données source. Avec l'option [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getembedattachments/), vous pouvez incorporer les données source de l'objet OLE en tant que pièce jointe dans le PDF. Vous pouvez double-cliquer sur l'icône ou la vignette dans le PDF pour ouvrir le fichier source de l'objet OLE.

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
