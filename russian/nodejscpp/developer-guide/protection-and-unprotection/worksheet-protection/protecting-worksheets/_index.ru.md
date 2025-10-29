---
title: Защита листов с помощью Node.js через C++
linktitle: Защита листов
type: docs
weight: 10
url: /ru/nodejs-cpp/protecting-worksheets/
description: Изучите, как защитить листы в Excel с помощью Aspose.Cells for Node.js via C++, включая защиту строк, столбцов и определённых ячеек.
---


{{% alert color="primary" %}}

Когда лист защищён, действия, доступные пользователю, ограничены. Например, он не может вводить данные, вставлять или удалять строки или столбцы и т.п.

{{% /alert %}}

## **Защита листов**

### **Введение**

Основные параметры защиты в Microsoft Excel:

- Содержимое
- Объекты
- Сценарии

Защита листов не скрывает и не защищает конфиденциальные данные, поэтому это отличается от шифрования файлов. Обычно защита листа подходит для ознакомительных целей. Она предотвращает изменение данных, содержимого и форматирования в листе.

### **Защита листа**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет метод [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-), который используется для применения защиты на листе. Метод [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) принимает следующие параметры:

- Тип защиты, тип защиты, применяемый к листу. Тип защиты применяется с помощью перечисления [**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype).
- Новый пароль, новый пароль, используемый для защиты листа.
- Старый пароль, старый пароль, если лист уже защищен паролем. Если лист еще не защищен, то просто передайте null.

Перечисление [**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype) содержит следующие предопределённые типы защиты:

|**Типы защиты**|**Описание**|
| :- | :- |
|All|Пользователь не может изменять ничего на этом листе|
|Contents|Пользователь не может вводить данные на этом листе|
|Objects|Пользователь не может изменять рисуночные объекты|
|Scenarios|Пользователь не может изменять сохраненные сценарии|
|Structure|Пользователь не может изменять структуру|
|Windows|Защита применяется к окнам|
|None|Никакая защита не применяется|

Приведенный ниже пример показывает, как защитить лист паролем.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file buffer
const excel = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = excel.getWorksheets().get(0);

// Protecting the worksheet with a password
worksheet.protect(AsposeCells.ProtectionType.All, "aspose", null);

// Saving the modified Excel file in default format
excel.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

Как только указанный выше код используется для защиты листа, вы можете проверить защиту на листе, открыв его. После открытия файла и попытки добавить данные на лист, вы увидите следующий диалог:

|**Предупреждение о том, что пользователь не может изменять лист**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Для работы на листе снимите защиту листа, выбрав **Защита**, затем **Снять защиту таблицы** из меню **Инструменты**.

После выбора пункта меню Снять защиту таблицы откроется диалоговое окно, призывающее вас ввести пароль, чтобы вы могли работать на листе, как показано ниже:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Защита нескольких ячеек на листе c помощью Microsoft Excel**

В некоторых случаях нужно защитить только определённые ячейки в листе. Если вы хотите заблокировать конкретные ячейки, необходимо разблокировать все остальные ячейки в листе. Все ячейки в листе изначально настроены на блокировку; проверьте это, открыв любой файл Excel в MS Excel, выбрав **Формат | Ячейки...**, чтобы открыть диалоговое окно **Формат ячейки**, и перейдя на вкладку **Защита**, где по умолчанию стоит флажок «Заблокировано».

Следующие пункты описывают, как заблокировать ячейки в MS Excel. Этот метод подходит для Microsoft Office Excel 97, 2000, 2002, 2003 и более новых версий.

1. Выберите весь лист, нажав кнопку **Выбрать все** (серый прямоугольник над номером строки для строки 1 и слева от буквы столбца A).
2. Нажмите **Ячейки** в меню **Формат**, перейдите на вкладку **Защита**, и снимите галочку с **Заблокировано**.
   Это разблокирует все ячейки в листе.
   Если команда **Ячейки** недоступна, части листа могут уже быть заблокированы. На меню **Инструменты** наведите указатель на **Защита**, а затем щелкните **Снять защиту листа**.
3. Выберите только те ячейки, которые нужно заблокировать, и повторите шаг 2, но на этот раз выберите флажок **Заблокировано**.
4. В меню **Инструменты** наведите указатель на **Защита**, выберите **Защитить лист** и нажмите **ОК**.
5. В диалоговом окне **Защита листа** у вас есть возможность указать пароль и выбрать элементы, которые пользователи смогут изменять.

### **Защитите несколько ячеек в листе, используя Aspose.Cells**

В этом методе мы используем только API Aspose.Cells для выполнения задачи.

Пример: Следующий пример показывает, как защитить несколько ячеек в листе. Он сначала разблокирует все ячейки листа, затем блокирует 3 ячейки (A1, B1, C1). В конце он защищает лист. Объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) содержит свойство типа boolean, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Вы можете установить свойство [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) в true или false и применить метод *Column/Row.applyStyle()* для блокировки или разблокировки строки/столбца с желаемыми атрибутами.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object
const styleflag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get((i)).getStyle();
style.setIsLocked(false);
styleflag.setLocked(true);
sheet.getCells().getColumns().get((i)).applyStyle(style, styleflag);
}

// Lock the three cells...i.e. A1, B1, C1.
style = sheet.getCells().get("A1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("A1").setStyle(style);
style = sheet.getCells().get("B1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("B1").setStyle(style);
style = sheet.getCells().get("C1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("C1").setStyle(style);

// Finally, Protect the sheet now.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Защита строки на листе**

Aspose.Cells позволяет легко блокировать любую строку в листе. Здесь мы можем использовать метод [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) класса [**Aspose.Cells.Row**](https://reference.aspose.com/cells/nodejs-cpp/row), чтобы применить [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) к конкретной строке в листе. Этот метод принимает два аргумента: объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) и объект [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag), который содержит все участники, связанные с применением форматирования.

Следующий пример показывает, как защитить строку в листе. Он сначала разблокирует все ячейки листа, затем блокирует первую строку. В конце он защищает лист. Объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) содержит свойство типа boolean, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Вы можете установить свойство [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) в true или false, чтобы заблокировать или разблокировать строку/столбец, используя объект [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first row style.
style = sheet.getCells().getRows().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Set the lock setting.
flag.setLocked(true);

// Apply the style to the first row.
sheet.getCells().applyRowStyle(0, style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Защита столбца на листе**

Aspose.Cells позволяет легко заблокировать любой столбец в листе. Мы можем использовать метод [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/column/#applyStyle-style-styleflag-) класса [**Aspose.Cells.Column**](https://reference.aspose.com/cells/nodejs-cpp/column), чтобы применить [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) к конкретному столбцу. Этот метод принимает два аргумента: объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) и объект [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag), который содержит все участники, связанные с применением форматирования.

Следующий пример показывает, как защитить столбец в листе. Он сначала разблокирует все ячейки листа, затем блокирует первый столбец. В конце он защищает лист. Объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) содержит свойство типа boolean, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Вы можете установить свойство [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) в true или false, чтобы заблокировать или разблокировать строку/столбец, используя объект [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first column style.
style = sheet.getCells().getColumns().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Apply the style to the first column.
sheet.getCells().getColumns().get(0).applyStyle(style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Разрешить пользователям редактировать диапазоны**

В следующем примере показано, как разрешить пользователям редактировать диапазон в защищенном листе.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Get the first (default) worksheet
const sheet = book.getWorksheets().get(0);

// Get the Allow Edit Ranges
const allowRanges = sheet.getAllowEditRanges();

// Define ProtectedRange
let protected_range;

// Create the range
const idx = allowRanges.add("r2", 1, 1, 3, 3);
protected_range = allowRanges.get(idx);

// Specify the password
protected_range.setPassword("123");

// Protect the sheet
sheet.protect(AsposeCells.ProtectionType.All);

// Save the Excel file
book.save(path.join(dataDir, "protectedrange.out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
