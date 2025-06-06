---  
title: 如何用C++阻止用户打印Excel文件  
linktitle: 如何防止用户打印Excel文件  
type: docs  
weight: 600  
url: /zh/cpp/how-to-prevent-printing-excel/  
description: 了解如何通过Aspose.Cells for C++ API防止用户打印Excel。  
keywords: excel打印、防止excel打印、如何防止用户打印excel、excel防止打印、防止打印工作簿、使用VBA阻止用户打印整个工作簿  
---  

## **可能的使用场景**  
在日常工作中，Excel文件中可能包含一些重要信息；为了防止内部数据传播，公司不会允许我们打印。这份文件将告诉你如何阻止他人打印Excel文件。  

## **如何防止用户在MS-Excel中打印文件**  
您可以应用以下VBA代码以保护您的特定文件不被打印。  
1. 打开您不允许他人打印的工作簿。  
1. 在Excel功能区选择“开发者”标签，然后点击“控件”中的“查看代码”按钮。或者，您可以按下ALT + F11键打开Microsoft Visual Basic for Applications窗口。  
<br>  
<img src="1.png" width=70% />  
1. 然后在左侧的项目资源管理器中，双击ThisWorkbook以打开模块，并添加一些VBA代码。  
<br>  
<img src="2.png" width=70% />  
1. 保存并关闭代码，返回到工作簿，现在当您打印示例文件时，将不允许打印，并会显示以下警告框：  
<br>  
<img src="3.png" width=70% />  

## **如何使用Aspose.Cells for C++阻止用户打印Excel文件**  

以下示例代码说明如何防止用户打印Excel文件：  

1. 加载[示例文件](sample.xlsx)。  
1. 从工作簿的VbaProject属性获取VbaModuleCollection对象。  
1. 通过“ThisWorkbook”名称获取VbaModule对象。  
1. 设置VbaModule的代码属性。  
1. 将示例文件保存为[xlsm格式](out.xlsm)。  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook from existing Excel file
    Workbook workbook(u"Sample.xlsx");

    // Access VBA project modules
    VbaModuleCollection modules = workbook.GetVbaProject().GetModules();

    // Set VBA code for 'ThisWorkbook' module
    modules.Get(u"ThisWorkbook").SetCodes(u"Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n");

    // Save the workbook as macro-enabled Excel file
    workbook.Save(u"out.xlsm");

    std::cout << "VBA code added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
