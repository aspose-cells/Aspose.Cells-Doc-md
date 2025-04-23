---
title: Festlegen, wie Text in der Ausgabe PDF und im Bild gekreuzt wird mit C++
linktitle: Angabe, wie Zeichen in der Ausgabedatei PDF und Bild gekreuzt werden sollen
type: docs
weight: 120
url: /de/cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Lernen Sie, wie Sie die Textüberschreitung in PDF und Bildausgaben mit Aspose.Cells for C++ kontrollieren.
---

## **Mögliche Verwendungsszenarien**

Wenn eine Zelle Text oder Zeichen enthält, das größer ist als die Zellbreite, überläuft die Zeichenfolge, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Wenn Sie Ihre Excel-Datei in PDF oder Bild speichern, können Sie dieses Überlaufen steuern, indem Sie den Kreuztyp mit [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/) Enumeration angeben. Es hat die folgenden Werte:

- **TextCrossType.Default**: Zeigen Sie Text wie MS Excel, abhängig von der nächsten Zelle. Wenn die nächste Zelle null ist, wird die Zeichenfolge gekreuzt oder abgeschnitten.

- **TextCrossType.CrossKeep**: Zeigen Sie die Zeichenfolge wie MS Excel beim Exportieren in PDF/Bild.

- **TextCrossType.CrossOverride**: Zeigen Sie den gesamten Text, indem Sie andere Zellen kreuzen und den Text der gekreuzten Zellen überschreiben.

- **TextCrossType.StrictInCell**: Zeige nur den String innerhalb der Breite der Zelle an.

## **Angabe, wie Zeichen in der Ausgabedatei PDF/Bild mithilfe von TextCrossType überquert werden sollen**

Der folgende Beispielcode lädt die Beispiel-Excel-Datei und speichert sie im PDF-/Bildformat, indem verschiedene [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/) angegeben werden. Die Beispiel-Excel-Datei und Ausgabedateien können von den folgenden Links heruntergeladen werden:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Beispielcode

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load template Excel file
    Workbook wb(srcDir + u"sampleCrosssType.xlsx");

    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Save PDF file
    wb.Save(outDir + u"outputCrosssType.pdf", pdfSaveOptions);

    // Initialize image or print options
    ImageOrPrintOptions imageSaveOptions;
    imageSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Initialize sheet renderer object
    SheetRender sheetRenderer(wb.GetWorksheets().Get(0), imageSaveOptions);

    // Save PNG image
    sheetRenderer.ToImage(0, outDir + u"outputCrosssType.png");

    Aspose::Cells::Cleanup();
}
```
