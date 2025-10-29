---
title: Changer la direction de l’étiquette des graduations avec C++
linktitle: Modifier la direction des étiquettes de graduation
description: Apprenez comment changer la direction des étiquettes des graduations dans Aspose.Cells for C++. Notre guide vous aidera à comprendre comment ajuster l’orientation des étiquettes des graduations sur les axes, y compris horizontal, vertical et inclinée.
keywords: Aspose.Cells for C++, étiquettes de graduation, direction, orientation, axes, horizontal, vertical, inclinée.
type: docs
weight: 170
url: /fr/cpp/change-tick-label-direction/
---

## **Changer la direction des étiquettes des graduations**

Aspose.Cells vous offre la possibilité de changer la direction des étiquettes de graduation du graphique en utilisant la propriété [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/). La propriété [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/) accepte la valeur d'énumération [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype). L'énumération [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) fournit les membres suivants :

- Horizontale
- Verticale
- Rotation90
- Rotation270
- Empilée

L’image suivante compare le fichier source et le fichier de sortie :

### **Image du fichier source**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Image du fichier de sortie**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Le snippet de code suivant change la direction des étiquettes de graduation de Rotation90 à Horizontale.

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory source and output paths
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook and load the sample Excel file
    Workbook workbook(sourceDir + u"SampleChangeTickLabelDirection.xlsx");

    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from the source worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set the category axis tick labels direction to Horizontal
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Horizontal);

    // Output the modified workbook to a new file
    workbook.Save(outDir + u"outputChangeChartDataLableDirection.xlsx");

    std::cout << "Chart tick label direction changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Les fichiers source et de sortie peuvent être téléchargés à partir des liens suivants.

[Fichier source](105480221.xlsx)

[Fichier de sortie](105480223.xlsx)
{{< app/cells/assistant language="cpp" >}}
