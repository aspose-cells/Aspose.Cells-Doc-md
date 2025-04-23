---
title: Ignorer les erreurs lors du rendu d’Excel en PDF avec C++
linktitle: Ignorer les erreurs lors de la conversion Excel en PDF
type: docs
weight: 80
url: /fr/cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Apprenez à ignorer les erreurs lors de la conversion d’Excel en PDF en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Parfois, lors de la conversion d’un fichier Excel en PDF, des erreurs ou exceptions se produisent et le processus de conversion se termine. Vous pouvez ignorer toutes ces erreurs pendant la conversion en utilisant la propriété [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/). De cette façon, le processus de conversion s’achèvera en douceur sans générer d’erreur ou d’exception, mais des pertes de données peuvent survenir. Donc, utilisez cette propriété uniquement si la perte de données n’est pas critique pour vous.

## **Ignorer les erreurs lors du rendu Excel vers PDF**

Le code suivant charge le [fichier Excel d’exemple](55541778.xlsx), mais ce fichier Excel est erroné et génère une erreur lors de la [conversion en PDF](55541779.pdf) en version 17.11. Cependant, comme nous utilisons la propriété [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/), cela ne génère pas d’erreur. Cependant, une *flèche rouge arrondie* comme illustré dans cette capture d'écran est perdue.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleErrorExcel2Pdf.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"outputErrorExcel2Pdf.pdf";

    // Load the Sample Workbook that throws Error on Excel2Pdf conversion
    Workbook wb(inputFilePath);

    // Specify Pdf Save Options - Ignore Error
    PdfSaveOptions opts;
    opts.SetIgnoreError(true);

    // Save the Workbook in Pdf with Pdf Save Options
    wb.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully with error ignored!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
