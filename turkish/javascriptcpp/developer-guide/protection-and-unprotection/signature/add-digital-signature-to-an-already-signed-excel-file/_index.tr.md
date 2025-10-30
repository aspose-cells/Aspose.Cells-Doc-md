---
title: JavaScript kullanarak C++ ile zaten imzalanmış Excel dosyasına Dijital İmza Ekle
linktitle: Zaten İmzalanmış Bir Excel Dosyasına Dijital İmza Eklemek
type: docs
weight: 20
url: /tr/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Bu makale, Aspose.Cells for JavaScript kullanılarak JavaScript ile zaten imzalanmış Excel dosyasına dijital imza eklemeyi anlatmaktadır.
keywords: Zaten imzalanmış bir Excel dosyasına Dijital İmza Ekleme, JavaScript kullanarak C++ ile zaten imzalanmış bir Excel belgesine dijital imza ekleme prosedürü.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for JavaScript kullanılarak C++ ile sağlanan [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) yöntemi ile zaten imzalanmış Excel dosyasına dijital imza ekleyebilirsiniz.

{{% alert color="primary" %}}

Lütfen, zaten imzalanmış bir Excel belgesine dijital imza eklerken, orijinal belge Aspose.Cells tarafından oluşturulmuşsa, düzgün çalışır. Ancak belgenin diğer motorlar (ör. Microsoft Excel vb.) tarafından oluşturulmuş olması durumunda, Aspose.Cells dosyayı yükledikten ve kaydettikten sonra aynı şekilde tutamayabilir, bu da orijinal imzayı geçersiz kılacaktır.

{{% /alert %}}

## **Zaten İmzalanmış Bir Excel Dosyasına Dijital İmza Eklemek**

Aşağıdaki örnek kod, [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) metodunu kullanarak zaten imzalanmış bir Excel dosyasına dijital imza eklemeyi gösterir. Lütfen bu kodda kullanılan [örnek Excel dosyasını](50528280.xlsx) kontrol edin. Bu dosya zaten dijital olarak imzalanmıştır. Lütfen kod tarafından oluşturulan [çıktı Excel dosyasını](50528281.xlsx) inceleyin. Bu kodda, şifre koruması için [AsposeDemo.pfx](50528279.pfx) adlı demo sertifikasını kullandık, şifresi **aspose**. Ekran görüntüsü, kodun çalışan sonrası örnek Excel dosyasındaki etkisini gösterir.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Digital Signature Example</title>
    </head>
    <body>
        <h1>Add Digital Signature to Workbook</h1>
        <p>Select an Excel file and a PFX certificate, enter the certificate password, then click "Add Digital Signature".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <br/><br/>
        <input type="file" id="certInput" accept=".pfx" />
        <br/><br/>
        <label for="certPassword">Certificate Password:</label>
        <input type="password" id="certPassword" value="aspose" />
        <br/><br/>
        <button id="runExample">Add Digital Signature</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, DigitalSignature, DigitalSignatureCollection, SaveFormat, Utils } = AsposeCells;

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
            const certInput = document.getElementById('certInput');
            const passwordInput = document.getElementById('certPassword');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!certInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a .pfx certificate file.</p>';
                return;
            }

            // Read files as ArrayBuffer
            const excelFile = fileInput.files[0];
            const certFile = certInput.files[0];
            const certPassword = passwordInput.value;

            const excelArrayBuffer = await excelFile.arrayBuffer();
            const certArrayBuffer = await certFile.arrayBuffer();

            // Instantiate Workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(excelArrayBuffer));

            // Create the digital signature collection
            const dsCollection = new DigitalSignatureCollection();

            // Create new digital signature and add it in digital signature collection
            // Using certificate bytes (Uint8Array), password, comment and signing date
            const signature = new DigitalSignature(new Uint8Array(certArrayBuffer), certPassword, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
            dsCollection.add(signature);

            // Add digital signature collection inside the workbook
            workbook.addDigitalSignature(dsCollection);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDigitallySignedByCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Digitally Signed Excel File';

            // Dispose the workbook
            workbook.dispose();

            resultDiv.innerHTML = '<p style="color: green;">Digital signature added successfully! Click the download link to get the signed file.</p>';
        });
    </script>
</html>
```
