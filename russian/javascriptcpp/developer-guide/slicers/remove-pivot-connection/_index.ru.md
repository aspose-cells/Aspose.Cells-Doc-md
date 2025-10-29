---
title: Удаление соединения оси с помощью JavaScript через C++
linktitle: Удалить связь сводной таблицы
type: docs
weight: 30
url: /ru/javascript-cpp/remove-pivot-connection/
description: Узнайте, как удалить соединение оси с помощью Aspose.Cells for JavaScript через C++.
keywords: Удалите соединение оси без Office 2013, Office 2016, Office 2019 и Office 365 с помощью JavaScript через C++.
---

## **Возможные сценарии использования**

Если вы хотите отвязать слайсер и сводную таблицу в Excel, щелкните правой кнопкой мыши по слайсеру и выберите пункт "Соединения отчета...". В списке опций установите или снимите флажок. Аналогично, чтобы программно отвязать слайсер и сводную таблицу с помощью API Aspose.Cells for JavaScript через C++, используйте метод [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#removePivotConnection-pivottable-). Он отвяжет слайсер и сводную таблицу.

## **Отсоединить срезку и сводную таблицу**

Следующий пример кода загружает [пример файла Excel](remove-pivot-connection.xlsx), содержащий существующий сегментатор. Он обращается к сегментаторам и затем разрывает связь сегментатора и сводной таблицы. В конце он сохраняет рабочую книгу как [выходной файл Excel](remove-pivot-connection-out.xlsx).

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Connection</title>
    </head>
    <body>
        <h1>Remove Pivot Connection Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first PivotTable inside the PivotTable collection.
            const pivotTable = worksheet.pivotTables.get(0);

            // Access the first slicer inside the slicer collection.
            const slicer = worksheet.slicers.get(0);

            // Remove PivotTable connection.
            slicer.removePivotConnection(pivotTable);

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'remove-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
