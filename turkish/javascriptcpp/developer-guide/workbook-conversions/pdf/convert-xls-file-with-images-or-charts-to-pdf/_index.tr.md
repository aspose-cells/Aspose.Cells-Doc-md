---
title: Resimler veya Grafikler içeren XLS Dosyasını JavaScript ile C++ kullanarak PDF ye dönüştürün
linktitle: İmaj veya Grafik İçeren XLS Dosyasını PDF ye Dönüştürme
type: docs
weight: 50
url: /tr/javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells, resimler ve grafikler içeren XLS dosyalarını PDF belgelerine dönüştürmeyi destekler. Aspose.Cells for JavaScript ile C++ bağımsız olarak bir elektronik tabloyu PDF'ye dönüştürebilir: Aspose.PDF for JavaScript C++'a gerek yoktur. İşlem bellekte yapılabilir çünkü bu süreç geçici veya aracı XML dosyalarına bağlı değildir. Bu, büyük Excel dosyalarının, örneğin, resim, grafik ve diğer çizim nesneleri içerenlerin, hızlı ve verimli bir şekilde dönüştürülmesini sağlar.

{{% /alert %}} 
## **Örnek Kod**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}} 

Eğer elektronik tablo formüller içeriyorsa, PDF'ye dönüştürmeden hemen önce [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) metodunu çağırmak en iyisidir. Böylece, formüle bağlı değerler yeniden hesaplanır ve PDF'de doğru değerler gösterilir.

{{% /alert %}}
