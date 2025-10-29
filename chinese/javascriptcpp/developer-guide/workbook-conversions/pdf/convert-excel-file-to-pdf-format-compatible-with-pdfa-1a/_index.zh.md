---
title: 将Excel文件转换为兼容PDF/A 1a的PDF格式，使用JavaScript通过C++
linktitle: 将Excel文件转换为PDF/A 1a兼容的PDF格式
type: docs
weight: 130
url: /zh/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: 学习如何使用Aspose.Cells for Java脚本通过C++将Excel文件转换为符合PDF/A标准的PDF文件。
---

## **可能的使用场景**  

PDF/A是针对长期保存的文件而设计的PDF特殊版本，是ISO标准化的可携带文档格式（PDF）的一种归档格式，嵌入了文档中使用的所有字体。PDF/A与普通PDF的区别在于，禁止某些功能，如字体链接（而非字体嵌入）和加密。Aspose.Cells for Java脚本通过C++支持将Excel文件保存为PDF/A合规的PDF（支持PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab和PDF/A-3u）。此话题介绍了如何将Excel工作簿保存为符合PDF/A标准（PDF/A-1a）的PDF文件。  

## **将Excel文件转换为与PDF/A-1a兼容的PDF格式**  

 开发者可以使用[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)类设置转换的不同属性。设置[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)类的不同属性，可以控制输出PDF的打印、字体、安全性和压缩设置。最重要的属性是[**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--)，它允许你将Excel文件保存为符合PDF/A标准的PDF文件。  

 以下示例代码说明如何将Excel文件转换为兼容PDF/A-1a的PDF格式。请参考其[输出PDF](outputCompliancePdfA1a.pdf)及截图。  

## **屏幕截图**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export to PDF (PDFA-1a) Example</h1>
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
            // Create workbook object
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and add some message inside it
            const cell = ws.cells.get("B5");
            cell.value = "This PDF format is compatible with PDFA-1a.";

            // Create pdf save options and set its compliance to PDFA-1a
            const opts = new AsposeCells.PdfSaveOptions();
            opts.compliance = AsposeCells.PdfCompliance.PdfA1a;

            // Save the output pdf
            const outputData = wb.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCompliancePdfA1a.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
