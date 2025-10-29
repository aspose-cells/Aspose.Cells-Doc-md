---
title: Автоматическая подстройка высоты строки при загрузке файла с помощью JavaScript через C++
linktitle: Автоматическое подгонение высоты строки при загрузке файла
type: docs
weight: 120
url: /ru/javascript-cpp/autofit-row-height/
description: узнайте, как подогнать высоту строк с нестандартной высотой при загрузке файла с помощью Aspose.Cells for JavaScript через C++.
keywords: Автоподгонка высоты строки при загрузке файла с помощью JavaScript через C++, автоматическая настройка высоты строки при открытии файла Excel с помощью JavaScript через C++ 
---

## **Возможные сценарии использования**
Высота строки автоматически соответствует размеру шрифта содержимого, но когда высота кэшированной строки не совпадает с высотой содержимого в файле, MS Excel автоматически регулирует высоту строки при загрузке файла, в то время как Aspose.Cells for JavaScript через C++ этого делать не будет для повышения производительности. Если необходимо, чтобы программа Aspose.Cells автоматически совпадала с высотой строк при загрузке файлов, это можно реализовать через параметр [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) в вашем коде.

Пожалуйста, ознакомьтесь с изображением ниже. Наблюдается, что кешированная высота строки в строке 11 составляет 15, но Excel автоматически подогнал высоту строки при загрузке файла.
<br>
<img src="1.png" width=70% />

## **Настройка высоты строки с помощью Aspose.Cells for JavaScript через C++**
Если вы напрямую загрузите файл и сохраните его как PDF, данные не будут полностью отображаться в PDF, поскольку кешированная высота строки равна только 15.
<br>
<img src="2.png" width=70% />
<br>
Если установить параметр [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) в true при загрузке файла, тогда Aspose.Cells автоматически подгонит высоту строки. Подогнанная высота строки эффективно отвечает требованиям отображения текста.
<br>
<img src="3.png" width=70% />

## **Пример кода на JavaScript**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LoadOptions & AutoFitter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none;">Download out.pdf</a>
        </div>
        <div>
            <a id="downloadLink2" style="display: none;">Download out2.pdf</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, AutoFitterOptions } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const downloadLink1 = document.getElementById('downloadLink1');
            const downloadLink2 = document.getElementById('downloadLink2');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const data = new Uint8Array(arrayBuffer);

            // Load workbook and save as out.pdf
            const workbook = new Workbook(data);
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            downloadLink1.href = URL.createObjectURL(blob);
            downloadLink1.download = 'out.pdf';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download out.pdf';

            // Prepare LoadOptions with AutoFitterOptions and onlyAuto = true
            const loadOptions = new LoadOptions();
            loadOptions.autoFitterOptions = new AutoFitterOptions();
            loadOptions.autoFitterOptions.onlyAuto = true;

            // Load workbook with loadOptions and save as out2.pdf
            const book = new Workbook(data, loadOptions);
            const outputData2 = book.save(SaveFormat.Pdf);
            const blob2 = new Blob([outputData2], { type: 'application/pdf' });
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'out2.pdf';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download out2.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download links to get the generated PDF files.</p>';
        });
    </script>
</html>
```
