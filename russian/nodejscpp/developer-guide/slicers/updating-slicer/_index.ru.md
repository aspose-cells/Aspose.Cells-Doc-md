---
title: Обновление среза с помощью Node.js через C++
linktitle: Обновление среза
type: docs
weight: 50
url: /ru/nodejs-cpp/updating-slicer/
description: Эта статья показывает, как обновить срез, чтобы фильтровать данные связанной сводной таблицы или таблицы с помощью Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js via C++, обновление среза Node.js, как изменить срез Node.js, как отфильтровать сводную таблицу срезом в Node.js, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Обновление среза означает фильтрацию данных сводной таблицы или таблицы, к которой подключен срез. Когда вы выбираете или отменяете выбор элементов среза в Microsoft Excel, связанная сводная таблица или таблица пересчитывается соответствующим образом. С Aspose.Cells for Node.js via C++ вам не нужно перебирать элементы кэша среза и обновлять срез вручную — метод [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/) обновляет срез и пересчитывает связанную сводную таблицу или таблицу напрямую из элементов фильтра:
- `Slicer.selectItems(labels, append)` — выбирает указанные метки и пересчитывает связанную сводную таблицу или таблицу. Если `append` равно `true`, изначально выбранные метки сохраняются, а указанные метки добавляются к выделению; если `append` равно `false`, все исходные выделения сбрасываются и выбранными остаются только указанные метки.
- `Slicer.unselectItems(labels)` — отменяет выбор части выбранных элементов.
- `Slicer.clearFilter()` — удаляет фильтр и выбирает все элементы.

{{% alert color="primary" %}}
Начиная с версии Aspose.Cells for Node.js via C++ 26.10, свойство `SlicerCacheItem.Selected` становится доступным только для чтения, и его сеттер больше не поддерживается. Используйте методы `Slicer.selectItems`, `Slicer.unselectItems` и `Slicer.clearFilter` вместо установки `SlicerCacheItem.Selected` для каждого элемента по отдельности.
{{% /alert %}}

## **Как обновить срез**
Следующий образец кода загружает [образец файла Excel](67338475.xlsx), содержащий существующий срез, подключенный к сводной таблице. Он выбирает только элементы "Blue" и "Pink" среза с помощью `Slicer.selectItems(labels, false)` — сводная таблица пересчитывается напрямую из элементов фильтра, без ручного вызова `Slicer.refresh()`. Затем он сохраняет рабочую книгу как [выходной файл Excel](67338476.xlsx). На следующем скриншоте показано влияние образца кода на образец файла Excel. Как видно на скриншоте, сводная таблица отображает только отфильтрованные элементы.
![todo:image_alt_text](updating-slicer_1.png)

## **Образец кода**
Замените текущее выделение (выбранными остаются только указанные метки) и пересчитайте связанную сводную таблицу или таблицу:

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], false);
// Save the modified workbook.
wb.save("out.xlsx");
```

Сохраните текущие выбранные метки и дополнительно выберите другие элементы:

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Отмените выбор части выбранных элементов:

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Удалите фильтр (выберите все элементы):

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="nodejs-cpp" >}}