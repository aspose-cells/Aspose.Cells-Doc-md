---
title: Verifica se la Firma Digitale del Codice VBA è Valida con C++
linktitle: Verifica se la Firma Digitale del Codice VBA è Valida
type: docs
weight: 120
url: /it/cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Impara come verificare la validità di una firma digitale nel codice VBA usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells ti permette di verificare se la firma digitale del codice VBA è valida usando la proprietà [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isvalidsigned/). Restituirà **true** se la firma è valida; altrimenti, restituirà **false**. La firma digitale del codice VBA diventa invalida quando si modifica il codice VBA.

{{% /alert %}}

## **Verifica se la Firma Digitale del Codice VBA è Valida in C++**

Il seguente esempio di codice dimostra l’uso di questa proprietà utilizzando il [file Excel di esempio](5115030.xlsm) che puoi scaricare dal link fornito. Lo stesso file Excel ha una firma valida, ma quando modifichiamo il suo codice VBA e salviamo il workbook, poi lo rifacciamo controllare, troviamo che la firma è diventata invalida.

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
