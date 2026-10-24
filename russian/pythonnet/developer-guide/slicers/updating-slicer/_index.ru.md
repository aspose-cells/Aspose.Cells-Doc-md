---
title: Обновление среза
linktitle: Обновление среза
type: docs
weight: 50
url: /ru/python-net/updating-slicer/
description: Узнайте, как обновить срез, чтобы фильтровать данные связанной сводной таблицы или таблицы с помощью Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, библиотека Python для Excel, Python обновление среза без Excel, фильтрация сводной таблицы срезом в Python, Slicer select_items, Slicer clear_filter.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Обновление среза означает фильтрацию данных сводной таблицы или таблицы, к которой подключен срез. Когда вы выбираете или снимаете выбор с элементов среза в Microsoft Excel, связанная сводная таблица или таблица пересчитывается соответствующим образом. С Aspose.Cells for Python via .NET вам не нужно перебирать элементы кэша среза и обновлять срез вручную — метод [**Slicer.select_items(labels, append)**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/selectitems/) обновляет срез и пересчитывает связанную сводную таблицу или таблицу напрямую из элементов фильтра:
- `Slicer.select_items(labels, append)` — выбирает указанные метки и пересчитывает связанную сводную таблицу или таблицу. Если `append` равно `True`, изначально выбранные метки сохраняются, а указанные метки добавляются к выделению; если `append` равно `False`, все исходные выделения сбрасываются и выбранными остаются только указанные метки.
- `Slicer.unselect_items(labels)` — отменяет выбор части выбранных элементов.
- `Slicer.clear_filter()` — удаляет фильтр и выбирает все элементы.

{{% alert color="primary" %}}
Начиная с версии Aspose.Cells for Python via .NET 26.10, свойство `SlicerCacheItem.selected` становится доступным только для чтения, и его сеттер больше не поддерживается. Используйте методы `Slicer.select_items`, `Slicer.unselect_items` и `Slicer.clear_filter` вместо установки `SlicerCacheItem.selected` для каждого элемента по отдельности.
{{% /alert %}}

## **Как обновить срез с помощью библиотеки Aspose.Cells для Python Excel**
Следующий образец кода загружает [образец файла Excel](67338475.xlsx), содержащий существующий срез, подключенный к сводной таблице. Он выбирает только элементы "Blue" и "Pink" среза с помощью `Slicer.select_items(labels, False)` — сводная таблица пересчитывается напрямую из элементов фильтра, без ручного вызова `Slicer.refresh()`. Затем он сохраняет рабочую книгу как [выходной файл Excel](67338476.xlsx). На следующем скриншоте показано влияние образца кода на образец файла Excel. Как видно на скриншоте, сводная таблица отображает только отфильтрованные элементы.
![todo:image_alt_text](updating-slicer_1.png)

## **Образец кода**
Замените текущее выделение (выбранными остаются только указанные метки) и пересчитайте связанную сводную таблицу или таблицу:

```python
import aspose.cells as ac
# Load sample Excel file containing slicer.
workbook = ac.Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.worksheets[0]
# Access the first slicer inside the slicer collection.
slicer = worksheet.slicers[0]
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.select_items(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
```

Сохраните текущие выбранные метки и дополнительно выберите другие элементы:

```python
# Keep the current selection and add "Red" to it.
slicer.select_items(["Red"], True)
```

Отмените выбор части выбранных элементов:

```python
# Remove "Pink" from the current selection.
slicer.unselect_items(["Pink"])
```

Удалите фильтр (выберите все элементы):

```python
# Clear the filter; all slicer items become selected again.
slicer.clear_filter()
```

{{< app/cells/assistant language="python-net" >}}