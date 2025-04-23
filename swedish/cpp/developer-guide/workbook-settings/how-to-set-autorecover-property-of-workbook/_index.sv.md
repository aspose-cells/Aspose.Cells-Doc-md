---
title: Hur man ställer in AutoRecover egenskapen för arbetsbok med C++
linktitle: Hur man ställer in egenskapen AutoRecover för arbetsboken
type: docs
weight: 220
url: /sv/cpp/how-to-set-autorecover-property-of-workbook/
description: Lär dig hur du aktiverar eller inaktiverar AutoRecover egenskapen för en arbetsbok med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att ställa in AutoRecover-egenskapen för en arbetsbok. Standardvärdet för denna egenskap är **true**. När du ställer in den till **false** inaktiverar Microsoft Excel AutoRecover (Autospara) för den Excel-filen.

Aspose.Cells tillhandahåller egenskapen [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) för att aktivera eller inaktivera detta alternativ.

{{% /alert %}}

Följande kod förklarar hur man använder [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/)-egenskapen för arbetsboken. Koden läser först standardvärdet för denna egenskap, vilket är **true**, ändrar den till **false** och sparar arbetsboken. Därefter läser den arbetsboken igen och hämtar värdet av denna egenskap, vilket är **false** nu.

## C++ kod för att ställa in AutoRecover-egenskapen för arbetsbok

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook.GetSettings().GetAutoRecover() << std::endl;

    // Set AutoRecover property to false
    workbook.GetSettings().SetAutoRecover(false);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    // Read the saved workbook again
    Workbook workbook2(outDir + u"output_out.xlsx");

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook2.GetSettings().GetAutoRecover() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Output**

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
