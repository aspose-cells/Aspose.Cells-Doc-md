---
title: Comment créer un graphique en secteur en soleil avec C++
description: Apprenez à créer un graphique en soleil dans Aspose.Cells for C++, un graphique qui présente les données sous forme de cercle. Notre guide vous aidera à configurer diverses propriétés et mise en forme de votre graphique, notamment les étiquettes de données, les légendes, les couleurs, et plus encore.
keywords: Aspose.Cells for C++, graphique en soleil, créer, définir des propriétés, étiquettes de données, légende, format, couleur, cercle, rendu des données.
type: docs
weight: 162
url: /fr/cpp/creating-sunburst-chart/
---

## **Scénarios d'utilisation possibles**
Les graphiques en arbre sont bons pour comparer les proportions au sein de la hiérarchie, cependant, les graphiques en arbre ne sont pas très efficaces pour montrer les niveaux hiérarchiques entre les plus grandes catégories et chaque point de données. Un graphique en rayon de soleil est un bien meilleur visuel pour montrer cela. Le graphique en rayon de soleil est idéal pour afficher des données hiérarchiques. Chaque niveau de la hiérarchie est représenté par un anneau ou un cercle, le cercle le plus interne étant le sommet de la hiérarchie. Un graphique en rayon de soleil sans données hiérarchiques (un seul niveau de catégories) ressemble à un graphique en anneau. Cependant, un graphique en rayon de soleil avec plusieurs niveaux de catégories montre comment les anneaux extérieurs se rapportent aux anneaux intérieurs. Le graphique en rayon de soleil est le plus efficace pour montrer comment un anneau est divisé en ses parties contributives, tandis qu’un autre type de graphique hiérarchique, le graphique en arbre, est idéal pour comparer les tailles relatives.

![todo:image_alt_text](sample.png)
## **Diagramme sunburst**
Après avoir exécuté le code ci-dessous, vous verrez le diagramme sunburst comme indiqué ci-dessous.

![todo:image_alt_text](result.png)
## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](sunburst.xlsx) et génère le [fichier Excel de sortie](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sunburst.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Sunburst, 5, 6, 25, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Sunburst Chart");

    // Add series data range
    chart.GetNSeries().Add(u"D2:D16", true);

    // Set category data (A2:A16 is incorrect, as hierarchical category)
    chart.GetNSeries().SetCategoryData(u"A2:C16");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
