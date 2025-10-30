---
title: Stellen Sie die Spaltenbreite auf eine skalierbare Einheit wie em oder Prozent mit C++ ein
linktitle: Legen Sie die Spaltenbreite auf eine skalierbare Einheit wie em oder Prozent fest
type: docs
weight: 130
url: /de/cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Lernen Sie, wie man die Spaltenbreite mit Aspose.Cells for C++ auf skalierbare Einheiten wie em oder Prozent einstellt.
---

Das Generieren einer HTML-Datei aus einer Tabellenkalkulation ist sehr verbreitet. Die Größe der Spalten ist in "pt" definiert, was in vielen Fällen funktioniert. Es kann jedoch der Fall eintreten, dass diese feste Größe nicht erforderlich ist. Zum Beispiel, wenn die Breite eines Containerpanels 600px beträgt, in dem diese HTML-Seite angezeigt wird. In diesem Fall kann ein horizontaler Bildlaufbalken angezeigt werden, wenn die Breite der generierten Tabelle größer ist. Es war erforderlich, dass diese feste Größe in eine skalierbare Einheit wie em oder Prozent umgewandelt wird, um eine bessere Darstellung zu erhalten. Der folgende Beispielcode kann verwendet werden, wobei [**HtmlSaveOptions.GetWidthScalable()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getwidthscalable/) auf **true** gesetzt ist, um eine skalierbare Breite zu erstellen.

Beispiel-Quelldatei und Ausgabedateien können von folgenden Links heruntergeladen werden:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

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

    // Load sample source file
    Workbook wb(srcDir + u"sampleForScalableColumns.xlsx");

    // Specify Html Save Options
    HtmlSaveOptions options;

    // Set the property for scalable width
    options.SetWidthScalable(true);

    // Specify image save format
    options.SetExportImagesAsBase64(true);

    // Save the workbook in Html format with specified Html Save Options
    wb.Save(outDir + u"outsampleForScalableColumns.html", options);

    std::cout << "Workbook saved successfully with scalable columns!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
