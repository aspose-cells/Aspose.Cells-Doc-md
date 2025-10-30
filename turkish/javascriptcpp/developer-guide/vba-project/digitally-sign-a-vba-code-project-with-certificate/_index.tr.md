---
title: VBA Kod Projesini Dijital Sertifika ile İmzala C++ ile JavaScript kullanarak
linktitle: Sertifika ile bir VBA Kod Projesini Dijital Olarak İmzalama
type: docs
weight: 110
url: /tr/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Aspose.Cells for JavaScript kullanarak bir VBA Kod Projesini dijital sertifika ile nasıl imzalanacağını öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak ve [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-) yöntemi ile VBA kod projenizi dijital olarak imzalayabilirsiniz. Excel dosyanızın dijital olarak sertifika ile imzalanıp imzalanmadığını kontrol etmek için lütfen bu adımları izleyin.

- **Geliştirici** sekmesinden **Görsel Temel**'e tıklayarak **Görsel Temel Uygulamaları (IDE)**'ni açın.
- **Görsel Temel Uygulamaları IDE**'nin **Araçlar** > **Dijital İmzalar...**'ına tıklayın

ve **Dijital İmza Formu**'nu göstererek belgenin sertifika ile dijital olarak imzalanıp imzalanmadığını gösterecektir.

{{% /alert %}} 

## ** JavaScript ile VBA Kod Projesini Dijital Olarak Sertifika ile İmzala**

Aşağıdaki örnek kod, [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-) yönteminin nasıl kullanılacağını gösterir. İşte örnek kodun giriş ve çıkış dosyaları. Bu kodu test etmek için herhangi bir Excel dosyası ve herhangi bir sertifika kullanabilirsiniz.

- Örnek Excel dosyası](5115028.xlsm) örnek kodda kullanılan.
- [Örnek pfx dosyası](5115039.pfx) Dijital İmza oluşturmak için. Bu kodu çalıştırmak için lütfen bilgisayarınıza kurun. Şifresi 1234'tür.
- [Çıktı Excel dosyası](5115029.xlsm) örnek kod tarafından oluşturulan.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sign VBA Project with Digital Signature</h1>
        <div>
            <label for="fileInput">Select Excel Workbook (.xlsm): </label>
            <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
        </div>
        <div>
            <label for="pfxInput">Select PFX Certificate (.pfx): </label>
            <input type="file" id="pfxInput" accept=".pfx" />
        </div>
        <button id="runExample">Sign VBA Project</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, DigitalSignature } = AsposeCells;

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
            const pfxInput = document.getElementById('pfxInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length || !pfxInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select both the Excel workbook and the PFX certificate files.</p>';
                return;
            }

            const workbookFile = fileInput.files[0];
            const pfxFile = pfxInput.files[0];

            // Read files as ArrayBuffer
            const [wbArrayBuffer, pfxArrayBuffer] = await Promise.all([
                workbookFile.arrayBuffer(),
                pfxFile.arrayBuffer()
            ]);

            // Prepare bytes
            const wbBytes = new Uint8Array(wbArrayBuffer);
            const pfxBytes = new Uint8Array(pfxArrayBuffer);

            // Set Digital Signature parameters
            const password = "1234";
            const comment = "Signing Digital Signature using Aspose.Cells";
            const digitalSignature = new DigitalSignature(pfxBytes, password, comment, new Date());

            // Create workbook object from excel file
            const workbook = new Workbook(wbBytes);

            // Sign VBA Code Project with Digital Signature
            workbook.vbaProject.sign(digitalSignature);

            // Save the workbook as XLSM
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDigitallySignVbaProjectWithCertificate.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Signed Workbook';

            resultDiv.innerHTML = '<p style="color: green;">Workbook signed successfully! Click the download link to download the signed workbook.</p>';
        });
    </script>
</html>
```
