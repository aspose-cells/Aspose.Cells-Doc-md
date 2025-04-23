---
title: Trier des données dans une colonne avec une liste de tri personnalisée avec C++
linktitle: Trier les données dans une colonne avec une liste de tri personnalisée
type: docs
weight: 290
url: /fr/cpp/sort-data-in-column-with-custom-sort-list/
description: Apprenez comment trier des données dans une colonne en utilisant une liste personnalisée avec l API Aspose.Cells for C++.
keywords: Trier les données dans une colonne avec une liste de tri personnalisée, trier les données par liste personnalisée.
---

## **Scénarios d'utilisation possibles**

Vous pouvez trier des données dans une colonne à l'aide d'une liste personnalisée. Cela peut être fait en utilisant la méthode [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/). Cependant, cette méthode ne fonctionne que si les éléments de la liste personnalisée ne contiennent pas de virgules. Si elles contiennent des virgules comme "USA,US", "China,CN", vous devez utiliser la méthode [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/). Ici, le dernier paramètre n'est pas une chaîne, mais un tableau de chaînes.

## **Trier les données dans une colonne avec une liste de tri personnalisée**

Le code d'exemple suivant explique comment utiliser la méthode [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) pour trier les données avec une liste de tri personnalisée. Veuillez voir le [fichier Excel d'exemple](50528327.xlsx) utilisé dans ce code et le [fichier Excel de sortie](50528328.xlsx) généré par celui-ci. La capture d'écran suivante montre l'effet du code sur le fichier Excel d'exemple lors de son exécution.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

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

    // Load the source Excel file
    Workbook wb(srcDir + u"sampleSortData_CustomSortList.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify cell area - sort from A1 to A40
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A40");

    // Create Custom Sort list
    Vector<U16String> customSortList = { u"USA,US", u"Brazil,BR", u"China,CN", u"Russia,RU", u"Canada,CA" };

    // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
    wb.GetDataSorter().AddKey(0, SortOrder::Ascending, customSortList);
    wb.GetDataSorter().Sort(ws.GetCells(), ca);

    // Save the output Excel file
    wb.Save(outDir + u"outputSortData_CustomSortList.xlsx");

    std::cout << "Data sorted successfully with custom sort list!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
