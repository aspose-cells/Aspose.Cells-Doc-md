---
title: Configuración de opciones de impresión con JavaScript vía C++
linktitle: Configuración de Opciones de Impresión
type: docs
weight: 40
url: /es/javascript-cpp/setting-print-options/
description: Este artículo demuestra cómo establecer programáticamente las opciones de impresión de la función Configuración de página de la hoja de cálculo de Excel usando la API de JavaScript y la biblioteca C++. Puede establecer el área de impresión, los títulos de impresión y el orden de las páginas.
keywords: establecer área de impresión en Excel con JavaScript vía C++, establecer títulos de impresión en Excel con JavaScript vía C++, establecer orden de página en Excel con JavaScript vía C++
---

{{% alert color="primary" %}}

La configuración de página de Microsoft Excel proporciona varias opciones de impresión (también conocidas como opciones de hoja) que permiten a los usuarios controlar cómo se imprimen las páginas de la hoja de cálculo.

{{% /alert %}}

## **Configuración de Opciones de Impresión**

Estas opciones de impresión permiten a los usuarios:

- Seleccionar un área de impresión específica en una hoja de cálculo.
- Títulos de impresión.
- Líneas de cuadrícula de impresión.
- Encabezados de fila/columna de impresión.
- Lograr calidad de borrador.
- Comentarios de impresión.
- Errores de celda de impresión.
- Definir el orden de páginas.

 Aspose.Cells for JavaScript vía C++ soporta todas las opciones de impresión ofrecidas por Microsoft Excel y los desarrolladores pueden configurar fácilmente estas opciones para las hojas de cálculo usando las propiedades ofrecidas por la clase [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup). Cómo se usan estas propiedades se discute más abajo en más detalle.

### **Establecer Área de Impresión**

De forma predeterminada, el área de impresión abarca todas las áreas de la hoja de cálculo que contienen datos. Los desarrolladores pueden establecer un área de impresión específica de la hoja de cálculo.

Para seleccionar un área de impresión específica, utilice la propiedad [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) de la clase [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup). Asigne un rango de celdas que defina el área de impresión a esta propiedad.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Print Area Example</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Specifying the cells range (from A1 cell to T35 cell) of the print area
            pageSetup.printArea = "A1:T35";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintArea_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Establecer Títulos de Impresión**

Aspose.Cells le permite designar encabezados de fila y columna para repetir en todas las páginas de una hoja de cálculo impresa. Para hacerlo, utilice las propiedades [**PageSetup.printTitleColumns**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleColumns--) y [**PageSetup.printTitleRows**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleRows--) de la clase [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup).

Las filas o columnas que se repetirán se definen pasando sus números de fila o columna. Por ejemplo, las filas se definen como $1:$2 y las columnas se definen como $A:$B.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Title</title>
    </head>
    <body>
        <h1>Set Print Title Columns and Rows Example</h1>
        <p>You may optionally select an existing Excel file to modify. If no file is selected, a new workbook will be created.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Defining column numbers A & B as title columns
            pageSetup.printTitleColumns = "$A:$B";

            // Defining row numbers 1 & 2 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintTitle_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print title columns and rows set successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **Establecer Otras Opciones de Impresión**

La clase [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) también proporciona varias otras propiedades para establecer opciones generales de impresión como sigue:

- [**PageSetup.printGridlines**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printGridlines--): una propiedad booleana que define si imprimir o no las líneas de cuadrícula.
- [**PageSetup.printHeadings**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printHeadings--): una propiedad booleana que define si imprimir o no encabezados de filas y columnas.
- [**PageSetup.blackAndWhite**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#blackAndWhite--): una propiedad booleana que define si imprimir la hoja de cálculo en modo blanco y negro o no.
- [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--): define si mostrar los comentarios de impresión en la hoja de cálculo o al final de la hoja.
- [**PageSetup.printDraft**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printDraft--): una propiedad booleana que define si imprimir la hoja sin gráficos.
- [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--): define si se deben imprimir los errores de celda como se muestra, en blanco, como guion o N/A.

 Para establecer las propiedades [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) y [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--), Aspose.Cells for JavaScript vía C++ también proporciona dos enumeraciones, [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) y [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype) que contienen valores predefinidos que se asignarán a las propiedades [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) y [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--) respectivamente.

Los valores predefinidos en la enumeración [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) se muestran a continuación con sus descripciones.

|**Tipos de Imprimir Comentarios**|**Descripción**|
| :- | :- |
|PrintInPlace| Especifica imprimir comentarios como se muestra en la hoja de cálculo.
|PrintNoComments| Especifica no imprimir comentarios.
|PrintSheetEnd| Especifica imprimir comentarios al final de la hoja de cálculo.

Los valores predefinidos de la enumeración [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype) se muestran a continuación con sus descripciones.

|**Tipos de Imprimir Errores**|**Descripción**|
| :- | :- |
|PrintErrorsBlank| Especifica no imprimir errores.
|PrintErrorsDash| Especifica imprimir errores como "--".
|PrintErrorsDisplayed| Especifica imprimir errores como se muestra.
|PrintErrorsNA| Especifica imprimir errores como "#N/A".

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Other Print Options</title>
    </head>
    <body>
        <h1>Other Print Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintCommentsType, PrintErrorsType } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = PrintErrorsType.PrintErrorsNA;

            // Saving the modified workbook to Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OtherPrintOptions_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Establecer Orden de Páginas**

La clase [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) proporciona la propiedad [**PageSetup.order**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#order--) que se usa para ordenar varias páginas de su hoja de cálculo para su impresión. Hay dos posibilidades para ordenar las páginas de la siguiente manera.

-  imprime todas las páginas hacia abajo antes de imprimir cualquier página a la derecha.
-  imprime las páginas de izquierda a derecha antes de imprimir las páginas debajo.

Aspose.Cells proporciona una enumeración, [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype) que contiene todos los tipos de orden predefinidos.

Los valores predefinidos de la enumeración [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype) se muestran a continuación.

|**Tipos de Orden de Impresión**|**Descripción**|
| :- | :- |
|DownThenOver|Representa el orden de impresión como primero hacia abajo y luego hacia adelante.|
|OverThenDown|Representa el orden de impresión como primero hacia adelante y luego hacia abajo.|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Set Page Order Example</title>
    </head>
    <body>
        <h1>Set Page Order Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintOrderType } = AsposeCells;

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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;
            pageSetup.order = PrintOrderType.OverThenDown;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPageOrder_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page order set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
