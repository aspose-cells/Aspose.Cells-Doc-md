---
title: Удаление слайсера с помощью JavaScript через C++
linktitle: Удаление срезки
type: docs
weight: 30
url: /ru/javascript-cpp/removing-slicer/
---

## **Возможные сценарии использования**

Если вы хотите удалить сегментатор в Excel, просто выберите его и нажмите кнопку *Delete*. Аналогично, чтобы удалить его программным путём через API Aspose.Cells, используйте метод [**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/javascript-cpp/slicercollection/#remove-slicer-). Он удалит сегментатор с листа.

## **Удаление срезки**

Следующий пример кода загружает [пример файла Excel](67338478.xlsx), содержащий существующий сегментатор. Он обращается к сегментаторам, затем удаляет его и сохраняет книгу как [выходной файл Excel](67338477.xlsx). На изображении ниже показан сегментатор, который будет удалён после выполнения примера.

![todo:image_alt_text](removing-slicer_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Removing Slicer Example</title>
    </head>
    <body>
        <h1>Removing Slicer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        const asposeReady = AsposeCells.onReady({
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

            await asposeReady;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection.
            const slicer = worksheet.slicers.get(0);

            // Remove slicer.
            worksheet.slicers.remove(slicer);

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRemovingSlicer.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
