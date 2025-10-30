---
title: Skydda och avskydda kalkylblad med C++
linktitle: Skydda och avskydda kalkylblad
type: docs
weight: 40
url: /sv/cpp/protect-and-unprotect-worksheets/
description: Skydda och avskaffa kalkylblad i Excel filer med Aspose.Cells for C++.
---

{{% alert color="primary" %}}
För att förhindra att andra användare avsiktligt eller oavsiktligt ändrar, flyttar eller tar bort data i ett kalkylblad kan du låsa cellerna i ditt Excel-kalkylblad och sedan skydda kalkylbladet med ett lösenord. 
{{% /alert %}}

## **Skydda och avskydda kalkylblad i MS Excel**

**![skydda och avskydda Arbetsblad](skydda-och-avskydda-arbetsblad.png)**

1. Klicka på **Översikt > Skydda arbetsblad**.
1. Ange ett lösenord i **Lösenordsrutan**.
1. Välj **tillåt** alternativ.
1. Välj **OK**, ange lösenordet igen för att bekräfta det, och välj sedan **OK** igen.

## **Skydda kalkylblad med Aspose.Cells for C++**
Bara behöver följande enkla koder för att implementera skydd av arbetsbokens struktur för Excel-filer.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Protect contents of the worksheet
    sheet.Protect(ProtectionType::Contents);

    // Protect worksheet with password
    sheet.GetProtection().SetPassword(u"test");

    // Save as Excel file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Avskydda kalkylblad med Aspose.Cells for C++**
Avsökning av arbetsblad är enkel med Aspose.Cells API. Om arbetsbladet är lösenordsskyddat krävs ett korrekt lösenord.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet with password
    sheet.Unprotect(u"password");

    // Save the workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Worksheet unprotected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortsatta ämnen**
- [Avancerade skyddsinställningar sedan Excel XP](/cells/sv/cpp/advanced-protection-settings-since-excel-xp/)
- [Upptäck om arbetsbladet är lösenordsskyddat](/cells/sv/cpp/detect-if-worksheet-is-password-protected/)
- [Skydda kalkylblad](/cells/sv/cpp/protecting-worksheets/)
- [Avskydda ett kalkylblad](/cells/sv/cpp/unprotect-a-worksheet/)
- [Verifiera lösenord som används för att skydda arbetsbladet](/cells/sv/cpp/verify-password-used-to-protect-the-worksheet/)
{{< app/cells/assistant language="cpp" >}}
