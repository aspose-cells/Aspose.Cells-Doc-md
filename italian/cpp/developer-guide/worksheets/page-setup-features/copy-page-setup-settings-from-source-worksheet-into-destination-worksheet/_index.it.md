---
title: Copia le impostazioni della configurazione della pagina dal foglio di origine a quello di destinazione con C++
linktitle: Copia le impostazioni della configurazione della pagina
type: docs
weight: 80
url: /it/cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Questo articolo spiega come usare il codice esempio dell API o libreria C++ per copiare le impostazioni della configurazione della pagina dal foglio di origine a quello di destinazione in modo programmatico.
keywords: copia impostazioni configurazione pagina C++, copia impostazioni configurazione pagina nel foglio di destinazione C++
---

## **Possibili Scenari di Utilizzo**

Quando si aggiunge un nuovo foglio a un libro, contiene le impostazioni predefinite *Impostazioni pagina*. Ci possono essere momenti in cui è necessario trasferire le impostazioni ([**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)) da un foglio a un altro foglio. Questo documento spiega come copiare le impostazioni di configurazione pagina da un foglio a un altro utilizzando le API di Aspose.Cells.

## **Copia le impostazioni del layout pagina dal foglio di origine al foglio di destinazione**

Il seguente codice di esempio illustra come copiare le *impostazioni di configurazione pagina* da un foglio all'altro utilizzando il metodo [**PageSetup.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/copy/). Si prega di vedere il seguente codice di esempio e il suo output sulla console per un riferimento.

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    wb.GetWorksheets().Add(u"TestSheet1");
    wb.GetWorksheets().Add(u"TestSheet2");

    Worksheet TestSheet1 = wb.GetWorksheets().Get(u"TestSheet1");
    Worksheet TestSheet2 = wb.GetWorksheets().Get(u"TestSheet2");

    TestSheet1.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3ExtraTransverse);

    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    CopyOptions copyOptions;
    TestSheet2.GetPageSetup().Copy(TestSheet1.GetPageSetup(), copyOptions);

    std::cout << "After Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "After Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Output della console**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
