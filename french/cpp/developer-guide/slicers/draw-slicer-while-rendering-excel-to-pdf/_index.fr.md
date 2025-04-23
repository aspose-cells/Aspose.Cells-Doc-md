---
title: Dessiner un segment lors de la conversion d Excel en PDF avec C++
linktitle: Dessiner une trancheuse lors du rendu d Excel en PDF
type: docs
weight: 60
url: /fr/cpp/draw-slicer-while-rendering-excel-to-pdf/
description: Exporter Excel en PDF avec les paramètres du segment en utilisant Aspose.Cells avec C++.
---

## **Dessiner un tronçonneur lors du rendu Excel en PDF**
Si vous avez un fichier Excel qui a un segment appliqué et que vous souhaitez exporter le fichier Excel en PDF avec les paramètres du segment, Aspose.Cells prend désormais en charge cela par défaut. Il suffit d'exporter le fichier Excel avec un segment en PDF, et le PDF généré affichera le segment appliqué.

Le code d'exemple suivant charge le [fichier Excel d'exemple](94044165.xlsx) contenant une trancheuse existante. Ensuite, il enregistre le classeur de travail en tant que [fichier PDF de sortie](94044166.pdf). La capture d'écran suivante compare le fichier Excel source et le fichier PDF généré.

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **Code d'exemple**
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleSlicerChart.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"SampleSlicerChart.pdf";

    // Create workbook from the excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PDF file
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved as PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
