---
title: Comment gérer PivotChart avec PivotOptions en C++
linktitle: Options de pivot
type: docs
weight: 10
url: /fr/cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Comment gérer PivotChart avec PivotOptions en utilisant C++.
keywords: Tableau croisé dynamique
---

## Qu'est-ce qu'un tableau croisé dynamique

Un tableau croisé dynamique dans Excel est une représentation graphique des données créée à partir d'un tableau croisé dynamique. Il permet aux utilisateurs de visualiser et d'analyser les données de manière dynamique en résumant et en affichant les informations sous forme de graphique. Les tableaux croisés dynamiques sont interactifs et peuvent être facilement modifiés pour montrer différentes perspectives des données, ce qui en fait un outil puissant pour l'analyse et la présentation de données dans Excel.

## Comment gérer un PivotChart avec PivotOptions

En utilisant Aspose.Cells, vous pouvez utiliser [**PivotOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/pivotoptions/) pour gérer un PivotChart.

Fichier et code d'exemple :  
[Fichier d'exemple](Sample.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path for the sample Excel file
    U16String path = u"..\\Data\\01_SourceDirectory\\";

    // Create a Workbook object from the sample file
    Workbook book(path + u"Sample.xlsx");

    // Get the first chart from the first worksheet
    Chart chart = book.GetWorksheets().Get(0).GetCharts().Get(0);

    // Get the PivotOptions from the chart
    PivotOptions opt = chart.GetPivotOptions();

    // Hide ZoneFilter in PivotChart
    opt.SetDropZoneFilter(false); // HideZoneFilter

    // You can set more properties, try them!
    // opt.SetDropZoneCategories(false);  // HideZoneCategories
    // opt.SetDropZoneData(false);        // HideZoneData
    // opt.SetDropZoneSeries(false);      // HideZoneSeries
    // opt.SetDropZonesVisible(false);    // Hide All

    // Save the modified file to see the effect
    book.Save(path + u"HideZoneFilter.xlsx");

    std::cout << "Pivot chart updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Avec le code d'exemple ci-dessus, vous pouvez vérifier le fichier résultant avec l'effet suivant, tel qu'illustré dans la figure :

**![Résultat](Output.png)**
{{< app/cells/assistant language="cpp" >}}
