---
title: Verificar contraseña de archivos cifrados con JavaScript a través de C++
linktitle: Verificar contraseña de archivos cifrados
type: docs
weight: 10
url: /es/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Verifica la contraseña de archivos cifrados de Excel (xlsx, xlsb, xls, xlsm) y Open Office (ODS) usando Aspose.Cells for JavaScript a través de C++.
---

{{% alert color="primary" %}}  
Si los archivos Excel (xlsx, xlsb, xls, xlsm) y Open Office (ODS) están bloqueados con contraseña, Aspose soporta la verificación simple de contraseña sin analizar datos específicos de los archivos.  
{{% /alert %}}  

## **Verificar la contraseña del archivo cifrado**  

Para verificar la contraseña del archivo cifrado, Aspose.Cells for JavaScript a través de C++ proporciona el método [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-). Este método acepta dos parámetros, el flujo de archivo y la contraseña que necesita verificarse.  
El siguiente fragmento de código muestra el uso del método [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-) para verificar si la contraseña proporcionada es válida o no.  

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
