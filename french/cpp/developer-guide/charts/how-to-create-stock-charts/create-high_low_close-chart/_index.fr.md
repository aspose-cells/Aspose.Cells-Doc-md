--- 
title: Créer un graphique bourse Haut Bas Fermeture (HLC) avec C++ 
linktitle: Créer un graphique de stocks High Low Close (HLC) 
description: Apprenez comment créer un graphique bourse haut bas fermeture en utilisant Aspose.Cells for C++. Notre guide étape par étape démontrera comment tracer les données du marché boursier, y compris les prix hauts, bas et de clôture, pour une meilleure analyse et visualisation. 
keywords: Aspose.Cells for C++, Graphique bourse Haut Bas Fermeture, Données du marché boursier, Analyse, Visualisation. 
type: docs 
weight: 181 
url: /fr/cpp/create-high-low-close-stock-chart/ 
--- 

## **Scénarios d'utilisation possibles** 
Le graphique boursier High-Low-Close (HLC) utilise quatre colonnes de données. La première colonne est une catégorie, généralement une date, mais les noms des actions peuvent aussi être utilisés. Les trois colonnes suivantes sont, dans l'ordre, pour les prix élevés, bas et de clôture. La plage de prix pour chaque catégorie est indiquée par une ligne verticale allant du bas au haut, et le prix de clôture est montré à l'aide d'une marque s'étendant vers la droite de cette ligne. 

![todo:image_alt_text](sample.png) 
## **Améliorations de la visibilité dans le graphique** 
Parfois, pour rendre le graphique plus intuitif, nous pouvons modifier l'apparence du marqueur (clôture), ou le faire s'afficher sur l'axe secondaire. 

![todo:image_alt_text](sample2.png) 
## **Code d'exemple** 
Le code d'exemple suivant charge le [fichier Excel d'exemple](High-Low-Close.xlsx) et génère le [fichier Excel de sortie](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::StockHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:D9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set the marker with the built-in data 
    chart.GetNSeries().Get(2).GetMarker().SetMarkerStyle(ChartMarkerType::Dash);
    chart.GetNSeries().Get(2).GetMarker().SetMarkerSize(20);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetForegroundColor(Color::Maroon());

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 
{{< app/cells/assistant language="cpp" >}}
