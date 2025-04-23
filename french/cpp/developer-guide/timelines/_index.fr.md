---
title: Insérer une timeline avec C++
linktitle: Chronologies
type: docs
weight: 170
url: /fr/cpp/create-timeline/
description: Apprenez à créer une chronologie avec Aspose.Cells en utilisant C++.
---

## **Scénarios d'utilisation possibles**

Au lieu d'ajuster les filtres pour afficher les dates, vous pouvez utiliser une Chronologie de Tableau Croisé Dynamique—une option de filtre dynamique qui vous permet de filtrer facilement par date/heure, et de zoomer sur la période souhaitée avec un contrôle de curseur. Microsoft Excel vous permet de créer une chronologie en sélectionnant un tableau croisé dynamique et en cliquant ensuite sur *Insertion > Chronologie*. Aspose.Cells permet également de créer une chronologie en utilisant la méthode [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.timelines/timelinecollection/add/).

## **Créer une chronologie pour un tableau croisé dynamique**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](input.xlsx) qui contient le tableau croisé dynamique. Ensuite, il crée la chronologie en fonction du premier champ pivot de base. Enfin, il enregistre le classeur au format [XLSX de sortie](output.xlsx). La capture d'écran suivante montre la chronologie créée par Aspose.Cells dans le fichier Excel de sortie.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing pivot table
    U16String inputFilePath = u"input.xlsx";
    Workbook wb(inputFilePath);

    // Access second worksheet (index 1)
    Worksheet sheet = wb.GetWorksheets().Get(1);

    // Access first pivot table inside the worksheet
    PivotTable pivot = sheet.GetPivotTables().Get(0);

    // Add timeline relating to pivot table
    int index = sheet.GetTimelines().Add(pivot, 15, 1, u"Ship Date");

    // Access the newly added timeline from timeline collection
    Timeline timeline = sheet.GetTimelines().Get(index);

    // Save the modified workbook
    U16String outputFilePath = u"output.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Timeline added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
