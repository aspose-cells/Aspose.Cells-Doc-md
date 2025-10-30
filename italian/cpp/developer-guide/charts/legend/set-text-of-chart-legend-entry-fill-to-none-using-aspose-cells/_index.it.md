---
title: Imposta il testo dell elemento di legenda del grafico su None con C++
linktitle: Imposta il testo dell elemento di legenda del grafico su None
description: Impara come usare Aspose.Cells for C++ per impostare il testo dell elemento di legenda del grafico su nessuno. La nostra guida dimostrerà come modificare il colore di riempimento delle voci della legenda in grafici Microsoft Excel per una migliore visualizzazione e personalizzazione.
keywords: Aspose.Cells for C++, Riempimento dell Elemento di Legenda del Grafico, Microsoft Excel, Visualizzazione, Personalizzazione.
type: docs
weight: 320
url: /it/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Se desideri impostare il testo del riempimento dell'elemento legenda del grafico su nessuno in modo che non venga visualizzato all'interno della legenda del grafico, imposta il [**LegendEntry.IsTextNoFill**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legendentry/istextnofill/) su **true**.

{{% /alert %}}

Il codice di esempio seguente imposta il testo del secondo riempimento dell'elemento legenda del grafico su nessuno. Scarica il [file Excel di esempio](5115219.xlsx) utilizzato in questo codice e il [file Excel di output](5115217.xlsx) generato da esso per ulteriori informazioni.

La seguente schermata evidenzia l'effetto di questo codice sul [file excel di esempio](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ChartLegendEntry_out.xlsx";

    // Open the template file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = sheet.GetCharts().Get(0);

    // Set text of second legend entry fill to none
    chart.GetLegend().GetLegendEntries().Get(1).SetIsTextNoFill(true);

    // Save the workbook in xlsx format
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Chart legend entry modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
