---
title: Check if Digital Signature of VBA Code is Valid with C++
linktitle: Check if Digital Signature of VBA Code is Valid
type: docs
weight: 120
url: /cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Learn how to check the validity of a digital signature in VBA code using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

Aspose.Cells allows you to check if the digital signature of the VBA code is valid using the [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isvalidsigned/) property. It will return **true** if the signature is valid; otherwise, it will return **false**. The digital signature of the VBA code becomes invalid when you change the VBA code.

{{% /alert %}}

## **Check if Digital Signature of VBA Code is Valid in C++**

The following code demonstrates the usage of this property using the [sample excel file](5115030.xlsm) which you can download from the provided link. The same Excel file has a valid signature, but when we modify its VBA code and save the workbook and then recheck, we find its signature has become invalid.

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
{{< app/cells/assistant language="cpp" >}}