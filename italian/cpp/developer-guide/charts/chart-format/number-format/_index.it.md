---
title: Imposta il codice di formato valori delle serie del grafico con C++
linktitle: Formato numero
type: docs
weight: 100
url: /it/cpp/set-the-values-format-code-of-chart-series/
description: Impara come impostare il codice di formato valori delle serie del grafico in Aspose.Cells for C++. La nostra guida ti aiuterà a capire come formattare i dati della serie del grafico usando il codice di formato appropriato, permettendoti di presentare i tuoi dati in modo accurato e professionale.
keywords: Aspose.Cells for C++, serie di grafico, codice di formato valori, formattazione, presentazione dei dati, precisione, professionalità.
---

## **Possibili Scenari di Utilizzo**
Puoi impostare il codice di formato valori delle serie del grafico usando la proprietà [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/). Questa proprietà è utile non solo per le serie basate sull'intervallo all'interno del foglio di lavoro, ma funziona anche bene per le serie create con un array di valori.

## **Impostare il codice di formato dei valori della serie del grafico**
Il seguente esempio di codice aggiunge una serie in un grafico vuoto che non aveva serie prima. Aggiunge la serie usando l'array di valori. Una volta aggiunta, la si formatta con il codice `$#,##0` usando la proprietà [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/) e il numero `10000` diventa `$10.000`. Lo screenshot mostra l'effetto del codice sul [file Excel di esempio](51740712.xlsx) e sul [file Excel di output](51740713.xlsx) dopo l'esecuzione.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Codice di Esempio**
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
