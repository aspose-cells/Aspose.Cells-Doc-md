---
title: Her Çalışma Sayfasını Farklı PDF Dosyası olarak Kaydetmek JavaScript ile C++
linktitle: Her bir Çalışsayfayı Farklı Bir PDF Dosyasına Kaydet
type: docs
weight: 130
url: /tr/javascript-cpp/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}}  
Aspose.Cells, resimleri, chart'ları vb. içeren XLS dosyalarını PDF'ye dönüştürmeyi destekler. Aspose.Cells for JavaScript kullanılarak C++ ile bağımsız olarak bir çalışma kitabını PDF'ye dönüştürmek mümkündür ve dönüştürmek için Aspose.PDF kullanmanıza gerek yoktur. Dönüşüm tüm işle mi in-memory yapılabilir ve herhangi bir geçici dosya oluşturmak gerekmez.  
{{% /alert %}}  

## **Her Çalışsayarı Farklı Bir PDF Dosyasına Kaydet**  
Şablon Excel dosyanızdaki her çalışma sayfasını farklı PDF dosyaları oluşturmak için kaydetmeniz gerekiyorsa, bunu kolayca başarabilirsiniz. Bir seferde bir sheet indeksini [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfs%20saveoptions/#sheetSet) seçeneğiyle ayarlayarak PDF'ye dönüştürmeyi deneyebilirsiniz.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Each Worksheet to PDF</title>
    </head>
    <body>
        <h1>Export Each Worksheet to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SheetSet, SaveFormat } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const mainDownloadLink = document.getElementById('downloadLink');
            resultDiv.innerHTML = '';
            mainDownloadLink.style.display = 'none';
            mainDownloadLink.href = '';
            mainDownloadLink.textContent = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new workbook and open the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the count of the worksheets in the workbook
            const sheetCount = workbook.worksheets.count;

            // Prepare container for links
            const linksContainer = document.createElement('div');

            for (let j = 0; j < sheetCount; j++) {
                const ws = workbook.worksheets.get(j);

                // set worksheet to output
                const sheetSet = new SheetSet([ws.index]);
                const pdfSaveOptions = new PdfSaveOptions();
                pdfSaveOptions.sheetSet = sheetSet;

                // Save current worksheet as PDF
                const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
                const blob = new Blob([outputData], { type: 'application/pdf' });

                const fileName = `worksheet-${ws.name}.out.pdf`;
                const url = URL.createObjectURL(blob);

                const link = document.createElement('a');
                link.href = url;
                link.download = fileName;
                link.textContent = `Download ${fileName}`;
                link.style.display = 'block';
                linksContainer.appendChild(link);

                // For the first generated PDF, also set the main download link element
                if (j === 0) {
                    mainDownloadLink.href = url;
                    mainDownloadLink.download = fileName;
                    mainDownloadLink.style.display = 'block';
                    mainDownloadLink.textContent = `Download ${fileName}`;
                }
            }

            resultDiv.innerHTML = `<p style="color: green;">Generated ${sheetCount} PDF file(s). Use the links below to download them.</p>`;
            resultDiv.appendChild(linksContainer);
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.  
{{% /alert %}}
