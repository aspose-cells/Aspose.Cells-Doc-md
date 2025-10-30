---
title: Aggiungere Testo Riche in HTML all interno della Cell con C++
linktitle: Valore stringa HTML
type: docs
weight: 50
url: /it/cpp/adding-html-rich-text-inside-the-cell/
description: Impara come aggiungere testo ricco HTML all interno della cella tramite l API Aspose.Cells for C++.
keywords: Aggiungi testo HTML ricco all interno della cella, Imposta testo HTML ricco all interno della cella, Aggiungi testo HTML ricco nella cella
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione di HTML orientato a Microsoft Excel in formato XLS/XLSX. Ciò significa che l'HTML generato da Microsoft Excel può essere convertito nuovamente in formato XLS/XLSX utilizzando Aspose.Cells.

Analogamente, se c'è dell'HTML semplice, Aspose.Cells può convertirlo in HTML Ricco. Aspose.Cells fornisce il metodo [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) che può prendere tale HTML semplice e convertirlo in testo di celle formattato.

{{% /alert %}}

Il seguente esempio di codice ti mostra come aggiungere testo ricco in HTML all'interno della cella. Si prega di consultare lo screenshot del file Excel di output.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set HTML formatted text in the cell
    cell.SetHtmlString(u"<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "HTML formatted text added to cell A1 successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Articoli correlati

- [Visualizza pallini impostando il valore della cella utilizzando HTML](/cells/it/cpp/display-bullets-by-setting-cell-value-using/)
- [Ottieni una stringa HTML5 dalla cella](/cells/it/cpp/get-html5-string-from-cell/)
{{< app/cells/assistant language="cpp" >}}
