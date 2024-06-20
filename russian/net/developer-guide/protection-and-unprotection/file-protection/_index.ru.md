---
title: Шифрование и дешифрование файлов Excel
type: docs
weight: 10
url: /ru/net/encrypt-and-decrypt-excel-files/
description: Как зашифровать и дешифровать файлы Excel с помощью C#. Блокировать и разблокировать файлы Excel.
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

В следующем примере показано, как зашифровать и защитить паролем файл Excel с использованием API Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Указание опции 'Пароль на изменение'**

В следующем примере показано, как установить опцию 'Пароль на изменение' для существующего файла Microsoft Excel с помощью API Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **Дешифрование файла Excel с помощью Aspose.Cells**
Открыть защищенный паролем файл Excel и расшифровать его при помощи API Aspose.Cells можно по следующим кодам:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **Продвинутые темы**
- [Шифрование и дешифрование файлов ODS](/cells/ru/net/encrypt-and-decrypt-ods-files/)
- [Установка сильного типа шифрования](/cells/ru/net/setting-strong-encryption-type/)
- [Укажите автора при защите от записи книги](/cells/ru/net/specify-author-while-write-protecting-workbook/)
- [Проверка пароля зашифрованных файлов](/cells/ru/net/verify-password-of-encrypted-excel-and-ods-files/)

