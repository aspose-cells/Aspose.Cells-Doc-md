---
title: Conversione di Grafico in Immagine in formato SVG con C++
linktitle: Conversione del grafico in un immagine nel formato SVG
type: docs
weight: 240
url: /it/cpp/converting-chart-to-image-in-svg-format/
description: Impara come convertire grafici in immagini SVG usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Scalable Vector Graphics (SVG) è un formato di immagine vettoriale basato su XML per grafica bidimensionale che supporta anche l'interattività e l'animazione. La specifica SVG è uno standard aperto sviluppato dal World Wide Web Consortium (W3C) dal 1999.

Le immagini SVG e i loro comportamenti sono definiti in file di testo XML. Ciò significa che possono essere cercati, indicizzati, scriptati e compressi. Come file XML, le immagini SVG possono essere create e modificate con qualsiasi editor di testo, ma vengono più spesso create con software di disegno.

Aspose.Cells può salvare i grafici come immagini in vari formati come BMP, JPEG, PNG, GIF, SVG, ecc. Questo articolo spiega come salvare un grafico in formato SVG.

{{% /alert %}}

Nel seguente codice di esempio viene spiegato come utilizzare Aspose.Cells per convertire un grafico in un'immagine nel formato SVG. Il codice carica il file Microsoft Excel di origine e poi salva il primo grafico trovato nel primo foglio di lavoro in SVG.

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
