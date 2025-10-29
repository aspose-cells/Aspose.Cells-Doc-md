---
title: Обновление сегментатора с помощью Node.js через C++
linktitle: Обновление срезки
type: docs
weight: 50
url: /ru/nodejs-cpp/updating-slicer/
description: Эта статья показывает, как обновлять связанные сводные таблицы, обновляя сегментатор с помощью Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js через C++, обновление сегментатора Node.js, как изменить сегментатор Node.js, как настроить сегментатор в Node.js, как выбрать или снять выбор с элементов сегментатора Node.js через C++.
---

## **Возможные сценарии использования**

Если хотите обновить сегментатор в Microsoft Excel, выберите или отмените выбор его элементов, и он обновит таблицу сегментатора или сводную таблицу соответственно. Используйте [**Slicer.getSlicerCacheItems()**](https://reference.aspose.com/cells/nodejs-cpp/slicercache/#getSlicerCacheItems--) для выбора или снятия выбора элементов сегментатора с помощью Aspose.Cells, затем вызовите метод [**Slicer.refresh()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#refresh--) для обновления таблицы сегментатора или сводной таблицы.

## **Как обновить фильтр**

Следующий образец кода загружает [образец файла Excel](67338475.xlsx), содержащий существующий фильтр. Он отменяет выбор 2-го и 3-го элементов фильтра и обновляет фильтр. Затем сохраняет рабочую книгу в [выходной файл Excel](67338476.xlsx). На следующем скриншоте показан эффект образца кода на образцовый файл Excel. Как вы можете видеть на скриншоте, обновление фильтра с выбранными элементами также обновило сводную таблицу соответственно.

![todo:image_alt_text](updating-slicer_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleUpdatingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Access the slicer items.
const scItems = slicer.getSlicerCache().getSlicerCacheItems();

const items = slicer.getSlicerCache().getSlicerCacheItems();

for (let i = 0; i < items.getCount(); i++) {
const item = items.get(i);
if (item.getValue() === "Pink" || item.getValue() === "Green") {
item.setSelected(false);
}
}
slicer.refresh();
wb.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
