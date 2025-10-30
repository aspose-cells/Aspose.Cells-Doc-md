---
title: Verificar contraseña para modificar usando Aspose.Cells for JavaScript via C++
linktitle: Verificar contraseña para modificar
type: docs
weight: 2400
url: /es/javascript-cpp/check-password-to-modify-using-aspose-cells/
description: Aprende cómo verificar si la contraseña para modificar coincide usando Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
A veces, necesitas verificar programáticamente si la contraseña dada coincide con la **Contraseña para modificar**. Aspose.Cells proporciona el método `WorkbookSettings.writeProtection.validatePassword()` que puedes usar para verificar si la contraseña dada es correcta o no.  
{{% /alert %}}  

## **Verificar Contraseña para modificar en Microsoft Excel**  

Puedes asignar **Contraseña para abrir** y **Contraseña para modificar** al crear tus libros de trabajo en Microsoft Excel. Por favor, mira esta captura de pantalla que muestra la interfaz que Microsoft Excel proporciona para especificar estas contraseñas.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Verificar contraseña para modificar usando Aspose.Cells for JavaScript vía C++**  

Los siguientes códigos de ejemplo cargan el archivo de [origen de Excel](5112232.xlsx). Tiene una contraseña para abrirla 1234 y una contraseña para modificarla 5678. Primero comprueba si 567 es la contraseña correcta para modificar y devuelve falso, luego verifica si 5678 es la contraseña y devuelve verdadero.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Write Protection Passwords</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, SaveFormat, Utils } = AsposeCells;

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

            // Specify password to open inside the load options
            const opts = new LoadOptions();
            opts.password = "1234";

            // Open the source Excel file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Check if 567 is Password to modify
            let ret = workbook.settings.writeProtection.validatePassword("567");
            let outputHtml = `<p>Is 567 correct Password to modify: ${ret}</p>`;

            // Check if 5678 is Password to modify
            ret = workbook.settings.writeProtection.validatePassword("5678");
            outputHtml += `<p>Is 5678 correct Password to modify: ${ret}</p>`;

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```  

### **Salida de la consola**  



{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}
