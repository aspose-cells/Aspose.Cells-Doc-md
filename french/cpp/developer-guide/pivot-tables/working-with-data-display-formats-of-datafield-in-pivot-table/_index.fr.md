---
title: Travailler avec les formats d affichage des données du DataField dans un tableau croisé dynamique avec C++
linktitle: Travailler avec les formats d affichage des données du DataField dans un tableau croisé dynamique
type: docs
weight: 140
url: /fr/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Apprenez comment travailler avec les formats d affichage des données du DataField dans un tableau croisé dynamique à l aide de Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge tous les formats d'affichage des données de DataField.

{{% /alert %}}

## **Option de format d'affichage "Classement du plus petit au plus grand" et "Classement du plus grand au plus petit"**

Aspose.Cells offre la possibilité de définir l'option de format d'affichage pour les champs de pivot. Pour cela, l'API fournit la propriété [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/). Pour classer du plus grand au plus petit, vous pouvez définir la propriété [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/) à [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/). L'extrait de code suivant démontre comment définir ces options de format d'affichage.

Les fichiers source et de sortie de l'échantillon peuvent être téléchargés d'ici pour tester le code d'échantillon:

[Fichier Excel source](101089332.xlsx)

[Fichier Excel de sortie](101089333.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load a template file
    Workbook workbook(srcDir + u"PivotTableSample.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotIndex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Accessing the data fields
    PivotFieldCollection pivotFields = pivotTable.GetDataFields();

    // Accessing the first data field in the data fields
    PivotField pivotField = pivotFields.Get(0);

    // Setting data display format
    pivotField.GetShowValuesSetting().SetCalculationType(PivotFieldDataDisplayFormat::RankLargestToSmallest);

    // Calculate data
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outDir + u"PivotTableDataDisplayFormatRanking_out.xlsx");

    std::cout << "PivotTable data display format ranking applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
