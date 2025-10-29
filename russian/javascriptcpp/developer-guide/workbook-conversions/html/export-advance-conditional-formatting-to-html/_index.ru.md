---
title: Экспорт условий форматирования DataBar, ColorScale и IconSet при преобразовании Excel в HTML с помощью JavaScript через C++
linktitle: Экспорт условного форматирования данных, цветовой шкалы и набора значков при преобразовании Excel в HTML
type: docs
weight: 30
url: /ru/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
---

{{% alert color="primary" %}} 

Вы можете экспортировать условия форматирования DataBar, ColorScale и IconSet при преобразовании файла Excel в HTML. Эта функция частично поддерживается Microsoft Excel, но Aspose.Cells for JavaScript через C++ поддерживает её полностью.

{{% /alert %}}  

## **Экспорт условного форматирования данных, цветовой шкалы и набора значков при преобразовании Excel в HTML**  
Следующий скриншот показывает [образец excel файла](5115558.xlsx) с форматированием условного оформления DataBar, ColorScale и IconSet. Вы можете скачать [образец excel файла](5115558.xlsx) по данной ссылке.  

![todo:image_alt_text](conversion_1.png)  

Следующий скриншот показывает вывод Aspose.Cells в виде HTML файла с форматированием условного оформления DataBar, ColorScale и IconSet. Как видите, он выглядит точно так же, как и [образец excel файла](5115558.xlsx).  

![todo:image_alt_text](conversion_2.png)  

### **Образец кода**  
Следующий пример кода преобразует пример файла Excel в HTML, это простое [преобразование Excel в HTML](/cells/ru/javascript-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Converting Excel to HTML Example</h1>
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

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in HTML format
            const outputData = workbook.save(SaveFormat.Html);

            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToHTMLFiles_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
