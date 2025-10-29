---
title: 在保存为PDF时，仅更改单个Unicode字符的字体，使用JavaScript通过C++
linktitle: 在保存为PDF时仅更改特定Unicode字符的字体
type: docs
weight: 260
url: /zh/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: 学习如何在使用Aspose.Cells for Java脚本通过C++保存为PDF时更改特定Unicode字符的字体。 
---

{{% alert color="primary" %}} 

一些Unicode字符无法使用用户指定的字体显示。其中一个这样的Unicode字符是**非间断连字**（U+2011），其Unicode编号为8209。这个字符不能用**Times New Roman**显示，但可以用其他字体如**Arial Unicode MS**显示。

 当某个字符出现在一些单词或句子中，而这些内容使用特定字体（如Times New Roman）时，Aspose.Cells会将整个单词或句子的字体更改为可以显示该字符的字体，如Arial Unicode MS或MS。

 然而，对于一些用户来说，这种行为是不理想的，他们希望只改变该特定字符的字体，而不是更改整个单词或句子的字体。

 为了解决这个问题，Aspose.Cells提供了`PdfSaveOptions.isFontSubstitutionCharGranularity`属性，应将其设置为true，以便只更改那些无法显示的特定字符的字体为可显示的字体，而其余的单词或句子仍然保持原始字体。

{{% /alert %}} 

## **示例**
以下屏幕截图比较了以下示例代码生成的两个输出PDF。

 一个是在不设置`PdfSaveOptions.isFontSubstitutionCharGranularity`属性的情况下生成的，另一个是在设置`PdfSaveOptions.isFontSubstitutionCharGranularity`属性为true后生成的。

 如第一个PDF所示，由于非断字符号，整个句子的字体由Times New Roman变为Arial Unicode MS。而在第二个PDF中，只有非断字符号的字体发生了变化。

| **第一个PDF文件** |
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


| **第二个PDF文件** |
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **示例代码**


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
