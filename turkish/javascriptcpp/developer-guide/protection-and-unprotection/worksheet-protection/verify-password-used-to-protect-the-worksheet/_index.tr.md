---
title: JavaScript ve C++ kullanarak Çalışma Sayfasını Korumada Kullanılan Parolayı Doğrulama
linktitle: Çalışma Sayfasını Korumak İçin Kullanılan Şifreyi Doğrulayın
type: docs
weight: 370
url: /tr/javascript-cpp/verify-password-used-to-protect-the-worksheet/
description: C++ aracılığıyla Aspose.Cells for JavaScript kullanarak çalışma sayfasını korumak için kullanılan parolayı doğrulamayı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells API'leri, [**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection) sınıfını çeşitli kullanışlı özellikler ve metodlar ile geliştirdi. Bu metodlardan biri, şifreyi bir *string* örneği olarak belirlemeye olanak tanıyan ve çalışma sayfasını korumak için kullanılan şifreyi doğrulayan [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-) metodudur.

{{% /alert %}}

[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-) metodu, belirttiğiniz şifre ile korunan çalışma sayfasının şifresi eşleşiyorsa **true**, eşleşmiyorsa **false** döner. Bu kod parçacığı, şifre koruma tespiti için [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-) metodunu ve [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) özelliğini kullanır ve şifreyi doğrular.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Worksheet Password Protection</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook with file bytes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Check if Worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                // Verify the password used to protect the Worksheet
                if (sheet.protection.verifyPassword("1234")) {
                    resultDiv.innerHTML = '<p style="color: green;">Specified password has matched</p>';
                } else {
                    resultDiv.innerHTML = '<p style="color: red;">Specified password has not matched</p>';
                }
            } else {
                resultDiv.innerHTML = '<p style="color: blue;">Worksheet is not password protected</p>';
            }
        });
    </script>
</html>
```
