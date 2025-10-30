---
title: Misura la larghezza e l altezza del valore della cella in unità di pixel con C++
linktitle: Misura la dimensione
type: docs
weight: 260
url: /it/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Impara come misurare la larghezza e l altezza del valore della cella in unità di pixel tramite l API Aspose.Cells for C++.
keywords: Misura la Larghezza del Valore della Cella in Unità di Pixel, Misura l Altezza del Valore della Cella in Unità di Pixel, Ottieni la Larghezza del Valore della Cella in Unità di Pixel, Ottieni l Altezza del Valore della Cella in Unità di Pixel
---

{{% alert color="primary" %}}

A volte è necessario calcolare la larghezza e l'altezza del valore della cella per adattare il valore della cella all'interno della cella stessa. Aspose.Cells fornisce i seguenti metodi per questo scopo. Utilizzando questi metodi è possibile calcolare la larghezza e l'altezza del valore della cella e quindi impostare la larghezza della colonna e l'altezza della riga di quella cella rispettivamente e questo regolerà o adatterà il valore della cella all'interno della cella.

In alternativa, puoi anche [adattare automaticamente righe e colonne della tua cella o intervallo di celle](/cells/it/cpp/autofit-rows-and-columns/) usando le API di Aspose.Cells.

{{% /alert %}}

Il codice seguente spiega l'uso dei metodi [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) e [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell B2 and add some value inside it
    Cell cell = worksheet.GetCells().Get(u"B2");
    cell.PutValue(u"Welcome to Aspose!");

    // Enlarge its font to size 16
    Style style = cell.GetStyle();
    style.GetFont().SetSize(16);
    cell.SetStyle(style);

    // Calculate the width and height of the cell value in unit of pixels
    int32_t widthOfValue = cell.GetWidthOfValue();
    int32_t heightOfValue = cell.GetHeightOfValue();

    // Print both values
    std::wcout << u"Width of Cell Value: " << widthOfValue << std::endl;
    std::wcout << u"Height of Cell Value: " << heightOfValue << std::endl;

    // Set the row height and column width to adjust/fit the cell value inside cell
    worksheet.GetCells().SetColumnWidthPixel(1, widthOfValue);
    worksheet.GetCells().SetRowHeightPixel(1, heightOfValue);

    // Save the output excel file
    U16String outFilePath = u"output_out.xlsx";
    workbook.Save(outFilePath);

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Ottieni larghezza testo del valore della cella](/cells/it/cpp/get-text-width-of-cell-value/)
{{< app/cells/assistant language="cpp" >}}
