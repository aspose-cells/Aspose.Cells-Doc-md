---
title: Ottieni hyperlink in un intervallo con C++
linktitle: Ottieni i collegamenti ipertestuali nell intervallo
type: docs
weight: 100
url: /it/cpp/get-hyperlinks-in-range/
description: Impara come ottenere hyperlink in un intervallo tramite l API Aspose.Cells for C++.
keywords: Ottieni collegamenti ipertestuali nell intervallo, Ottieni tutti i collegamenti ipertestuali nell intervallo selezionato, Elimina collegamenti ipertestuali nell intervallo, Elimina i collegamenti ipertestuali nell intervallo selezionato
---

## **Ottieni i collegamenti ipertestuali nell'intervallo**

La classe [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) fornisce una proprietà [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/gethyperlinks/) che restituisce tutti i collegamenti ipertestuali nell'intervallo selezionato. È inoltre possibile eliminare il collegamento ipertestuale chiamando il metodo [**Hyperlink.Delete**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/delete/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"HyperlinksSample.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Range range = worksheet.GetCells().CreateRange(u"A2", u"B3");
    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();

    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink& link = hyperlinks[i];
        std::cout << link.GetArea().ToString().ToUtf8() << " : " << link.GetAddress().ToUtf8() << std::endl;
        link.Delete();
    }

    workbook.Save(outDir + u"HyperlinksSample_out.xlsx");
    std::cout << "Hyperlinks processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
