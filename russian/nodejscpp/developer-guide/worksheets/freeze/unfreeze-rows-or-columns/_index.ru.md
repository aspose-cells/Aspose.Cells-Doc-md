---
title: Разморозить строки или столбцы с помощью Node.js через C++
linktitle: Снять замораживание панелей
type: docs
weight: 190
url: /ru/nodejs-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: В этой статье вы узнаете, как программно разморозить строки, столбцы или области листа Excel, используя API Node.js с C++.
keywords: Разморозить области, строки, столбцы, окно с помощью Node.js через C++.
---

## **Введение**

В этой статье мы узнаем, как разморозить строки, столбцы и области. Если в файлах Excel листы заморожены, иногда необходимо разморозить их или отрегулировать замороженные строки, столбцы или области.


## **В Excel**

1. Нажмите вкладку Просмотр > Заморозить панели > Снять заморозку панелей.

**![снять замораживание панелей в Excel](Unfreeze-Panes.png)**




## **Разморозить строки, столбцы или области с помощью Aspose.Cells for Node.js via C++**
Легко разморозить области с помощью Aspose.Cells for Node.js via C++. Используйте метод [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unFreezePanes--) для разморозки областей.

1. Создать Рабочую книгу для открытия замороженного файла.
2. Разморозить области с помощью метода Worksheet.unfreezePanes().
3. Сохранить файл.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const frozenFilePath = path.join(dataDir, "Frozen.xlsx");

const workbook = new AsposeCells.Workbook(frozenFilePath); 
workbook.getWorksheets().get(0).unFreezePanes();
workbook.save("Unfrozen.xlsx");
```

Прикреплен [образец исходного файла Excel](Frozen.xlsx).
{{< app/cells/assistant language="nodejs-cpp" >}}
