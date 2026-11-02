---
title: Обновление среза с помощью Golang через C++
linktitle: Обновление среза
type: docs
weight: 50
url: /ru/go-cpp/updating-slicer/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Эта статья показывает, как обновить срез, чтобы фильтровать данные связанной сводной таблицы или таблицы с помощью API Aspose.Cells for Go via C++.
keywords: Aspose.Cells Go via C++ обновление среза, Go как изменить срез, как отфильтровать сводную таблицу срезом в Go, Slicer SelectItems, Slicer ClearFilter, Slicer UnselectItems.
---

## **Возможные сценарии использования**
Обновление среза означает фильтрацию данных сводной таблицы или таблицы, к которой подключен срез. Когда вы выбираете или отменяете выбор элементов среза в Microsoft Excel, связанная сводная таблица или таблица пересчитывается соответствующим образом. С Aspose.Cells for Go via C++ вам не нужно перебирать элементы кэша среза и обновлять срез вручную — метод [**Slicer.SelectItems(labels, append)**](https://reference.aspose.com/cells/go-cpp/slicer/) обновляет срез и пересчитывает связанную сводную таблицу или таблицу напрямую из элементов фильтра:
- `Slicer.SelectItems(labels, append)` — выбирает указанные метки и пересчитывает связанную сводную таблицу или таблицу. Если `append` равно `true`, изначально выбранные метки сохраняются, а указанные метки добавляются к выделению; если `append` равно `false`, все исходные выделения сбрасываются и выбранными остаются только указанные метки.
- `Slicer.UnselectItems(labels)` — отменяет выбор части выбранных элементов.
- `Slicer.ClearFilter()` — удаляет фильтр и выбирает все элементы.

{{% alert color="primary" %}}
Начиная с версии Aspose.Cells for Go via C++ 26.10, свойство `SlicerCacheItem.Selected` становится доступным только для чтения, и его сеттер больше не поддерживается. Используйте методы `Slicer.SelectItems`, `Slicer.UnselectItems` и `Slicer.ClearFilter` вместо установки `SlicerCacheItem.Selected` для каждого элемента по отдельности.
{{% /alert %}}

## **Как обновить срез**
Следующий образец кода загружает [образец файла Excel](67338475.xlsx), содержащий существующий срез, подключенный к сводной таблице. Он выбирает только элементы "Blue" и "Pink" среза с помощью `Slicer.SelectItems(labels, false)` — сводная таблица пересчитывается напрямую из элементов фильтра, без ручного вызова `Slicer.Refresh()`. Затем он сохраняет рабочую книгу как [выходной файл Excel](67338476.xlsx). На следующем скриншоте показано влияние образца кода на образец файла Excel. Как видно на скриншоте, сводная таблица отображает только отфильтрованные элементы.
![todo:image_alt_text](updating-slicer_1.png)

## **Образец кода**
Замените текущее выделение (выбранными остаются только указанные метки) и пересчитайте связанную сводную таблицу или таблицу:

```go
package main

import (
    "fmt"

    . "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)

func main() {
    // Load sample Excel file containing slicer.
    wb, _ := NewWorkbook_String("sampleUpdatingSlicer.xlsx")

    // Access first worksheet.
    wss, _ := wb.GetWorksheets()
    ws, _ := wss.Get_Int(0)

    // Access the first slicer inside the slicer collection.
    slicers, _ := ws.GetSlicers()
    slicer, _ := slicers.Get_Int(0)

    // Select only "Blue" and "Pink"; the linked pivot table or table
    // is recalculated directly from the filter items.
    slicer.SelectItems([]string{ "Blue", "Pink" }, false)

    // Save the modified workbook.
    wb.Save_String("out.xlsx")

    fmt.Println("Slicer updated and workbook saved successfully!")
}
```

Сохраните текущие выбранные метки и дополнительно выберите другие элементы:

```go
// Keep the current selection and add "Red" to it.
slicer.SelectItems([]string{ "Red" }, true)
```

Отмените выбор части выбранных элементов:

```go
// Remove "Pink" from the current selection.
slicer.UnselectItems([]string{ "Pink" })
```

Удалите фильтр (выберите все элементы):

```go
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter()
```

{{< app/cells/assistant language="go" >}}