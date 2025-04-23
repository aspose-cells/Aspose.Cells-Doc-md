---
title: C++を使った暗号化済みファイルのパスワード検証
linktitle: 暗号化されたファイルのパスワードを確認する
type: docs
weight: 10
url: /ja/cpp/verify-password-of-encrypted-excel-and-ods-files/
description: C++コードを使って、暗号化されたExcel（xlsx、xlsb、xls、xlsm）およびOpenOffice（ODS）ファイルのパスワード検証を行います。
---

{{% alert color="primary" %}} 
Excel（xlsx、xlsb、xls、xlsm）およびOpenOffice（ODS）ファイルがパスワードで保護されている場合、Asposeは特定のデータを解析せずに単純なパスワード検証をサポートします。
{{% /alert %}} 

## **暗号化されたファイルのパスワードを確認します**

暗号化されたファイルのパスワードを検証するために、Aspose.Cells for C++は[**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/)メソッドを提供します。このメソッドは、ファイルストリームと検証したいパスワードの二つのパラメータを受け取ります。
以下のコードスニペットは、提供されたパスワードが有効かどうかを確認する[**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/)メソッドの使用を示しています。

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
