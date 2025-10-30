---
title: Belge Dönüşüm Sürecini İzle Javascript ile C++ kullanarak
linktitle: Belge Dönüşüm İlerlemesini İzle
type: docs
weight: 970
url: /tr/javascript-cpp/track-document-conversion-progress/
description: Excel dosyalarında belge dönüşüm sürecini nasıl takip edeceğinizi Aspose.Cells for JavaScript ile C++ kullanarak öğrenin.
---

## **Olası Kullanım Senaryoları**  

Bazen büyük Excel dosyalarını dönüştürmek zaman alabilir. Bu süre zarfında, uygulamanızın kullanılabilirliğini artırmak için sadece yükleniyor ekranı yerine belge dönüşüm sürecini göstermek isteyebilirsiniz. Aspose.Cells for JavaScript, C++ aracılığıyla, özel sınıfınızda uygulayabileceğiniz [**IPageSavingCallback**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback) arayüzü sağlayarak belge dönüştürme işlemini izlemeyi destekler. [**IPageSavingCallback**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback) arayüzü, [**IPageSavingCallback.pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) ve [**IPageSavingCallback.pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-) yöntemleriyle kendi özel sınıfınızda uygulayabileceğiniz özellikler sunar. Ayrıca, nasıl sayfaların görüntüleneceği üzerinde kontrol sağlayabilirsiniz, bu örnekte *TestPageSavingCallback* özel sınıfı gösterilmiştir.  

## **Belge Dönüşüm İlerlemesini İzle**  

Aşağıdaki kod örneği, [kaynak excel dosyasını](94896151.xlsx) yükler ve *TestPageSavingCallback* özelleştirilmiş sınıfını kullanarak dönüştürme ilerlemesini konsola yazdırır. Bu sınıf, [**IPageSavingCallback**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback) arayüzünü uygular.  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Pages to PDF with Progress Callback</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat } = AsposeCells;

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

        // Define TestPageSavingCallback class
        class TestPageSavingCallback {
            onPageSaving(pageIndex, fileName) {
                console.log(`Saving page ${pageIndex} to ${fileName}`);
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PdfSaveOptions and assign the page saving callback
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.pageSavingCallback = new TestPageSavingCallback();

            // Save workbook as PDF with options
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DocumentConversionProgress.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF conversion started/completed. Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```  

*TestPageSavingCallback* özel sınıfının kodu aşağıdadır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Saving Callback Example</title>
    </head>
    <body>
        <h1>Page Saving Callback Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example (Save as PDF with Callback)</button>
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

        class TestPageSavingCallback {
            pageStartSaving(args) {
                console.log(`Start saving page index ${args.pageIndex} of pages ${args.pageCount}`);

                // don't output pages before page index 2.
                if (args.pageIndex < 2) {
                    args.isToOutput = false;
                }
            }

            pageEndSaving(args) {
                console.log(`End saving page index ${args.pageIndex} of pages ${args.pageCount}`);

                // don't output pages after page index 8.
                if (args.pageIndex >= 8) {
                    args.hasMorePages = false;
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PDF save options and attach the page saving callback
            const options = new PdfSaveOptions();
            options.pageSavingCallback = new TestPageSavingCallback();

            // Save workbook as PDF with the callback applied
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Konsol Çıktısı**  

{{< highlight java >}}  

Start saving page index 0 of pages 11</br>  
End saving page index 0 of pages 11</br>  
Start saving page index 1 of pages 11</br>  
End saving page index 1 of pages 11</br>  
Start saving page index 2 of pages 11</br>  
End saving page index 2 of pages 11</br>  
Start saving page index 3 of pages 11</br>  
End saving page index 3 of pages 11</br>  
Start saving page index 4 of pages 11</br>  
End saving page index 4 of pages 11</br>  
Start saving page index 5 of pages 11</br>  
End saving page index 5 of pages 11</br>  
Start saving page index 6 of pages 11</br>  
End saving page index 6 of pages 11</br>  
Start saving page index 7 of pages 11</br>  
End saving page index 7 of pages 11</br>  
Start saving page index 8 of pages 11</br>  
End saving page index 8 of pages 11  

{{< /highlight >}}
