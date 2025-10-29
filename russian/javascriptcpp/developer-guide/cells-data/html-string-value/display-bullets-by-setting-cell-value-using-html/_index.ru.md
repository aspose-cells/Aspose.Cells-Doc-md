---
title: Отображение маркеров, устанавливая значение ячейки с использованием HTML
type: docs
weight: 130
url: /ru/javascript-cpp/display-bullets-by-setting-cell-value-using/
description: Добавьте маркеры в ячейки Excel с помощью HTML и простого в использовании Aspose.Cells for JavaScript через C++ API.
keywords: добавляйте маркеры в Excel JavaScript через C++, отображайте маркеры в Excel JavaScript через C++, добавляйте маркеры в Excel с HTML JavaScript через C++, отображайте маркеры в Excel с HTML JavaScript через C++, добавляйте маркеры в Excel, используя HTML JavaScript через C++
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает отображение маркеров с помощью HTML-кода. Эта статья объяснит, как отображать маркеры, устанавливая значение ячейки с помощью HTML. Мы используем метод [**Cell.htmlString(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-) для установки значения ячейки с нашим HTML.

{{% /alert %}}

## JavaScript код для отображения маркеров с помощью установки значения ячейки через HTML

Следующий код использует HTML-код для установки значения ячейки. После запуска этого кода вы получите вывод, как показано на изображении ниже.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Bullets In Cells</title>
    </head>
    <body>
        <h1>Bullets In Cells Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set the HTML string (converted from setHtmlString -> htmlString property)
            cell.htmlString = "<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>";

            // Auto fit the Columns
            worksheet.autoFitColumns();

            // Save the workbook to a Blob and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'BulletsInCells_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File: BulletsInCells_out.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## Вывод, созданный образцовым кодом

На следующем скриншоте показан вывод вышеприведенного образца кода.

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
