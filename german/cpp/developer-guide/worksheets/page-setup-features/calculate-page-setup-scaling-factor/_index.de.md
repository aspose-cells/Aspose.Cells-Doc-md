---
title: Berechnen Sie den Seitenansicht Skalierungsfaktor mit C++
linktitle: Berechnen des Maßstabsfaktors für die Seiteneinrichtung
type: docs
weight: 300
url: /de/cpp/calculate-page-setup-scaling-factor/
description: Dieser Artikel enthält Beispielcode, der erklärt, wie man die C++ API oder Bibliothek verwendet, um den Seitenansicht Skalierungsfaktor mithilfe der Option „Anpassen auf n Seite(n) breit und m hoch“ in Excel programmgesteuert zu berechnen.
keywords: Anpassen auf n Seiten breit und m hoch in Excel, C++ Berechnung des Seitenansicht Skalierungsfaktors
---

{{% alert color="primary" %}}

Wenn Sie die Seiteneinrichtung mit der Option **Fit auf n Seite(n) breit x m Seite(n) hoch** festlegen, berechnet Microsoft Excel den Maßstabsfaktor für die Seiteneinrichtung. Sie können dasselbe mit der Eigenschaft [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/) berechnen. Diese Eigenschaft gibt einen Double-Wert zurück, der in einen Prozentwert umgewandelt werden kann. Wenn beispielsweise 0,5 zurückgegeben wird, bedeutet dies, dass der Maßstabsfaktor 50% beträgt.

{{% /alert %}}

Der folgende Beispielcode veranschaulicht, wie der Maßstabsfaktor für die Seiteneinrichtung mit der Eigenschaft [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/) berechnet wird.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some data in these cells
    worksheet.GetCells().Get(u"A4").PutValue(u"Test");
    worksheet.GetCells().Get(u"S4").PutValue(u"Test");

    // Set paper size
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Set fit to pages wide as 1
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Calculate page scale via sheet render
    ImageOrPrintOptions options;
    SheetRender sr(worksheet, options);

    // Convert page scale double value to percentage
    double pageScale = sr.GetPageScale();
    std::wstring strPageScale = std::to_wstring(pageScale * 100) + L"%";

    // Write the page scale value
    std::wcout << strPageScale << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
