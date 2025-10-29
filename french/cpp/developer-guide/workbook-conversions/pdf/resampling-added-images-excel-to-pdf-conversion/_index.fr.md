---
title: Ressampling des images ajoutées  Conversion Excel en PDF avec C++
linktitle: Rééchantillonnage des images ajoutées  Conversion d Excel en PDF
type: docs
weight: 150
url: /fr/cpp/resampling-added-images-excel-to-pdf-conversion/
description: Apprenez comment resampler les images ajoutées pour réduire la taille du PDF en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Lorsque vous travaillez avec de gros fichiers Microsoft Excel comportant de nombreuses images, vous devrez peut-être compresser les images ajoutées pour réduire la taille du fichier PDF de sortie et améliorer les performances globales de conversion. Aspose.Cells prend en charge le rééchantillonnage des images ajoutées pour réduire la taille du fichier PDF de sortie et améliorer quelque peu les performances.

{{% /alert %}}

Veuillez consulter le code d'exemple suivant qui décrit comment effectuer la tâche à l'aide de l'API Aspose.Cells. L'exemple convertit un fichier Microsoft Excel en un fichier PDF tout en compressant les images dans le fichier.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Initialize a new Workbook and open an Excel file
    U16String inputPath = srcDir + u"input.xlsx";
    Workbook workbook(inputPath);

    // Instantiate the PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set Image Resample properties
    pdfSaveOptions.SetImageResample(300, 70);

    // Save the PDF file
    U16String outputPath = outDir + u"OutputFile_out_pdf.pdf";
    workbook.Save(outputPath, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

L'utilisation de l'option [**SetImageResample**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setimageresample/) minimise la taille du PDF de sortie mais peut affecter légèrement la qualité de l'image.

{{% /alert %}} 

{{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}
