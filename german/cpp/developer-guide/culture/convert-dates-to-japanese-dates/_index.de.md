---
title: Datumsangaben in japanische Daten mit C++ konvertieren
linktitle: Datumsangaben in japanische Datumsangaben konvertieren
type: docs
weight: 350
url: /de/cpp/convert-dates-to-japanese-dates/
description: Lernen Sie, wie Sie gregorianische Daten mit Aspose.Cells for C++ in japanische Daten umwandeln.
---

{{% alert color="primary" %}}

Im japanischen Kalender beginnt eine neue Ära mit der Herrschaft eines neuen Kaisers. Am 1. Mai 2019 kam ein neuer Kaiser an die Macht, mit dem die Heisei-Ära endete und die Reiwa-Ära begann.

{{% /alert %}}

Aspose.Cells bietet eine Möglichkeit, Gregorianische Daten in japanische Daten umzuwandeln. Während dieser Umwandlung werden auch Änderungen in der Ära berücksichtigt. Der folgende Codeausschnitt konvertiert die [Quell-Excel](90112015.xlsx) Datei mit Gregorianischen Daten in eine [Ausgabe-PDF](90112016.pdf) mit japanischen Daten, wie im Bild unten gezeigt.

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

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

    // Create load options for XLSX format
    LoadOptions options(LoadFormat::Xlsx);

    // Set culture info to Japanese
    options.SetLanguageCode(CountryCode::Japan);

    // Load the workbook with Japanese dates
    Workbook workbook(srcDir + u"JapaneseDates.xlsx", options);

    // Save the workbook as PDF
    workbook.Save(outDir + u"JapaneseDates.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF with Japanese dates!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
