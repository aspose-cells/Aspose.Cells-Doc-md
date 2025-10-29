---
title: 使用JavaScript通过C++避免在没有内容打印时生成空白页的输出PDF
linktitle: 避免输出PDF中的空白页在没有内容打印时
type: docs
weight: 30
url: /zh/javascript-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: 学习如何在没有内容打印时，使用Aspose.Cells for Java脚本通过C++避免输出PDF中的空白页。
---

## **可能的使用场景**

当Excel文件为空且用户使用Aspose.Cells for Java脚本通过C++将其保存为PDF时，输出的PDF中会渲染空白页。有时，这种默认行为并不理想。Aspose.Cells提供了[**PdfSaveOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#outputBlankPageWhenNothingToPrint--)属性来处理此问题。如果将其设置为**false**，则在没有内容时打印输出的PDF会抛出异常。

## **当没有需要打印的内容时，避免在输出PDF中出现空白页**

以下示例代码创建一个空工作簿，然后将其保存为PDF，并将[**PdfSaveOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#outputBlankPageWhenNothingToPrint--)属性设置为**false**。由于输出的PDF中没有任何内容可打印，因此会发生如下所示的异常。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Save Workbook to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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
                // No file selected - will create an empty workbook (to mirror original JavaScript behavior)
                document.getElementById('result').innerHTML = '<p>No file selected. Creating an empty workbook and attempting to save to PDF.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Loading selected workbook...</p>';
            }

            // Instantiate workbook from file if provided, otherwise create an empty workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create Pdf save options.
            const opts = new PdfSaveOptions();

            // Default value of OutputBlankPageWhenNothingToPrint is true.
            // Setting false means - Do not output blank page when there is nothing to print.
            opts.outputBlankPageWhenNothingToPrint = false;

            // Save workbook to Pdf format.
            // Note: If workbook has nothing to print and outputBlankPageWhenNothingToPrint is false,
            // this operation may throw an exception which will propagate (no try-catch per requirements).
            const outputData = workbook.save(SaveFormat.Pdf, opts);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **异常**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
