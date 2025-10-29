---
title: Insérer un slicer avec C++
linktitle: Segmentateurs
type: docs
weight: 170
url: /fr/cpp/create-slicer/
description: Gérer les slicers des fichiers Excel avec Aspose.Cells en C++.
---

## **Scénarios d'utilisation possibles**

Un slicer est utilisé pour filtrer rapidement les données. Il peut être utilisé pour filtrer des données dans un tableau ou dans un tableau croisé dynamique. Microsoft Excel vous permet de créer un slicer en sélectionnant un tableau ou un tableau croisé dynamique, puis en cliquant sur *Insérer > Slicer*. Aspose.Cells vous permet également de créer un slicer en utilisant la méthode [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/add/).

## **Créer un segmentateur pour un tableau croisé dynamique**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel exemple](67338470.xlsx) qui contient le tableau croisé dynamique. Il crée ensuite le segmentateur en fonction du premier champ de base du tableau croisé dynamique. Enfin, il enregistre le classeur au format [XLSX de sortie](67338471.xlsx) et [XLSB de sortie](67338472.xlsb). La capture d'écran suivante montre le segmentateur créé par Aspose.Cells dans le fichier Excel de sortie.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
using namespace Aspose::Cells::Slicers;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCreateSlicerToPivotTable.xlsx";

    // Path of output Excel files
    U16String outputFilePathXlsx = outDir + u"outputCreateSlicerToPivotTable.xlsx";
    U16String outputFilePathXlsb = outDir + u"outputCreateSlicerToPivotTable.xlsb";

    // Load sample Excel file containing pivot table
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table inside the worksheet
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Add slicer relating to pivot table with first base field at cell B22
    int idx = ws.GetSlicers().Add(pt, u"B22", pt.GetBaseFields().Get(0));

    // Access the newly added slicer from slicer collection
    Slicer slicer = ws.GetSlicers().Get(idx);

    // Save the workbook in output XLSX format
    wb.Save(outputFilePathXlsx, SaveFormat::Xlsx);

    // Save the workbook in output XLSB format
    wb.Save(outputFilePathXlsb, SaveFormat::Xlsb);

    std::cout << "Slicer created and workbooks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Créer un segmentateur pour un tableau Excel**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel exemple](sampleCreateSlicerToExcelTable.xlsx) qui contient un tableau. Il crée ensuite le segmentateur en fonction de la première colonne. Enfin, il enregistre le classeur au format [XLSX de sortie](outputCreateSlicerToExcelTable.xlsx).

### **Code d'exemple**

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

    // Load sample Excel file containing a table
    Workbook workbook(srcDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    // Save the workbook in output XLSX format
    workbook.Save(outDir + u"outputCreateSlicerToExcelTable.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer added successfully to the Excel table!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Modifier les propriétés du segmentateur](/cells/fr/cpp/change-slicer-properties/)
- [Dessiner un tronçonneur lors du rendu Excel en PDF](/cells/fr/cpp/draw-slicer-while-rendering-excel-to-pdf/)
- [Formatage d'un tronçonneur](/cells/fr/cpp/formatting-slicer/)
- [Suppression du tronçonneur](/cells/fr/cpp/removing-slicer/)
- [Rendu du tronçonneur](/cells/fr/cpp/rendering-slicer/)
- [Mise à jour du tronçonneur](/cells/fr/cpp/updating-slicer/)
{{< app/cells/assistant language="cpp" >}}
