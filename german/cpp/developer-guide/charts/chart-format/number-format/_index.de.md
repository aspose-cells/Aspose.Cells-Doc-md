---
title: Setzen Sie den Werte Formatcode der Diagrammserie mit C++
linktitle: Zahlenformat
type: docs
weight: 100
url: /de/cpp/set-the-values-format-code-of-chart-series/
description: Lernen Sie, wie Sie den Werte Formatcode der Diagrammserie in Aspose.Cells for C++ einstellen. Unser Leitfaden hilft Ihnen, Ihre Diagrammseriendaten mit dem geeigneten Formatcode zu formatieren, um Ihre Daten genau und professionell zu präsentieren.
keywords: Aspose.Cells for C++, Diagrammserie, Werte Formatcode, Formatierung, Datenpräsentation, Genauigkeit, Professionalität.
---

## **Mögliche Verwendungsszenarien**
Sie können den Werte-Formatcode der Diagrammserie mit der Eigenschaft [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/) festlegen. Diese Eigenschaft ist nicht nur nützlich für Serien, die auf den Bereich innerhalb des Arbeitsblatts basieren, sondern funktioniert auch gut für Serien, die mit einem Werte-Array erstellt wurden.

## **Setzen des Werteformatcodes der Diagrammserie**
Der folgende Beispielcode fügt einer leeren Diagrammserie, die zuvor keine Serie hatte, eine Serie hinzu. Er verwendet ein Werte-Array. Nach dem Hinzufügen formatiert er die Serie mit dem Code `$#,##0` unter Verwendung der Eigenschaft [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/) und die Zahl `10000` wird zu `$10.000`. Der Screenshot zeigt die Wirkung des Codes auf das Beispiel-Excel-File (51740712.xlsx) und das Ausgabedatei (51740713.xlsx) nach der Ausführung.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Beispielcode**
```cpp
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"51740712.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"51740713.xlsx";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = worksheet.GetCharts().Get(0);

    // Add series using an array of values
    ch.GetNSeries().Add(U16String(u"{10000, 20000, 30000, 40000}"), true);

    // Access the series and set its values format code
    Series srs = ch.GetNSeries().Get(0);
    srs.SetValuesFormatCode(U16String(u"$#,##0"));

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "Chart series added and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
