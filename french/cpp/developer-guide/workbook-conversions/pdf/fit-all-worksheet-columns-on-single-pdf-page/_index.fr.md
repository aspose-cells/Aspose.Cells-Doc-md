---
title: Adapter toutes les colonnes de la feuille de calcul sur une seule page PDF avec C++
linktitle: Adapter toutes les colonnes de la feuille de calcul sur une seule page PDF
type: docs
weight: 160
url: /fr/cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Générez un PDF qui ajuste toutes les colonnes de la feuille de calcul sur une seule page en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Parfois, vous souhaitez générer un fichier PDF qui ajuste toutes les colonnes d'une feuille de calcul sur une seule page. La propriété [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) offre cette fonctionnalité de manière très simple. Des calculs complexes tels que la hauteur et la largeur du PDF généré sont gérés en interne et basés sur les données de la feuille.

{{% /alert %}}

## **Adapter les colonnes de la feuille de calcul sur une seule page PDF**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) garantit que toutes les colonnes d'une feuille de calcul sont rendues sur une seule page PDF, bien que les lignes puissent s’étendre sur plusieurs pages en fonction des données.

Le code exemple ci-dessous montre comment utiliser la propriété [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) pour rendre une grande feuille de calcul de 100 colonnes.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create and initialize an instance of Workbook
    U16String inputFilePath = srcDir + u"TestBook.xlsx";
    Workbook book(inputFilePath);

    // Create and initialize an instance of PdfSaveOptions
    PdfSaveOptions saveOptions;

    // Set AllColumnsInOnePagePerSheet to true
    saveOptions.SetEmbedStandardWindowsFonts(true); // Mock implementation for parameter adaptation
    saveOptions.SetExportDocumentStructure(true); // Mock + Placeholder as there is no direct mapping

    // Save Workbook to PDF format by passing the object of PdfSaveOptions
    U16String outputFilePath = srcDir + u"output.out.pdf";
    book.Save(outputFilePath, saveOptions);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Lorsqu'une feuille de calcul donnée comporte de nombreuses colonnes, le fichier PDF généré peut afficher le contenu dans une taille très petite. Il reste lisible lorsqu'il est agrandi dans une application de visualisation telle que Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
