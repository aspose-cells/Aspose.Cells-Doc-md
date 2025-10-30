---
title: Verifica password per modificare usando Aspose.Cells con C++
linktitle: Verifica password per modificare
type: docs
weight: 2400
url: /it/cpp/check-password-to-modify-using-aspose-cells/
description: Verifica se la password fornita corrisponde alla Password per modificare usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte, è necessario controllare programmaticamente se la password fornita corrisponde alla **Password per modificare**. Aspose.Cells fornisce il metodo WorkbookSettings.WriteProtection.ValidatePassword() che può essere usato per verificare se la Password per modificare è corretta oppure no.

{{% /alert %}}

## **Verificare la password per modificare in Microsoft Excel**

È possibile assegnare **Password per aprire** e **Password per modificare** durante la creazione dei propri workbook in Microsoft Excel. Si prega di vedere questa schermata che mostra l'interfaccia fornita da Microsoft Excel per specificare queste password.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Controllare la password per la modifica utilizzando Aspose.Cells**

I seguenti codici di esempio caricano il [file Excel di origine](5112232.xlsx). Ha una Password per aprire come 1234 e una Password per modificare come 5678. Il codice prima verifica se 567 è la Password per modificare corretta e restituisce false e poi verifica se 5678 è la Password per modificare e restituisce true.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleBook.xlsx";

    // Specify password to open inside the load options
    LoadOptions opts;
    opts.SetPassword(u"1234");

    // Open the source Excel file with load options
    Workbook workbook(inputFilePath, opts);

    // Check if "567" is the password to modify
    bool ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"567");
    std::wcout << L"Is 567 correct Password to modify: " << ret << std::endl;

    // Check if "5678" is the password to modify
    ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"5678");
    std::wcout << L"Is 5678 correct Password to modify: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Output della console**

Ecco l'output della console del codice di esempio precedente dopo aver caricato il [file Excel di origine](5112232.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
