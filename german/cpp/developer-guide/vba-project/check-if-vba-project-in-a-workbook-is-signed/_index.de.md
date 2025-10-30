---
title: Überprüfen, ob das VBA Projekt in einer Arbeitsmappe mit C++ signiert ist
linktitle: Überprüfen, ob das VBA Projekt in einer Arbeitsmappe signiert ist
type: docs
weight: 70
url: /de/cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Überprüfen, ob das VBA Projekt in einer Arbeitsmappe mit Aspose.Cells und C++ signiert ist.
---

{{% alert color="primary" %}}

Sie können überprüfen, ob Ihr VBA-Projekt mit Microsoft Excel signiert ist, über das Menü **Tools > Digitale Signaturen...**. Ebenso können Sie es programmatisch mit Aspose.Cells [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned) überprüfen.

{{% /alert %}}

## **Überprüfen, ob das VBA-Projekt in einer Arbeitsmappe in C++ signiert ist**

Der folgende Code lädt die Arbeitsmappe und überprüft, ob ihr VBA-Projekt mit der [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned)-Eigenschaft signiert ist. Die Eigenschaft gibt **true** zurück, wenn das Projekt signiert ist, andernfalls **false**.

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
