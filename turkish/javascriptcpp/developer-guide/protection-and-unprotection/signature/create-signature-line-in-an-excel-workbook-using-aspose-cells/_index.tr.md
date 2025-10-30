---
title: C++ kullanarak Excel Çalışma Kitabı içinde İmza Satırı Oluşturma
linktitle: Aspose.Cells ile Excel Çalışma Kitabında İmza Satırı Oluşturma
type: docs
weight: 150
url: /tr/javascript-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Bu makale, JavaScript kullanarak Aspose.Cells for JavaScript ile bir Excel Çalışma Kitabında İmza Satırı oluşturmayı anlatmaktadır.
keywords: JavaScript kullanarak Excel Çalışma Kitabında İmza Satırı Oluşturma, Excel dosyasına İmza Satırı nasıl eklenir, İmza Satırı ekleme, Excel dosyasına İmza Satırı ekleme yolları.
---

## **Giriş**  

Microsoft Excel, Excel çalışma kitaplarına **İmza Satırı** eklemek için bir özellik sağlar. Aspose.Cells de bu özelliği sağlar ve bunun için {0} özelliğini sunmuştur. Bu makale, bu özelliği kullanmanın nasıl olduğunu açıklar.  

## **Excel için İmza Çizgisi Oluşturmayı**  

Aspose.Cells for JavaScript kullanılarak C++ ayrıca bu özelliği sağlar ve bu amaçla [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) özelliğini açığa çıkarmıştır. Bu makale, Aspose.Cells kullanarak bu özelliği kullanarak İmza Satırı eklemeyi açıklayacaktır.  

Aşağıdaki örnek kod, [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) özelliğini kullanarak İmza Çizgisi ekler ve çalışma kitabını kaydeder.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Signature Line Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SignatureLine, Utils } = AsposeCells;

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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create signature line object
            const signatureLine = new SignatureLine();
            signatureLine.signer = "John Doe";
            signatureLine.title = "Development Lead";
            signatureLine.email = "john.doe@aspose.com";

            // Adds a Signature Line to the first worksheet.
            workbook.worksheets.get(0).shapes.addSignatureLine(1, 1, signatureLine);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Signature line added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
