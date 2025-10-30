---
title: Accedi alla Text Box tramite il Nome con C++
linktitle: Accedere alla casella di testo per nome
type: docs
weight: 230
url: /it/cpp/access-the-text-box-by-the-name/
description: Impara come accedere a una text box tramite il suo nome usando Aspose.Cells for C++.
---

## Accedere alla casella di testo per nome

In passato, le caselle di testo erano accessibili tramite indice dalla collezione [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/), ma ora puoi anche accedere alla casella di testo per nome da questa collezione. Questo metodo è comodo e rapido se conosci già il suo nome.

Il seguente esempio di codice crea prima una text box e le assegna del testo e un nome. Successivamente, nelle righe successive, accediamo alla stessa text box tramite il suo nome e stampiamo il suo testo.

### Codice C++ per accedere alla text box tramite nome

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    int idx = sheet.GetTextBoxes().Add(10, 10, 10, 10);

    // Access newly created TextBox using its index & name it
    TextBox tb1 = sheet.GetTextBoxes().Get(idx);
    tb1.SetName(u"MyTextBox");

    // Set text for the TextBox
    tb1.SetText(u"This is MyTextBox");

    // Access the same TextBox via its name
    TextBox tb2 = sheet.GetTextBoxes().Get(u"MyTextBox");

    // Display the text of the TextBox accessed via name
    std::cout << tb2.GetText().ToUtf8() << std::endl;

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
}
```

### Uscita della console generata dal codice di esempio

Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
