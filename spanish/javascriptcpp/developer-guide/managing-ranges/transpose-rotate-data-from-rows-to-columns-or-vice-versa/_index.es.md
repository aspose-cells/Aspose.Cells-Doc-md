---
title: Transponer Rango
linktitle: Transponer Rango
description: Este artículo explica cómo transponer o rotar datos de filas a columnas o viceversa en archivos de Excel usando Aspose.Cells for JavaScript via C++ con tres enfoques diferentes.
keywords: Aspose.Cells, JavaScript via C++, hoja de cálculo, transponer rango, rotar datos, función TRANSPOSE, fórmula de matriz dinámica, fórmula de matriz, Excel TRANSPOSE, Filas a Columnas
type: docs
weight: 80
url: /es/javascript-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ admite la transposición (rotación) de datos de manera que las filas se convierten en columnas y las columnas en filas, mediante tres maneras diferentes. El primer enfoque utiliza el método `range.transpose()` in‑place y funciona en todas las versiones de Excel, mientras que el segundo usa `cell.setDynamicArrayFormula()` para escribir una fórmula de matriz dinámica moderna `=TRANSPOSE(...)` que se expande automáticamente en Excel 365 o Excel 2021. El tercer enfoque emplea `cell.setArrayFormula()` para escribir una fórmula de matriz clásica Ctrl+Shift+Enter (CSE) que es compatible con versiones anteriores de Excel. Este artículo recorre cada enfoque con instrucciones paso a paso y ejemplos de código completos.
{{% /alert %}}

## **Introducción**
Transponer un rango significa rotarlo de modo que lo que era una fila se convierta en una columna y lo que era una columna se convierta en una fila, reflejando efectivamente los datos a través de su diagonal principal. En Microsoft Excel, la función de hoja de cálculo `TRANSPOSE` realiza esta operación, y la referencia conceptual está documentada en [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Este concepto puede aplicarse programáticamente a un rango de celdas, lo que resulta útil en muchos escenarios de negocio e informes.
- Reorientar informes de ventas trimestrales o anuales donde los trimestres normalmente aparecen a lo largo de la página y las regiones abajo de la página, o viceversa.  
- Cambiar la orientación de los ejes en paneles o gráficos para que una serie temporal se muestre verticalmente en lugar de horizontalmente.  
- Remodelar datos importados de sistemas externos para que coincidan con el diseño esperado por plantillas de análisis o informes posteriores.
Para hacer concreto el resto del artículo, cada ejemplo utiliza la siguiente tabla pequeña de ventas por región y trimestre. En el libro de trabajo de ejemplo, esta tabla ocupa el rango **A1:D5**, con **A1** vacío como esquina superior izquierda, **B1:D1** conteniendo los encabezados de región y **A2:A5** conteniendo los encabezados de trimestre.
| Región | Europa | Asia | América del Norte |
|--------|--------|------|--------------------|
| Trimestre 1 | 21704714 | 8774099 | 12094215 |
| Trimestre 2 | 17987034 | 12214447 | 10873099 |
| Trimestre 3 | 19485029 | 14356879 | 15689543 |
| Trimestre 4 | 22567894 | 15763492 | 17456723 |
El artículo luego presenta tres maneras diferentes de transponer estos datos usando Aspose.Cells for JavaScript via C++, cada una adecuada para una versión de Excel y caso de uso diferentes.

## **Enfoque 1 — Transponer Rango In‑place (Range.transpose)**
Utilice este enfoque siempre que desee transponer datos sin involucrar la función de hoja de cálculo `TRANSPOSE`. Funciona en **todas las versiones de Excel** y no depende de matrices dinámicas, lo que lo convierte en la opción más segura y compatible entre versiones. Es ideal cuando solo necesita el resultado transpuesto final y no necesita mantener la fórmula `TRANSPOSE` original en el libro de trabajo.

### **API utilizada**
`Range.transpose()` es un método de instancia en la clase `Aspose.Cells.Range`. Al llamarlo, invierte el rango in‑place al intercambiar sus filas y columnas, de modo que lo que era una fila pasa a ser una columna y viceversa. El método modifica directamente las celdas subyacentes sin escribir una fórmula.

### **Pasos**
1. Abra el libro de trabajo fuente con `LoadOptions` configurado al formato `.xlsx` llamando a `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.  
2. Obtenga la primera hoja de cálculo del libro mediante `workbook.getWorksheets().get(0)`.  
3. Acceda a la colección de celdas de la hoja mediante `worksheet.getCells()`.  
4. Cree el rango fuente que cubre **A1:D5** llamando a `cells.createRange("A1:D5")`.  
5. Llame a `source.transpose()` para rotar el rango in‑place, intercambiando filas y columnas.  
6. Guarde el libro de trabajo con `workbook.save(outputFile)`.
Después de la transposición, este rango ancla contiene los datos rotados. La primera fila muestra (vacía, **Europa**, **Asia**, **América del Norte**) y la primera columna muestra (vacía, **Trimestre 1**, **Trimestre 2**, **Trimestre 3**, **Trimestre 4**). Cada columna original de ventas se convierte en una fila en el rango transpuesto.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an .xlsx file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const source = cells.createRange("A1:D5");
                source.transpose();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "transposed.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred while processing the file.</p>';
            }
        });
    </script>
</html>
```

## **Enfoque 2 — Transponer con una Fórmula de Matriz Dinámica (Excel 365 / 2021)**
Utilice este enfoque cuando desee preservar la fórmula `=TRANSPOSE(A1:D5)` como una fórmula activa en el libro de trabajo de salida, de modo que el resultado se actualice automáticamente si los datos de origen cambian, y el archivo objetivo se abrirá en **Excel 365 / Excel 2021 o posterior**, donde se admiten matrices dinámicas y el operador de desbordamiento.

### **API utilizada**
`Cell.setDynamicArrayFormula(formula, options, calculateValue)` es un método de la clase `Aspose.Cells.Cell` que establece la fórmula de la celda como una **fórmula de matriz dinámica**. Excel evalúa la fórmula una vez y expande automáticamente el resultado a las celdas circundantes. El tercer parámetro, cuando se establece en `true`, indica an Aspose.Cells que también calcule los valores resultantes en el momento de la escritura.

### **Pasos**
1. Cargue el libro de trabajo fuente usando `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.  
2. Obtenga la primera hoja de cálculo y acceda a su colección de celdas.  
3. Coloque la fórmula de matriz dinámica en la celda **A6**, justo debajo del rango fuente, llamando a `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)`.  
4. El argumento `new FormulaParseOptions()` utiliza la configuración predeterminada de `FormulaParseOptions`, y el tercer argumento `true` indica an Aspose.Cells que trate la fórmula como una matriz dinámica y la evalúe para que los valores desbordados se escriban en el libro.  
5. Guarde el libro de trabajo con `workbook.save(outputFile)`.
La celda **A6** contiene la fórmula `=TRANSPOSE(A1:D5)` y Excel expande el resultado automáticamente al rango **A6:E9**, un bloque de 4 filas por 5 columnas que equivale a los datos transpuestos.

{{% alert color="primary" %}}
Este enfoque funciona **solo en Excel 365 / 2021 o posterior**. Las versiones anteriores de Excel no expandirán correctamente las fórmulas de matrices dinámicas.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FormulaParseOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            const workbook = new Workbook(new Uint8Array(await fileInput.files[0].arrayBuffer()));
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A6").setDynamicArrayFormula(
                "=TRANSPOSE(A1:D5)",
                new FormulaParseOptions(),
                true
            );
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_transpose_dynamic.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Enfoque 3 — Transponer con una Fórmula de Matriz Clásica (CSE)**
Utilice este enfoque cuando quiera que se preserve una fórmula `TRANSPOSE` en el libro de trabajo, pero el archivo objetivo pueda abrirse en **versiones antiguas de Excel (pre‑2021, incluidas 2019, 2016, 2013, etc.)** donde no se admiten matrices dinámicas. La fórmula clásica CSE (Ctrl+Shift+Enter) es la alternativa compatible con versiones anteriores que todas las versiones de Excel pueden evaluar.

### **API utilizada**
`Cell.setArrayFormula(arrayFormula, nRows, nColumns)` es un método de la clase `Aspose.Cells.Cell` que asigna una **fórmula de matriz clásica (CSE)** a la celda ancla y declara las dimensiones de la matriz resultante. Aspose.Cells escribe el marcador de fórmula de matriz multicíelda para que Excel evalúe la fórmula como una única expresión de matriz que llena el rango declarado.

### **Pasos**
1. Cargue el libro de trabajo fuente como se describió en los enfoques anteriores.  
2. Obtenga la primera hoja de cálculo y acceda a su colección de celdas.  
3. Llame a `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. El segundo argumento `4` indica el número de filas de la matriz de destino y el tercer argumento `5` indica el número de columnas.  
4. Guarde el libro de trabajo con `workbook.save(outputFile)`.
La celda **A6** es el ancla de la fórmula de matriz y la matriz evaluada abarca 4 filas por 5 columnas a partir de A6, coincidiendo con las dimensiones transpuestas del origen **A1:D5**. Excel escribe un marcador de fórmula de matriz única a través del rango resultante para que las versiones antiguas de Excel la evalúen correctamente.

{{% alert color="primary" %}}
Las fórmulas de matriz CSE son la forma clásica de Excel para evaluar una expresión `TRANSPOSE` y este enfoque es universalmente compatible en todas las versiones de Excel.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await initialization;
                const fileInput = document.getElementById('fileInput');
                const downloadLink = document.getElementById('downloadLink');
                const result = document.getElementById('result');
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Please select an XLSX workbook.");
                }
                // Cargar el libro de trabajo de origen con LoadOptions de xlsx
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
                const workbook = new Workbook(
                    new Uint8Array(await file.arrayBuffer()),
                    loadOptions
                );
                // Acceder a la primera hoja de cálculo y a su colección de celdas
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Establecer la fórmula de matriz clásica CSE en la celda A6.
                // La fórmula =TRANSPOSE(A1:D5) rota el rango de origen de 5 filas por 4 columnas
                // a una matriz de 4 filas por 5 columnas. El segundo argumento (4) es el número de filas
                // y el tercer argumento (5) es el número de columnas de la matriz resultante.
                // Aspose.Cells escribe el marcador de fórmula de matriz CSE para que Excel la evalúe como
                // una única fórmula de matriz de varias celdas, compatible con versiones antiguas de Excel
                // (2019, 2016, 2013, etc.) que no admiten el desbordamiento de matrices dinámicas.
                cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
                // Guardar el libro de trabajo para que el marcador de fórmula de matriz persista
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Error: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Comparación — Cuándo Utilizar Cada Enfoque**
| Enfoque | API / Método | Versión de Excel | ¿Fórmula de origen preservada? | Rango de salida |
|----------|--------------|-------------------|-------------------------------|-----------------|
| Enfoque 1 — Transposición in‑place | `range.transpose()` | Todas las versiones de Excel | No (solo valores) | Rango ancla inicial, 5×4 |
| Enfoque 2 — Fórmula de matriz dinámica | `cell.setDynamicArrayFormula()` | Excel 365 / 2021+ | Sí (se expande dinámicamente) | Expansión desde el ancla |
| Enfoque 3 — Fórmula de matriz clásica (CSE) | `cell.setArrayFormula()` | Todas las versiones de Excel | Sí (fórmula de matriz multicíelda) | Tamaño explícito, 4×5 |
Use **Enfoque 1** cuando necesite una transformación rápida, compatible con todas las versiones, y solo requiera los valores transpuestos escritos en el archivo. Use **Enfoque 2** cuando se garantice Excel moderno y desee que la fórmula permanezca viva y se actualice si el origen cambia. Use **Enfoque 3** cuando necesite la mayor compatibilidad posible con una fórmula preservada en todas las versiones de Excel, incluidas las versiones más antiguas que no soportan matrices dinámicas.

{{< app/cells/assistant language="javascript-cpp" >}}