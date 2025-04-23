---
title: Проверка пароля зашифрованных файлов с помощью C++
linktitle: Проверить пароль зашифрованных файлов
type: docs
weight: 10
url: /ru/cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Проверьте пароль зашифрованных файлов Excel (xlsx, xlsb, xls, xlsm) и OpenOffice (ODS), используя C++.
---

{{% alert color="primary" %}} 
Если файлы Excel (xlsx, xlsb, xls, xlsm) и OpenOffice (ODS) защищены паролем, Aspose поддерживает простую проверку пароля без разбора конкретных данных файлов.
{{% /alert %}} 

## **Проверьте пароль зашифрованного файла**

Для проверки пароля зашифрованного файла Aspose.Cells for C++ предоставляет метод [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/). Этот метод принимает два параметра: поток файла и пароль, который необходимо проверить.
Следующий фрагмент кода демонстрирует использование метода [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/) для проверки, является ли предоставленный пароль допустимым или нет.

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
