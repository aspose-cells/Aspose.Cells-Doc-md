---
title: Désactiver le retour à la ligne du texte pour les étiquettes de données du graphique avec C++
linktitle: Désactiver le retour à la ligne du texte pour les étiquettes de données
description: Apprenez comment désactiver le retour à la ligne pour les étiquettes de données dans les graphiques en utilisant Aspose.Cells for C++. Notre guide vous montrera comment empêcher le chevauchement de longues étiquettes et fournir des affichages de graphique plus lisibles et clairs.
keywords: Aspose.Cells for C++, diagramme, étiquettes de données, retour à la ligne, chevauchement, lisibilité, affichages.
type: docs
weight: 70
url: /fr/cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 permet aux utilisateurs de mettre en forme ou de défaire le retour à la ligne à l'intérieur des étiquettes de données du graphique. Par défaut, le texte à l'intérieur des étiquettes de données du graphique est à l'état de retour à la ligne.

Aspose.Cells fournit une propriété [**DataLabels.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/istextwrapped/) que vous pouvez régler sur True ou False pour activer ou désactiver le retour à la ligne des étiquettes de données respectivement.

{{% /alert %}}

L'exemple de code ci-dessous montre comment désactiver le retour à la ligne pour les étiquettes de données du graphique.

```cpp
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Load the sample Excel file inside the workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Disable the Text Wrapping of Data Labels in all Series
    chart.GetNSeries().Get(0).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(1).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(2).GetDataLabels().SetIsTextWrapped(false);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Text wrapping disabled successfully in data labels!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
