---
title: Arbeitsmappen Komprimierungsgrad mit C++ anpassen
linktitle: Arbeitsmappen Komprimierungsgrad anpassen
type: docs
weight: 180
url: /de/cpp/adjust-workbook-compression-level/
description: Lernen Sie, wie Sie den Komprimierungsgrad einer Arbeitsmappe mit Aspose.Cells for C++ anpassen, um Dateigröße und Verarbeitungszeit zu optimieren.
---

## **Arbeitsmappenkompressionsniveau anpassen**

Entwickler können den Komprimierungsgrad der Arbeitsmappe anpassen, wenn sie mit größeren Arbeitsmappen arbeiten. Entwickler können kleinere Dateigrößen höher priorisieren als die Verarbeitungszeit oder umgekehrt. Aspose.Cells stellt die [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) Enumeration bereit, die zur Festlegung des Komprimierungsgrads der Arbeitsmappe verwendet werden kann. Die [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) Enumeration bietet die folgenden Elemente.

- Level1: Die schnellste, aber am wenigsten effektive Kompression.
- Level2: Etwas langsamer, aber besser als Level 1.
- Stufe3: Etwas langsamer, aber besser als Stufe 2.
- Stufe4: Etwas langsamer, aber besser als Stufe 3.
- Stufe5: Etwas langsamer als Stufe 4, aber mit besserer Kompression.
- Stufe6: Ein gutes Gleichgewicht zwischen Geschwindigkeit und Kompressionseffizienz.
- Stufe7: Ziemlich gute Kompression!
- Stufe8: Bessere Kompression als Stufe7!
- Stufe9: Die "beste" Kompression, wobei beste die größte Reduzierung der Größe des Eingabedatenstroms bedeutet. Dies ist auch die langsamste Kompression.

Der folgende Codeausschnitt zeigt die Verwendung der [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) Enumeration und vergleicht die Konvertierungszeit für Level1, Level6 und Level9. Sie können auch die Größen der generierten Dateien vergleichen.

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"LargeSampleFile.xlsx");

    // Create XlsbSaveOptions object
    XlsbSaveOptions options;

    // Set compression level to 1 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level1);
    auto start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_1_out.xlsb", options);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 1 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 6 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level6);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_6_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 6 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 9 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level9);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_9_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 9 Elapsed Time: " << duration.count() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
