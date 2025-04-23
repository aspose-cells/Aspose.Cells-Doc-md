---
title: Charger le fichier source Excel sans graphiques avec C++
linktitle: Charger le fichier Excel source sans graphiques
type: docs
weight: 420
url: /fr/cpp/load-source-excel-file-without-charts/
description: Apprenez à charger un fichier Excel sans graphiques en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de charger votre fichier Excel sans graphiques. Veuillez utiliser la propriété [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) à cette fin.

{{% /alert %}}

## **Charger la feuille de calcul sans graphiques**

Le code d’exemple suivant charge le fichier Excel d’exemple sans graphiques et le sauvegarde au format PDF en sortie.

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

    // Specify the load options and filter the data
    LoadOptions options;

    // Include everything except charts
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xlsx";

    // Load the workbook with specified load options
    Workbook workbook(inputFilePath, options);

    // Path of output PDF file
    U16String outputFilePath = outDir + u"ResultWithoutChart.pdf";

    // Save the workbook in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully without charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
