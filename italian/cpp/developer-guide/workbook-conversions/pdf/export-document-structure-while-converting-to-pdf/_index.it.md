---  
title: Esportare la struttura del documento durante la conversione in PDF con C++  
linktitle: Esportare la Struttura del Documento Durante la Conversione in PDF  
type: docs  
weight: 360  
url: /it/cpp/export-document-structure-while-converting-to-pdf/  
description: Impara come esportare la struttura del documento durante la conversione in PDF con Aspose.Cells in C++.  
---  

Le strutture logiche PDF forniscono un meccanismo per incorporare informazioni sulla struttura del contenuto del documento in un file PDF. Aspose.Cells mantiene le informazioni sulla struttura di un documento Microsoft Excel, come celle, righe, tabelle, fogli di lavoro, immagini, forme, intestazioni/piedi pagina, ecc.  

Con l’opzione [PdfSaveOptions.GetExportDocumentStructure()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getexportdocumentstructure/), puoi salvare in un PDF etichettato con la struttura del documento esportata.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the Excel file with image, shape, chart, etc.
    Workbook workbook(u"document-structure-example.xlsx");

    // Set to export document structure.
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetExportDocumentStructure(true);

    // Save the PDF file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file saved successfully with document structure!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  


