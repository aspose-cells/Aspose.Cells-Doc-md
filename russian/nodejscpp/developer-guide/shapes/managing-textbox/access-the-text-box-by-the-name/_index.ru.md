---
title: Доступ к текстовому полю по имени с помощью Node.js через C++
linktitle: Доступ к текстовому полю по имени
type: docs
weight: 230
url: /ru/nodejs-cpp/access-the-text-box-by-the-name/
description: Узнайте, как получить доступ к текстовому полю по имени из коллекции в Aspose.Cells for Node.js via C++. 
---

## Доступ к текстовому полю по имени

Ранее текстовые поля получали по индексу из коллекции [**Worksheet.getTextBoxes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTextBoxes--), но теперь их также можно получить по имени из этой коллекции. Это удобный и быстрый способ доступа к вашему текстовому полю, если вы уже знаете его имя.

Приведенный ниже образец кода сначала создает текстовое поле и назначает ему некоторый текст и имя. Затем в следующих строках мы получаем доступ к тому же текстовому полю по его имени и печатаем его текст.

### Код Node.js для доступа к текстовому полю по имени

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
const idx = sheet.getTextBoxes().add(10, 10, 10, 10);

// Access newly created TextBox using its index & name it
const tb1 = sheet.getTextBoxes().get(idx);
tb1.setName("MyTextBox");

// Set text for the TextBox
tb1.setText("This is MyTextBox");

// Access the same TextBox via its name
const tb2 = sheet.getTextBoxes().get("MyTextBox");

// Display the text of the TextBox accessed via name
console.log(tb2.getText());

console.log("Press any key to continue...");
```

### Вывод консоли, сгенерированный примерным кодом

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
