---
title: 使用 JavaScript 通过 C++ 将日期转换为日本日期
linktitle: 将日期转换为日本日期
type: docs
weight: 350
url: /zh/javascript-cpp/convert-dates-to-japanese-dates/
description: 学习如何使用Aspose.Cells for JavaScript通过C++将公历日期转换为日本日期。
---  

{{% alert color="primary" %}}  

在日本** **历法中，新的一个时代开始于新天皇的即位。2019年5月1日，新天皇即位，平成时代结束，令和时代开始。  

{{% /alert %}}  

Aspose.Cells 提供一种将公历日期转换为日本日期的方法。在此转换过程中，也考虑了时代的变化。下面的代码片段将包含公历日期的[源Excel](90112015.xlsx)文件转换为带有日本日期的[输出PDF](90112016.pdf)，如下图所示。  

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel with Japanese Dates to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, CountryCode } = AsposeCells;

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

            // Create LoadOptions for XLSX and set language/region to Japan
            const options = new LoadOptions(LoadFormat.Xlsx);
            options.languageCode = CountryCode.Japan;
            options.region = CountryCode.Japan;

            // Instantiate workbook from uploaded file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'JapaneseDates.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
