---
title: Verifica se il Workbook contiene collegamenti esterni nascosti con C++
linktitle: Controllare se il foglio di lavoro contiene collegamenti esterni nascosti
type: docs
weight: 230
url: /it/cpp/check-if-workbook-contains-hidden-external-links/
description: Impara come rilevare collegamenti esterni nascosti nei workbooks Excel usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**
A volte, il workbook contiene collegamenti esterni nascosti che non possono essere visualizzati in Microsoft Excel. Aspose.Cells recupera tutti i collegamenti esterni, siano visibili o nascosti. Tuttavia, puoi verificare la proprietà [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) per controllare se il collegamento esterno è visibile o meno.

## **Controllare se il foglio di lavoro contiene collegamenti esterni nascosti**
Il seguente esempio di codice carica il [file Excel di origine](5115413.xlsx) che contiene collegamenti esterni nascosti. Questi collegamenti non sono visibili in Microsoft Excel ma sono presenti nel workbook. Dopo aver stampato [ExternalLink.GetDataSource()](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/getdatasource/) e la proprietà [ExternalLink.IsReferred](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isreferred/), viene stampata la proprietà [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/). Nell'output della console, si vede che tutti i collegamenti esterni non sono visibili.

### **Codice di Esempio**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Loads the workbook which contains hidden external links
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the external link collection of the workbook
    ExternalLinkCollection links = workbook.GetWorksheets().GetExternalLinks();

    // Print all the external links and check their IsVisible property
    for (int i = 0; i < links.GetCount(); i++)
    {
        ExternalLink link = links.Get(i);
        std::cout << "Data Source: " << link.GetDataSource().ToUtf8() << std::endl;
        std::cout << "Is Visible: " << (link.IsVisible() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Output della console**
Ecco l'output della console del codice di esempio sopra quando eseguito con il [file di Excel di esempio](5115413.xlsx).

{{< highlight java >}}

Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
