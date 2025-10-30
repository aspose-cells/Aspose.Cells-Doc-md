---
title: Lösenordsskydda eller avkryptera den delade arbetsboken med C++
linktitle: Lösenordsskydda eller upphäva skyddet för delad arbetsbok
type: docs
weight: 10
url: /sv/cpp/password-protect-or-unprotect-the-shared-workbook/
description: Lär dig hur du lösenordsskyddar eller avslyssnar en delad arbetsbok med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Du kan skydda eller avskydda den delade arbetsboken med Microsoft Excel enligt följande skärmbild. Aspose.Cells stöder också denna funktion med metoderna [**Workbook::ProtectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/protectsharedworkbook/) och [**Workbook::UnprotectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/unprotectsharedworkbook/).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Lösenordsskydda eller upplåsa den delade arbetsboken**

Följande exempelkod skapar en arbetsbok och skyddar den medan du aktiverar delning och sparar den som [utdata Excelfil](55541777.xlsx). På skärmbilden visas det att när du försöker avskydda den, ber Microsoft Excel dig att ange lösenordet för att avskydda den.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty Excel file
    Workbook wb;

    // Protect the Shared Workbook with Password
    wb.ProtectSharedWorkbook(u"1234");

    // Uncomment this line to Unprotect the Shared Workbook
    // wb.UnprotectSharedWorkbook(u"1234");

    // Save the output Excel file
    wb.Save(u"outputProtectSharedWorkbook.xlsx");

    std::cout << "Shared workbook protection applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
