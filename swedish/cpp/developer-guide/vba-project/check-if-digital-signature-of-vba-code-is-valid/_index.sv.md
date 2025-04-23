---
title: Kontrollera om digital signatur av VBA koden är giltig med C++
linktitle: Kontrollera om den digitala signaturen av VBA koden är giltig
type: docs
weight: 120
url: /sv/cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Lär dig hur du kontrollerar giltigheten av en digital signatur i VBA kod med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att kontrollera om den digitala signaturen för VBA-koden är giltig med hjälp av [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isvalidsigned/)-egenskapen. Den returnerar **true** om signaturen är giltig; annars returnerar den **false**. Den digitala signaturen för VBA-koden blir ogiltig när du ändrar VBA-koden.

{{% /alert %}}

## **Kontrollera om digital signatur av VBA-koden är giltig i C++**

 Följande kod demonstrerar användningen av denna egenskap med [exempel-Excelfilen](5115030.xlsm) som du kan ladda ner från länken. Samma Excel-fil har en giltig signatur, men när vi ändrar dess VBA-kod och sparar arbetsboken och sedan kontrollerar igen, konstaterar vi att dess signatur har blivit ogiltig.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the workbook from an existing Excel file with VBA project
    Workbook workbook(srcDir + u"sampleVBAProjectSigned.xlsm");

    // Check if the VBA Code Project is valid signed
    std::cout << "Is VBA Code Project Valid Signed: " << (workbook.GetVbaProject().IsValidSigned() ? "True" : "False") << std::endl;

    // Modify the VBA Code
    U16String code = workbook.GetVbaProject().GetModules().Get(1).GetCodes();
    code = u"Welcome to Aspose.Cells"; // Directly setting new code here
    workbook.GetVbaProject().GetModules().Get(1).SetCodes(code);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsm");

    // Reload the workbook
    workbook = Workbook(srcDir + u"output_out.xlsm");

    // Now the signature is invalid
    std::cout << "Is VBA Code Project Valid Signed: " << (workbook.GetVbaProject().IsValidSigned() ? "True" : "False") << std::endl;

    Aspose::Cells::Cleanup();
}
```
