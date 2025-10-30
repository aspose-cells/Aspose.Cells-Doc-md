---
title: Ställa in olika rubriker och fotnoter för olika sidor med C++
linktitle: Ställa in olika rubriker och fotnoter
type: docs
weight: 35
url: /sv/cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Denna artikel ger exempel på hur man programmässigt kan ställa in olika rubriker och fotnoter i Excel arbetsblads sidsetup med C++ biblioteket och API. Du kan ställa in rubriker och fotnoter för första sidan, udda sidor och jämna sidor.
keywords: ställe in excel rubrik fotfot första sida c++, ställe in excel rubrik fotnot udda sidor c++, ställ in excel rubrik fotnot jämna sidor c++
---

{{% alert color="primary" %}}

MS Excel stöder att ställa in olika rubriker och fotnoter för första sidan, udda sidor och jämna sidor sedan Excel 2007.
Aspose.Cells stöder samma funktion.

{{% /alert %}}

## **Inställning av olika sidhuvuden och sidfötter i MS Excel**

**![Inställning av olika sidhuvuden och sidfötter](difpage.png)**

1. Klicka **Sidlayout > Skriv ut titlar > Rubrik/Fotnot**.
1. Kontrollera **Olika udda och jämna sidor** eller **Olika första sidan**.
1. Ange olika sidhuvuden och sidfötter.

## **Inställning av olika sidhuvuden och sidfötter med Aspose.Cells**

Aspose.Cells beter sig på samma sätt som Excel.
1. Sätter flaggorna [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdiffoddeven/) och [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdifffirst/) 
1. Ange olika sidhuvuden och sidfötter.

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
