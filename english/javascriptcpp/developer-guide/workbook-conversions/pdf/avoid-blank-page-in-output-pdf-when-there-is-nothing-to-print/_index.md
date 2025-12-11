---
title: Avoid Blank Page in Output PDF when there is Nothing to Print with JavaScript via C++
linktitle: Avoid Blank Page in Output PDF when there is Nothing to Print
type: docs
weight: 30
url: /javascript-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Learn how to avoid blank pages in output PDF when there is nothing to print using Aspose.Cells for JavaScript via C++.
---

## **Possible Usage Scenarios**

When the Excel file is empty and the user saves it to PDF using Aspose.Cells for JavaScript via C++, it renders a blank page in the output PDF. Sometimes, this default behavior is undesirable. Aspose.Cells provides the [**PdfSaveOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#outputBlankPageWhenNothingToPrint--) property to handle this issue. If you set it to **false**, then an exception will be thrown when there is nothing to print in the output PDF.

## **Avoid Blank Page in Output PDF when there is Nothing to Print**

The following sample code creates an empty workbook and then saves it as PDF after setting the [**PdfSaveOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#outputBlankPageWhenNothingToPrint--) property to **false**. Since there is nothing to print in the output PDF, the exception occurs as shown below.

## **Sample Code**

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
            // Setting it to false means do not output a blank page when there is nothing to print.
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

## **Exception**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}