---
title: Çıktı PDF sinde Yazdırılacak Öğe Yokken Boş Sayfa Oluşumunu JavaScript ile C++ kullanarak önleyin
linktitle: Boş sayfa olmadığında Çıktı PDF de Boş Sayfa İşlemi
type: docs
weight: 30
url: /tr/javascript-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Çıktı PDF sinde hiçbir şey yazdırılacak öğe olmadığında boş sayfaları nasıl önleyeceğinizi Aspose.Cells for JavaScript ile C++ kullanarak öğrenin.
---

## **Olası Kullanım Senaryoları**

Excel dosyası boş ve kullanıcı onu PDF'ye kaydettiğinde, çıktı PDF'sinde boş sayfa oluşur. Bazen, bu varsayılan davranış istenmeyebilir. Aspose.Cells, bu sorunu çözmek için [**PdfSaveOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#outputBlankPageWhenNothingToPrint--) özelliğini sağlar. Bunu **false** olarak ayarlarsanız, çıktı PDF'sinde yazdırılacak herhangi bir şey olmadığında istisna oluşur.

## **Çıktı PDF'inde Boş Sayfa Oluşmasını Engelle**

Aşağıdaki örnek kod, boş bir çalışma kitabı oluşturur ve [**PdfSaveOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#outputBlankPageWhenNothingToPrint--) özelliğini **false** olarak ayarladıktan sonra PDF olarak kaydeder. Çıktı PDF'sinde yazdırılacak bir şey olmadığından, aşağıdaki gibi istisna oluşur.

## **Örnek Kod**

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

## **İstisna**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
