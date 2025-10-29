---
title: Comment définir une série comme invisible avec C++
linktitle: Comment définir une série comme invisible
description: Dans un graphique Excel, vous pouvez avoir besoin de rendre une série invisible. Cet article décrit comment utiliser Aspose.Cells avec C++ pour le faire.
keywords: Graphique Excel, Série, Invisible, EstFiltré.
type: docs
weight: 74
url: /fr/cpp/how-to-set-series-invisible/
---

## Comment définir une série comme invisible dans un graphique Excel

Dans un graphique Excel, vous pouvez faire un clic droit sur un graphique, cliquer sur "Sélectionner des données", et dans la fenêtre contextuelle, vous pouvez définir si une série est visible en cochant ou décochant l’option. Vous pouvez télécharger le [fichier d’exemple]([SeriesFiltered.xlsx](https://example.com/SeriesFiltered.xlsx)) et l’opérer dans Excel comme indiqué dans la figure pour réaliser cette fonction. Ensuite, nous vous expliquerons comment faire cela en utilisant la bibliothèque Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Comment définir une série comme invisible en utilisant Aspose.Cells 

Nous utilisons le code suivant pour définir une série comme invisible en utilisant Aspose.Cells :

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // File path for the input and output Excel files
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file
    Workbook workbook(filePath + u"SeriesFiltered.xlsx");

    // Access the charts collection of the first worksheet
    ChartCollection charts = workbook.GetWorksheets().Get(0).GetCharts();

    // Access a specific chart by name
    Chart chart = charts.Get(u"Chart 1");

    // Access filtered and non-filtered series collections
    SeriesCollection nSeriesFiltered = chart.GetFilteredNSeries();
    SeriesCollection nSeries = chart.GetNSeries();

    // Set the visibility of the first two series to be filtered
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Save the modified Excel file
    workbook.Save(filePath + u"output.xlsx");

    std::cout << "Series filtered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Vous pouvez obtenir le [Fichier d'entrée](SeriesFiltered.xlsx) et le [Fichier de sortie](output.xlsx).

Comme indiqué dans la figure ci-dessous, les deux premières séries qui étaient initialement visibles, sont devenues invisibles dans le fichier de sortie.  
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="cpp" >}}
