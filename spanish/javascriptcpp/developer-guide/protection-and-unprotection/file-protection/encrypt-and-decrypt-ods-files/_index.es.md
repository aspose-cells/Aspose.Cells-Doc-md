---
title: Cifrar y descifrar archivos ODS con JavaScript a través de C++
linktitle: Cifrar y Descifrar archivos ODS
type: docs
weight: 10
url: /es/javascript-cpp/encrypt-and-decrypt-ods-files/
description: Proteger con contraseña y cifrar archivos ODS usando Aspose.Cells for JavaScript a través de C++. 
---

{{% alert color="primary" %}}
OpenOffice.org es un paquete de oficina completo que soporta proteger y cifrar archivos con contraseña. Sin embargo, un archivo ODS encriptado solo puede abrirse en OpenOffice tras proporcionar la contraseña. Excel no puede abrir el archivo ODS encriptado y puede mostrar mensajes de advertencia. Las opciones de cifrado no son aplicables a archivos ODS, a diferencia de otros tipos de archivos. 
Aspose.Cells permite encriptar y desencriptar archivos ODS. Los archivos ODS desencriptados pueden abrirse tanto en Excel como en OpenOffice.
{{% /alert %}}

## **Cifrar con OpenOffice Calc**
1. Selecciona **Guardar como** y haz clic en la casilla **Guardar con contraseña**.
1. Haz clic en el botón **Guardar**.
1. Escribe tu contraseña deseada en los campos **Introducir Contraseña para Abrir** y **Confirmar Contraseña** en la ventana Establecer Contraseña que se abre. 
1. Haz clic en el botón **Aceptar** para guardar el archivo.

## **Cifrar archivo ODS con Aspose.Cells for JavaScript a través de C++**
Para cifrar un archivo ODS, carga el archivo y establece el valor [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) con la contraseña actual antes de guardarlo. El archivo ODS cifrado resultante solo puede abrirse en OpenOffice.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect ODS File</title>
    </head>
    <body>
        <h1>Protect ODS File Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
        <button id="runExample">Protect and Download ODS</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded ODS file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Password protect the file (converted from getSettings().setPassword -> settings.password)
            workbook.settings.password = "1234";

            // Saving the ODS file
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEncryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File protected successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```

## **Descifrar archivo ODS con Aspose.Cells for JavaScript a través de C++**
Para descifrar un archivo ODS, carga el archivo proporcionando una contraseña en [**LoadOptions.password**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#password--). Una vez cargado, establece la cadena [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) en null.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Decrypt ODS Example</title>
    </head>
    <body>
        <h1>Decrypt ODS Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open an encrypted ODS file with load options
            const loadOptions = new LoadOptions(LoadFormat.Ods);

            // Set original password
            loadOptions.password = "1234";

            // Load the encrypted ODS file with the appropriate load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Set the password to null (remove password from settings)
            workbook.settings.password = null;

            // Save the decrypted ODS file and provide download link
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDecryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Decrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Decryption completed successfully! Click the download link to get the decrypted file.</p>';
        });
    </script>
</html>
```
