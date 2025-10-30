---
title: Mostrare l intervallo di celle come etichette dati con C++
linktitle: Mostrare l intervallo di celle come etichette dati
description: Impara come mostrare un intervallo di celle come etichette dati nei grafici usando Aspose.Cells for C++. La nostra guida dimostrerà come collegare le etichette alla fonte dati e formattarle per fornire informazioni accurate e significative nei tuoi grafici.
keywords: Aspose.Cells for C++, tracciamento, etichette dati, intervallo di celle, fonte dati, formattazione, precisione, informazioni significative.
type: docs
weight: 130
url: /it/cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

In Microsoft Excel 2013, puoi visualizzare un intervallo di celle per le etichette dati. Aspose.Cells supporta questa funzionalità.

{{% /alert %}}

## **Casella di controllo per mostrare l'intervallo di celle come etichette dati**

Per mostrare l'intervallo di celle come etichette dati in Microsoft Excel:

1. Seleziona le etichette dati della serie e fai clic con il tasto destro per aprire il menu contestuale.
1. Seleziona **Formatta etichette dati**. Le opzioni di etichettatura vengono visualizzate.
1. Seleziona o deseleziona l'opzione **L'etichetta contiene - Valore dalle celle**.

Il codice di esempio qui sotto accede alle etichette dati di una serie del grafico e imposta la proprietà [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/getshowcellrange/) su **true** per selezionare l'opzione **L'etichetta contiene - Valore dalle celle**.

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
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook from the source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Check the "Label Contains - Value From Cells"
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();
    dataLabels.SetShowCellRange(true);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
