---
title: 在工作簿的VBA项目中添加库引用
linktitle: 在工作簿中为VBA项目添加库引用
type: docs
weight: 80
url: /zh/cpp/add-a-library-reference-to-vba-project-in-workbook/
description: 学习如何使用Aspose.Cells for C++向VBA项目添加或注册库引用。
---

{{% alert color="primary" %}}

有时，您需要通过代码添加或注册VBA项目的库引用。您可以使用Aspose.Cells [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/)方法来实现。

{{% /alert %}}

## **在Microsoft Excel中为VBA项目添加库引用**

在Microsoft Excel中，您可以通过手动点击**工具 > 引用...**来添加VBA项目的库引用。

## **使用Aspose.Cells在工作簿中为VBA项目添加库引用**

以下示例代码使用[**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/)方法向工作簿的VBA项目添加或注册了两个库引用。

```c++
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

    // Path of output excel file
    U16String outputPath = outDir + u"Output_out.xlsm";

    // Create a new workbook
    Workbook workbook;

    // Get the VBA project from the workbook
    VbaProject vbaProj = workbook.GetVbaProject();

    // Add registered references to the VBA project
    vbaProj.GetReferences().AddRegisteredReference(u"stdole", u"*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation");
    vbaProj.GetReferences().AddRegisteredReference(u"Office", u"*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library");

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "VBA project references added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
