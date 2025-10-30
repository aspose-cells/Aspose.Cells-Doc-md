---
title: Cómo prevenir que los usuarios impriman el archivo de Excel con JavaScript vía C++
linktitle: Cómo Prevenir que los Usuarios Impriman un Archivo de Excel
type: docs
weight: 600
url: /es/javascript-cpp/how-to-prevent-printing-excel/
description: Aprende cómo impedir que los usuarios impriman archivos de Excel usando Aspose.Cells for JavaScript vía C++.
keywords: impresión de excel, evitar la impresión de excel, cómo evitar que los usuarios impriman excel, excel evitar impresión, evitar impresión del libro de trabajo, Evitar que los usuarios impriman el libro completo con VBA.
---

## **Escenarios de uso posibles**  
En nuestro trabajo diario, puede haber información importante en el archivo de Excel; para proteger los datos internos de la difusión, la empresa no nos permitirá imprimirlos. Este documento le dirá cómo evitar que otros impriman archivos de Excel.  

## **Cómo evitar que los usuarios impriman archivos en MS-Excel**  
Puede aplicar el siguiente código VBA para proteger su archivo específico de ser impreso.  
1. Abra su libro de trabajo que no permite que otros lo impriman.  
1. Seleccione la pestaña "Desarrollador" en la cinta de opciones de Excel y haga clic en el botón "Ver código" en la sección "Controles". Alternativamente, puede mantener presionadas las teclas ALT + F11 para abrir la ventana de Microsoft Visual Basic para Aplicaciones.  
<br>  
<img src="1.png" width=70% />  
1. Y luego, en el Explorador de proyectos en la izquierda, haga doble clic en ThisWorkbook para abrir el módulo, y agregue algunos códigos VBA.  
<br>  
<img src="2.png" width=70% />  
1. Luego, guarde y cierre este código, regrese al libro en blanco, y ahora cuando imprima el archivo de muestra, no se permitirá imprimir, y recibirá el siguiente cuadro de advertencia:  
<br>  
<img src="3.png" width=70% />  

## **Cómo impedir que los usuarios impriman un archivo de Excel usando Aspose.Cells for JavaScript vía C++**  

El siguiente código de muestra ilustra cómo prevenir que los usuarios impriman un archivo de Excel:  

1. Cargar el [archivo de muestra](sample.xlsx).  
1. Obtenga el objeto VbaModuleCollection desde la propiedad VbaProject del libro de trabajo.  
1. Obtenga el objeto VbaModule mediante el nombre "ThisWorkbook".  
1. Establezca la propiedad de códigos de VbaModule.  
1. Guarde el archivo de muestra en [formato xlsm](out.xlsm).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
        <button id="runExample">Run Example</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing VBA project and its modules
            const modules = workbook.vbaProject.modules;
            const module = modules.get("ThisWorkbook");

            // Setting module codes (converted from setCodes -> codes assignment)
            module.codes = "Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n";

            // Saving the modified workbook as macro-enabled workbook
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
