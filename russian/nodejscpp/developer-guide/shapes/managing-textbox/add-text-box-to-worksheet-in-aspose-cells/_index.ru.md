---
title: Как добавить/вставить TextBox в лист с помощью Node.js через C++
linktitle: Добавить текстовое поле на лист
type: docs
weight: 10
url: /ru/nodejs-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Как добавить/вставить TextBox в лист в Aspose.Cells for Node.js via C++.
keywords: добавить/вставить TextBox, TextBox, лист, Excel, Aspose, Node.js через C++
---

## Добавление текстового поля в лист Excel

В программе Excel (версия 07 и выше) есть два места, куда можно вставлять текстовые поля. Одно в "insert-shapes", другое — справа от верхнего меню опции "Insert".

### метод первый:

![1](1.png)

### метод второй:

![2](2.png)

## Как создать

Вы можете создавать текстовые поля с горизонтальным или вертикальным текстом.

- Выберите соответствующую опцию (горизонтальную или вертикальную)
- Щелкните левой кнопкой мыши на странице
- Удерживайте левую кнопку и перетаскивайте на странице
- Отпустите левую кнопку

Теперь у вас есть текстовое поле.

## Добавление TextBox в лист в Aspose.Cells for Node.js via C++

Когда необходимо массово вставлять TextBox в лист, ручной метод вставки очевидно неудобен. Если это вас беспокоит, данный документ вам поможет. [Aspose.Cells](https://products.aspose.com/cells/) предоставляет API для быстрой массовой вставки в вашем коде.

В следующем примере кода создается текстовое поле.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an object of the Workbook class
const workbook = new AsposeCells.Workbook();

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
sheet.getTextBoxes().add(6, 10, 100, 200);

// Save. You can check your text box in this way.
workbook.save("result.xlsx", AsposeCells.SaveFormat.Xlsx);
```

Вы получите файл, похожий на [итоговый файл](result.xlsx). В файле вы увидите следующее:

![](52449.png)

{{< app/cells/assistant language="nodejs-cpp" >}}
