---
title: Desactivar el Verificador de Compatibilidad en Excel con JavaScript mediante C++
linktitle: Deshabilitar el Comprobador de Compatibilidad en Excel
type: docs
weight: 170
url: /es/javascript-cpp/disable-compatibility-checker-in-excel/
description: Aprende cómo desactivar el verificador de compatibilidad a través del Script Aspose.Cells for JavaScript mediante la API de C++.
keywords: JavaScript Desactivar el Verificador de Compatibilidad, Desactivar el Verificador de Compatibilidad en Excel con JavaScript a través de C++, Desactivar el Verificador de Compatibilidad en el Libro de Trabajo.
---

## Desactivar el Verificador de Compatibilidad en las hojas de Excel con JavaScript  

{{% alert color="primary" %}}  
El Comprobador de compatibilidad de Microsoft Excel señala cuando guardar un archivo en un formato anterior podría causar problemas de funcionamiento o pérdida de fidelidad. El Comprobador de compatibilidad es una característica de Microsoft Office Excel 2007 y Microsoft Excel 2010.  

Al guardar un libro de trabajo en una versión anterior, Excel 97 a través de Excel 2003, desde Excel 2007 o Excel 2010, el Comprobador de Compatibilidad escanea el libro de trabajo para ver si contiene funciones que no son compatibles con la versión anterior. Para ayudarlo a tomar decisiones sobre cómo manejar problemas de compatibilidad, el Comprobador de Compatibilidad muestra cuadros de diálogo con opciones. También se puede utilizar para crear un informe sobre cualquier problema en el libro de trabajo o deshabilitar la función.  

A veces, necesitas desactivar el Comprobador de Compatibilidad para una hoja de cálculo en particular. Con las API de Aspose.Cells, puedes hacer esto programáticamente para que los usuarios no se frustren ni se confundan con la ventana de diálogo del Comprobador de Compatibilidad que aparece cuando vuelven a guardar el archivo manualmente en Microsoft Excel.  
{{% /alert %}}  

## **Cómo Deshabilitar el Comprobador de compatibilidad usando Microsoft Excel**  

Para deshabilitar el Comprobador de compatibilidad en Microsoft Excel (por ejemplo, Microsoft Excel 2007/2010):  

- (Excel 2007) En el botón de Office, haz clic en **Preparar**, luego en **Ejecutar Comprobador de compatibilidad**, y luego desmarca la opción **Comprobar compatibilidad al guardar este libro**.  
- (Excel 2010) En la pestaña **Archivo**, haz clic en **Información**, luego en **Buscar problemas**, haz clic en **Comprobar compatibilidad** y, finalmente, desmarca la opción **Comprobar compatibilidad al guardar este libro**.  

## **Cómo Deshabilitar el Comprobador de compatibilidad usando las API de Aspose.Cells**  

Establece la propiedad [**Workbook.checkCompatibility**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCompatibility--) en **falso** para desactivar el Comprobador de Compatibilidad de Microsoft Excel.  

### **Ejemplos de código**  

Los ejemplos de código que siguen muestran cómo desactivar el Verificador de Compatibilidad con Script Aspose.Cells for JavaScript a través de C++.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Compatibility Checker Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Disable the compatibility checker
            workbook.settings.checkCompatibility = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_BK_CompCheck.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Compatibility check disabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
