---
title: Rafraîchir et calculer un tableau croisé dynamique contenant des éléments calculés avec C++
linktitle: Actualiser et calculer un tableau croisé dynamique avec des éléments calculés
type: docs
weight: 40
url: /fr/cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Rafraîchir et calculer un tableau croisé dynamique avec des éléments calculés en utilisant Aspose.Cells en C++.
---

{{% alert color="primary" %}}

Aspose.Cells prend désormais en charge le rafraîchissement et le calcul du tableau croisé dynamique comportant des éléments calculés. Veuillez utiliser les [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) et [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) comme d'habitude pour effectuer cette fonction.

{{% /alert %}}

## **Actualiser et calculer un tableau croisé dynamique avec des éléments calculés**

 Le code d'exemple suivant charge le [fichier Excel source](5115238.xlsx) contenant un tableau croisé dynamique avec trois éléments calculés tels que "add", "div", "div2". Nous modifions d'abord la valeur de la cellule D2 à 20, puis rafraîchissons et calculons le tableau croisé dynamique en utilisant les API Aspose.Cells et enregistrons le classeur au format PDF. Les résultats dans le [PDF de sortie](5115229.pdf) montrent qu'Aspose.Cells a rafraîchi et calculé avec succès le tableau croisé dynamique contenant des éléments calculés. Vous pouvez le vérifier manuellement avec Microsoft Excel en entrant la valeur 20 dans la cellule D2, puis en rafraîchissant le tableau croisé dynamique via la touche de raccourci Alt+F5 ou en cliquant sur le bouton de rafraîchissement du tableau croisé dynamique.

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

    // Load source Excel file containing a pivot table having calculated items
    U16String sampleFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(sampleFilePath);

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell D2
    sheet.GetCells().Get(u"D2").PutValue(20);

    // Refresh and calculate all the pivot tables inside this sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    for (int32_t i = 0; i < pivotTables.GetCount(); ++i)
    {
        PivotTable pt = pivotTables.Get(i);
        pt.RefreshData();
        pt.CalculateData();
    }

    // Save the workbook in output PDF
    U16String outputFilePath = srcDir + u"RefreshAndCalculateItems_out.pdf";
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
