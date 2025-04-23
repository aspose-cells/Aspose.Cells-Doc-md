---
title: Afficher la plage de cellules comme étiquettes de données avec C++
linktitle: Afficher la plage de cellules en tant qu étiquettes de données
description: Apprenez comment afficher une plage de cellules en tant qu’étiquettes de données dans les graphiques en utilisant Aspose.Cells for C++. Notre guide démontrera comment lier les étiquettes à votre source de données et les formater pour fournir des informations précises et significatives dans vos graphiques.
keywords: Aspose.Cells for C++, création de graphiques, étiquettes de données, plage de cellules, source de données, formatage, précision, informations significatives.
type: docs
weight: 130
url: /fr/cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

Dans Microsoft Excel 2013, vous pouvez afficher une plage de cellules pour les étiquettes de données. Aspose.Cells prend en charge cette fonctionnalité.

{{% /alert %}}

## **Case à cocher pour afficher la plage de cellules en tant qu'étiquettes de données**

Pour afficher la plage de cellules en tant qu'étiquettes de données dans Microsoft Excel :

1. Sélectionnez les étiquettes de données de la série et cliquez avec le bouton droit pour ouvrir le menu contextuel.
1. Sélectionnez **Format des étiquettes de données**. Les options d'étiquetage sont affichées.
1. Sélectionnez ou désélectionnez l'option **L'étiquette contient - Valeur à partir des cellules**.

Le code d'exemple ci-dessous accède aux étiquettes de données d'une série de graphiques et définit la propriété [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/getshowcellrange/) à **true** pour sélectionner l'option **L'étiquette contient - Valeur à partir des cellules**.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook from the source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Check the "Label Contains - Value From Cells"
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();
    dataLabels.SetShowCellRange(true);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
