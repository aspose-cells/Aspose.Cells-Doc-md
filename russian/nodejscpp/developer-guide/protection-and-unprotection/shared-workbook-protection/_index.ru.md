---
title: Защита паролем или снятие защиты с общей книги с помощью Node.js через C++
linktitle: Защита паролем или снятие защиты общей рабочей книги
type: docs
weight: 10
url: /ru/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Возможные сценарии использования**

Вы можете защитить или снять защиту с общей книги в Microsoft Excel, как показано на следующем скриншоте. Aspose.Cells for Node.js via C++ также поддерживает эту функцию с помощью методов [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#protectSharedWorkbook-string-) и [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#unprotectSharedWorkbook-string-).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Защита паролем или снятие защиты общей книги**

В следующем образце кода создается рабочая книга, защищенная во время включения совместного использования, и сохраняется как [выходной файл Excel](55541777.xlsx). На снимке экрана показано, что при попытке снять защиту Microsoft Excel просит вас ввести пароль для снятия защиты.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty Excel file
const workbook = new AsposeCells.Workbook();

// Protect the Shared Workbook with Password
workbook.protectSharedWorkbook("1234");

// Uncomment this line to Unprotect the Shared Workbook
// workbook.unprotectSharedWorkbook("1234");

// Save the output Excel file
workbook.save("outputProtectSharedWorkbook.xlsx");
```
