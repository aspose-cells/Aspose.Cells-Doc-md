---
title: Проверьте, подписан ли VBA проект в рабочей книге с помощью C++
linktitle: Проверка подписан ли проект VBA в книге Excel
type: docs
weight: 70
url: /ru/cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Проверьте, подписан ли VBA проект в рабочей книге с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Вы можете проверить, подписан ли ваш VBA-проект или нет, используя Microsoft Excel через меню **Инструменты > Цифровые подписи...**. Аналогично, это можно сделать программно с помощью Aspose.Cells [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned).

{{% /alert %}}

## **Проверьте, подписан ли VBA-проект в рабочей книге с помощью C++**

Следующий код загружает рабочую книгу и проверяет, подписан ли VBA-проект с помощью свойства [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned). Свойство вернет **true**, если проект подписан, иначе — **false**.

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
