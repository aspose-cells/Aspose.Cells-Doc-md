---
title: Rileva il tipo di hyperlink con C++
linktitle: Rileva il tipo di collegamento ipertestuale
type: docs
weight: 160
url: /it/cpp/detect-hyperlink-type/
description: Impara come rilevare il tipo di hyperlink tramite l API Aspose.Cells for C++.
keywords: Rileva il tipo di collegamento ipertestuale, Rileva il tipo di collegamento ipertestuale, Ottieni il tipo di collegamento ipertestuale
---

## **Rilevare il tipo di collegamento ipertestuale**

Un file di Excel può avere diversi tipi di collegamenti ipertestuali come esterno, riferimento alla cella, percorso del file, ecc. Aspose.Cells supporta la funzione per rilevare il tipo di collegamento ipertestuale. I tipi di collegamenti ipertestuali sono rappresentati dall'Enumerazione [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). L'Enumerazione [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) ha i seguenti membri.

- Esterno: collegamento esterno
- PercorsoFile: percorso locale e completo dei file\cartelle.
- Email: email
- RiferimentoCella: collegamento a cella o intervallo denominato.

Per controllare il tipo di collegamento ipertestuale, la classe [**Hyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/) fornisce una proprietà [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) con un tipo di ritorno [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). Il seguente frammento di codice mostra l'uso della proprietà [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) utilizzando questo [file Excel di origine](94896195.xlsx).

### Codice Sorgente

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"LinkTypes.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    if (!worksheet)
    {
        std::cerr << "Worksheet not found!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Range range = worksheet.GetCells().CreateRange(u"A1", u"A7");
    if (!range)
    {
        std::cerr << "Range creation failed!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();


    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink link = hyperlinks[i];
        if (link)
        {
            std::cout << link.GetTextToDisplay().ToUtf8() << ": "
                << static_cast<int>(link.GetLinkType()) << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Di seguito è riportato l'output generato dal frammento di codice indicato sopra.

### Output della console
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
