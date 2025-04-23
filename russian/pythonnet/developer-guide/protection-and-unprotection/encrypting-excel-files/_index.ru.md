---
title: Шифрование файлов Excel
type: docs
weight: 90
url: /ru/python-net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (с 97 по 365) позволяет шифровать и защищать паролем ваши электронные таблицы. Для этого используются алгоритмы, предоставляемые поставщиком криптографических услуг, или CSP - набор криптографических алгоритмов с различными свойствами. CSP по умолчанию - 'Office 97/2000 Compatible' или 'Weak Encryption (XOR)'. Важно выбрать соответствующую длину ключа шифрования. Некоторые CSP не поддерживают более 40 или 56 бит. Это считается слабым шифрованием. Для сильного шифрования требуется минимальная длина ключа 128 бит. Microsoft Windows содержит CSP, которые также предлагают сильные типы шифрования, например, 'Microsoft Strong Cryptographic Provider'. Для примера, 128-битное шифрование используется банками для шифрования соединения с их системами Интернет-банкинга.

Aspose.Cells for Python via .NET позволяет шифровать и защищать паролем файлы Microsoft Excel с выбранным вами типом шифрования.

{{% /alert %}}

## **Использование Microsoft Excel**

Для установки параметров шифрования файла в Microsoft Excel (например, Microsoft Excel 2003):

1. Из меню **Инструменты** выберите **Параметры**. Появится диалоговое окно.
1. Выберите вкладку **Безопасность**.
1. Введите пароль и нажмите **Дополнительно**.
1. Выберите тип шифрования и подтвердите пароль.

## **Шифрование с помощью Aspose.Cells**

Следующий пример показывает, как зашифровать и защитить паролем файл Excel с помощью API Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **Указание опции 'Пароль на изменение'**

Следующий пример показывает, как установить опцию **Пароль для изменения** в Microsoft Excel для существующего файла с помощью API Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}

## **Проверьте пароль зашифрованного файла**

Для проверки пароля зашифрованного файла Aspose.Cells for Python via .NET предоставляет метод [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password). Эти методы принимают два параметра: файловый поток и пароль, который нужно проверить.
Следующий фрагмент кода демонстрирует использование метода [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) для проверки, является ли предоставленный пароль допустимым или нет.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}

## **Шифрование/Дешифрование файла ODS**

Aspose.Cells for Python via .NET позволяет шифровать и дешифровать файл ODS. Расшифрованный файл ODS можно открыть как в Excel, так и в OpenOffice, однако зашифрованный файл ODS можно открыть только в OpenOffice при вводе пароля. Excel не может открыть зашифрованный файл ODS и может вывести предупреждение. Варианты шифрования не применимы к файлам ODS, в отличие от других типов файлов. Для шифрования файла ODS загрузите файл и установите значение [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) в фактический пароль перед сохранением. ИССходящий зашифрованный файл ODS можно открыть только в OpenOffice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

Для расшифровки файла ODS загрузите файл, предоставив пароль в [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). После загрузки файла установите строку [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) в null.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

