---
title: Verifica se il progetto VBA in un Workbook è Firmato con C++
linktitle: Verifica se il progetto VBA in un workbook è firmato
type: docs
weight: 70
url: /it/cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Verifica se il progetto VBA in un Workbook è Firmato usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Puoi verificare se il tuo progetto VBA è firmato o meno usando Microsoft Excel tramite il comando del menu **Strumenti > Firma Digitale...**. Allo stesso modo, puoi verificarlo programmaticamente usando Aspose.Cells [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned).

{{% /alert %}}

## **Verifica se il progetto VBA in un Workbook è Firmato in C++**

Il seguente esempio di codice carica il workbook e verifica se il suo progetto VBA è firmato usando la proprietà [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned). La proprietà restituirà **true** se il progetto è firmato, altrimenti restituirà **false**.

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
