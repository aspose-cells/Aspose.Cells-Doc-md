---
title: Comment créer un graphique en tornade avec C++
linktitle: Créer un graphique en tornade
type: docs
weight: 73
url: /fr/cpp/create-tornado-chart/
description: Apprenez comment créer un graphique en tornade avec l API Aspose.Cells for C++.
keywords: C++ créer un graphique en tornade, ajouter un graphique en tornade, insérer un graphique en tornade
---

## **Introduction**
Un diagramme en forme de tornade, également connu sous le nom de diagramme en forme de tornade ou graphique en forme de tornade, est un type de visualisation de données souvent utilisé pour l'analyse de sensibilité dans Excel. Il vous aide à comprendre l'impact des variables changeantes sur un résultat particulier.

## **Comment créer un diagramme en forme de tornade dans Excel**
Vous pouvez créer un diagramme en forme de tornade dans Excel en suivant ces étapes :
1. Sélectionnez les données et allez dans Insertion --> Graphiques --> Insérer un histogramme ou un graphique à barres --> Graphique à barres empilées. Cliquez dessus.
<br>
<img src="1.png" width=70% />
2. Modifiez l'axe des Y : Cliquez avec le bouton droit sur l'axe des y. Cliquez sur formater l'axe. Dans les étiquettes, cliquez sur le menu déroulant de la position des étiquettes et sélectionnez l'élément inférieur.
<br>
<img src="2.png" width=70% />
3. Sélectionnez une barre quelconque et allez dans le formatage. Définissez une largeur d'écart appropriée.
<br>
<img src="3.png" width=70% />
4. Supprimons le signe moins (-) du diagramme en forme de tornade. Sélectionnez l'axe des x. Allez dans le formatage. Dans les options d'axe, cliquez sur le nombre. Dans la catégorie, sélectionnez personnalisé. Dans le code de format, écrivez ###0,###0. Cliquez sur ajouter.
<br>
<img src="4.png" width=70% />
5. Cliquez sur l'axe Y et allez dans les options d'axe. Dans les options d'axe, cochez **Catégories en ordre inverse**.
<br>
<img src="5.png" width=70% />

## **Comment ajouter un diagramme en forme de tornade dans Aspose.Cells**
Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](sample.xlsx) qui contient des données d'exemple. Ensuite, il crée le graphique à barres empilées basé sur les données initiales et définit les propriétés pertinentes. Enfin, il enregistre le classeur au format [XLSX de sortie](out.xlsx). La capture d'écran suivante montre le diagramme en forme de tornade créé par Aspose.Cells dans le fichier Excel de sortie.
<br>
<img src="6.png" width=70% />

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Get the chart collection from the worksheet
    ChartCollection charts = sheet.GetCharts();

    // Add a bar chart
    int index = charts.Add(ChartType::BarStacked, 8, 1, 24, 8);
    Chart chart = charts.Get(index);

    // Set data for the bar chart
    chart.SetChartDataRange(u"A1:C7", true);

    // Set properties for the bar chart
    chart.GetTitle().SetText(u"Tornado chart");
    chart.SetStyle(2);
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetPlotArea().GetBorder().SetColor(Color::White());
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set properties for the category axis
    chart.GetCategoryAxis().SetTickLabelPosition(TickLabelPositionType::Low);
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set gap width
    chart.SetGapWidth(10);

    // Set properties for the value axis
    Axis valueAxis = chart.GetValueAxis();
    valueAxis.GetTickLabels().SetNumberFormat(u"#,##0;#,##0");

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
