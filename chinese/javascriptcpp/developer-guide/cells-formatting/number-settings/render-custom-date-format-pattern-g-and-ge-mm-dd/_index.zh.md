---
title: 以自定义日期格式模式g和ge.mm.dd呈现
linktitle: 以自定义日期格式模式g和ge.mm.dd呈现  
description: 了解如何通过C++在Aspose.Cells for JavaScript中呈现自定义日期格式模式 g 和 ge ，以控制电子表格中的日期显示。  
keywords: Aspose.Cells，JavaScript库，电子表格，自定义日期格式，渲染，模式 g ，模式 ge ，控制显示    
type: docs  
weight: 160  
url: /zh/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/  
---  

{{% alert color="primary" %}}  

Aspose.Cells现在能够呈现类似于g、ge.mm.dd等自定义日期格式模式。请查看附加的源Excel文件(5112361.xlsx)和Aspose.Cells转换的PDF(5112360.pdf)作为参考。

{{% /alert %}}  

下面的示例代码将转换包含类似于g和ge.mm.dd的自定义格式模式的源Excel文件(5112361.xlsx)成为输出PDF(5112360.pdf)。  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomDateFormat_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
