---
title: Aggiorna i valori delle forme collegate con C++
linktitle: Aggiorna i valori delle forme collegate
type: docs
weight: 3200
url: /it/cpp/refresh-values-of-linked-shapes/
description: Impara come aggiornare i valori delle forme collegate nei file Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte, hai una forma collegata nel tuo file Excel che è collegata a una cella. In Microsoft Excel, modificando il valore della cella collegata viene modificato anche il valore della forma collegata. Questo funziona anche bene con Aspose.Cells se vuoi salvare il tuo documento di lavoro in formato XLS o XLSX. Tuttavia, se desideri salvare il tuo documento di lavoro in formato PDF o HTML, allora dovrai chiamare il metodo [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/) per aggiornare il valore della forma collegata.

{{% /alert %}}

## Esempio

Lo screenshot seguente mostra il file Excel di origine utilizzato nel codice di esempio qui sotto. Ha un'immagine collegata collegata alle celle A1 a E4. Modificheremo il valore della cella B4 con Aspose.Cells e poi chiameremo il metodo [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/) per aggiornare il valore dell'immagine e salvarlo in formato PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Puoi scaricare il [file Excel di origine](95584291.xlsx) e il [PDF di output](95584292.pdf) dai link forniti.

### Codice C++ per aggiornare i valori delle forme collegate

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleRefreshValueOfLinkedShapes.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell B4
    Cell cell = worksheet.GetCells().Get(u"B4");
    cell.PutValue(100);

    // Update the value of the Linked Picture which is linked to cell B4
    worksheet.GetShapes().UpdateSelectedValue();

    // Save the workbook in PDF format
    workbook.Save(outDir + u"outputRefreshValueOfLinkedShapes.pdf", SaveFormat::Pdf);

    std::cout << "Linked shapes value refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
