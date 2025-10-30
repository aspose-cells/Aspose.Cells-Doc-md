---
title: Arbeitsblatt in den Grafik Kontext rendern mit C++
linktitle: Arbeitsblatt in Grafikkontext rendern
type: docs
weight: 300
url: /de/cpp/render-worksheet-to-graphic-context/
description: Erfahren Sie, wie Sie ein Arbeitsblatt in einen Grafik Kontext mit Aspose.Cells for C++ rendern.
---

{{% alert color="primary" %}}

Aspose.Cells kann jetzt ein Arbeitsblatt in einen Grafik-Kontext rendern. Der Grafik-Kontext kann alles sein, z.B. eine Bilddatei, der Bildschirm oder ein Drucker. Bitte verwenden Sie eine der folgenden beiden Methoden, um ein Arbeitsblatt in einen Grafik-Kontext zu rendern.

- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)
- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)

{{% /alert %}}

Der folgende Code zeigt, wie man Aspose.Cells verwendet, um ein Arbeitsblatt in einen Grafik-Kontext zu rendern. Nach Ausführung des Codes wird das gesamte Arbeitsblatt gedruckt, der übrig gebliebene leere Raum wird im Grafik-Kontext mit blauer Farbe ausgefüllt, und das Bild wird als **OutputImage_out_.png** gespeichert. Sie können jede beliebige Ausgangs-Excel-Datei verwenden, um diesen Code auszuprobieren. Lesen Sie auch die Kommentare im Code für ein besseres Verständnis.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleBook.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outDir + u"OutputImage_out.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
