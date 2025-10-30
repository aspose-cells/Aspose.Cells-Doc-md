---
title: Autoadatta colonne e righe durante il caricamento HTML in Workbook con C++
linktitle: Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook
type: docs
weight: 120
url: /it/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Impara come autofittare colonne e righe durante il caricamento di HTML in un Workbook usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

È possibile adattare automaticamente le colonne e le righe durante il caricamento del file HTML all'interno dell'oggetto Workbook. Impostare la proprietà [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) su **true** a tale scopo.

## **Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook**

Il seguente codice di esempio carica innanzitutto l'HTML di esempio in un Workbook senza alcuna opzione di caricamento e lo salva in formato XLSX. Quindi carica nuovamente l'HTML di esempio in un Workbook ma questa volta, carica l'HTML dopo aver impostato la proprietà [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) su **true** e lo salva in formato XLSX. Si prega di scaricare entrambi i file di output di Excel, cioè [File di Excel di output senza AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) e [File di Excel di output con AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). La seguente schermata mostra l'effetto della proprietà [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) su entrambi i file di output di Excel.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

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

    // Sample HTML string
    U16String sampleHtml(u"<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>");

    // Convert HTML string to memory stream
    std::string utf8Data = sampleHtml.ToUtf8();
    Vector<uint8_t> ms(utf8Data.size());
    std::memcpy(ms.GetData(), utf8Data.data(), utf8Data.size());

    // Load memory stream into workbook
    Workbook wb(ms);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputWithout_AutoFitColsAndRows.xlsx");

    // Specify the HTMLLoadOptions and set AutoFitColsAndRows = true
    HtmlLoadOptions opts;
    opts.SetAutoFitColsAndRows(true);

    // Load memory stream into workbook with the above HTMLLoadOptions
    Workbook wbWithOptions(ms, opts);

    // Save the workbook in xlsx format
    wbWithOptions.Save(outDir + u"outputWith_AutoFitColsAndRows.xlsx");

    std::cout << "HTML to Excel conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
