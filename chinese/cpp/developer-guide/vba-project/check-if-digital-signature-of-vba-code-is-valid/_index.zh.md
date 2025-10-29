---
title: 用C++检查VBA代码的数字签名是否有效
linktitle: 检查VBA代码的数字签名是否有效
type: docs
weight: 120
url: /zh/cpp/check-if-digital-signature-of-vba-code-is-valid/
description: 学习如何用Aspose.Cells在C++中检查VBA代码的数字签名的有效性。
---

{{% alert color="primary" %}}

Aspose.Cells允许你使用[**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isvalidsigned/)属性检查VBA代码数字签名是否有效。如果验证通过，返回**true**；否则返回**false**。当你修改VBA代码后，数字签名会失效。

{{% /alert %}}

## **用C++检查VBA代码的数字签名是否有效**

以下代码演示了如何使用[示例Excel文件](5115030.xlsm)测试此属性。该Excel文件有有效签名，但修改其VBA代码后，保存并重新检测时，签名变得无效。

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
