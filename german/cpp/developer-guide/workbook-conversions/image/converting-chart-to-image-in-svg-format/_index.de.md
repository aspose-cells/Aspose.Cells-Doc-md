---
title: Umwandlung eines Diagramms in ein SVG Bild mit C++
linktitle: Diagramm in SVG Format konvertieren
type: docs
weight: 240
url: /de/cpp/converting-chart-to-image-in-svg-format/
description: Lernen Sie, wie man Diagramme mit Aspose.Cells in SVG Bilder umwandelt.
---

{{% alert color="primary" %}}

Scalable Vector Graphics (SVG) ist ein auf XML basierendes Vektorbildformat für zweidimensionale Grafiken, das auch Interaktivität und Animation unterstützt. Die SVG-Spezifikation ist ein offener Standard, der seit 1999 vom World Wide Web Consortium (W3C) entwickelt wird.

SVG-Bilder und ihr Verhalten sind in XML-Textdateien definiert. Das bedeutet, dass sie durchsucht, indexiert, skriptgesteuert und komprimiert werden können. Als XML-Dateien können SVG-Bilder mit jedem Texteditor erstellt und bearbeitet werden, werden jedoch häufiger mit Zeichensoftware erstellt.

Aspose.Cells kann Diagramme in verschiedenen Formaten wie BMP, JPEG, PNG, GIF, SVG usw. als Bilder speichern. Dieser Artikel erklärt, wie man ein Diagramm im SVG-Format speichert.

{{% /alert %}}

Der folgende Beispielcode erläutert, wie Aspose.Cells verwendet wird, um ein Diagramm in ein SVG-Formatbild zu konvertieren. Der Code lädt die Quelldatei von Microsoft Excel und speichert dann das erste auf dem ersten Arbeitsblatt gefunden Diagramm als SVG.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleChartBook.xlsx";

    // Create workbook object from source file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetImageType(Aspose::Cells::Drawing::ImageType::Svg);

    // Save the chart to svg format
    chart.ToImage(outDir + u"Image_out.svg", opts);

    std::cout << "Chart saved to SVG format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
