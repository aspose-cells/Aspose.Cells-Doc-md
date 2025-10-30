---
title: Congelar paneles de la hoja de Excel con JavaScript a través de C++
linktitle: Congelar paneles
type: docs
weight: 190
url: /es/javascript-cpp/how-to-freeze-panes-of-excel-worksheet
description: En este artículo, aprenderá cómo congelar paneles de las hojas de Excel de manera programática usando Aspose.Cells for JavaScript a través de C++.
keywords: Congelar paneles, congelar ventana.
---

## **Introducción**  

En este artículo, aprenderemos Cómo congelar paneles. Cuando tienes una gran cantidad de datos bajo un encabezado común, no puedes ver el encabezado cuando te desplazas hacia abajo en la hoja de cálculo. Y cada registro contiene muchos datos. Puedes congelar paneles para que puedas ver esa parte congelada incluso cuando se desplaza el resto de los datos. Puedes ver fácilmente los encabezados en las filas superiores o en las primeras columnas. Congelar y descongelar paneles solo cambia la vista de los datos sin modificarlos.  

## **En Excel**  

**![Congelar paneles en Excel](Congelar-paneles.png)**  

1. Si deseas congelar paneles, congelar filas y columnas, primero selecciona una celda (como B2).  
2. Haz clic en Ver > Congelar paneles.  
3. En el menú desplegable, haga clic en Congelar paneles.  
4. Si te desplazas hacia abajo o a la derecha, la primera fila y columna permanecen congeladas.  

**![Paneles congelados](Frozen-Panes.png)**  

Como puedes ver, la primera fila y la columna A están congeladas, la segunda fila es 32 y la segunda columna visible es D.  

Las ventanas congeladas te permiten ver tus datos grandes sin llevar un seguimiento de la fila o etiqueta de columna.  

## **Congelar paneles con Aspose.Cells for JavaScript vía C++**  
Es simple congelar paneles con Aspose.Cells for JavaScript vía C++. Por favor, utilice el método [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) para congelar paneles en la celda seleccionada.  
1. Construir un libro de trabajo para abrir el archivo o crear un archivo vacío.  
2. Congelar paneles con el método Worksheet.freezePanes().  
3. Guarda el archivo.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <p>Select an Excel file (Freeze.xlsx) and click "Run Example" to freeze panes at B2.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Freezing panes at the cell B2
            worksheet.freezePanes("B2", 1, 1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Panes frozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```  

Adjunto [archivo de Excel de origen de muestra](Freeze.xlsx).
