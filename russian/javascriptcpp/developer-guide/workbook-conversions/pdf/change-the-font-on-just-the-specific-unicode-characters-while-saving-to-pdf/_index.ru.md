---
title: Измените шрифт только для конкретных символов Юникода при сохранении в PDF с помощью Script Aspose.Cells for Java через C++
linktitle: Изменение шрифта только для определенных символов Unicode при сохранении в PDF
type: docs
weight: 260
url: /ru/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Узнайте, как изменить шрифт для конкретных символов Юникода при сохранении в PDF с помощью Script Aspose.Cells for Java через C++. 
---

{{% alert color="primary" %}} 

Некоторые символы Unicode не могут быть отображены заданным пользователем шрифтом. Один из таких символов Unicode - это **Неразрывный дефис** (U+2011) и его Unicode-номер 8209. Этот символ не может быть отображен шрифтом **Times New Roman**, но его можно отобразить другими шрифтами, такими как **Arial Unicode MS**.

Когда такой символ встречается внутри слова или предложения, которое использует шрифт Times New Roman, Aspose.Cells меняет шрифт всего слова или предложения на шрифт, который может отображать этот символ, например Arial Unicode или MS.

Однако такое поведение нежелательно для некоторых пользователей, и они хотят менять шрифт только для конкретного символа, а не для всего слова или предложения.

Для решения этой проблемы Aspose.Cells предоставляет свойство `PdfSaveOptions.isFontSubstitutionCharGranularity`, которое нужно установить в true, чтобы изменялся шрифт только для тех символов, которые нельзя отобразить, а остальные оставались в исходном шрифте.

{{% /alert %}} 

## **Пример**
На следующем скриншоте сравниваются два выходных PDF-файла, сгенерированных примерным кодом ниже.

Один PDF создается без установки свойства `PdfSaveOptions.isFontSubstitutionCharGranularity`, а другой — после установки этого свойства в true.

Как видно в первом PDF, шрифт всего предложения изменен с Times New Roman на Arial Unicode MS из-за тире, неразрывного. Во втором PDF изменен только шрифт этого тире.

|**Первый файл PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Второй файл PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Образец кода**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Result PDF 1</a>
        <a id="downloadLink2" style="display: none;">Download Result PDF 2</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p>Running example...</p>';

            // Create workbook object
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            let style = cell1.style;
            style.font.name = "Times New Roman";
            cell1.style = style;
            cell2.style = style;

            // Put the values inside the cell
            cell1.value = "Hello without Non-Breaking Hyphen";
            cell2.value = "Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen";

            // Autofit the columns
            worksheet.autoFitColumns();

            // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
            const outputData1 = workbook.save(SaveFormat.Pdf);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'SampleOutput_out.pdf';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download SampleOutput_out.pdf';

            // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
            const opts = new PdfSaveOptions();
            opts.isFontSubstitutionCharGranularity = true;
            const outputData2 = workbook.save(SaveFormat.Pdf, opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'SampleOutput2_out.pdf';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download SampleOutput2_out.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Use the download links to get the generated PDFs.</p>';
        });
    </script>
</html>
```
