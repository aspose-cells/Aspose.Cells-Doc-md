---
title: Сравнение и миграция с помощью JavaScript через C++
linktitle: Сравнение и миграция
type: docs
weight: 250
url: /ru/javascript-cpp/comparison-migration/
description: Изучите различия и стратегию миграции для использования Aspose.Cells с JavaScript через C++.
keywords: Сравнение Aspose.Cells JavaScript C++, миграция с .NET на JavaScript через C++
---

## **Сравнение между .NET и JavaScript через C++**

При переходе с Aspose.Cells for .NET на Aspose.Cells for JavaScript через C++ необходимо учитывать определенные различия в структуре библиотеки, синтаксисе и функциональности. Ниже приведено сравнение, чтобы помочь вам понять эти различия.

### **1. Инициализация**
В .NET объекты часто инициализируются через конструкторы. В JavaScript через C++ обычно создаются экземпляры с использованием ключевого слова `new`, встроенного в синтаксис JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Workbook Creation Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook (or load selected file)</button>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
                document.getElementById('result').innerHTML = '<p style="color: green;">Loaded workbook from selected file.</p>';
            } else {
                workbook = new Workbook();
                document.getElementById('result').innerHTML = '<p style="color: green;">Created a new empty workbook.</p>';
            }

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

### **2. Доступ к листам**
В .NET вы можете увидеть такой код для доступа к листу:
