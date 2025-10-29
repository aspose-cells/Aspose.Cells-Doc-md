---
title: Разблокировать лист с Node.js через C++
linktitle: Снять защиту листа
type: docs
weight: 20
url: /ru/nodejs-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Если разработчику необходимо удалить защиту с защищенного листа во время выполнения, чтобы внести изменения в файл? Это легко можно сделать с помощью Aspose.Cells.

{{% /alert %}}

## **Снятие защиты с листа**

### **Использование Microsoft Excel**

Для снятия защиты с листа:

Из меню **Инструменты** выберите **Защита**, затем **Снять защиту листа**. Защита будет снята, если лист не защищен паролем. В этом случае появится диалог, запрашивающий пароль. Введите пароль, и лист будет разблокирован.

### **Снятие защиты с просто защищенного листа с помощью Aspose.Cells**

Лист можно разблокировать, вызвав метод [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) класса [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--). Простой защищенный лист — это такой, который не защищен паролем. Такой лист можно разблокировать, вызвав метод [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) без передачи параметра.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet without a password
worksheet.unprotect();

// Saving the Workbook
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Снятие защиты с защищенного паролем листа с помощью Aspose.Cells**

Лист, защищенный паролем, — это лист, который защищен паролем. Его можно разблокировать, вызвав переопределенную версию метода [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--), принимающую пароль как параметр.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet with a password
worksheet.unprotect("");

// Save Workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
