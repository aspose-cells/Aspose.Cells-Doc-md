---
title: Mostra punti elenco impostando il valore della cella usando HTML con C++
linktitle: Mostra Elenco puntato impostando il Valore della Cella utilizzando HTML
type: docs
weight: 130
url: /it/cpp/display-bullets-by-setting-cell-value-using/
description: Aggiungi punti elenco alle celle Excel usando HTML e l API facile da usare Aspose.Cells for C++.
keywords: aggiungi punti elenco in Excel, aggiungi punti elenco in Excel C++, visualizza punti elenco in Excel, visualizza punti elenco in Excel C++, aggiungi punti elenco in Excel con HTML, aggiungi punti elenco in Excel con HTML C++, visualizza punti elenco in Excel con HTML, visualizza punti elenco in Excel con HTML C++, visualizza punti elenco in Excel usando HTML, aggiungi punti elenco in Excel usando HTML
---

{{% alert color="primary" %}}

Aspose.Cells supporta la visualizzazione di elenchi puntati con codice HTML. In questo articolo verrà spiegato come visualizzare i punti elenco impostando il valore della cella utilizzando HTML. Verrà utilizzata la proprietà [**Cell.GetHtmlString()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) per impostare il valore della cella con il nostro HTML.

{{% /alert %}}

## Codice C++ per visualizzare punti elenco impostando il valore della cella usando HTML

Il codice seguente utilizza il codice HTML per impostare il valore della cella. Una volta eseguito questo codice, otterrai l'output mostrato nell'immagine sottostante.

```cpp
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

    // Access cell A1
    Cell cell = worksheet.GetCells().Get("A1");

    // Set the HTML string
    cell.SetHtmlString(u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>");

    // Auto fit the Columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputFilePath = u"BulletsInCells_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Output generato dal codice di esempio

Lo screenshot seguente mostra l'output del codice di esempio precedente.

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
{{< app/cells/assistant language="cpp" >}}
