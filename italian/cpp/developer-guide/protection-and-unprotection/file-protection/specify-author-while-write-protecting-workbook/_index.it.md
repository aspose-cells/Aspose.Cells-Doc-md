---
title: Specificare autore durante la protezione in scrittura del workbook con C++
linktitle: Specificare l autore durante la protezione in scrittura del libro di lavoro
type: docs
weight: 40
url: /it/cpp/specify-author-while-write-protecting-workbook/
description: Impara come specificare un nome autore mentre si protegge a scrittura un workbook usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Puoi specificare il nome dell'autore durante la protezione in scrittura del tuo workbook utilizzando l'API Aspose.Cells. Si prega di usare la proprietà [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/) a questo scopo.

## **Specificare l'autore durante la protezione in scrittura del workbook**

Il seguente esempio di codice spiega l'uso della proprietà [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/). Il codice crea un workbook vuoto, lo protegge con password, specifica il nome dell'autore e lo salva come un [file Excel di output](67338582.xlsx). Lo screenshot seguente illustra l'effetto del codice di esempio sul file Excel di output per riferimento.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create empty workbook
    Workbook wb;

    // Write protect workbook with password
    wb.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Specify author while write protecting workbook
    wb.GetSettings().GetWriteProtection().SetAuthor(u"SimonAspose");

    // Save the workbook in XLSX format
    wb.Save(outDir + u"outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx");

    std::cout << "Workbook write protected with author specified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
