---
title: Обновление слайсера с помощью JavaScript через C++
linktitle: Обновление срезки
type: docs
weight: 50
url: /ru/javascript-cpp/updating-slicer/
description: В этой статье показано, как обновлять связные сводные таблицы, обновляя слайсер с помощью Aspose.Cells for JavaScript через C++.
keywords: Aspose.Cells JavaScript через C++, обновление слайсера JavaScript, как изменить слайсер JavaScript, как настроить слайсер в JavaScript, как выбрать или отменить выбор элементов слайсера JavaScript через C++.
---

## **Возможные сценарии использования**

Если хотите обновить сегментатор в Microsoft Excel, выберите или отмените выбор его элементов, и он обновит таблицу сегментатора или сводную таблицу соответственно. Используйте [**Slicer.slicerCacheItems**](https://reference.aspose.com/cells/javascript-cpp/slicercache/#slicerCacheItems--) для выбора или снятия выбора элементов сегментатора с помощью Aspose.Cells, затем вызовите метод [**Slicer.refresh()**](https://reference.aspose.com/cells/javascript-cpp/slicer/#refresh--) для обновления таблицы сегментатора или сводной таблицы.

## **Как обновить фильтр**

Следующий образец кода загружает [образец файла Excel](67338475.xlsx), содержащий существующий фильтр. Он отменяет выбор 2-го и 3-го элементов фильтра и обновляет фильтр. Затем сохраняет рабочую книгу в [выходной файл Excel](67338476.xlsx). На следующем скриншоте показан эффект образца кода на образцовый файл Excel. Как вы можете видеть на скриншоте, обновление фильтра с выбранными элементами также обновило сводную таблицу соответственно.

![todo:image_alt_text](updating-slicer_1.png)

## **Образец кода**

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
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Access the slicer items via slicer cache
            const items = slicer.slicerCache.slicerCacheItems;

            // Iterate items and deselect "Pink" and "Green"
            for (let i = 0; i < items.count; i++) {
                const item = items.get(i);
                if (item.value === "Pink" || item.value === "Green") {
                    item.selected = false;
                }
            }

            // Refresh slicer to apply changes
            slicer.refresh();

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
