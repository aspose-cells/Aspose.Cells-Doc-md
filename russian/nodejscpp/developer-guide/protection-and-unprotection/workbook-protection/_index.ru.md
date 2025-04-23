---  
title: Защита и отмена защиты структуры книги с помощью Node.js через C++  
linktitle: Защита и снятие защиты структуры рабочей книги  
type: docs  
weight: 40  
url: /ru/nodejs-cpp/protect-and-unprotect-workbook-structure/  
description: Защита и снятие защиты структуры книги файлов Excel с помощью Node.js через C++.  
---  


{{% alert color="primary" %}}  
Чтобы предотвратить просмотр скрытых листов, добавление, перемещение, удаление или скрытие листов другими пользователями и переименование листов, вы можете защитить структуру своей рабочей книги Excel паролем.  
{{% /alert %}}  


## **Защита и снятие защиты структуры рабочей книги в MS Excel**  

**![защита и снятие защиты структуры рабочей книги](protect-and-unprotect-workbook-structure.png)**  

1. Нажмите **Обзор > Защитить книгу**.  
1. Введите пароль в **поле Пароль**.  
1. Выберите **OK**, введите пароль для подтверждения, затем снова выберите **OK**.  


## **Защитить структуру книги с помощью Aspose.Cells for Node.js via C++**  
Для реализации защиты структуры рабочей книги Excel достаточно следующих простых строк кода.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Protect workbook structure.
workbook.protect(AsposeCells.ProtectionType.Structure, "password");
// Save Excel file.
workbook.save(filePath);
```  

## **Снять защиту с структуры книги с помощью Aspose.Cells for Node.js via C++**  
Снятие защиты структуры рабочей книги легко с помощью API Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open an Excel file which workbook structure is protected.
const workbook = new AsposeCells.Workbook(filePath);
// Unprotect workbook structure.
workbook.unprotect("password");
// Save Excel file.
workbook.save(filePath);
```  

{{% alert color="primary" %}}  
Примечание: требуется правильный пароль.  
{{% /alert %}}  

