---
title: Überprüfen, ob die Digitale Signatur des VBA Codes mit C++ gültig ist
linktitle: Prüfen, ob die digitale Signatur des VBA Codes gültig ist
type: docs
weight: 120
url: /de/cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Erfahren Sie, wie Sie die Gültigkeit einer digitalen Signatur in VBA Code mithilfe von Aspose.Cells mit C++ überprüfen.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es, zu überprüfen, ob die digitale Signatur des VBA-Codes mit der [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isvalidsigned/)-Eigenschaft gültig ist. Es gibt **true** zurück, wenn die Signatur gültig ist; andernfalls gibt es **false** zurück. Die digitale Signatur des VBA-Codes wird ungültig, wenn Sie den VBA-Code ändern.

{{% /alert %}}

## **Überprüfen, ob die Digitale Signatur des VBA-Codes in C++ gültig ist**

Der folgende Code demonstriert die Verwendung dieser Eigenschaft anhand der [Beispiel-Excel-Datei](5115030.xlsm), die Sie über den bereitgestellten Link herunterladen können. Die gleiche Excel-Datei hat eine gültige Signatur, aber wenn wir ihren VBA-Code ändern, die Arbeitsmappe speichern und erneut überprüfen, stellen wir fest, dass ihre Signatur ungültig geworden ist.

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
