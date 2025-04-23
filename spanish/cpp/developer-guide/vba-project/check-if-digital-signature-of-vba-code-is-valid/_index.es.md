---
title: Verifica si la firma digital del código VBA es válida con C++
linktitle: Verifica si la Firma Digital del Código VBA es Válida
type: docs
weight: 120
url: /es/cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Aprende cómo verificar la validez de una firma digital en el código VBA usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells te permite verificar si la firma digital del código VBA es válida usando la propiedad [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isvalidsigned/). Retornará **true** si la firma es válida; de lo contrario, retornará **false**. La firma digital del código VBA se vuelve inválida cuando cambias el código VBA.

{{% /alert %}}

## **Verifica si la firma digital del código VBA es válida en C++**

El siguiente código demuestra el uso de esta propiedad con el [archivo de Excel de ejemplo](5115030.xlsm) que puedes descargar del enlace proporcionado. El mismo archivo de Excel tiene una firma válida, pero cuando modificamos su código VBA y guardamos el libro de trabajo y luego volvemos a verificar, encontramos que su firma se volvió inválida.

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
