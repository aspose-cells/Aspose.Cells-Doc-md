---
title: Kontrollera lösenord för att ändra med Aspose.Cells och C++
linktitle: Kontrollera lösenord för att ändra
type: docs
weight: 2400
url: /sv/cpp/check-password-to-modify-using-aspose-cells/
description: Kontrollera om det angivna lösenordet matchar lösenordet för att ändra med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Ibland måste du kontrollera om det angivna lösenordet matchar **lösenordet för att ändra** programmässigt. Aspose.Cells erbjuder metoden WorkbookSettings.WriteProtection.ValidatePassword() som du kan använda för att kontrollera om det angivna lösenordet är korrekt eller inte.

{{% /alert %}}

## **Kontrollera lösenord för modifiering i Microsoft Excel**

Du kan tilldela **Lösenord för att öppna** och **Lösenord för att modifiera** när du skapar dina arbetsböcker i Microsoft Excel. Se denna skärmbild som visar gränssnittet som Microsoft Excel tillhandahåller för att ange dessa lösenord.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Kontrollera lösenord för modifiering med Aspose.Cells**

Följande kodexempel laddar den [käll-Excel-filen](5112232.xlsx). Den har ett Lösenord för att öppna som 1234 och ett Lösenord för att modifiera som 5678. Koden kontrollerar först om 567 är korrekt lösenord för modifiering och returnerar falskt och sedan kontrollerar den om 5678 är lösenord för modifiering och det returnerar sant.

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

### **Konsoloutput**

Här är konsolens utmatning av ovanstående kod efter att ha laddat den [käll-Excel-filen](5112232.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
