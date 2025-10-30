---
title: Filtern der Art der Daten beim Laden der Arbeitsmappe aus einer Vorlagendatei mit C++
linktitle: Daten filtern beim Laden der Arbeitsmappe
type: docs
weight: 400
url: /de/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Erfahren Sie, wie Sie beim Laden einer Arbeitsmappe aus einer Vorlage mit Aspose.Cells und C++ bestimmte Datentypen filtern.
---

{{% alert color="primary" %}}

Manchmal möchten Sie angeben, welche Art von Daten beim Erstellen der Arbeitsmappe aus der Vorlage geladen werden soll. Das Filtern der geladenen Daten kann die Leistung für Ihren speziellen Zweck verbessern, insbesondere bei der Verwendung [LightCells-APIs](/cells/de/cpp/using-lightcells-api/). Bitte verwenden Sie hierfür die Eigenschaft [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/).

{{% /alert %}}

Der folgende Beispielcode lädt nur Formobjekte beim Laden des Arbeitsbuches aus der [Vorlagendatei](5115552.xlsx), die Sie aus dem angegebenen Link herunterladen können. Der folgende Screenshot zeigt den Inhalt der [Vorlagendatei](5115552.xlsx) und erklärt auch, dass die Daten in roter Farbe und gelbem Hintergrund nicht geladen werden, da das [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/)-Eigenschaft auf [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) gesetzt wurde.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Der folgende Screenshot zeigt das [Ausgabe-PDF](5115555.pdf), das Sie aus dem angegebenen Link herunterladen können. Hier sehen Sie, dass die Daten in roter Farbe und gelbem Hintergrund nicht vorhanden sind, aber alle Formen sind vorhanden.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

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

    // Set the load options, we only want to load shapes and do not want to load data
    LoadOptions loadOptions(LoadFormat::Xlsx);
    loadOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Create workbook object from sample excel file using load options
    Workbook workbook(srcDir + u"sampleFilterChars.xlsx", loadOptions);

    // Save the output in pdf format
    workbook.Save(outDir + u"sampleFilterChars_out.pdf", SaveFormat::Pdf);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
