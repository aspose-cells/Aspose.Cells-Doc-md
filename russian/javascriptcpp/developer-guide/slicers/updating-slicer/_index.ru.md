---
title: Обновление среза с помощью JavaScript через C++
linktitle: Обновление среза
type: docs
weight: 50
url: /ru/javascript-cpp/updating-slicer/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Эта статья показывает, как обновить срез, чтобы фильтровать данные связанной сводной таблицы или таблицы с помощью Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells JavaScript via C++, обновление среза JavaScript, как изменить срез в JavaScript, как отфильтровать сводную таблицу срезом в JavaScript, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
---

## **Возможные сценарии использования**
Обновление среза означает фильтрацию данных сводной таблицы или таблицы, к которой подключен срез. Когда вы выбираете или снимаете выбор с элементов среза в Microsoft Excel, связанная сводная таблица или таблица пересчитывается соответствующим образом. С Aspose.Cells for JavaScript via C++ вам не нужно перебирать элементы кэша среза и обновлять срез вручную — метод [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/javascript-cpp/slicer/) обновляет срез и пересчитывает связанную сводную таблицу или таблицу напрямую из элементов фильтра:
- `Slicer.selectItems(labels, append)` — выбирает указанные метки и пересчитывает связанную сводную таблицу или таблицу. Если `append` равно `true`, изначально выбранные метки сохраняются, а указанные метки добавляются к выделению; если `append` равно `false`, все исходные выделения сбрасываются и выбранными остаются только указанные метки.
- `Slicer.unselectItems(labels)` — отменяет выбор части выбранных элементов.
- `Slicer.clearFilter()` — удаляет фильтр и выбирает все элементы.

{{% alert color="primary" %}}
Начиная с версии Aspose.Cells for JavaScript via C++ 26.10, свойство `SlicerCacheItem.selected` становится доступным только для чтения, и его сеттер больше не поддерживается. Используйте методы `Slicer.selectItems`, `Slicer.unselectItems` и `Slicer.clearFilter` вместо установки `SlicerCacheItem.selected` для каждого элемента по отдельности.
{{% /alert %}}

## **Как обновить срез**
Следующий образец кода загружает [образец файла Excel](67338475.xlsx), содержащий существующий срез, подключенный к сводной таблице. Он выбирает только элементы "Blue" и "Pink" среза с помощью `Slicer.selectItems(labels, false)` — сводная таблица пересчитывается напрямую из элементов фильтра, без ручного вызова `Slicer.refresh()`. Затем он сохраняет рабочую книгу как [выходной файл Excel](67338476.xlsx). На следующем скриншоте показано влияние образца кода на образец файла Excel. Как видно на скриншоте, сводная таблица отображает только отфильтрованные элементы.
![todo:image_alt_text](updating-slicer_1.png)

## **Образец кода**
Замените текущее выделение (выбранными остаются только указанные метки) и пересчитайте связанную сводную таблицу или таблицу:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update Slicer</title>
    </head>
    <body>
        <h1>Update Slicer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Select only "Blue" and "Pink"; the linked pivot table or table
            // is recalculated directly from the filter items
            slicer.selectItems(["Blue", "Pink"], false);

            // Save modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Сохраните текущие выбранные метки и дополнительно выберите другие элементы:

```javascript
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Отмените выбор части выбранных элементов:

```javascript
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Удалите фильтр (выберите все элементы):

```javascript
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="javascript-cpp" >}}