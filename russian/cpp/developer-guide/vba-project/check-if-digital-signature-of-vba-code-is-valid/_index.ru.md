---
title: Проверьте, действителен ли цифровой подпись VBA кода с помощью C++
linktitle: Проверить, действителен ли цифровой подпись кода VBA
type: docs
weight: 120
url: /ru/cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Узнайте, как проверить действительность цифровой подписи в VBA коде, используя Aspose.Cells с C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет проверить, является ли цифровая подпись VBA-кода действительной, используя свойство [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isvalidsigned/). Если подпись действительна, оно вернет **true**, в противном случае — **false**. Цифровая подпись VBA-кода становится недействительной, если вы измените VBA-код.

{{% /alert %}}

## **Проверьте, действительна ли цифровая подпись VBA-кода в C++**

Следующий код демонстрирует использование этого свойства с помощью [пример файла Excel](5115030.xlsm), который можно скачать по предоставленной ссылке. Этот файл Excel имеет действительную подпись, но при изменении его VBA-кода и сохранении рабочей книги подпись становится недействительной.

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
