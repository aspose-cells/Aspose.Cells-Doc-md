---
title: 用数字证书为VBA代码项目数字签名（C++）
linktitle: 使用证书为VBA代码项目进行数字签名
type: docs
weight: 110
url: /zh/cpp/digitally-sign-a-vba-code-project-with-certificate/
description: 了解如何使用证书和Aspose.Cells for C++数字签名您的VBA代码项目。
---

{{% alert color="primary" %}} 

您可以使用Aspose.Cells及其[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/)方法对VBA代码项目进行数字签名。请按照以下步骤检查您的Excel文件是否已用证书进行数字签名。

- 点击**开发工具**标签中的**Visual Basic**以打开**Visual Basic for Applications IDE**。
- 在**Visual Basic for Applications IDE**中点击**工具** > **数字签名...**。

它将显示**数字签名表单**，显示文档是否已使用证书进行数字签名。

{{% /alert %}} 

## **用C++为VBA代码项目进行数字签名并使用证书**

以下示例代码演示如何使用[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/)方法。此示例代码的输入和输出文件都已列出。您可以使用任何Excel文件和任何证书测试此代码。

- [用于示例代码的源Excel文件](5115028.xlsm)
- [示例pfx文件](5115039.pfx)用于创建数字签名。请在计算机上安装它以运行此代码。其密码为1234。
- [示例代码生成的输出Excel文件](5115029.xlsm)

```cpp
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String password(u"1234");
    U16String pfxPath = srcDir + u"sampleDigitallySignVbaProjectWithCertificate.pfx";
    U16String comment(u"Signing Digital Signature using Aspose.Cells");

    Vector<uint8_t> certData;

    std::time_t now = std::time(nullptr);
    std::tm* now_tm = std::localtime(&now);
    int year = now_tm->tm_year + 1900;
    int month = now_tm->tm_mon + 1;
    int day = now_tm->tm_mday;
    int hour = now_tm->tm_hour;
    int minute = now_tm->tm_min;
    int second = now_tm->tm_sec;

    DigitalSignature digitalSignature(certData, password, comment, Date{year, month, day, hour, minute, second, 0});

    U16String inputFilePath = srcDir + u"sampleDigitallySignVbaProjectWithCertificate.xlsm";
    Workbook workbook(inputFilePath);

    workbook.GetVbaProject().Sign(digitalSignature);

    U16String outputFilePath = outDir + u"outputDigitallySignVbaProjectWithCertificate.xlsm";
    workbook.Save(outputFilePath);

    std::cout << "VBA project digitally signed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
