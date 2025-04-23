---
title: 使用 C++ 验证加密文件密码
linktitle: 验证加密文件的密码
type: docs
weight: 10
url: /zh/cpp/verify-password-of-encrypted-excel-and-ods-files/
description: 使用 C++ 代码验证加密的Excel（xlsx、xlsb、xls、xlsm）和OpenOffice（ODS）文件的密码。
---

{{% alert color="primary" %}} 
 如果Excel（xlsx、xlsb、xls、xlsm）和OpenOffice（ODS）文件被密码锁定，Aspose支持简单的密码验证，无需解析文件的特定数据。
{{% /alert %}} 

## **验证加密文件的密码**

 要验证加密文件的密码，Aspose.Cells for C++ 提供了 [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/) 方法。该方法接受两个参数：文件流和需要验证的密码。
以下代码片段演示了使用[**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/)方法来验证提供的密码是否有效。

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputPath = srcDir + u"EncryptedBook1.xlsx";
    std::vector<uint8_t> fileData;

    std::ifstream file(inputPath.ToUtf8(), std::ios::binary);
    if (file)
    {
        file.seekg(0, std::ios::end);
        fileData.resize(file.tellg());
        file.seekg(0, std::ios::beg);
        file.read(reinterpret_cast<char*>(fileData.data()), fileData.size());
    }
    Vector<uint8_t> data(fileData.data(), static_cast<int32_t>(fileData.size()));
    bool isPasswordValid = FileFormatUtil::VerifyPassword(data, u"123456");
    std::cout << "Password is Valid: " << std::boolalpha << isPasswordValid << std::endl;

    Aspose::Cells::Cleanup();
}
```
