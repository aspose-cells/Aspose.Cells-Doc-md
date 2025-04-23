---
title: Frigör olägliga resurser för arbetsboken med C++
linktitle: Frigör ohanterade resurser i arbetsboken
type: docs
weight: 310
url: /sv/cpp/release-unmanaged-resources-of-the-workbook/
description: Lär dig hur du frigör olägliga resurser för arbetsboken med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) metoden för att frigöra ohanterade resurser från [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objektet. Dispose-mönstret används endast för objekt som har åtkomst till ohanterade resurser, såsom fil- och rörhandtag, registerhandtag, väntehandtag eller pekare till block av ohanterat minne. Detta beror på att sop samlaren är mycket effektiv på att ta tillbaka oanvända hanterade objekt, men den kan inte ta tillbaka ohanterade objekt.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-objektet implementerar nu *IDisposable*-gränssnittet som har en enda metod [**Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/). Du kan antingen direkt anropa [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/)-metoden eller använda *Using*-satset för att automatiskt anropa denna metod.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb1;

    // Call Dispose method
    wb1.Dispose();

    // Call Dispose method via RAII (Resource Acquisition Is Initialization)
    {
        Workbook wb2;
        // Any other code goes here
    } // wb2 is automatically disposed when it goes out of scope

    Aspose::Cells::Cleanup();
}
```
