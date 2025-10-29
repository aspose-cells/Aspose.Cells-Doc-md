---
title: Автоматическое обновление OLE объекта через Microsoft Excel с помощью Aspose.Cells for JavaScript через C++
linktitle: Автоматическое обновление объекта OLE через Microsoft Excel с помощью Aspose.Cells
type: docs
weight: 270
url: /ru/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Узнайте, как автоматически обновлять OLE объекты в Excel с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}  
Aspose.Cells предоставляет свойство [**OleObject.autoLoad**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#autoLoad--) для обновления объекта OLE при открытии файла Excel в Microsoft Excel. Благодаря этому свойству объект OLE будет отображать правильное изображение OLE, созданное Microsoft Excel.  
{{% /alert %}}  

Следующий образец кода загружает [образец файла Excel](5115231.xlsx), который содержит ненастоящее изображение OLE. Объект OLE на самом деле является документом Microsoft Word, но образец файла Excel показывает изображение животного вместо изображения Microsoft Word. Но если вы откроете [выходной файл Excel](5115225.xlsx), вы увидите, что Microsoft Excel отображает правильное изображение OLE.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh OLE Objects Example</title>
    </head>
    <body>
        <h1>Refresh OLE Objects Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Set auto load property of first ole object to true
            sheet.oleObjects.get(0).autoLoad = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RefreshOLEObjects_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">OLE object autoLoad set to true. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
