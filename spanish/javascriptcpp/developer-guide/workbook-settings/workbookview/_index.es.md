---
title: Cómo Controlar la Vista del Libro de Trabajo con JavaScript a través de C++
linktitle: Cómo Controlar la Vista del Libro de Trabajo
type: docs
weight: 600
url: /es/javascript-cpp/how-to-control-workbook-view/
description: Aprende a controlar la Vista del Libro de Trabajo a través del script Aspose.Cells for Java mediante API C++.
keywords: Cómo Controlar la Vista del Libro de Trabajo con JavaScript mediante C++, Configurar Vista de Excel en JavaScript mediante C++, Operar Vista de Libro de Trabajo en JavaScript mediante C++, Configurar vista de libro de trabajo en JavaScript mediante C++, Controlar Vista de Excel en JavaScript mediante C++.
---

## **Escenarios de uso posibles**
 Cuando necesitas ajustar la visualización de páginas de Excel, debes conocer cómo controlar cada módulo, como barras de desplazamiento horizontales y verticales, si ocultar o no archivos de Excel abiertos, y más. El script Aspose.Cells for Java a través de C++ ofrece esta característica. El script Aspose.Cells for Java proporciona las siguientes propiedades y métodos para ayudarte a lograr tus objetivos.

- [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--)
- [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--)
- [**WorkbookSettings.isHidden()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHidden--)
- [**WorkbookSettings.isMinimized()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isMinimized--)
- [**WorkbookSettings.windowHeight**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowHeight--)
- [**WorkbookSettings.windowWidth**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowWidth--)
- [**WorkbookSettings.windowLeft**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowLeft--)
- [**WorkbookSettings.windowTop**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowTop--)

## **Cómo Controlar la Vista del Libro usando Aspose.Cells for JavaScript a través de C++**
Este ejemplo muestra cómo:

1. Crear un libro de trabajo.
1. Agregar datos a las celdas en la primera hoja de cálculo.
1. Ocultar las barras de desplazamiento horizontal y vertical de la Vista del Libro de Trabajo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
        <p>Select an existing .xls/.xlsx file to modify, or leave empty to create a new workbook.</p>
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
            // If a file is selected, open it; otherwise create a new workbook (matches original Node behavior)
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue => value)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;

            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Apply style: createStyle(), font/color adjustments converted from get/set to properties
            cell = cells.get("E10");
            const temp = workbook.createStyle();
            temp.font.color = AsposeCells.Color.Red;
            cell.style = temp;

            // Hide horizontal and vertical scrollbars (converted getSettings().set... -> settings.is... = ...)
            workbook.settings.isHScrollBarVisible = false;
            workbook.settings.isVScrollBarVisible = false;

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Vista previa del archivo resultante:
<br>
<image src="result.png" width="70%" />
