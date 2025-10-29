---
title: Définir le texte de l entrée de la légende du graphique sur Aucun avec C++
linktitle: Définissez le texte de l entrée de la légende du graphique sur Aucun
description: Apprenez à utiliser Aspose.Cells for C++ pour définir le texte de remplissage de l entrée de la légende du graphique sur None. Notre guide démontrera comment modifier la couleur de remplissage des entrées de la légende dans les graphiques Excel pour une meilleure visualisation et personnalisation.
keywords: Aspose.Cells for C++, Remplissage de l entrée de la légende du graphique, Microsoft Excel, Visualisation, Personnalisation.
type: docs
weight: 320
url: /fr/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Si vous souhaitez définir le texte du remplissage de l'entrée de légende du graphique afin qu'il ne s'affiche pas dans la légende du graphique, veuillez définir [**LegendEntry.IsTextNoFill**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legendentry/istextnofill/) sur **true**.

{{% /alert %}}

Le code d'exemple suivant définit le texte du remplissage de la deuxième entrée de légende du graphique sur aucun. Veuillez télécharger le [fichier Excel d'exemple](5115219.xlsx) utilisé dans ce code et le [fichier Excel de sortie](5115217.xlsx) généré par celui-ci pour votre référence.

La capture d'écran suivante met en évidence l'effet de ce code sur le [fichier Excel d'exemple](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ChartLegendEntry_out.xlsx";

    // Open the template file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = sheet.GetCharts().Get(0);

    // Set text of second legend entry fill to none
    chart.GetLegend().GetLegendEntries().Get(1).SetIsTextNoFill(true);

    // Save the workbook in xlsx format
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Chart legend entry modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
