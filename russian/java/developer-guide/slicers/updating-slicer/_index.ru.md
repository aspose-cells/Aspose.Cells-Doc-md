---
title: Обновление среза
linktitle: Обновление среза
type: docs
weight: 50
url: /ru/java/updating-slicer/
description: Эта статья показывает, как обновить срез, чтобы фильтровать данные связанной сводной таблицы или таблицы с помощью API Aspose.Cells for Java.
keywords: Aspose.Cells Java обновление среза, Java как изменить срез, как отфильтровать сводную таблицу срезом в Java, Java Slicer selectItems, Java Slicer clearFilter, Java Slicer unselectItems.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Обновление среза означает фильтрацию данных сводной таблицы или таблицы, к которой подключен срез. Когда вы выбираете или отменяете выбор элементов среза в Microsoft Excel, связанная сводная таблица или таблица пересчитывается соответствующим образом. С Aspose.Cells for Java вам не нужно перебирать элементы кэша среза и обновлять срез вручную — метод [Slicer.selectItems(String[], boolean)](https://reference.aspose.com/cells/java/com.aspose.cells/slicer/#selectItems-java.lang.String---boolean-) обновляет срез и пересчитывает связанную сводную таблицу или таблицу напрямую из элементов фильтра:
- `Slicer.selectItems(labels, append)` — выбирает указанные метки и пересчитывает связанную сводную таблицу или таблицу. Если `append` равно `true`, изначально выбранные метки сохраняются, а указанные метки добавляются к выделению; если `append` равно `false`, все исходные выделения сбрасываются и выбранными остаются только указанные метки.
- `Slicer.unselectItems(labels)` — отменяет выбор части выбранных элементов.
- `Slicer.clearFilter()` — удаляет фильтр и выбирает все элементы.

{{% alert color="primary" %}}
Начиная с версии Aspose.Cells for Java 26.10, свойство `SlicerCacheItem.Selected` становится доступным только для чтения, и его сеттер больше не поддерживается. Используйте методы `Slicer.selectItems`, `Slicer.unselectItems` и `Slicer.clearFilter` вместо установки `SlicerCacheItem.Selected` для каждого элемента по отдельности.
{{% /alert %}}

## **Обновление среза**
Следующий образец кода загружает [образец файла Excel](67338506.xlsx), содержащий существующий срез, подключенный к сводной таблице. Он выбирает только элементы "Blue" и "Pink" среза с помощью `Slicer.selectItems(labels, false)` — сводная таблица пересчитывается напрямую из элементов фильтра, без ручного вызова `Slicer.refresh()`. Затем он сохраняет рабочую книгу как [выходной файл Excel](67338505.xlsx). На следующем скриншоте показано влияние образца кода на образец файла Excel. Как видно на скриншоте, сводная таблица отображает только отфильтрованные элементы.
![todo:image_alt_text](updating-slicer_1.png)

## **Образец кода**
Замените текущее выделение (выбранными остаются только указанные метки) и пересчитайте связанную сводную таблицу или таблицу:

```java
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
import com.aspose.cells.Slicer;
// Load sample Excel file containing slicer.
Workbook workbook = new Workbook("sampleUpdatingSlicer.xlsx");
// Access first worksheet.
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
Slicer slicer = worksheet.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(new String[] { "Blue", "Pink" }, false);
// Save the modified workbook.
workbook.save("out.xlsx");
```

Сохраните текущие выбранные метки и дополнительно выберите другие элементы:

```java
// Keep the current selection and add "Red" to it.
slicer.selectItems(new String[] { "Red" }, true);
```

Отмените выбор части выбранных элементов:

```java
// Remove "Pink" from the current selection.
slicer.unselectItems(new String[] { "Pink" });
```

Удалите фильтр (выберите все элементы):

```java
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="java" >}}