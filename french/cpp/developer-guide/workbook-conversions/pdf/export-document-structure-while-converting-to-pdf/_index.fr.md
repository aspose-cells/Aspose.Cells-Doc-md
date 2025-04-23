---  
title: Structure du document d exportation lors de la conversion en PDF avec C++  
linktitle: Exporter la structure du document lors de la conversion en PDF  
type: docs  
weight: 360  
url: /fr/cpp/export-document-structure-while-converting-to-pdf/  
description: Apprenez à exporter la structure du document lors de la conversion en PDF avec Aspose.Cells en C++.  
---  

Les fonctionnalités de structure logique PDF offrent un mécanisme pour incorporer des informations concernant la structure du contenu du document dans un fichier PDF. Aspose.Cells conserve les informations sur la structure d’un document Microsoft Excel, telles que la cellule, la ligne, la table, la feuille de calcul, l’image, la forme, l’en-tête/pièce, etc.  

Avec l’option [PdfSaveOptions.GetExportDocumentStructure()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getexportdocumentstructure/), vous pouvez enregistrer en PDF balisé avec la structure du document exportée.  

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


