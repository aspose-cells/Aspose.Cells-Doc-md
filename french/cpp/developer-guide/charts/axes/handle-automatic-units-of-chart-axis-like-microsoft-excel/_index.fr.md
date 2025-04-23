---
title: Gérer les unités automatiques de l’axe du graphique comme Microsoft Excel avec C++
linktitle: Gérer les unités automatiques de l’axe du graphique
description: Apprenez à gérer les unités automatiques sur les axes du graphique dans Aspose.Cells for C++, similaire à Microsoft Excel. Notre guide vous montrera comment configurer et personnaliser les unités automatiques sur un axe du graphique, y compris l’affichage de la notation scientifique et l’ajustement de l’échelle.
keywords: Aspose.Cells for C++, axes du graphique, unités automatiques, Microsoft Excel, configuration, personnalisation, notation scientifique, échelle.
type: docs
weight: 120
url: /fr/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Scénarios d'utilisation possibles**
Les premières versions d'Aspose.Cells ne pouvaient pas gérer correctement les unités automatiques de l'axe de graphique lorsque le graphique est rendu en image ou en PDF. Maintenant, Aspose.Cells prend en charge la gestion des unités automatiques de l'axe de graphique. Aucun changement de code n'est nécessaire. Il suffit de convertir votre graphique en image ou en PDF et il rendra l'axe du graphique exactement comme le fait Microsoft Excel.

## **Gérer les unités automatiques de l'axe du graphique comme dans Microsoft Excel**
Le code d'exemple suivant charge le [fichier Excel d'exemple](61767755.xlsx) et génère le [graphique PDF de sortie](61767752.pdf). La capture d'écran montre les unités automatiques de l'axe du graphique dans les rectangles rouges et compare également le graphique du fichier Excel d'exemple avec le graphique PDF de sortie. Les deux sont exactement similaires.

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)

## **Code d'exemple**
```c++
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

    // Load the sample Excel file
    U16String inputFilePath = srcDir + u"sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access first chart
    ChartCollection charts = ws.GetCharts();
    Chart ch = charts.Get(0);

    // Render chart to PDF
    U16String outputFilePath = outDir + u"outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf";
    ch.ToPdf(outputFilePath);

    std::cout << "Chart rendered to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
