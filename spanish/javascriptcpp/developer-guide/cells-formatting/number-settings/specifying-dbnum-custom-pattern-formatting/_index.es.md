---
title: Especificar Formato de Patrón Personalizado DBNum
linktitle: Especificar Formato de Patrón Personalizado DBNum
description: Aspose.Cells es una biblioteca para JavaScript vía C++ que soporta el formateo de fechas y números usando patrones de formato personalizados. Este artículo muestra cómo especificar el patrón de formato personalizado dbnum para un mejor control sobre la visualización de números.
keywords: Aspose.Cells, JavaScript vía C++, hoja de cálculo electrónica, patrón de formato personalizado, formateo, dbnum , control de visualización
type: docs
weight: 110
url: /es/javascript-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Escenarios de uso posibles**

Aspose.Cells for JavaScript vía C++ soporta el formato de patrón personalizado *DBNum*. Por ejemplo, si el valor de tu celda es 123 y especificas su formato personalizado como [DBNum2][$-804]General, se mostrará como 壹佰贰拾叁. Puedes especificar el formato personalizado de la celda usando el método [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) y el método [**Style.custom(string)**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-).

## **Código de muestra**

El siguiente código de ejemplo ilustra cómo especificar el formato de patrón personalizado *DBNum*. Por favor, revisa su [archivo PDF de salida](43352081.pdf) para más ayuda.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - DBNum Custom Formatting Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Access cell A1 and put value 123.
            const cell = ws.cells.get("A1");
            cell.value = 123;

            // Access cell style.
            const st = cell.style;

            // Specifying DBNum custom pattern formatting.
            st.custom = "[DBNum2][$-804]General";

            // Set the cell style.
            cell.style = st;

            // Set the first column width.
            ws.cells.columns.get(0).width = 30;

            // Save the workbook in output pdf format.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDBNumCustomFormatting.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
