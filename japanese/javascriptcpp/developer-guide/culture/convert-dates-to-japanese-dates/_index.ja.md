---
title: JavaScriptを介してC++で日付を日本語日付に変換
linktitle: 日本の日付への変換
type: docs
weight: 350
url: /ja/javascript-cpp/convert-dates-to-japanese-dates/
description: Aspose.Cells for JavaScriptを使用して、西暦日を日本の日付に変換する方法を学びます。
---  

{{% alert color="primary" %}}  

日本のカレンダーでは、新しい天皇の即位とともに新しい元号が始まります。2019年5月1日に新しい天皇が即位し、平成時代が終了し令和時代が始まりました。  

{{% /alert %}}  

Aspose.Cellsは、西暦日付を日本の元号に変換する方法を提供します。この変換では、元号の変化も考慮されます。次のコードスニペットは、西暦日付を含む[源のExcel](90112015.xlsx)ファイルを日本の和暦付きの[出力PDF](90112016.pdf)に変換します。画像の例も示します。  

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
