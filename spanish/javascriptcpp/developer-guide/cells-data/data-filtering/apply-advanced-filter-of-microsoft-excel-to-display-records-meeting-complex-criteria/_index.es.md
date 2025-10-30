---
title: Aplicar filtro avanzado de Microsoft Excel para mostrar registros que cumplan criterios complejos
type: docs
weight: 280
url: /es/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Aprende cómo aplicar el filtro avanzado de Microsoft Excel para mostrar registros que cumplen criterios complejos usando el script Aspose.Cells for Java a través de la API C++.
keywords: Aplicar filtro avanzado JavaScript a través de C++, configurar filtro avanzado JavaScript a través de C++, agregar filtro avanzado JavaScript a través de C++, crear filtro avanzado JavaScript a través de C++, cómo agregar filtro avanzado a un rango JavaScript mediante C++
---

## **Escenarios de uso posibles**  

Microsoft Excel permite aplicar *Filtro Avanzado* en datos de hojas de cálculo para mostrar registros que cumplen criterios complejos. Puedes aplicar Filtro Avanzado con Microsoft Excel usando su comando *Datos > Avanzadas* como se muestra en esta captura.  

![todo:image_alt_text](1.png)  

El script Aspose.Cells for Java a través de C++ también permite aplicar el filtro avanzado usando el método [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-). Al igual que Microsoft Excel, acepta los siguientes parámetros.  

**isFilter**  

Indica si se está filtrando la lista en su lugar.  

**listRange**  

El rango de la lista.  

**criteriaRange**  

El rango de criterios.  

**copyTo**  

El rango donde se copian los datos.  

**uniqueRecordOnly**  

Solo muestra o copia filas únicas.  

## **Aplicar Filtro Avanzado de Microsoft Excel para Mostrar Registros que Cumplen Criterios Complejos**  

El siguiente código de ejemplo aplica el filtro avanzado en el [Archivo de Excel de muestra](48496692.xlsx) y genera el [Archivo de Excel de salida](48496691.xlsx). La captura de pantalla muestra ambos archivos para comparación. Como puedes ver en la captura, los datos han sido filtrados en el archivo de Excel de salida de acuerdo con criterios complejos.  

![todo:image_alt_text](2.png)  

## **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Advanced Filter Example</title>
    </head>
    <body>
        <h1>Advanced Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Advanced Filter</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (sampleAdvancedFilter.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const wb = new Workbook(new Uint8Array(arrayBuffer));

            const ws = wb.worksheets.get(0);

            // Apply advanced filter on range A5:D19 with criteria A1:D2, filter in place, include all records (not unique)
            ws.advanced_Filter(true, "A5:D19", "A1:D2", "", false);

            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAdvancedFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Advanced filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
