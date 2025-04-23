---  
title: Защита и снятие защиты листа с помощью Node.js через C++  
linktitle: Защитить и снять защиту листа  
type: docs  
weight: 40  
url: /ru/nodejs-cpp/protect-and-unprotect-worksheets/  
description: Защитить и снять защиту листа файлов Excel с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Чтобы предотвратить случайное или умышленное изменение, перемещение или удаление данных на листе, вы можете заблокировать ячейки на листе Excel, а затем защитить лист паролем.  
{{% /alert %}}  

## **Защитить и снять защиту листа в MS Excel**  

**![защита и снятие защиты листа](protect-and-unprotect-worksheet.png)**  

1. Нажмите **Обзор > Защитить лист**.  
1. Введите пароль в **поле Пароль**.  
1. Выберите варианты **разрешить**.  
1. Выберите **OK**, введите пароль для подтверждения, затем снова выберите **OK**.  

## **Защитить лист с помощью Aspose.Cells for Node.js via C++**  
Для реализации защиты структуры рабочей книги Excel достаточно следующих простых строк кода.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.protect(AsposeCells.ProtectionType.Contents);
// Protect worksheet with password.
sheet.getProtection().setPassword("test");
// Save as Excel file.
workbook.save("Book1.xlsx");
```  

## **Снять защиту листа с помощью Aspose.Cells for Node.js via C++**  
Снятие защиты листа — это просто с API Aspose.Cells. Если лист защищен паролем, потребуется правильный пароль.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook(filePath);
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.unprotect("password");
// Save Excel file.
workbook.save("Book1.xlsx");
```  

## **Продвинутые темы**  
- [Расширенные настройки защиты с момента появления Excel XP](/cells/ru/nodejs-cpp/advanced-protection-settings-since-excel-xp/)  
- [Определение, защищен ли рабочий лист паролем](/cells/ru/nodejs-cpp/detect-if-worksheet-is-password-protected/)  
- [Защита листов](/cells/ru/nodejs-cpp/protecting-worksheets/)  
- [Снятие защиты с листа](/cells/ru/nodejs-cpp/unprotect-a-worksheet/)  
- [Проверить Пароль, Используемый для Защиты Листа](/cells/ru/nodejs-cpp/verify-password-used-to-protect-the-worksheet/)  

