---
title: Graphique en PDF avec C++
linktitle: Graphique en PDF
description: Apprenez comment utiliser Aspose.Cells for C++ pour convertir un graphique en un document PDF. Notre guide montrera comment exporter un graphique depuis Microsoft Excel et le sauvegarder en tant que PDF pour une distribution et une archivage ultérieurs.
keywords: Aspose.Cells for C++, Graphique en PDF, Microsoft Excel, Conversion en PDF, Exportation, Distribution, Archivage.
type: docs
weight: 47
url: /fr/cpp/chart-to-pdf/
---

## **Rendu du graphique en PDF**

Pour rendre le graphique au format PDF, les API Aspose.Cells ont exposé la méthode [**Chart::ToPdf**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/topdf/) avec la capacité de stocker le PDF résultant sur le chemin du disque ou en Stream.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its index to WorksheetCollection
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Convert chart to PDF
    chart.ToPdf(outDir + u"chartPDF_out.pdf");

    std::cout << "Chart converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Créer un PDF de graphique avec la taille de page souhaitée**
Vous pouvez créer un PDF de graphique avec la taille de page souhaitée en utilisant Aspose.Cells et spécifier comment vous souhaitez aligner le graphique à l’intérieur de la page, en haut, en bas, au centre, à gauche, à droite, etc. De plus, le graphique généré peut être créé dans un flux ou sur disque. Veuillez consulter le code exemple ci-dessous qui charge le fichier Excel [exemple](64716906.xlsx), accède au premier graphique dans la feuille de calcul, puis le convertit en [PDF de sortie](64716907.pdf) avec la taille de page souhaitée. La capture d’écran suivante montre que la taille de la page dans le PDF de sortie est 7x7 comme spécifié dans le code, et que le graphique est centré à la fois horizontalement et verticalement.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)

## **Code d'exemple**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file containing the chart
    Workbook wb(srcDir + u"sampleCreateChartPDFWithDesiredPageSize.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart ch = ws.GetCharts().Get(0);

    // Create chart pdf with desired page size
    ch.ToPdf(outDir + u"outputCreateChartPDFWithDesiredPageSize.pdf", 7, 7, PageLayoutAlignmentType::Center, PageLayoutAlignmentType::Center);

    std::cout << "Chart PDF created successfully with desired page size!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
