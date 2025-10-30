---
title: Desproteger una hoja de cálculo con JavaScript a través de C++
linktitle: Desproteger una hoja de cálculo
type: docs
weight: 20
url: /es/javascript-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Si un desarrollador necesita quitar la protección de una hoja de cálculo protegida en tiempo de ejecución para poder realizar algunos cambios en el archivo, esto se puede hacer fácilmente con Aspose.Cells.

{{% /alert %}}

## **Desproteger una Hoja de Cálculo**

### **Usar Microsoft Excel**

Para quitar la protección de una hoja de cálculo:

Desde el menú **Herramientas**, seleccione **Protección** y luego **Desproteger hoja**. La protección se eliminará a menos que la hoja esté protegida con contraseña. En ese caso, aparecerá un cuadro de diálogo solicitando la contraseña. Ingrese la contraseña y la hoja quedará desprotegida.

### **Desproteger una hoja de cálculo simplemente protegida utilizando Aspose.Cells**

Una hoja de cálculo puede desprotegerse llamando al método [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--) de la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Una hoja protegida sin contraseña no tiene protección con contraseña. Estas pueden desprotegerse llamando al método [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--) sin pasarle un parámetro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Unprotect Worksheet Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unprotecting the worksheet without a password
            worksheet.unprotect();

            // Saving the Workbook in Excel97To2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Desproteger una hoja de cálculo protegida con contraseña utilizando Aspose.Cells**

Una hoja protectada con contraseña es aquella protegida con una contraseña. Tales hojas se pueden desproteger llamando a una versión sobrecargada del método [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--) que recibe la contraseña como parámetro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unprotecting the worksheet with a password (empty password in original code)
            worksheet.unprotect("");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
