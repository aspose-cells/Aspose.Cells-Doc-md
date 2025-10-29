---
title: 用指定打印纸张大小的via JavaScript和C++加载工作簿
linktitle: 加载指定打印纸张大小的工作簿
type: docs
weight: 430
url: /zh/javascript-cpp/load-workbook-with-specified-printer-paper-size/
description: 学习如何在用Aspose.Cells for JavaScript通过C++加载工作簿时设置打印纸张大小
---

{{% alert color="primary" %}}
在加载工作簿时，可以使用[**LoadOptions.paperSize(PaperSizeType)**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#paperSize-papersizetype-)属性指定所需的打印纸张大小。请注意，如果你在MS Excel中新建文件，纸张大小会与您的机器默认打印机设置相同。
{{% /alert %}}

以下示例代码演示了[**LoadOptions.paperSize(PaperSizeType)**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#paperSize-papersizetype-)属性的用法。它首先创建一个工作簿，然后将其以XLSX格式保存在内存流中。然后它以A5纸张大小加载，并以PDF格式保存。接着再次加载，设置为A3纸张大小，并再次保存为PDF格式。如果你打开输出的PDF文件并检查它们的纸张大小，就会看到它们不同，一个是A5，另一个是A3。请下载由代码生成的[A5输出PDF](5115234.pdf)和[A3输出PDF](5115233.pdf)以供参考。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Load Workbook With Printer Size Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLinkA5" style="display: none; margin-right: 10px;">Download A5 PDF</a>
        <a id="downloadLinkA3" style="display: none;">Download A3 PDF</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, PaperSizeType, SaveFormat, Utils } = AsposeCells;

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
            // This example does not require a file input; file input is present per template.
            const resultDiv = document.getElementById('result');

            // Create a sample workbook and add some data inside the first worksheet
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("P30");
            cell.value = "This is sample data.";

            // Save the workbook into a byte array (in-memory)
            const msData = workbook.save(SaveFormat.Xlsx);

            // Load the workbook from memory with A5 paper size
            const opts = new LoadOptions(LoadFormat.Xlsx);
            opts.paperSize = PaperSizeType.PaperA5;
            const workbookA5 = new Workbook(msData, opts);

            // Save the workbook in PDF format (A5)
            const outputDataA5 = workbookA5.save(SaveFormat.Pdf);
            const blobA5 = new Blob([outputDataA5], { type: 'application/pdf' });
            const downloadLinkA5 = document.getElementById('downloadLinkA5');
            downloadLinkA5.href = URL.createObjectURL(blobA5);
            downloadLinkA5.download = 'LoadWorkbookWithPrinterSize-a5_out.pdf';
            downloadLinkA5.style.display = 'inline-block';
            downloadLinkA5.textContent = 'Download A5 PDF';

            // Load the workbook again from the same memory data with A3 paper size
            opts.paperSize = PaperSizeType.PaperA3;
            const workbookA3 = new Workbook(msData, opts);

            // Save the workbook in PDF format (A3)
            const outputDataA3 = workbookA3.save(SaveFormat.Pdf);
            const blobA3 = new Blob([outputDataA3], { type: 'application/pdf' });
            const downloadLinkA3 = document.getElementById('downloadLinkA3');
            downloadLinkA3.href = URL.createObjectURL(blobA3);
            downloadLinkA3.download = 'LoadWorkbookWithPrinterSize-a3_out.pdf';
            downloadLinkA3.style.display = 'inline-block';
            downloadLinkA3.textContent = 'Download A3 PDF';

            resultDiv.innerHTML = '<p style="color: green;">PDF files generated successfully. Use the links above to download the A5 and A3 PDFs.</p>';
        });
    </script>
</html>
```
