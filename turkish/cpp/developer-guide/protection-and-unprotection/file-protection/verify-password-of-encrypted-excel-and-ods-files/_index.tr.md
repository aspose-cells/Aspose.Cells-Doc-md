---
title: C++ ile Şifreli Dosyaların Parolası Doğrulama
linktitle: Şifrelenmiş Dosyaların Şifresini Doğrulama
type: docs
weight: 10
url: /tr/cpp/verify-password-of-encrypted-excel-and-ods-files/
description: C++ kodlarını kullanarak şifreli Excel (xlsx, xlsb, xls, xlsm) ve Open Office (ODS) dosyalarının parolasını doğrulayın.
---

{{% alert color="primary" %}} 
Excel (xlsx, xlsb, xls, xlsm) ve Open Office (ODS) dosyaları şifreyle kilitlenmişse, Aspose basit parola doğrulamasını dosyaların belirli verilerini ayrıştırmadan destekler.
{{% /alert %}} 

## **Şifrelenmiş dosyanın parolasını doğrulama**

Şifreyi doğrulamak için Aspose.Cells for C++, [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/) yöntemini sağlar. Bu yöntem iki parametre alır, dosya akışı ve doğrulanması gereken parola.
Aşağıdaki kod parçası, sağlanan parolanın geçerli olup olmadığını doğrulamak için [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/) yönteminin nasıl kullanıldığını göstermektedir.

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
