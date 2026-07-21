---
title: Отключить ленту сводных таблиц
type: docs
weight: 90
url: /ru/javascript-cpp/disable-pivot-table-ribbons/
description: Как отключить ленты сводных таблиц с помощью Aspose.Cells for JavaScript для C++.
keywords: Aspose.Cells for JavaScript для C++ Excel, библиотека Excel JavaScript через C++, отключение лент сводных таблиц с помощью Aspose.Cells for JavaScript для C++ Excel Library.
---

{{% alert color="primary" %}}

Отчеты на основе сводных таблиц полезны, но могут быть подвержены ошибкам, если целевые пользователи не обладают подробными знаниями Excel для настройки этих отчетов. В таких случаях организации захотят ограничить возможность пользователей изменять отчет на основе сводной таблицы. Общие функции сводных таблиц, такие как добавление дополнительных фильтров, слайсеров, полей или изменение порядка элементов в отчете, в большинстве случаев не рекомендуется предоставлять всем пользователям. С другой стороны, эти пользователи должны иметь возможность обновлять отчет и использовать существующие фильтры или слайсеры. Aspose.Cells for JavaScript для C++ предоставляет разработчикам такую возможность для ограничения пользователей в изменении этих отчетов при их создании. Для этой цели Excel предоставляет функцию для отключения ленты сводных таблиц, и такую же функцию предоставляет Aspose.Cells for JavaScript для C++, т.е. разработчик может отключить ленту, которая содержит инструменты для изменения этих отчетов.

{{% /alert %}}

## **Как отключить ленту сводных таблиц с помощью Aspose.Cells for JavaScript для C++**

Следующий код демонстрирует эту функцию, получая доступ к сводной таблице из листа, а затем устанавливая [**enableWizard**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#enableWizard-boolean-) в **false**. Образец файла сводной таблицы можно скачать по этой [ссылке](pivot_table_test.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Pivot Table Wizard Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiating a Workbook object by opening the Excel file through the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the pivot table in the first sheet
            const pt = workbook.worksheets.get(0).pivotTables.get(0);

            // Disable ribbon for this pivot table
            pt.enableWizard = false;

            // Save output file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table wizard disabled successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
