---
title: Proteger y Desproteger la Hoja de Cálculo con JavaScript a través de C++
linktitle: Proteger y Desproteger Hoja de Cálculo
type: docs
weight: 40
url: /es/javascript-cpp/protect-and-unprotect-worksheets/
description: Proteger y desproteger la hoja de cálculo de archivos de Excel con Aspose.Cells for JavaScript a través de C++.
---

{{% alert color="primary" %}}  
Para evitar que otros usuarios cambien, muevan o eliminen datos en una hoja de cálculo de forma accidental o deliberada, puede bloquear las celdas en su hoja de cálculo de Excel y luego proteger la hoja con una contraseña.  
{{% /alert %}}  

## **Proteger y desproteger Hoja de Cálculo en MS Excel**  

**![proteger y desproteger Hoja de Cálculo](protect-and-unprotect-worksheet.png)**  

1. Haga clic en **Revisar > Proteger Hoja**.  
1. Ingrese una contraseña en **el cuadro de Contraseña**.  
1. Seleccione las opciones de **permitir**.  
1. Seleccione **Aceptar**, vuelva a ingresar la contraseña para confirmarla y luego seleccione **Aceptar** nuevamente.  

## **Proteger la hoja de cálculo usando Aspose.Cells for JavaScript a través de C++**  
Solo necesitas las siguientes líneas de código simples para implementar la protección de la estructura del libro de trabajo de archivos de Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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
            // Create a new file (workbook)
            const workbook = new Workbook();

            // Gets the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Protect contents of the worksheet.
            sheet.protect(ProtectionType.Contents);

            // Protect worksheet with password.
            sheet.protection.password = "test";

            // Save as Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected and file is ready. Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Desproteger la hoja de cálculo usando Aspose.Cells for JavaScript a través de C++**  
Desproteger la hoja de trabajo es fácil con la API Aspose.Cells. Si la hoja está protegida por contraseña, se requiere una contraseña correcta.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Unprotect Worksheet Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Worksheet</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unprotect contents of the worksheet using password
            sheet.unprotect("password");

            // Save the modified workbook to XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Temas avanzados**  
- [Configuración de Protección Avanzada desde Excel XP](/cells/es/javascript-cpp/advanced-protection-settings-since-excel-xp/)  
- [Detectar si la hoja de cálculo está protegida con contraseña](/cells/es/javascript-cpp/detect-if-worksheet-is-password-protected/)  
- [Protección de Hojas de Cálculo](/cells/es/javascript-cpp/protecting-worksheets/)  
- [Desproteger una Hoja de Cálculo](/cells/es/javascript-cpp/unprotect-a-worksheet/)  
- [Verificar la Contraseña Utilizada para Proteger la Hoja de Cálculo](/cells/es/javascript-cpp/verify-password-used-to-protect-the-worksheet/)
