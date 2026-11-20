---
title: Agrupar campos dinámicos en la Tabla Dinámica
linktitle: Agrupar campos dinámicos en la Tabla Dinámica
description: Aprenda a agrupar campos dinámicos de fila y columna en una tabla dinámica en periodos de fechas como meses y trimestres, y en rangos numéricos, mediante PivotField.group y PivotFieldGroupOptions en Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, tabla dinámica, agrupar campo dinámico, PivotField.group, PivotFieldGroupOptions, agrupación de fechas, agrupación de números, meses, trimestres, rango numérico, JavaScript via C++
type: docs
weight: 80
url: /es/javascript-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
- Agrupar campos dinámicos resulta útil cuando un campo de fila o columna de una tabla dinámica contiene muchos elementos distintos, como un campo de fecha con cientos de fechas o un campo numérico con muchos valores dispersos. La agrupación contrae estos elementos en secciones significativas: las fechas se agrupan en meses, trimestres y años, y los números en rangos como 0-1, 2-3 y 4-5. Esto permite que una tabla dinámica grande sea más compacta y fácil de analizar. Aspose.Cells ofrece esta funcionalidad mediante el método `PivotField.group()` (agrupación automática por tipo de datos) y `PivotField.group(PivotFieldGroupOptions)` (opciones de agrupación personalizadas).
- La agrupación de fechas consolida las fechas individuales en periodos más amplios, como días, meses, trimestres y años, y crea una jerarquía temporal (por ejemplo, Años, Trimestres, Meses). Las tendencias a lo largo del tiempo se hacen visibles de inmediato y cada nivel de periodo se convierte en su propio campo dinámico en el área de fila o columna de la tabla dinámica.
- La agrupación solo está disponible para campos colocados en el área FILA o COLUMNA de una tabla dinámica. Un campo de datos (valor) no se puede agrupar directamente. Para agrupar dicho campo, primero debe agregarlo al área de fila o columna de la tabla dinámica.

## **Agrupar campos dinámicos automáticamente**
La sobrecarga sin parámetros `PivotField.group()` examina el tipo de datos del campo y lo agrupa automáticamente. Un campo que contiene únicamente fechas (y valores en blanco) se agrupa por meses. Un campo que contiene únicamente números (y valores en blanco) se agrupa en rangos numéricos mediante un intervalo automático.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Automatically</title>
    </head>
    <body>
        <h1>Auto-Group a Pivot Field</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the second worksheet and its pivot table
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the first row field automatically by its data type
                pt.rowFields.get(0).group();
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputAutoGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Agrupar campos dinámicos con opciones personalizadas**
La clase `PivotFieldGroupOptions` proporciona una configuración de agrupación personalizada. Para los campos de fecha, establezca `startDate`, `endDate` y `groupTypes`. Para los campos numéricos, establezca `startNumber`, `endNumber` e `interval`. La propiedad `newPivotField` controla si la agrupación crea nuevos campos dinámicos junto con el original (consulte la sección Nota al final de este artículo).

### **Agrupar un campo de fecha por meses y trimestres**
El siguiente ejemplo agrupa por meses y trimestres el campo de fila de tipo fecha de la tabla dinámica de ejemplo, entre una fecha de inicio y una fecha de finalización. El código carga el [archivo Excel de ejemplo](sampleGroupPivotFieldsInPivotTable.xlsx), realiza la agrupación, calcula los datos de la tabla dinámica y guarda el resultado agrupado. La captura de pantalla muestra el efecto: el campo de fila de tipo fecha ahora está agrupado por trimestres y meses.
Tenga en cuenta que el orden de los valores de `options.groupTypes` se omite. Independientemente del orden en que se indiquen los tipos de agrupación, los campos agrupados siempre se muestran desde el periodo más amplio al más pequeño: años, trimestres, meses, días, horas, minutos y segundos. En este ejemplo, los meses aparecen antes que los trimestres en `options.groupTypes`; sin embargo, los trimestres se muestran como el nivel exterior y los meses como el nivel interior.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Date Field by Months and Quarters</title>
    </head>
    <body>
        <h1>Group a Date Pivot Field</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the date row field by months and quarters between the given dates
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startDate = new Date(2008, 1, 1);
                options.endDate = new Date(2008, 9, 5);
                options.groupTypes = [AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters];
                pt.rowFields.get(0).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputGroupPivotFieldsInPivotTable.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

![Tabla dinámica agrupada por meses y trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Agrupar un campo numérico en rangos**
`FieldTwo` de la tabla dinámica de ejemplo es inicialmente un campo de datos (valor). Como solo se pueden agrupar campos de fila o columna, el código primero llama a `PivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` para mover `FieldTwo` al área de fila, actualiza la tabla dinámica y, a continuación, agrupa el campo numérico en los rangos 0-1, 2-3 y 4-5 mediante `startNumber = 0`, `endNumber = 5` e `interval = 2`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Numeric Field into Ranges</title>
    </head>
    <body>
        <h1>Group a Numeric Pivot Field</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // FieldTwo is a data field: move it to the row area first,
                // because only row/column fields can be grouped
                pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
                pt.calculateData();
                // Group the numeric field into the ranges 0-1, 2-3, 4-5
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startNumber = 0;
                options.endNumber = 5;
                options.interval = 2;
                pt.rowFields.get(1).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputNumberGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Nota**

{{% alert color="primary" %}}
- Las sobrecargas del método `PivotField.groupBy()` están en desuso y se han eliminado de la superficie de la API. `PivotField.group()` y `PivotField.group(PivotFieldGroupOptions)` son sus sustitutos.
- En Microsoft Excel, al agrupar un campo numérico, el campo dinámico original se SUSTITUYE por los rangos agrupados, mientras que al agrupar un campo de fecha se crean NUEVOS campos dinámicos (uno por cada nivel de agrupación, por ejemplo, Trimestres y Meses) junto al campo original. A partir de Aspose.Cells 26.10, los métodos `PivotField.group()` siguen el mismo comportamiento que Excel. La propiedad `PivotFieldGroupOptions.newPivotField` existe por compatibilidad con versiones anteriores: su valor predeterminado es false para la agrupación numérica y true para la agrupación de fecha y hora; established en false si desea que la agrupación de fechas sustituya el campo dinámico original en lugar de crear nuevos campos dinámicos.
- La propiedad `PivotFieldGroupOptions.interval` solo surte efecto para la agrupación numérica y para la agrupación de fechas por días (por ejemplo, al agrupar fechas en periodos de 7 días); se omite cuando las fechas se agrupan por meses, trimestres o años.
{{% /alert %}}

## **Artículos relacionados**
- [Agregar campos de fila y columna en la Tabla Dinámica](/cells/es/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Filtrar Tablas Dinámicas por etiqueta o valor](/cells/es/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Agregar un campo de página en la Tabla Dinámica](/cells/es/javascript-cpp/add-page-field-in-pivot-table/)
- [Aplicar estilo a la Tabla Dinámica](/cells/es/javascript-cpp/apply-style-to-pivot-table/)
- [Actualizar la Tabla Dinámica](/cells/es/javascript-cpp/refresh-pivot-table/)
- [Agrupación discreta de elementos de campos de tablas dinámicas](/cells/es/javascript-cpp/discrete-group-pivot-fields/)

{{< app/cells/assistant language="javascript-cpp" >}}