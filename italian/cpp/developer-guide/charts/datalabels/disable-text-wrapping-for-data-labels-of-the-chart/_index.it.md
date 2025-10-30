---
title: Disabilita l andamento del testo per le etichette dei dati del grafico con C++
linktitle: Disabilita l andamento del testo per le etichette dei dati
description: Scopri come disabilitare l andamento del testo per le etichette dei dati nei grafici utilizzando Aspose.Cells for C++. La nostra guida ti mostrerà come evitare che etichette lunghe si sovrappongano e come ottenere grafici più leggibili e chiari.
keywords: Aspose.Cells for C++, grafici, etichette dei dati, andamento del testo, sovrapposizione, leggibilità, visualizzazioni.
type: docs
weight: 70
url: /it/cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 consente agli utenti di abilitare o disabilitare il testo all'interno delle etichette dati del grafico. Per impostazione predefinita, il testo all'interno delle etichette dati del grafico è nello stato di testo a capo.

Aspose.Cells fornisce una proprietà [**DataLabels.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/istextwrapped/) che è possibile impostare su True o False per abilitare o disabilitare il testo a capo delle etichette dati rispettivamente.

{{% /alert %}}

Il campione di codice sottostante mostra come disabilitare il testo a capo per le etichette dati del grafico.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Load the sample Excel file inside the workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Disable the Text Wrapping of Data Labels in all Series
    chart.GetNSeries().Get(0).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(1).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(2).GetDataLabels().SetIsTextWrapped(false);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Text wrapping disabled successfully in data labels!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
