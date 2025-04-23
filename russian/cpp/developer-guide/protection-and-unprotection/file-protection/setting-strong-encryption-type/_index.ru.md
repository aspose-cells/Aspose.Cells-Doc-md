---
title: Установка сильного типа шифрования с C++
linktitle: Установка сильного типа шифрования
type: docs
weight: 60
url: /ru/cpp/setting-strong-encryption-type/
description: Узнайте, как применить сильное шифрование и парольную защиту к файлам Excel с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) позволяет вам шифровать и защищать паролем электронные таблицы. Для этого используются алгоритмы, предоставленные поставщиком криптосервисов. Криптосервис (или CSP) представляет собой набор криптографических алгоритмов с различными свойствами. CSP по умолчанию - "Совместимое с Office 97/2000". Это CSP с некоторыми публично известными проблемами безопасности. Таблицы, защищенные "слабым шифрованием (XOR)" или шифрованием типа "Совместимое с Office 97/2000", могут быть легко взломаны.

Чтобы преодолеть эту проблему, используйте один из сильных типов шифрования, предоставленных Microsoft Excel. Вы можете изменить тип шифрования на самый сильный из доступных CSP. Для сильного шифрования требуется минимальная длина ключа 128 бит, например, 'Microsoft Strong Cryptographic Provider'.

Вы также можете шифровать и защищать паролем файлы Excel с сильным типом шифрования с использованием API Aspose.Cells.

{{% /alert %}}

## **Применение шифрования с помощью Microsoft Excel**
Для реализации шифрования файлов в Microsoft Excel (например, 2007):

1. В меню **Сервис** выберите **Параметры**.
1. Выберите вкладку **Безопасность**.
1. Введите значение для поля **Пароль для открытия**.
1. Нажмите **Дополнительно**.
1. Выберите тип шифрования и подтвердите пароль.

## **Применение шифрования с помощью Aspose.Cells**
Приведенные ниже примеры кода применяют сильное шифрование к файлу и устанавливают пароль.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"encryptedBook1.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider)
    workbook.SetEncryptionOptions(EncryptionType::StrongCryptographicProvider, 128);

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "File encrypted and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
