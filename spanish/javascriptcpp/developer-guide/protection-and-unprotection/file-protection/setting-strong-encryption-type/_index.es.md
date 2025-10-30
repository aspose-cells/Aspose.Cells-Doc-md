---
title: Establecer un tipo de cifrado fuerte con JavaScript a través de C++
linktitle: Establecer Tipo de Cifrado Fuerte
type: docs
weight: 60
url: /es/javascript-cpp/setting-strong-encryption-type/
description: Aprende cómo establecer tipos de cifrado fuerte para archivos Excel usando Aspose.Cells for JavaScript a través de C++.
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) te permite cifrar y proteger con contraseña hojas de cálculo. Utiliza algoritmos proporcionados por un Proveedor de Servicios Criptográficos. Un Proveedor de Servicios Criptográficos (o CSP) es un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es "Compatible con Office 97/2000". Este es un CSP con algunos problemas de seguridad conocidos públicamente. Las hojas de cálculo aseguradas con el cifrado "débil (XOR)" o con el tipo de cifrado "Compatible con Office 97/2000" pueden ser descifradas fácilmente.

Para superar este problema, utiliza uno de los tipos de cifrado fuerte proporcionados por Microsoft Excel. Puedes cambiar el tipo de cifrado al CSP más fuerte disponible. Para el cifrado fuerte, se requiere una longitud mínima de clave de 128 bits, por ejemplo, 'Proveedor Criptográfico Fuerte de Microsoft'.

También puedes cifrar y proteger con contraseña archivos de Excel con un tipo de cifrado fuerte utilizando la API de Aspose.Cells.

{{% /alert %}}  
## **Aplicar cifrado con Microsoft Excel**  
Para implementar el cifrado de archivos en Microsoft Excel (por ejemplo 2007):

1. Desde el menú **Herramientas**, selecciona **Opciones**.  
1. Selecciona la pestaña **Seguridad**.  
1. Ingresa un valor para el campo **Contraseña para abrir**.  
1. Haz clic en **Avanzado**.  
1. Elige el tipo de cifrado y confirma la contraseña.  

## **Aplicar cifrado con Aspose.Cells**  
Los ejemplos de código a continuación aplican cifrado fuerte en un archivo y establecen una contraseña.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Encrypt Workbook</title>
    </head>
    <body>
        <h1>Encrypt Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            workbook.encryptionOptions = [AsposeCells.EncryptionType.StrongCryptographicProvider, 128];
            workbook.settings.password = "1234";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File encrypted successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```
