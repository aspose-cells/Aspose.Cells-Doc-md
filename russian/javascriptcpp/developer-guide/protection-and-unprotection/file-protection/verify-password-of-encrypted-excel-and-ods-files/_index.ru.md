---
title: Проверка пароля зашифрованных файлов с помощью JavaScript через C++
linktitle: Проверить пароль зашифрованных файлов
type: docs
weight: 10
url: /ru/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Проверьте пароль зашифрованных файлов Excel (xlsx, xlsb, xls, xlsm) и Open Office (ODS) с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}  
Если файлы Excel (xlsx, xlsb, xls, xlsm) и Open Office (ODS) защищены паролем, Aspose поддерживает простую проверку пароля без разбора конкретных данных файлов.  
{{% /alert %}}  

## **Проверьте пароль зашифрованного файла**  

Для проверки пароля зашифрованного файла Aspose.Cells for JavaScript через C++ предоставляет метод [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-). Этот метод принимает два параметра: поток файла и пароль, который необходимо проверить.  
Следующий фрагмент кода демонстрирует использование метода [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-) для проверки, является ли предоставленный пароль допустимым или нет.  

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
