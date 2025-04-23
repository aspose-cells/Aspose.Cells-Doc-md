---
title: Verifica della password usata per proteggere il foglio di lavoro con C++
linktitle: Verificare la password utilizzata per proteggere il foglio di lavoro
type: docs
weight: 370
url: /it/cpp/verify-password-used-to-protect-the-worksheet/
description: Impara come verificare la password utilizzata per proteggere un foglio di lavoro usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Le API di Aspose.Cells hanno potenziato la classe [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) introducendo alcune proprietà e metodi utili. Uno di questi metodi è il [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) che consente di specificare una password come istanza di *stringa* e verifica se la stessa password è stata utilizzata per proteggere il [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

{{% /alert %}}

Il metodo [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) restituisce **true** se la password specificata corrisponde alla password usata per proteggere il foglio di lavoro dato e **false** se la password specificata non corrisponde. Il seguente esempio di codice utilizza il metodo [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) in combinazione con la proprietà [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) per rilevare la protezione con password e verificare la password.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"Sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        // Verify the password used to protect the Worksheet
        if (sheet.GetProtection().VerifyPassword(u"1234"))
        {
            std::cout << "Specified password has matched" << std::endl;
        }
        else
        {
            std::cout << "Specified password has not matched" << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
