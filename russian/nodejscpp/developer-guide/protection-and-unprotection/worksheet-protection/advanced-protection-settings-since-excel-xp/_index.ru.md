---
title: Расширенные настройки защиты с Excel XP с Node.js через C++
linktitle: Расширенные настройки защиты с Excel XP
type: docs
weight: 30
url: /ru/nodejs-cpp/advanced-protection-settings-since-excel-xp/
---


{{% alert color="primary" %}}

С момента выпуска Excel 2002 или XP, Microsoft добавила множество расширенных настроек защиты.

{{% /alert %}}


## **Введение**

Эти настройки защиты ограничивают или разрешают пользователям:

- Удалить строки или столбцы.
- Редактировать содержимое, объекты или сценарии.
- Форматировать ячейки, строки или столбцы.
- Вставлять строки, столбцы или гиперссылки.
- Выбирать заблокированные или разблокированные ячейки.
- Использовать сводные таблицы и многое другое.

Aspose.Cells for Node.js via C++ поддерживает все расширенные настройки защиты, предлагаемые начиная с Excel XP и более поздних версий.

### **Настройки расширенной защиты с использованием Excel XP и более поздних версий**

Чтобы просмотреть доступные настройки защиты в Excel XP:

1. Из меню **Инструменты** выберите **Защита**, а затем **Защитить лист**. Будет отображено диалоговое окно.

Чтобы просмотреть доступные настройки защиты в Excel 2016:

1. В меню **Файл** выберите **Защита книги**, а затем **Защитить текущий лист**.
1. Выберите **Защитить лист** в меню **Проверка**.

Следующие шаги откроют диалоговое окно, в котором вы можете разрешить или ограничить функции листа или применить пароль к листу.

### **Расширенные настройки защиты с использованием Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ поддерживает все расширенные настройки защиты.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет свойство [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--), которое используется для применения этих расширенных настроек защиты. Свойство [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) является объектом класса [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection), который инкапсулирует несколько булевых свойств для отключения или включения ограничений.

Ниже приведен небольшой пример приложения. Он открывает файл Excel и использует большинство поддерживаемых Excel XP и более поздних версий настроек защиты.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const fileBuffer = [];
fstream.on('data', chunk => fileBuffer.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Restricting users to delete columns of the worksheet
worksheet.getProtection().setAllowDeletingColumn(false);

// Restricting users to delete row of the worksheet
worksheet.getProtection().setAllowDeletingRow(false);

// Restricting users to edit contents of the worksheet
worksheet.getProtection().setAllowEditingContent(false);

// Restricting users to edit objects of the worksheet
worksheet.getProtection().setAllowEditingObject(false);

// Restricting users to edit scenarios of the worksheet
worksheet.getProtection().setAllowEditingScenario(false);

// Restricting users to filter
worksheet.getProtection().setAllowFiltering(false);

// Allowing users to format cells of the worksheet
worksheet.getProtection().setAllowFormattingCell(true);

// Allowing users to format rows of the worksheet
worksheet.getProtection().setAllowFormattingRow(true);

// Allowing users to insert columns in the worksheet
worksheet.getProtection().setAllowFormattingColumn(true);

// Allowing users to insert hyperlinks in the worksheet
worksheet.getProtection().setAllowInsertingHyperlink(true);

// Allowing users to insert rows in the worksheet
worksheet.getProtection().setAllowInsertingRow(true);

// Allowing users to select locked cells of the worksheet
worksheet.getProtection().setAllowSelectingLockedCell(true);

// Allowing users to select unlocked cells of the worksheet
worksheet.getProtection().setAllowSelectingUnlockedCell(true);

// Allowing users to sort
worksheet.getProtection().setAllowSorting(true);

// Allowing users to use pivot tables in the worksheet
worksheet.getProtection().setAllowUsingPivotTable(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);

// Closing the file stream to free all resources
fstream.close();
```

{{% alert color="primary" %}}

Пожалуйста, не вызывайте метод [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) класса [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) при использовании свойства [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--). Также сохраните файл в форматах Excel97To2003 или Xlsx, потому что расширенные настройки защиты поддерживаются только в Excel XP и более поздних версиях.

{{% /alert %}}

### **Проблема блокировки ячеек**

Если вы хотите ограничить редактирование ячеек пользователями, ячейки должны быть защищены (заблокированы) перед применением любых настроек защиты. В противном случае, ячейки могут редактироваться даже если лист защищен. В Microsoft Excel XP ячейки можно заблокировать через следующий диалог:

|**Диалог для блокировки ячеек в Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Также возможно заблокировать ячейки с помощью API Aspose.Cells. Каждая ячейка может иметь формат [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style), который содержит логическое свойство [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Установите свойство [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) в **true** или **false**, чтобы заблокировать или разблокировать ячейку.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").getStyle().setIsLocked(true);
// Finally, Protect the sheet now.
worksheet.protect(AsposeCells.ProtectionType.All);
workbook.save(path.join(dataDir, "output.xlsx"));
```
