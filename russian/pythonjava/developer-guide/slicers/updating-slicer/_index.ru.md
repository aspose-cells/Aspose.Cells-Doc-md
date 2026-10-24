---
title: Обновление среза
linktitle: Обновление среза
type: docs
weight: 60
url: /ru/python-java/updating-slicer/
description: Эта статья показывает, как обновить срез, чтобы фильтровать данные связанной сводной таблицы или таблицы с помощью API Aspose.Cells for Python via Java.
keywords: Aspose.Cells for Python via Java обновление среза, Python Java обновление среза, как отфильтровать сводную таблицу срезом в Python, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Обновление среза**
Обновление среза означает фильтрацию данных сводной таблицы или таблицы, к которой подключен срез. Aspose.Cells for Python via Java обновляет срез и пересчитывает связанную сводную таблицу или таблицу напрямую из элементов фильтра:
- `Slicer.selectItems(labels, append)` — выбирает указанные метки и пересчитывает связанную сводную таблицу или таблицу. Если `append` равно `True`, изначально выбранные метки сохраняются, а указанные метки добавляются к выделению; если `append` равно `False`, все исходные выделения сбрасываются и выбранными остаются только указанные метки.
- `Slicer.unselectItems(labels)` — отменяет выбор части выбранных элементов.
- `Slicer.clearFilter()` — удаляет фильтр и выбирает все элементы.

{{% alert color="primary" %}}
Начиная с версии Aspose.Cells for Python via Java 26.10, свойство `SlicerCacheItem.Selected` становится доступным только для чтения, и его сеттер больше не поддерживается. Используйте методы `Slicer.selectItems`, `Slicer.unselectItems` и `Slicer.clearFilter` вместо установки `SlicerCacheItem.Selected` для каждого элемента по отдельности.
Следующий фрагмент кода загружает [образец файла Excel](106365050.xlsx), содержащий срез, подключенный к сводной таблице. Он выбирает только элементы "Blue" и "Pink" среза с помощью `Slicer.selectItems(labels, False)` — сводная таблица пересчитывается напрямую из элементов фильтра, без ручного вызова `Slicer.refresh()`. Затем он сохраняет рабочую книгу как [выходной файл Excel](106365051.xlsx). На следующем скриншоте показано влияние образца кода на образец файла Excel. Как видно на скриншоте, сводная таблица отображает только отфильтрованные элементы.
![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
{{% /alert %}}

## **Образец кода**
Замените текущее выделение (выбранными остаются только указанные метки) и пересчитайте связанную сводную таблицу или таблицу:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Load sample Excel file containing slicer.
workbook = Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.getWorksheets().get(0)
# Access the first slicer inside the slicer collection.
slicer = worksheet.getSlicers().get(0)
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
jpype.shutdownJVM()
```

Сохраните текущие выбранные метки и дополнительно выберите другие элементы:

```python
# Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], True)
```

Отмените выбор части выбранных элементов:

```python
# Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"])
```

Удалите фильтр (выберите все элементы):

```python
# Clear the filter; all slicer items become selected again.
slicer.clearFilter()
```

{{< app/cells/assistant language="python" >}}