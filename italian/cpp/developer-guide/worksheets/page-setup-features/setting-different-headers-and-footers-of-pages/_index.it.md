---
title: Impostare intestazioni e piè di pagina diversi per pagine diverse con C++
linktitle: Impostare intestazioni e piè di pagina diversi
type: docs
weight: 35
url: /it/cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Questo articolo fornisce codice di esempio che mostra come impostare programmaticamente varie intestazioni e piè di pagina delle impostazioni di configurazione della pagina del foglio di lavoro Excel utilizzando la libreria e API C++. È possibile impostare le intestazioni e i piè di pagina per la prima pagina, le pagine dispari e le pagine pari.
keywords: imposta intestazione piè di pagina Excel prima pagina C++, imposta intestazione piè di pagina Excel pagine dispari C++, imposta intestazione piè di pagina Excel pagine pari C++
---

{{% alert color="primary" %}}

 MS Excel supporta la possibilità di impostare intestazioni e piè di pagina diversi per la prima pagina, le pagine dispari e le pagine pari dall'Excel 2007.
Aspose.Cells supporta la stessa funzionalità.

{{% /alert %}}

## **Impostazione di Intestazioni e piè di pagina diversi in MS Excel**

**![Impostazione di Intestazioni e piè di pagina diversi](difpage.png)**

1. Clicca su **Layout di pagina > Titoli di stampa > Intestazione/Piè di pagina**.
1. Seleziona **Pagine dispari e pari diverse** o **Prima pagina diversa**.
1. Inserisci intestazioni e piè di pagina diversi.

## **Impostazione di Intestazioni e piè di pagina diversi con Aspose.Cells**

Aspose.Cells si comporta allo stesso modo di Excel.
1. Imposta i flag [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdiffoddeven/) e [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdifffirst/) 
1. Inserisci intestazioni e piè di pagina diversi.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Get the first worksheet's page setup
    PageSetup pageSetup = wb.GetWorksheets().Get(0).GetPageSetup();

    // Set different headers for odd and even pages
    pageSetup.SetIsHFDiffOddEven(true);
    pageSetup.SetHeader(1, u"I am the header of the Odd page.");
    pageSetup.SetEvenHeader(1, u"I am the header of the Even page.");

    // Set a different header for the first page
    pageSetup.SetIsHFDiffFirst(true);
    pageSetup.SetFirstPageHeader(1, u"I am the header of the First page.");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
