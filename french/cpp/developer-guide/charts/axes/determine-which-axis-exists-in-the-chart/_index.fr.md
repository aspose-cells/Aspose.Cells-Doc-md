---
title: Déterminer quelle(s) axe(s) existent dans le graphique avec C++
description: Apprenez comment déterminer quels axes existent dans un graphique créé avec Aspose.Cells for C++. Notre guide vous aidera à comprendre comment identifier et accéder aux différents axes dans un graphique, y compris les axes de catégorie, de valeur et secondaires.
keywords: Aspose.Cells for C++, graphique, axe, existence, catégorie, valeur, secondaire.
type: docs
weight: 140
url: /fr/cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Parfois, l'utilisateur a besoin de savoir si un axe particulier existe dans le graphique. Par exemple, il veut savoir si un axe de valeurs secondaires existe à l'intérieur du graphique ou non. Certains graphiques comme Camembert, CamembertExploded, CamembertCamembert, CamembertBarre, Camembert3D, Camembert3DExploded, Anneau, AnneauExploded, etc. n'ont pas d'axe.

Aspose.Cells fournit [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/) méthode pour déterminer si le graphique a un axe particulier ou non.

{{% /alert %}}

Le code d'exemple suivant montre comment utiliser [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/) pour déterminer si le graphique d'exemple possède un axe de catégorie et de valeur principal et secondaire.

## Code C++ pour déterminer quels axes existent dans le graphique

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart
    Chart chart = worksheet.GetCharts().Get(0);

    // Determine which axis exists in the chart
    bool ret = chart.HasAxis(AxisType::Category, true);
    std::wcout << u"Has Primary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Category, false);
    std::wcout << u"Has Secondary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, true);
    std::wcout << u"Has Primary Value Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, false);
    std::wcout << u"Has Secondary Value Axis: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Sortie console générée par le code d'exemple

La sortie de la console du code est affichée ci-dessous, affichant true pour la Catégorie Principale et Axe de Valeur, et false pour la Catégorie Secondaire et Axe de Valeur.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
