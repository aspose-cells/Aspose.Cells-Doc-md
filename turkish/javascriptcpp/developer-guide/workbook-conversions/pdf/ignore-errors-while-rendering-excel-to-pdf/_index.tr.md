---
title: Excel i PDF ye dönüştürürken Hataları Yoksayma  C++ ve JavaScript kullanımı
linktitle: Excel i PDF olarak dönüştürürken Hataları Yoksay
type: docs
weight: 80
url: /tr/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: C++ kullanarak Excel dosyasını PDF ye dönüştürürken oluşturulan sayfa sayısını sınırlandırmayı öğrenin.
---

## **Olası Kullanım Senaryoları**  

Bazen, Excel dosyanızı PDF’ye dönüştürürken hatalar veya istisnalar oluşur ve dönüşüm işlemi sona erer. Bu hataları göz ardı etmek için [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--) özelliğini kullanabilirsiniz. Bu sayede dönüşüm sorunsuz tamamlanır, herhangi bir hata veya istisna atılmaz, ancak veri kaybı yaşanabilir. Bu nedenle, bu özelliği yalnızca veri kaybı sizin için kritik değilse kullanın.  

## **Excel'den PDF'e Dönüştürme Sırasında Hataları Yoksay**  

Aşağıdaki kod, [örnek Excel dosyasını](55541778.xlsx) yükler, ancak örnek Excel dosyası hatalıdır ve [PDF’ye dönüşüm sırasında](55541779.pdf) bir hata fırlatır; fakat [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--) özelliği kullanıldığı için hata ortaya çıkmaz. Ancak, bu ekran görüntüsünde gösterilen *yuvarlak kırmızı ok şeklinde* olan şekil kaybolur.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Excel to PDF (Ignore Errors) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF (Ignore Errors)</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Pdf Save Options - Ignore Error
            const opts = new PdfSaveOptions();
            opts.ignoreError = true;

            // Save the Workbook in Pdf with Pdf Save Options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputErrorExcel2Pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
