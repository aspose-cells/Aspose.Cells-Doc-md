---  
title: Узнать, защищен ли проект VBA с помощью C++  
linktitle: Определение, защищен ли проект VBA  
type: docs  
weight: 20  
url: /ru/cpp/find-out-if-vba-project-is-protected/  
description: Проверьте, защищен ли проект VBA файла Excel с помощью Aspose.Cells на C++.  
---  

## **Выясните, защищен ли проект VBA на C++**

Вы можете определить, защищен ли проект VBA (Visual Basic Applications) вашего файла Excel, используя свойство [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/) Aspose.Cells.

## **Образец кода**

Следующий пример создает рабочую книгу и проверяет, защищен ли ее проект VBA, затем защищает проект VBA и снова проверяет, защищен ли его проект VBA. Ознакомьтесь с выводом этой программы в консоли в качестве примера. Перед защитой [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/) возвращает **false**, но после защиты — **true**.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook wb;

    // Access the VBA project of the workbook.
    VbaProject vbaProj = wb.GetVbaProject();

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - Before Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    // Protect the VBA project.
    vbaProj.Protect(true, u"11");

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - After Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Вывод в консоль**

Это вывод консоли приведенного выше образца кода для справки.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
