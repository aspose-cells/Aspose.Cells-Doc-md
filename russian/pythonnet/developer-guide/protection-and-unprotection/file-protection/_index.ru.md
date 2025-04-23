---
title: Шифрование и дешифрование файлов Excel
type: docs
weight: 10
url: /ru/python-net/encrypt-and-decrypt-excel-files/
description: Как зашифровать и дешифровать файлы Excel с помощью Python. Блокировка и разблокировка файлов Excel.
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

## **Шифрование файла Excel с помощью Aspose.Cells**

Следующий пример показывает, как зашифровать и защитить паролем файл Excel с помощью API Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **Указание опции 'Пароль на изменение'**

Следующий пример показывает, как установить опцию **Пароль для изменения** в Microsoft Excel для существующего файла с помощью API Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}


## **Дешифрование файла Excel с помощью Aspose.Cells**
Очень просто открыть файл Excel под защитой пароля и дешифровать его, используя API Aspose.Cells for Python via .NET, как показано в следующих кодах:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-Decrypt-Excel-File.py" >}}


## **Продвинутые темы**
- [Шифрование и дешифрование файлов ODS](/cells/ru/python-net/encrypt-and-decrypt-ods-files/)
- [Установка сильного типа шифрования](/cells/ru/python-net/setting-strong-encryption-type/)
- [Укажите автора при защите от записи книги](/cells/ru/python-net/specify-author-while-write-protecting-workbook/)
- [Проверка пароля зашифрованных файлов](/cells/ru/python-net/verify-password-of-encrypted-excel-and-ods-files/)

