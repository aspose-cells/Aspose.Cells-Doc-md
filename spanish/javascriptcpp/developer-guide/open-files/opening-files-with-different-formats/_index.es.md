---
title: Abrir archivos con diferentes formatos con JavaScript a través de C++
linktitle: Apertura de archivos con diferentes formatos
type: docs
weight: 30
url: /es/javascript-cpp/opening-files-with-different-formats/
description: La API Aspose.Cells for JavaScript a través de C++ permite abrir/leer diferentes formatos como XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: abrir archivos xlsx, abrir archivos html, leer archivos fods, leer archivos ods, leer archivos sxc, abrir archivos csv, Delimitado por tabulaciones, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Con Aspose.Cells, puede abrir archivos con diferentes formatos. **Aspose.Cells** puede abrir una variedad de formatos de archivo como hojas de cálculo de Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valores separados por comas (CSV), archivos delimitados por tabulaciones (TSV), etc.

Si necesitas conocer todos los formatos de archivo admitidos, consulta las siguientes páginas:
[Formatos de archivos compatibles](https://docs.aspose.com/cells/javascript-cpp/supported-file-formats/)

{{% /alert %}}

## **Abriendo Archivos con Diferentes Formatos**

Aspose.Cells permite a los desarrolladores abrir archivos de hoja de cálculo con diferentes formatos como SpreadsheetML, valores separados por comas (CSV), valores delimitados por tabuladores (TSV), archivos ODS. Para abrir tales archivos, los desarrolladores pueden usar la misma metodología que usan para abrir archivos de diferentes versiones de Microsoft Excel.

### **Abriendo Archivos de SpreadsheetML**

Los archivos SpreadsheetML son representaciones XML de hojas de cálculo que incluyen toda la información sobre ellas, como formato, fórmulas, etc. Desde Microsoft Excel XP, se añadió una opción de exportación XML a Microsoft Excel que exporta tus hojas de cálculo a archivos SpreadsheetML.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open SpreadsheetML (Book3.xml)</h1>
        <input type="file" id="fileInput" accept=".xml,.xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an SpreadsheetML (.xml) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.SpreadsheetML);

            // Create a Workbook object and open the file from the uploaded data
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            document.getElementById('result').innerHTML = '<p style="color: green;">SpreadSheetML file opened successfully!</p>';
            console.log("SpreadSheetML file opened successfully!");
        });
    </script>
</html>
```

### **Abriendo Archivos HTML**

Aspose.Cells te permite abrir un archivo HTML en un objeto Workbook. El archivo HTML debe estar orientado a Microsoft Excel, es decir, MS-Excel debería poder abrirlo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert HTML to XLSX Example</h1>
        <input type="file" id="fileInput" accept=".html,.htm" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat } = AsposeCells;

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
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an HTML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);

            // Create a Workbook object and opening the file from the uploaded file data
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the XLSX file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted XLSX File';

            resultEl.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the converted file.</p>';
        });
    </script>
</html>
```

### **Abriendo Archivos CSV**

Los archivos de valores separados por comas (CSV) contienen registros donde los valores están separados por comas. Los datos se almacenan en forma de tabla donde cada columna está separada por el carácter coma y entrecomillada por el carácter de comillas dobles. Si un valor de campo contiene un carácter de comillas dobles, se escapa con un par de comillas dobles. También puedes usar Microsoft Excel para exportar datos de hojas de cálculo a CSV.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells CSV Open Example</title>
    </head>
    <body>
        <h1>Aspose.Cells CSV Open Example</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Open CSV</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions4 = new LoadOptions(LoadFormat.Csv);

            // Create a Workbook object and open the file from the uploaded data
            const wbCSV = new Workbook(new Uint8Array(arrayBuffer), loadOptions4);

            document.getElementById('result').innerHTML = '<p style="color: green;">CSV file opened successfully!</p>';
        });
    </script>
</html>
```

#### **Abriendo Archivos CSV y reemplazando caracteres inválidos**

En Excel, cuando se abre un archivo CSV con caracteres especiales, los caracteres se reemplazan automáticamente. Lo mismo hace la API Aspose.Cells, como se demuestra en el ejemplo de código a continuación.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Load CSV with TxtLoadOptions Example</title>
    </head>
    <body>
        <h1>Load CSV with TxtLoadOptions Example</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, TxtLoadOptions, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                const loadOptions = new TxtLoadOptions();
                loadOptions.separator = ';';
                loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.CellData);
                loadOptions.checkExcelRestriction = false;
                loadOptions.convertNumericData = false;
                loadOptions.convertDateTimeData = false;

                const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

                const worksheet = workbook.worksheets.get(0);
                const sheetName = worksheet.name;
                const nameLength = sheetName.length;

                console.log(sheetName);
                console.log(nameLength);
                console.log("CSV file opened successfully!");

                document.getElementById('result').innerHTML = `<p>Worksheet Name: ${sheetName}</p><p>Name Length: ${nameLength}</p><p style="color: green;">CSV file opened successfully!</p>`;
            });
        });
    </script>
</html>
```

### **Abriendo Archivos de Texto con Separador Personalizado**

Los archivos de texto se usan para contener datos de hojas de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells CSV to Text Example</title>
    </head>
    <body>
        <h1>Convert CSV to Text Example</h1>
        <input type="file" id="fileInput" accept=".csv,.txt" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Text File's LoadOptions
            const txtLoadOptions = new TxtLoadOptions();

            // Specify the separator
            txtLoadOptions.separator = ",";

            // Specify the encoding type
            txtLoadOptions.encoding = AsposeCells.EncodingType.UTF8;

            // Create a Workbook object and open the file from the uploaded data
            const wb = new Workbook(new Uint8Array(arrayBuffer), txtLoadOptions);

            // Save file as text and provide download link
            const outputData = wb.save(SaveFormat.Text);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.txt';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Text File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the converted file.</p>';
        });
    </script>
</html>
```

### **Apertura de archivos con formato de pestañas**

Los archivos delimitados por tabulaciones (Texto) contienen datos de hojas de cálculo pero sin formato. Los datos se organizan en filas y columnas como en tablas y hojas de cálculo. Básicamente, un archivo delimitado por tabulación es un tipo especial de archivo de texto simple con una tabulación entre cada columna.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Open Tab Delimited</title>
    </head>
    <body>
        <h1>Open Tab Delimited Example</h1>
        <input type="file" id="fileInput" accept=".txt,.csv,.tsv" />
        <button id="runExample">Open File</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a tab-delimited (.txt/.tsv) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.TabDelimited);

            // Create a Workbook object and open the file from the uploaded file buffer
            const wbTabDelimited = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            document.getElementById('result').innerHTML = '<p style="color: green;">Tab delimited file opened successfully!</p>';
        });
    </script>
</html>
```

### **Apertura de archivos de Valores Separados por Comas y con pestañas (TSV)**

Un archivo de valores delimitados por tabulaciones (TSV) contiene datos de hojas de cálculo pero sin ningún formato. Es lo mismo que un archivo delimitado por tabulaciones, donde los datos se disponen en filas y columnas como en tablas y hojas de cálculo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TSV Load Example</title>
    </head>
    <body>
        <h1>TSV Load Example</h1>
        <input type="file" id="fileInput" accept=".tsv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a TSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.Tsv);

            // Create a Workbook object and opening the file from the uploaded file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Using the Sheet 1 in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("C3");

            // Display cell name and value
            document.getElementById('result').innerHTML = `<p>Cell Name: ${cell.name} Value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **Apertura de archivos SXC**

StarOffice Calc es similar a Microsoft Excel y soporta fórmulas, gráficos, funciones y macros. Las hojas de cálculo creadas con este software se guardan con la extensión SXC. El archivo SXC también se usa para archivos de hojas de cálculo de OpenOffice.org Calc. Aspose.Cells puede leer archivos SXC, como se demuestra en el siguiente ejemplo de código.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read SXC Cell Example</h1>
        <input type="file" id="fileInput" accept=".sxc" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select an SXC file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.Sxc);

            // Create a Workbook object and open the file from the uploaded data
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Using the first worksheet in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("C3");

            // Display cell name and string value
            resultDiv.innerHTML = `<p>Cell Name: ${cell.name} Value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **Apertura de archivos FODS**

El archivo FODS es una hoja de cálculo guardada en XML OpenDocument sin compresión. Aspose.Cells puede leer archivos FODS, como se demuestra en el siguiente ejemplo de código.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Open FODS</title>
    </head>
    <body>
        <h1>Open FODS Example</h1>
        <input type="file" id="fileInput" accept=".fods" />
        <button id="runExample">Open FODS File</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select a FODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.Fods);

            // Create a Workbook object and open the file from the uploaded data
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            document.getElementById('result').innerHTML = '<p style="color: green;">FODS file opened successfully!</p>';
        });
    </script>
</html>
```
