---
title: Rich Text benutzerdefinierte Datenbeschriftung eines Diagrammpunkts mit C++
description: Erfahren Sie, wie Sie Rich Text Benutzerbeschriftungen für Diagrammpunkte in Aspose.Cells for C++ hinzufügen. Unser Leitfaden zeigt Ihnen, wie Sie Beschriftungen mit verschiedenen Schriftarten, Farben und Ausrichtungsoptionen formatieren, um das Erscheinungsbild und die Lesbarkeit Ihrer Diagramme zu verbessern.
keywords: Aspose.Cells for C++, Diagrammerstellung, Rich Text, benutzerdefinierte Datenbeschriftungen, Schriftarten, Farben, Ausrichtung, Aussehen, Lesbarkeit.
type: docs
weight: 10
url: /de/cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Sie können Aspose.Cells verwenden, um eine Rich-Text-Benutzerbeschriftung für den Diagrammpunkt zu erstellen. Aspose.Cells bietet die Methode [DataLabels.Characters()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/characters/), um das [FontSetting](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) Objekt zurückzugeben, mit dem die Schriftarteigenschaften des Textes wie Farbe, Fettdruck usw. festgelegt werden können.

{{% /alert %}}

## Benutzerdefinierte Rich-Text-Datenbeschriftung des Diagrammpunkts

Der folgende Code greift auf den ersten Diagrammpunkt der ersten Serie zu, setzt seinen Text und legt dann die Schriftart der ersten 10 Zeichen fest, indem er die Farbe auf Rot setzt und die Fettdruck-Option auf **true** setzt.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook from source Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the data label of first series first point
    DataLabels dlbls = chart.GetNSeries().Get(0).GetPoints().Get(0).GetDataLabels();

    // Set data label text
    dlbls.SetText(u"Rich Text Label");

    // Set the font setting of the first 10 characters
    FontSetting fntSetting = dlbls.Characters(0, 10);
    fntSetting.GetFont().SetColor(Color::Red());
    fntSetting.GetFont().SetIsBold(true);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
