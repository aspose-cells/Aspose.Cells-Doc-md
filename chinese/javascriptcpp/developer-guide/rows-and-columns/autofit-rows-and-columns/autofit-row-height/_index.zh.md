---
title: 加载文件时自动调整行高，使用JavaScript通过C++
linktitle: 在加载文件时自动调整行高
type: docs
weight: 120
url: /zh/javascript-cpp/autofit-row-height/
description: 学习如何在使用Aspose.Cells for Java脚本通过C++加载文件时调整非自定义高度的行。
keywords: 加载文件时自动调整行高，使用JavaScript通过C++，自动调整行高以打开Excel文件，使用JavaScript通过C++ 
---

## **可能的使用场景**
行高会自动匹配内容的字体，但当缓存的行高与文件中的内容高度不一致时，MS Excel在加载文件时会自动调整行高，而Aspose.Cells for Java脚本通过C++不会自动调整以提高性能。如果需要使用Aspose.Cells程序在加载文件时自动匹配行高，可以通过参数[autoFitterOptions(AutoFitterOptions)]实现。

请参考以下图片数据。可以观察到第11行的缓存行高为15，但Excel在加载文件时自动调整了行高。
<br>
<img src="1.png" width=70% />

## **使用Aspose.Cells for Java脚本通过C++调整行高**
如果直接加载文件并保存为PDF，数据可能无法全部显示在PDF中，因为其缓存行高仅为15。
<br>
<img src="2.png" width=70% />
<br>
如果在加载文件时将参数[autoFitterOptions(AutoFitterOptions)]设置为true，则Aspose.Cells会自动调整行高。调整后的行高能有效满足文本显示需求。
<br>
<img src="3.png" width=70% />

## **JavaScript示例代码**

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
