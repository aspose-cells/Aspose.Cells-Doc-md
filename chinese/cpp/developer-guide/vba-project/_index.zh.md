---
title: 用C++管理Excel宏启用工作簿的VBA代码
linktitle: 宏项目
type: docs
weight: 200
url: /zh/cpp/manage-vba-project/
description: 在C++中添加VBA模块并修改VBA或宏，使用Aspose.Cells库。
---

## **在C++中添加VBA模块**
{{% alert color="primary" %}}

Aspose.Cells允许通过Aspose.Cells添加新的VBA模块和宏代码。请使用[**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/add/)方法在工作簿中添加新的VBA模块。

{{% /alert %}}

以下示例代码创建一个新工作簿，添加一个VBA模块和宏代码，并以XLSM格式保存。打开输出的XLSM文件在Microsoft Excel中，点击*开发人员 > Visual Basic*菜单命令，你会看到名为"TestModule"的模块，里面有以下宏代码。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

以下是生成带有VBA模块和宏代码的输出XLSM文件的示例代码。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add VBA Module
    int32_t idx = workbook.GetVbaProject().GetModules().Add(worksheet);

    // Access the VBA Module, set its name and codes
    VbaModule module = workbook.GetVbaProject().GetModules().Get(idx);
    module.SetName(u"TestModule");

    U16String codes = u"Sub ShowMessage()\r\n"
                      u"    MsgBox \"Welcome to Aspose!\"\r\n"
                      u"End Sub";
    module.SetCodes(codes);

    // Save the workbook
    U16String outputPath = outDir + u"output_out.xlsm";
    workbook.Save(outputPath, SaveFormat::Xlsm);

    std::cout << "VBA module added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **在C++中修改VBA或宏**

{{% alert color="primary" %}} 

您可以使用Aspose.Cells修改VBA或宏代码。Aspose.Cells已添加以下名称空间和类来读取和修改Excel文件中的VBA项目。

- Aspose::Cells::Vba
- VbaProject
- VbaModuleCollection
- VbaModule

本文将向您展示如何使用Aspose.Cells更改源Excel文件中的VBA或宏代码。

{{% /alert %}} 

以下示例代码加载含有VBA或宏代码的源Excel文件：

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

经过Aspose.Cells示例代码执行后，VBA或宏代码将被修改成这样：

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

您可以从以下链接下载[源Excel文件](5112508.xlsm)和[输出Excel文件](5112511.xlsm)。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"sample.xlsm";
    U16String outputFilePath = outDir + u"output_out.xlsm";

    Workbook workbook(inputFilePath);

    VbaProject vbaProject = workbook.GetVbaProject();
    VbaModuleCollection modules = vbaProject.GetModules();

    for (int i = 0; i < modules.GetCount(); ++i)
    {
        VbaModule module = modules.Get(i);
        U16String code = module.GetCodes();
        U16String searchStr = u"This is test message.";
        U16String replaceStr = u"This is Aspose.Cells message.";

        if (code.IndexOf(searchStr) != -1)
        {
            U16String newCode;
            const char16_t* codeData = code.GetData();
            const char16_t* searchData = searchStr.GetData();
            int codeLen = code.GetLength();
            int searchLen = searchStr.GetLength();

            int pos = 0;
            int searchPos;

            while ((searchPos = code.IndexOf(searchStr)) != -1)
            {
                for (int j = pos; j < searchPos; j++)
                {
                    newCode += codeData[j];
                }

                newCode += replaceStr;

                pos = searchPos + searchLen;
            }

            for (int j = pos; j < codeLen; j++)
            {
                newCode += codeData[j];
            }

            module.SetCodes(newCode);
        }
    }

    workbook.Save(outputFilePath);

    std::cout << "VBA module codes updated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **高级主题**
- [在工作簿中添加VBA项目库引用](/cells/zh/cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [将宏分配给窗体控件](/cells/zh/cpp/assign-macro-to-form-control/)
- [检查VBA代码的数字签名是否有效](/cells/zh/cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [检查VBA代码是否已签名](/cells/zh/cpp/check-if-vba-code-is-signed/)
- [检查工作簿中的VBA项目是否已签名](/cells/zh/cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [检查VBA项目是否受保护并锁定以供查看](/cells/zh/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [将VBA宏用户表单DesignerStorage从模板复制到目标工作簿](/cells/zh/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [使用证书对VBA代码项目进行数字签名](/cells/zh/cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [将VBA证书导出到文件或流](/cells/zh/cpp/export-vba-certificate-to-file-or-stream/)
- [在加载工作簿时筛选VBA项目](/cells/zh/cpp/filter-vba-project-while-loading-a-workbook/)
- [查找VBA项目是否受保护](/cells/zh/cpp/find-out-if-vba-project-is-protected/)
- [为Excel工作簿的VBA项目设置密码保护](/cells/zh/cpp/password-protect-the-vba-project-of-excel-workbook/)
