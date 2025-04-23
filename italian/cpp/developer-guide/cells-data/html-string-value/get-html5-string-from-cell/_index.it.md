---
title: Ottieni la stringa HTML5 dalla cella con C++
linktitle: Ottieni la stringa HTML5 dalla cella
type: docs
weight: 90
url: /it/cpp/get-html5-string-from-cell/
description: Impara come ottenere la stringa HTML5 da una cella usando l API Aspose.Cells for C++.
keywords: Ottieni la stringa HTML5 dalla cella, Ottieni la stringa HTML5 dalla cella, Gestisci la stringa HTML5 della cella
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells restituisce la stringa HTML della cella usando il metodo [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) che accetta un parametro booleano. Se passi **false** come parametro, restituirà HTML normale, se passi **true**, restituirà la stringa HTML5.

## **Ottieni la stringa HTML5 dalla cella**

Il codice di esempio seguente crea un oggetto workbook e aggiunge del testo nella cella A1 della prima scheda di lavoro. Quindi ottiene l'HTML normale e l'HTML5 dalla cella A1 utilizzando il metodo [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) e li stampa sulla console.

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1 and put some text inside it
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(u"This is some text.");

    // Get the Normal and Html5 strings
    U16String strNormal = cell.GetHtmlString(false);
    U16String strHtml5 = cell.GetHtmlString(true);

    // Print the Normal and Html5 strings on console
    std::cout << "Normal:\r\n" << strNormal.ToUtf8() << std::endl;
    std::cout << std::endl;
    std::cout << "Html5:\r\n" << strHtml5.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Output della console**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
