---
title: Rimuovere le righe duplicate in un foglio di lavoro con C++
linktitle: Rimuovere righe duplicate in un foglio di lavoro
type: docs
weight: 370
url: /it/cpp/remove-duplicate-rows-in-a-worksheet/
description: Impara come rimuovere le righe duplicate in un foglio di lavoro usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Rimuovere righe duplicate è una delle molte funzioni utili di Microsoft Excel. Permette agli utenti di eliminare le righe duplicate in un foglio di lavoro, e puoi scegliere quali colonne devono essere controllate per informazioni duplicate.

Aspose.Cells offre il metodo `Cells::RemoveDuplicates()` per questo scopo. Puoi anche impostare `startRow`, `startColumn`, `endRow` e `endColumn` per selezionare le colonne.

Di seguito sono riportati i file di esempio che possono essere scaricati per testare questa funzionalità:

[removeduplicates.xlsx](removeduplicates.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook book(u"removeduplicates.xlsx");

    // Remove duplicates from the first worksheet
    book.GetWorksheets().Get(0).GetCells().RemoveDuplicates(0, 0, 5, 3);

    // Save the result
    book.Save(u"removeduplicates-result.xlsx");

    std::cout << "Duplicates removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
