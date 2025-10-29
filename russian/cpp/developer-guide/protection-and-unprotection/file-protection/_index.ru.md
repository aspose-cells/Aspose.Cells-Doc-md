---
title: Шифрование и расшифровка файлов Excel с помощью C++
linktitle: Шифрование и дешифрование файлов Excel
type: docs
weight: 10
url: /ru/cpp/encrypt-and-decrypt-excel-files/
description: Как зашифровать и расшифровать файлы Excel с помощью C++. Блокировка и разблокировка файлов Excel.
---

{{% alert color="primary" %}}

Microsoft Excel (с 97 по 365) позволяет шифровать и защищать паролем ваши электронные таблицы. Для этого используются алгоритмы, предоставляемые поставщиком криптографических услуг, или CSP - набор криптографических алгоритмов с различными свойствами. CSP по умолчанию - 'Office 97/2000 Compatible' или 'Weak Encryption (XOR)'. Важно выбрать соответствующую длину ключа шифрования. Некоторые CSP не поддерживают более 40 или 56 бит. Это считается слабым шифрованием. Для сильного шифрования требуется минимальная длина ключа 128 бит. Microsoft Windows содержит CSP, которые также предлагают сильные типы шифрования, например, 'Microsoft Strong Cryptographic Provider'. Для примера, 128-битное шифрование используется банками для шифрования соединения с их системами Интернет-банкинга.

Aspose.Cells позволяет шифровать и защищать паролем файлы Microsoft Excel с выбранным вами типом шифрования.

{{% /alert %}}

## **Использование Microsoft Excel**

Для установки параметров шифрования файла в Microsoft Excel (например, Microsoft Excel 2003):

1. Из меню **Инструменты** выберите **Параметры**. Появится диалоговое окно.
1. Выберите вкладку **Безопасность**.
1. Введите пароль и нажмите **Дополнительно**.
1. Выберите тип шифрования и подтвердите пароль.

## **Шифрование файла Excel с помощью Aspose.Cells**

Следующий пример показывает, как зашифровать и установить пароль на файл Excel с помощью API Aspose.Cells.

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
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"encryptedBook1.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify XOR encryption type
    workbook.SetEncryptionOptions(EncryptionType::XOR, 40);

    // Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider)
    workbook.SetEncryptionOptions(EncryptionType::StrongCryptographicProvider, 128);

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Workbook encrypted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Указание опции 'Пароль на изменение'**

В следующем примере показано, как установить опцию 'Пароль на изменение' для существующего файла Microsoft Excel с помощью API Aspose.Cells.

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
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"SpecifyPasswordToModifyOption.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Set the password for modification
    workbook.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Password for modification set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Дешифрование файла Excel с помощью Aspose.Cells**

Очень легко открыть защищенный паролем файл Excel и расшифровать его, используя API Aspose.Cells, как показано в следующем коде:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create load options and set password
    LoadOptions loadOptions;
    loadOptions.SetPassword(u"password");

    // Open encrypted Excel file
    Workbook workbook(u"Book1.xlsx", loadOptions);

    // Remove password protection
    workbook.GetSettings().SetPassword(nullptr);

    // Save the modified workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Password removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**

- [Шифрование и дешифрование файлов ODS](/cells/ru/cpp/encrypt-and-decrypt-ods-files/)
- [Установка сильного типа шифрования](/cells/ru/cpp/setting-strong-encryption-type/)
- [Укажите автора при защите от записи книги](/cells/ru/cpp/specify-author-while-write-protecting-workbook/)
- [Проверка пароля зашифрованных файлов](/cells/ru/cpp/verify-password-of-encrypted-excel-and-ods-files/)
{{< app/cells/assistant language="cpp" >}}
