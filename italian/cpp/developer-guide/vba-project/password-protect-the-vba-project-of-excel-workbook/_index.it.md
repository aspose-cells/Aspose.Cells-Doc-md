---
title: Proteggi con password il progetto VBA del workbook Excel con C++
linktitle: Proteggi con password il progetto VBA del workbook di Excel
type: docs
weight: 10
url: /it/cpp/password-protect-the-vba-project-of-excel-workbook/
description: Impara come proteggere con password il progetto VBA di un workbook Excel utilizzando Aspose.Cells con C++.
---

## **Proteggi con password il progetto VBA di un workbook Excel in C++**

Puoi proteggere con password il progetto VBA (Visual Basic Applications) di un workbook con Aspose.Cells utilizzando il metodo [**VbaProject.Protect()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/protect/).

## **Codice di Esempio**

Il seguente esempio di codice carica il [file Excel di esempio](43352067.xlsm), accede al suo progetto VBA e lo protegge con una password. Infine, lo salva come [file Excel di output](43352068.xlsm).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"samplePasswordProtectVBAProject.xlsm";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outputPasswordProtectVBAProject.xlsm";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Lock the VBA project for viewing with password
    vbaProject.Protect(true, u"11");

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "VBA project password protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
