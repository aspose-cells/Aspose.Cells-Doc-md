---
title: JavaScript kullanarak C++ ile Şifrelenmiş Dosyaların Parolasını Doğrula
linktitle: Şifrelenmiş Dosyaların Şifresini Doğrulama
type: docs
weight: 10
url: /tr/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/
description: C++ ile Aspose.Cells for JavaScript kullanarak şifrelenmiş Excel (xlsx, xlsb, xls, xlsm) ve Open Office (ODS) dosyalarının parolasını doğrula.
---

{{% alert color="primary" %}}  
Excel (xlsx, xlsb, xls, xlsm) ve Open Office (ODS) dosyaları şifre ile kilitliyse, Aspose spesifik verilerin ayrıştırılmasına ihtiyaç duymadan basit parola doğrulamasını destekler.  
{{% /alert %}}  

## **Şifrelenmiş dosyanın parolasını doğrulama**  

Şifreli dosyanın parolasını doğrulamak için, C++ ile Aspose.Cells for JavaScript [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-) metodunu sağlar. Bu metod iki parametre alır, dosya akışı ve doğrulanması gereken parola.  
Aşağıdaki kod parçası, sağlanan parolanın geçerli olup olmadığını doğrulamak için [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-) yönteminin nasıl kullanıldığını göstermektedir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Verify Excel Password Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Verify Password</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatUtil, Utils } = AsposeCells;

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
            const bytes = new Uint8Array(arrayBuffer);

            const isPasswordValid = FileFormatUtil.verifyPassword(bytes, "1234");

            document.getElementById('result').innerHTML = '<p>Password is Valid: ' + isPasswordValid + '</p>';
        });
    </script>
</html>
```
