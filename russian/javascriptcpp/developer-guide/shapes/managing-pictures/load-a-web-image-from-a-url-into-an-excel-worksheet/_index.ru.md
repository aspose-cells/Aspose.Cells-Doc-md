---
title: Загрузить изображение из URL в рабочий лист Excel с помощью JavaScript через C++
linktitle: Загрузка веб изображения из URL в рабочий лист Excel
type: docs
weight: 30
url: /ru/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: Как преобразовать изображение из URL в фактическое изображение Excel с помощью Aspose.Cells for JavaScript через C++.
keywords: excel показывает изображение из url, excel url к изображению, показывать изображение в excel из url, вставка изображения из url в excel, преобразование url в изображение в excel, excel изображение из url, загрузка изображения из url в excel, JavaScript, Excel
---

## Загрузка изображения из URL в рабочий лист Excel

Aspose.Cells for JavaScript через C++ предоставляет простой и удобный способ загрузки изображений из URL в рабочие листы Excel. В этой статье объясняется, как загружать данные изображений в поток, а затем вставлять их в рабочий лист с помощью API Aspose.Cells. Используя этот метод, изображения становятся частью файла Excel и не загружаются повторно при каждом открытии рабочего листа.

## Образец кода

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert Web Image</title>
    </head>
    <body>
        <h1>Insert Web Image into Excel</h1>
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
                // If no file provided, create a new workbook
                document.getElementById('result').innerHTML = '<p style="color: orange;">No input workbook selected. A new workbook will be created.</p>';
            }

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add("Sheet1");
            }
            const worksheet = workbook.worksheets.get(0);

            // Download the image from the web
            const url = "https://www.aspose.com/Images/aspose-logo.jpg";
            const response = await fetch(url);
            if (!response.ok) {
                document.getElementById('result').innerHTML = `<p style="color: red;">Failed to download image: ${response.status} ${response.statusText}</p>`;
                return;
            }
            const imgArrayBuffer = await response.arrayBuffer();
            const imgBytes = new Uint8Array(imgArrayBuffer);

            // Insert the image into the worksheet at row 0, column 0
            worksheet.pictures.add(0, 0, imgBytes);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'webimagebook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
 В некоторых случаях вы всегда хотите обновленное изображение с URL. Чтобы добиться этого, следуйте инструкциям, приведенным в статье [Вставить привязанное изображение из веб-адреса](/cells/ru/javascript-cpp/insert-a-linked-picture-from-web-address/). Следуя этому методу, изображение загружается с URL каждый раз, когда открывается рабочий лист.
{{% /alert %}}
