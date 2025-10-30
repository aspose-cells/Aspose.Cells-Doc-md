---  
title: Rimuovi stili inutilizzati all interno del libro di lavoro con C++  
linktitle: Rimuovere gli Stili Non Utilizzati all interno del Workbook  
type: docs  
weight: 340  
url: /it/cpp/remove-unused-styles-inside-the-workbook/  
description: Rimuovi stili inutilizzati nel libro di lavoro Excel usando Aspose.Cells con C++.  
---  

{{% alert color="primary" %}}  

 Gli stili inutilizzati nei file Excel non solo occupano spazio ma causano anche problemi di prestazioni durante la conversione in formati diversi come PDF, HTML, ecc. Aspose.Cells fornisce il funzionalità [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/) per rimuovere tutti gli stili inutilizzati all’interno del libro di lavoro.  

{{% /alert %}}  

 Il seguente codice spiega l'uso di {0}. Il codice carica il {1} file Excel modello che puoi scaricare dal link fornito. Contiene uno stile inutilizzato chiamato **AsposeStyle**; questo stile e tutti gli altri stili inutilizzati verranno rimossi dopo l'esecuzione del codice.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load template Excel file containing unused styles
    U16String templateFilePath = srcDir + u"Template-With-Unused-Custom-Style.xlsx";
    Workbook workbook(templateFilePath);

    // Remove all unused styles inside the template
    // This will also remove AsposeStyle which is an unused style inside the template
    workbook.RemoveUnusedStyles();

    // Save the file
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Unused styles removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
