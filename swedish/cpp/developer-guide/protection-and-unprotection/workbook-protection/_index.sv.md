---
title: Skydda och avskydda arbetsboksstrukturen med C++
linktitle: Skydda och avskydda arbetsbokens struktur
type: docs
weight: 40
url: /sv/cpp/protect-and-unprotect-workbook-structure/
description: Skydda och avsäkerställ arbetsboksstrukturen i Excel filer med C++ och Aspose.Cells.
---

{{% alert color="primary" %}}
För att förhindra att andra användare ser dolda kalkylblad, lägger till, flyttar, tar bort eller gömmer kalkylbladen, och döper om kalkylbladen, kan du skydda strukturen för din Excel-arbetsbok med ett lösenord.
{{% /alert %}}

## **Skydda och avskydda arbetsboksstrukturen i MS Excel**

**![skydda och avskydda arbetsbokens struktur](skydda-och-avskydda-arbetsbokens-struktur.png)**

1. Klicka på **Granska > Skydda arbetsbok**.
1. Ange ett lösenord i **Lösenordsrutan**.
1. Välj **OK**, ange lösenordet igen för att bekräfta det, och välj sedan **OK** igen.

## **Skydda arbetsboksens struktur med Aspose.Cells for C++**
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

    // Protect workbook structure with a password
    workbook.Protect(ProtectionType::Structure, u"password");

    // Save the workbook to a file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Avskydda arbetsboksstrukturen med Aspose.Cells for C++**
Det är enkelt att avskydda arbetsbokens struktur med Aspose.Cells API.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open an Excel file which workbook structure is protected.
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Unprotect workbook structure.
    workbook.Unprotect(u"password");

    // Save Excel file.
    workbook.Save(inputFilePath);

    std::cout << "Workbook structure unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}
Observera: Ett korrekt lösenord krävs.
{{% /alert %}}
