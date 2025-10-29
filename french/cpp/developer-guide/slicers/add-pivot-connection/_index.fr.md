---
title: Ajouter une connexion Pivot avec C++
linktitle: Ajouter une connexion de tableau croisé dynamique
type: docs
weight: 30
url: /fr/cpp/add-pivot-connection/
description: Apprenez comment ajouter une connexion pivot avec la bibliothèque Aspose.Cells en utilisant C++.
keywords: Ajouter une connexion pivot sans office 2013, office 2016, office 2019 et office 365.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez associer un segment de rapport et un tableau croisé dynamique dans Excel, vous devez cliquer avec le bouton droit sur le segment de rapport et sélectionner l'élément "Connexions de rapport...". Dans la liste des options, vous pouvez agir sur la case à cocher. De même, si vous souhaitez associer un segment de rapport et un tableau croisé dynamique à l'aide de l'API Aspose.Cells de manière programmatique, veuillez utiliser la méthode [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/addpivotconnection/). Cela associera le segment de rapport et le tableau croisé dynamique.

## **Associer une trancheuse et un tableau croisé dynamique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](add-pivot-connection.xlsx) qui contient une trancheuse existante. Il accède à la trancheuse et associe ensuite la trancheuse et le tableau croisé dynamique. Enfin, il enregistre le classeur sous forme de [fichier Excel de sortie](add-pivot-connection-out.xlsx). 

## **Code d'exemple**

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
    U16String inputFilePath = srcDir + u"add-pivot-connection.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"add-pivot-connection-out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    PivotTable pivotTable = pivotTables.Get(0);

    // Access the first slicer inside the slicer collection
    SlicerCollection slicers = worksheet.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Add PivotTable connection
    slicer.AddPivotConnection(pivotTable);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "PivotTable connection added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
