---  
title: 使用C++检测VBA项目是否受保护  
linktitle: 查看 VBA 项目是否已受保护  
type: docs  
weight: 20  
url: /zh/cpp/find-out-if-vba-project-is-protected/  
description: 利用Aspose.Cells与C++检测Excel文件的VBA项目是否受保护。  
---  

## **用C++检测VBA项目是否受保护**

你可以使用[**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/)属性，判断Excel文件中的VBA（Visual Basic for Applications）项目是否被保护。

## **示例代码**

以下示例代码创建一个工作簿，然后检测其VBA项目是否受保护，然后保护此VBA项目，再次检测。请查看控制台输出作为参考。在保护前，[**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/)返回**false**，保护后返回**true**。

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

## **控制台输出**

这是上述示例代码的控制台输出供参考。

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
{{< app/cells/assistant language="cpp" >}}
