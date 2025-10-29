---
title: Освобождение неуправляемых ресурсов рабочей книги с помощью JavaScript через C++
linktitle: Освобождение неуправляемых ресурсов книги
type: docs
weight: 310
url: /ru/javascript-cpp/release-unmanaged-resources-of-the-workbook/
description: Узнайте, как освобождать неуправляемые ресурсы объекта Workbook с использованием Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) метод для освобождения неуправляемых ресурсов объекта [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). Шаблон dispose используется только для объектов, получающих доступ к неуправляемым ресурсам, таким как дескрипторы файлов и каналов, дескрипторы реестра, дескрипторы ожидания или указатели на блоки неуправляемой памяти. Это потому, что сборщик мусора очень эффективен в освобождении неиспользуемых управляемых объектов, но не способен освобождать неуправляемые объекты.

{{% /alert %}}

Объект [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) теперь реализует интерфейс *System.IDisposable*, который имеет один метод [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--). Вы можете вызвать метод [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) напрямую или воспользоваться оператором *Using* для автоматического вызова этого метода.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Dispose Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create workbook object
            const wb1 = new Workbook();

            // Call Dispose method
            wb1.dispose();

            // Call Dispose method via a scoped approach
            (async () => {
                const wb2 = new Workbook();
                // Any other code goes here
                wb2.dispose();
            })();

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully!</p>';
        });
    </script>
</html>
```
