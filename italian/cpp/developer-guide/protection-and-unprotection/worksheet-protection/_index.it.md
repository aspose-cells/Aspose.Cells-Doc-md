---
title: Proteggi e Sblocca il Foglio di Lavoro con C++
linktitle: Proteggere e Difendere il Foglio di Lavoro
type: docs
weight: 40
url: /it/cpp/protect-and-unprotect-worksheets/
description: Proteggi e sblocca il foglio di lavoro di file Excel con Aspose.Cells for C++.
---

{{% alert color="primary" %}}
Per impedire ad altri utenti di modificare, spostare o eliminare accidentalmente o deliberatamente i dati in un foglio di lavoro, è possibile bloccare le celle nel foglio di lavoro di Excel e quindi proteggere il foglio con una password. 
{{% /alert %}}

## **Proteggi e Sblocca il Foglio di Lavoro in MS Excel**

**![proteggere e proteggere il foglio di lavoro](protect-and-unprotect-worksheet.png)**

1. Fare clic su **Revisione > Proteggi foglio di lavoro**.
1. Inserire una password nella **casella di Password**.
1. Selezionare le opzioni **consenti**.
1. Selezionare **OK**, reinserire la password per confermarla e quindi selezionare di nuovo **OK**.

## **Proteggi il Foglio di Lavoro usando Aspose.Cells for C++**
È sufficiente utilizzare le seguenti linee di codice per implementare la protezione della struttura della cartella di lavoro dei file di Excel.

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

## **Sblocca il Foglio di Lavoro usando Aspose.Cells for C++**
Sbloccare un foglio di lavoro è facile con l'API Aspose.Cells. Se il foglio di lavoro è protetto da password, è necessaria una password corretta.

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

## **Argomenti avanzati**
- [Impostazioni di protezione avanzate da Excel XP in poi](/cells/it/cpp/advanced-protection-settings-since-excel-xp/)
- [Verificare se il foglio di lavoro è protetto da password](/cells/it/cpp/detect-if-worksheet-is-password-protected/)
- [Protezione dei fogli di lavoro](/cells/it/cpp/protecting-worksheets/)
- [Sblocca un foglio di lavoro](/cells/it/cpp/unprotect-a-worksheet/)
- [Verificare la password utilizzata per proteggere il foglio di lavoro](/cells/it/cpp/verify-password-used-to-protect-the-worksheet/)
{{< app/cells/assistant language="cpp" >}}
