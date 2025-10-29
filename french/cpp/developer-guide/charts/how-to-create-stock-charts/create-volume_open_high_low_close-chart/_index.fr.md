---
title: Créer un graphique bourse Volume Ouverture Haut Bas Fermeture (VOHLC) avec C++
description: Apprenez comment créer un graphique bourse volume ouverture haut bas fermeture avec Aspose.Cells for C++. Notre guide montrera comment tracer les données du marché boursier, y compris le volume, l ouverture, le haut, le bas et la fermeture, pour une meilleure analyse et visualisation.
keywords: Aspose.Cells for C++, Graphique bourse Volume Ouverture Haut Bas Fermeture, Données du marché boursier, Analyse, Visualisation.
type: docs
weight: 184
url: /fr/cpp/create-volume-open-high-low-close-stock-chart/
---

## **Scénarios d'utilisation possibles**
Le quatrième graphique que nous examinerons est le graphique Volume Open High Low Close. Encore une fois, il est important de répéter que vous devez disposer des données dans le bon ordre. Si vous avez besoin de réarranger votre tableau de données, faites-le avant de configurer votre graphique. Ce graphique inclut une colonne pour le volume immédiatement après la première colonne (catégorie), et les graphiques incluent un graphique en colonnes sur l'axe principal affichant ce volume, tandis que les prix sont déplacés vers l'axe secondaire.

![todo:image_alt_text](data.png)

## **Graphique boursier Volume-Ouverture-Haut-Bas-Fermeture (VHLC)**

![todo:image_alt_text](sample.png)

## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](Volume-Open-High-Low-Close.xlsx) et génère le [fichier Excel de sortie](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-Open-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeOpenHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend to be shown
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-Open-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:F9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{0xff, 79, 129, 189});

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
