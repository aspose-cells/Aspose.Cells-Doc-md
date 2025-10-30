---
title: Kontrollera om VBA projektet i en arbetsbok är signerat med C++
linktitle: Kontrollera om VBA projektet i en arbetsbok är signerat
type: docs
weight: 70
url: /sv/cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Kontrollera om VBA projektet i en arbetsbok är signerat med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Du kan kontrollera om ditt VBA-projekt är signerat eller inte med hjälp av Microsoft Excel via menyn **Verktyg > Digitala signaturer...**. På samma sätt kan du programmässigt kontrollera detta med Aspose.Cells [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned).

{{% /alert %}}

## ** Kontrollera om VBA-projekt i en arbetsbok är signerat i C++**

Följande kod laddar arbetsboken och kontrollerar om dess VBA-projekt är signerat med hjälp av [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned)-egenskapen. Egenskapen returnerar **true** om projektet är signerat, annars returnerar den **false**.

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
    U16String sampleFilePath = srcDir + u"Sample1.xlsx";

    // Create workbook
    Workbook workbook(sampleFilePath);

    // Check if the VBA project is signed
    bool isSigned = workbook.GetVbaProject().IsSigned();
    std::wcout << u"VBA Project is Signed: " << (isSigned ? u"true" : u"false") << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
