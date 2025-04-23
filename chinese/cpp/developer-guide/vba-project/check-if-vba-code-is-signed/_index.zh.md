---  
title: 用C++检查VBA代码是否签名  
linktitle: 检查VBA代码是否已签名  
type: docs  
weight: 100  
url: /zh/cpp/check-if-vba-code-is-signed/  
description: 学习如何用Aspose.Cells在C++中检查Excel文件中的VBA代码是否已签名。  
---  

{{% alert color="primary" %}}  

Aspose.Cells允许用户检查VBA代码项目是否已签名。请使用[**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/)属性进行检测。  

{{% /alert %}}  

以下代码说明如何用[**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/)属性检测VBA代码是否已签名。你可以用任何Excel文件测试此代码，也可以用[此示例文件](5115032.xlsm)。  

## **用C++检查VBA代码是否签名**  

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Check if the VBA code project is signed
    std::wcout << U"Is VBA Code Project Signed: " << workbook.GetVbaProject().IsSigned() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  

## 控制台输出  

以下是上述代码的控制台输出，使用链接提供的[示例Excel文件](5115032.xlsm)。  

{{< highlight java >}}  

Is VBA Code Project Signed: True  

{{< /highlight >}}  
