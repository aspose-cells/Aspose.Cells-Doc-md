---
title: Automatisches Anpassen der Zeilen für die Darstellung mit C++
linktitle: AutoFit für das Rendern von Zeilen
type: docs
weight: 130
url: /de/cpp/autofit-rows-for-rendering/
description: Lernen Sie, wie Sie Zeilen für die Darstellung in Excel Dateien mit Aspose.Cells und C++ automatisch anpassen.
---

Im Allgemeinen, wenn Sie den gesamten Text in einer Zelle anzeigen möchten, können Sie die Zeile in der Normalansicht mit 100% Zoom in Microsoft Excel automatisch anpassen. Dies ermöglicht es, den Text in der Normalansicht vollständig sichtbar zu machen, und auch beim Drucken oder Speichern der Datei als PDF wird der Text richtig angezeigt.

Jedoch funktioniert in einigen Fällen das automatische Anpassen der Zeile in der Normalansicht gut, aber wenn Sie zur Druckansicht wechseln oder die Datei als PDF speichern, wird der Text beschnitten. Bitte überprüfen Sie die Quelldatei [Book1.xlsx](Book1.xlsx) und die Screenshots.

![Text wird in der Druckansicht beschnitten](text_clipped_in_printview.png)

Wenn Sie verhindern möchten, dass Text im gespeicherten PDF-Datei abgeschnitten wird, können Sie die Zeile mit der Option [AutoFitterOptions.GetForRendering()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getforrendering/) automatisch anpassen.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize workbook instance
    Workbook workbook(u"Book1.xlsx");

    // Set autofit options for rendering
    AutoFitterOptions autoFitterOptions;
    autoFitterOptions.SetForRendering(true);

    // Autofit rows with options
    workbook.GetWorksheets().Get(0).AutoFitRows(autoFitterOptions);

    // Save to PDF
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    Aspose::Cells::Cleanup();
}
```

Nun wird der Text nicht in der Ausgabe-PDF-Datei beschnitten.

![Text wird in der gespeicherten PDF-Datei nicht beschnitten](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="cpp" >}}
