---
title: Spécifier la position absolue de l élément de pivot avec C++
linktitle: Spécification de la position absolue de l élément du tableau croisé dynamique
type: docs
weight: 50
url: /fr/cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Apprenez comment spécifier la position absolue des éléments de pivot en C++ en utilisant Aspose.Cells.
---

{{% alert color="primary" %}}

Parfois, les utilisateurs doivent spécifier la position absolue des éléments de pivot. L'API Aspose.Cells a exposé quelques nouvelles propriétés et une méthode pour répondre à cette exigence.

- Ajouté la propriété [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/) qui peut être utilisée pour spécifier l'index de position dans tous les PivotItems indépendamment du nœud parent. Ajouté la propriété [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) qui peut être utilisée pour spécifier l'index de position dans les PivotItems sous le même nœud parent.
- Ajout de la méthode [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) pour déplacer l'élément vers le haut ou vers le bas en fonction de la valeur du compteur, où le compteur est le nombre de positions à déplacer l'élément Pivot vers le haut ou le bas. Si la valeur du compteur est inférieure à zéro, l'élément sera déplacé vers le haut, tandis que si la valeur du compteur est supérieure à zéro, l'élément Pivot sera déplacé vers le bas. Le paramètre de type booléen `isSameParent` indique si l'opération de déplacement doit être effectuée dans le même nœud parent ou non.
- La méthode `PivotItem.Move(int count)` est obsolète ; il est donc conseillé d'utiliser la nouvelle méthode [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/).

{{% /alert %}}

Le code d'exemple suivant crée un tableau croisé dynamique puis spécifie les positions des éléments de pivot dans le même nœud parent. Vous pouvez télécharger le [fichier Excel source](5112632.xlsx) et le [fichier Excel de sortie](5112619.xlsx) pour référence. Si vous ouvrez le fichier Excel de sortie, vous verrez que l'élément de pivot "4H12" est à la position 0 dans le parent "K11" et "DIF400" est à la position 3. De même, CA32 est à la position 1 et AAA3 à la position 2.

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

    // Create workbook
    Workbook wb(srcDir + u"source.xlsx");

    // Add new worksheet for pivot table
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet wsPivot = worksheets.Add(u"pvtNew Hardware");
    Worksheet wsData = worksheets.Get(u"New Hardware - Yearly");

    // Get the pivot tables collection for the pivot sheet
    PivotTableCollection pivotTables = wsPivot.GetPivotTables();

    // Add PivotTable to the worksheet
    int index = pivotTables.Add(u"='New Hardware - Yearly'!A1:D621", u"A3", u"HWCounts_PivotTable");

    // Get the PivotTable object
    PivotTable pvtTable = pivotTables.Get(index);

    // Add vendor row field
    pvtTable.AddFieldToArea(PivotFieldType::Row, u"Vendor");

    // Add item row field
    pvtTable.AddFieldToArea(PivotFieldType::Row, u"Item");

    // Add data field
    pvtTable.AddFieldToArea(PivotFieldType::Data, u"2014");

    // Turn off the subtotals for the vendor row field
    PivotField pivotField = pvtTable.GetRowFields().Get(u"Vendor");
    pivotField.SetSubtotals(PivotFieldSubtotalType::None, true);

    // Turn off grand total
    pvtTable.SetShowColumnGrandTotals(false);

    // Refresh and calculate data before modifying pivot items
    pvtTable.RefreshData();
    pvtTable.CalculateData();

    // Set positions for specific pivot items
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"4H12").SetPositionInSameParentNode(0);
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"DIF400").SetPositionInSameParentNode(3);

    // Recalculate data after modifying pivot items
    pvtTable.CalculateData();

    // Set positions for additional pivot items
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"CA32").SetPositionInSameParentNode(1);
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"AAA3").SetPositionInSameParentNode(2);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Veuillez noter qu'il est nécessaire d'appeler les méthodes `PivotTable.RefreshData` et `PivotTable.CalculateData` avant d'utiliser [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/), [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) et [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/).

{{% /alert %}}
