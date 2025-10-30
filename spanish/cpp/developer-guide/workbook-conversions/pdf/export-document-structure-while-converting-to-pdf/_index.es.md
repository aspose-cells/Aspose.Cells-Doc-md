---  
title: Exportar estructura del documento al convertir a PDF con C++  
linktitle: Exportar la Estructura del Documento al Convertir a PDF  
type: docs  
weight: 360  
url: /es/cpp/export-document-structure-while-converting-to-pdf/  
description: Aprende cómo exportar la estructura del documento al convertir a PDF con Aspose.Cells en C++.  
---  

Las facilidades de estructura lógica de PDF proporcionan un mecanismo para incorporar información sobre la estructura del contenido del documento en un archivo PDF. Aspose.Cells preserva la información sobre la estructura del documento de un archivo de Microsoft Excel, como celda, fila, tabla, hoja de cálculo, imagen, forma, encabezado/pie de página, etc.  

Con la opción [PdfSaveOptions.GetExportDocumentStructure()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getexportdocumentstructure/), puedes guardar en un PDF etiquetado con la estructura exportada del documento.  

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


{{< app/cells/assistant language="cpp" >}}
