---  
title: Шифрование и расшифровка Excel файлов с помощью Node.js через C++  
linktitle: Шифрование и дешифрование файлов Excel  
type: docs  
weight: 10  
url: /ru/nodejs-cpp/encrypt-and-decrypt-excel-files/  
description: Как шифровать и расшифровывать Excel файлы с помощью Node.js через C++. Блокировка и разблокировка Excel файлов.  
---  

{{% alert color="primary" %}}  
Microsoft Excel (с 97 по 365) позволяет шифровать и защищать паролем ваши электронные таблицы. Для этого используются алгоритмы, предоставляемые поставщиком криптографических услуг, или CSP - набор криптографических алгоритмов с различными свойствами. CSP по умолчанию - 'Office 97/2000 Compatible' или 'Weak Encryption (XOR)'. Важно выбрать соответствующую длину ключа шифрования. Некоторые CSP не поддерживают более 40 или 56 бит. Это считается слабым шифрованием. Для сильного шифрования требуется минимальная длина ключа 128 бит. Microsoft Windows содержит CSP, которые также предлагают сильные типы шифрования, например, 'Microsoft Strong Cryptographic Provider'. Для примера, 128-битное шифрование используется банками для шифрования соединения с их системами Интернет-банкинга.  

Aspose.Cells позволяет шифровать и защищать паролем файлы Microsoft Excel с выбранным вами типом шифрования.  
{{% /alert %}}  

## **Использование Microsoft Excel**  

Для установки параметров шифрования файла в Microsoft Excel (например, Microsoft Excel 2003):  

1. Из меню **Инструменты** выберите **Параметры**. Появится диалоговое окно.  
2. Выберите вкладку **Безопасность**.  
3. Введите пароль и нажмите **Дополнительно**  
4. Выберите тип шифрования и подтвердите пароль.  

## **Шифрование Excel-файла с помощью Aspose.Cells for Node.js via C++**  

Следующий пример показывает, как зашифровать и установить пароль на файл Excel с помощью API Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify XOR encryption type.
workbook.setEncryptionOptions(AsposeCells.EncryptionType.XOR, 40);

// Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```  

### **Указание опции пароля для изменений**  

В следующем примере показано, как установить опцию 'Пароль на изменение' для существующего файла Microsoft Excel с помощью API Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```  


## **Расшифровка Excel-файла с помощью Aspose.Cells for Node.js via C++**  
Очень легко открыть защищенный паролем файл Excel и расшифровать его, используя API Aspose.Cells, как показано в следующем коде:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open encrypted file with password.
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("password");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);

// Remove password.
workbook.getSettings().setPassword(null);

// Save the file.
workbook.save(filePath);
```  


## **Продвинутые темы**  
- [Шифрование и дешифрование файлов ODS](/cells/ru/nodejs-cpp/encrypt-and-decrypt-ods-files/)  
- [Установка сильного типа шифрования](/cells/ru/nodejs-cpp/setting-strong-encryption-type/)  
- [Укажите автора при защите от записи книги](/cells/ru/nodejs-cpp/specify-author-while-write-protecting-workbook/)  
- [Проверка пароля зашифрованных файлов](/cells/ru/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/)  


