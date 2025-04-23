---
title: Определить, является ли лист диалоговым окном с помощью Node.js через C++
linktitle: Проверить, является ли рабочий лист диалоговым листом
type: docs
weight: 90
url: /ru/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Эта статья содержит инструкции и пример кода для определения программным путем, является ли лист Excel диалоговым окном с помощью Aspose.Cells for Node.js via C++.
keywords: поиск диалогового типа листа Excel с помощью Node.js через C++, диалоговый лист Node.js через C++
---

## **Возможные сценарии использования**

Диалоговый лист — это устаревший формат листа, содержащий диалоговое окно. Такой лист может быть вставлен старой версией Microsoft Excel, например, 2003, как показано на скриншоте. Также его можно вставить с помощью VBA в более новых версиях, например, Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Вы можете определить, является ли лист диалоговым или другим типом листа, с помощью свойства [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--), предоставляемого Aspose.Cells for Node.js via C++. Если оно возвращает значение перечисления [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype), это означает, что вы имеете дело с диалоговым листом.

## **Определить, является ли рабочий лист диалоговым листом**

Следующий пример кода загружает [пример файла Excel](64716820.xlsx), содержащего диалоговый лист. Он проверяет свойство [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--), сравнивает его с [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype) и выводит сообщение. Для получения дополнительной информации посмотрите вывод в консоли приведенного ниже примера кода.

## **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFindIfWorksheetIsDialogSheet.xlsx");

// Load Excel file containing Dialog Sheet
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Find if the sheet type is dialog and print the message
if (ws.getType() === AsposeCells.SheetType.Dialog) {
console.log("Worksheet is a Dialog Sheet.");
}
```

## **Вывод в консоль**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
