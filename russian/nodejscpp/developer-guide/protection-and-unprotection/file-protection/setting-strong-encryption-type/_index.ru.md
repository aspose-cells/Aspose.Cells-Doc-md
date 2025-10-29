---  
title: Настройка типа сильного шифрования с помощью Node.js через C++  
linktitle: Установка сильного типа шифрования  
type: docs  
weight: 60  
url: /ru/nodejs-cpp/setting-strong-encryption-type/  
description: Узнайте, как установить типы сильного шифрования для файлов Excel с помощью Aspose.Cells for Node.js via C++.  
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

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the Excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
