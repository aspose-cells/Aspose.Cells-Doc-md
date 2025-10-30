---
title: C++ ile VBA Kodunun Dijital İmza Geçerliğini Kontrol Edin
linktitle: VBA Kodunun Dijital İmzasının Geçerli Olup Olmadığını Kontrol Et
type: docs
weight: 120
url: /tr/cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Aspose.Cells kullanarak VBA kodunun dijital imzasının geçerli olup olmadığını VBA kodunun geçerliliğini kontrol etmek için nasıl kullanılacağını öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, VBA kodunun dijital imzasının geçerliliğini [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isvalidsigned/) özelliği kullanarak kontrol etmenizi sağlar. İmza geçerliyse **true**, değilse **false** döner. VBA kodu değiştirildiğinde dijital imza geçersiz hale gelir.

{{% /alert %}}

## **C++ ile VBA Kodunun Dijital İmzasının Geçerli olup olmadığını Kontrol Edin**

 Aşağıdaki kod, sağlanan bağlantıdan indirilebilir [örnek excel dosyasıyla](5115030.xlsm) kullanımını gösterir. Aynı Excel dosyasının geçerli bir imzası vardır, fakat VBA kodunu değiştirdiğimizde ve çalışma kitabını kaydettiğimizde, imzası geçersiz hale gelir.

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
