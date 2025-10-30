---
title: Protetto o Sblocca il workbook condiviso con C++
linktitle: Proteggere o sbloccare la cartella di lavoro condivisa
type: docs
weight: 10
url: /it/cpp/password-protect-or-unprotect-the-shared-workbook/
description: Impara come proteggere con password o sbloccare un workbook condiviso usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

È possibile proteggere o sbloccare la cartella di lavoro condivisa con Microsoft Excel come mostrato nella seguente schermata. Aspose.Cells supporta anche questa funzionalità con i metodi [**Workbook::ProtectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/protectsharedworkbook/) e [**Workbook::UnprotectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/unprotectsharedworkbook/).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Proteggi o rimuovi la protezione con password dalla cartella di lavoro condivisa**

Il seguente codice di esempio crea una cartella di lavoro e la protegge abilitando la condivisione, quindi la salva come [file Excel di output](55541777.xlsx). La schermata mostra che quando si tenta di sbloccarla, Microsoft Excel richiede di inserire la password per sbloccarla.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Codice di Esempio**

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
