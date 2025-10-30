---  
title: Modifica la sorgente dati del grafico alla worksheet di destinazione durante la copia di righe o intervalli con C++  
description: Impara come cambiare la sorgente dati di un grafico a una worksheet di destinazione mentre si copiano righe o intervalli in Aspose.Cells for C++. La nostra guida ti mostrerà come aggiornare l intervallo di dati del grafico e collegarlo alla worksheet di destinazione, assicurando che le righe o gli intervalli copiati siano riflessi accuratamente nel grafico.  
keywords: Aspose.Cells for C++, creazione di grafici, sorgente dati, worksheet di destinazione, righe, intervalli, copia, aggiornamento, intervallo dati, collegamento.  
type: docs  
weight: 440  
url: /it/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **Possibili Scenari di Utilizzo**

Quando copi righe o intervalli che contengono grafici in un nuovo worksheet, la sorgente dati del grafico non cambia. Per esempio, se la sorgente dati del grafico è =Sheet1!$A$1:$B$4, dopo aver copiato righe o intervalli in un nuovo worksheet, la sorgente dati rimarrà la stessa, cioè =Sheet1!$A$1:$B$4. Riferisce ancora al vecchio worksheet, cioè Sheet1. Questo è anche il comportamento in Microsoft Excel. Ma se vuoi che si riferisca al nuovo worksheet di destinazione, utilizza la proprietà [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) e impostala su **true** chiamando il metodo [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/). Ora, se il tuo worksheet di destinazione è DestSheet, allora la sorgente dati del tuo grafico cambierà da =Sheet1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.

## **Modifica dell'origine dei dati del grafico al foglio di lavoro di destinazione durante la copia delle righe o dell'intervallo**

Il seguente esempio di codice spiega come utilizzare la proprietà [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) durante la copia di righe o intervalli contenenti grafici in un nuovo worksheet. Il codice utilizza il [file Excel di esempio](5113699.xlsx) e genera il [file Excel di output](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the first sheet which contains chart
    Worksheet source = wb.GetWorksheets().Get(0);

    // Add another sheet named DestSheet
    Worksheet destination = wb.GetWorksheets().Add(u"DestSheet");

    // Set CopyOptions.ReferToDestinationSheet to true
    CopyOptions options;
    options.SetReferToDestinationSheet(true);

    // Copy all the rows of source worksheet to destination worksheet which includes chart as well
    // The chart data source will now refer to DestSheet
    destination.GetCells().CopyRows(source.GetCells(), 0, 0, source.GetCells().GetMaxDisplayRange().GetRowCount(), options);

    // Save workbook in xlsx format
    wb.Save(srcDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
