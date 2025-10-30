---
title: Determinare se la dimensione della carta del foglio di lavoro è automatica con C++
linktitle: Determina se la dimensione carta del foglio di lavoro è automatica
type: docs
weight: 90
url: /it/cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Questo articolo spiega come usare l API o codice di esempio della libreria C++ per determinare se la dimensione della carta del foglio di lavoro è automatica in modo programmatico.
keywords: determinare se la dimensione della carta del foglio di lavoro è automatica C++
---

## **Possibili Scenari di Utilizzo**

 La maggior parte delle volte, la dimensione della carta del foglio di lavoro è automatica. Quando è automatica, è spesso impostata come *Lettera*. A volte l'utente imposta la dimensione della carta del foglio di lavoro in base alle proprie esigenze. In questo caso, la dimensione della carta non è automatica. È possibile verificare se la dimensione della carta del foglio di lavoro è automatica o meno usando la proprietà [**PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/isautomaticpapersize/) della classe **Worksheet**.

## **Determina se le dimensioni del foglio di lavoro sono automatiche**

Il codice di esempio riportato di seguito carica i seguenti due file Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

 e verifica se la dimensione della carta del primo foglio di lavoro è automatica o meno. In Microsoft Excel, puoi controllare se la dimensione della carta è automatica o meno tramite la finestra di configurazione della pagina come mostrato in questo screenshot.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the first workbook having automatic paper size false
    Workbook wb1(sourceDir + u"samplePageSetupIsAutomaticPaperSize-False.xlsx");

    // Load the second workbook having automatic paper size true
    Workbook wb2(sourceDir + u"samplePageSetupIsAutomaticPaperSize-True.xlsx");

    // Access the first worksheet of both workbooks
    Worksheet ws11 = wb1.GetWorksheets().Get(0);
    Worksheet ws12 = wb2.GetWorksheets().Get(0);

    // Print the PageSetup.IsAutomaticPaperSize property of both worksheets
    std::wcout << u"First Worksheet of First Workbook - IsAutomaticPaperSize: " << ws11.GetPageSetup().IsAutomaticPaperSize() << std::endl;
    std::wcout << u"First Worksheet of Second Workbook - IsAutomaticPaperSize: " << ws12.GetPageSetup().IsAutomaticPaperSize() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Output della console**

Ecco l'output sulla console del codice di esempio sopra quando eseguito con i file Excel di esempio forniti.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
