---
title: Proteggi e Sblocca la Struttura del Workbook con C++
linktitle: Proteggere e Difendere la Struttura del Workbook
type: docs
weight: 40
url: /it/cpp/protect-and-unprotect-workbook-structure/
description: Proteggi e sblocca la struttura del workbook di file Excel usando C++ con Aspose.Cells.
---

{{% alert color="primary" %}}
Per impedire ad altri utenti di visualizzare i fogli di lavoro nascosti, aggiungere, spostare, eliminare o nascondere fogli di lavoro e rinominare fogli di lavoro, è possibile proteggere la struttura del proprio foglio di lavoro di Excel con una password.
{{% /alert %}}

## **Proteggi e Sblocca la Struttura del Workbook in MS Excel**

**![proteggere e difendere la struttura del workbook](proteggere-e-difendere-la-struttura-del-workbook.png)**

1. Fare clic su **Revisione > Proteggi Cartella di Lavoro**.
1. Inserire una password nella **casella di Password**.
1. Selezionare **OK**, reinserire la password per confermarla e quindi selezionare di nuovo **OK**.

## **Proteggi la Struttura del Workbook usando Aspose.Cells for C++**
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

    // Protect workbook structure with a password
    workbook.Protect(ProtectionType::Structure, u"password");

    // Save the workbook to a file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sblocca la Struttura del Workbook usando Aspose.Cells for C++**
Sbloccare la struttura del workbook è semplice con l'API Aspose.Cells.

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
Nota: è necessaria una password corretta.
{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
