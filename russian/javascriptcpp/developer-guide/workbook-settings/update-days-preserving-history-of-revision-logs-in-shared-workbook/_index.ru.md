---
title: Обновление дней с сохранением истории журналов изменений в совместной рабочей книге с помощью JavaScript через C++
linktitle: Обновление дней, сохраняющих историю журналов версий в общей книге
type: docs
weight: 80
url: /ru/javascript-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Узнайте, как обновить количество дней для сохранения истории журнала изменений в совместных рабочих книгах с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**

Когда вы делитесь рабочей книгой, появляется опция ***Сохранить историю изменений на N дней***, как показано на следующем скриншоте. Вы можете обновить количество дней для сохранения истории, используя Aspose.Cells for JavaScript через C++ с помощью свойства [**WorksheetCollection.daysPreservingHistory**](https://reference.aspose.com/cells/javascript-cpp/revisionlogcollection/#daysPreservingHistory--).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Обновление дней, сохраняющих историю журналов версий в общей книге**

В следующем образце кода создается пустая книга, затем ее делят и обновляются журналы ревизии для сохранения истории на 7 дней, что обычно составляет 30 дней. Пожалуйста, обратитесь к [выходному файлу Excel](60489773.xlsx), созданному кодом в качестве справки.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Shared Workbook</title>
    </head>
    <body>
        <h1>Shared Workbook - DaysPreservingHistory Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Shared Workbook</button>
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
            // Create empty workbook
            const workbook = new Workbook();

            // Share the workbook
            workbook.settings.shared = true;

            // Update DaysPreservingHistory of RevisionLogs
            workbook.worksheets.revisionLogs.daysPreservingHistory = 7;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputShared_DaysPreservingHistory.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and configured. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
