---  
title: 使用Aspose.Cells用C++创建共享工作簿  
linktitle: 使用Aspose.Cells创建共享工作簿  
type: docs  
weight: 40  
url: /zh/cpp/create-shared-workbook-with-aspose-cells/  
description: 学习如何使用Aspose.Cells和C++创建共享工作簿。  
---  

## **可能的使用场景**  

Microsoft Excel允许您像在以下截图中所示共享工作簿。当您共享工作簿时，多个用户可以在网络上编辑此工作簿。Aspose.Cells使您能够使用[**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/)属性创建共享工作簿。  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **使用Aspose.Cells创建共享工作簿**  

以下示例代码通过将[**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/)属性设置为**true**，创建一个共享工作簿。当您在Microsoft Excel中打开[输出Excel文件](55541786.xlsx)时，您将看到**共享**与输出工作簿的名称，如截图所示。  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **示例代码**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create Workbook object
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>();

    // Share the Workbook
    wb->GetSettings().SetShared(true);

    // Save the Shared Workbook
    wb->Save(u"outputSharedWorkbook.xlsx");

    std::cout << "Shared workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
