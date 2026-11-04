---
title: Formatear parte de una tabla dinámica
description: Formatear parte de una tabla dinámica en Aspose.Cells for JavaScript via C++ aplicando estilos a regiones semánticas PivotArea o rectángulos CellArea mediante PivotTable.Format, con los formatos almacenados en PivotTable.PivotFormats y preservados cuando se actualiza la tabla dinámica.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for JavaScript via C++, tabla dinámica, formato, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /es/javascript-cpp/format-part-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
`PivotTable.FormatAll` aplica un solo estilo a toda la tabla dinámica y se cubre en la página principal. No distingue entre etiquetas, valores, totales o regiones particulares del informe.  
En la práctica, solo una parte de una tabla dinámica suele necesitar resaltarse. Los objetivos comunes incluyen las etiquetas pertenecientes a un campo de fila, las celdas de valor producidas por un campo, la fila de total general o un rectángulo arbitrario como las dos primeras filas de ítems.  
Aplicar un estilo directamente a las celdas de la hoja de cálculo de una tabla dinámica no es equivalente. Excel almacena el formato de la tabla dinámica como regiones semánticas `PivotArea` en lugar de registros ordinarios de estilo de celda. Un formato de área de pivote permanece vinculado a una región como las etiquetas de un campo o los valores de datos, y se vuelve a resolver cuando la tabla dinámica se recalcula, actualiza o expande. Un estilo escrito directamente en una celda, por otro lado, pertenece a esa posición de celda y no es rastreado por el modelo de pivote.  
Aspose.Cells expone toda la familia de sobrecargas `PivotTable.Format` para que ambos tipos de formato estén disponibles:
- `Format(PivotArea, Style)` ancla un estilo a una región semántica que se construye con `PivotArea.Select` o `PivotArea.SelectField`.
- `Format(CellArea, Style)` ancla un estilo a un rectángulo de hoja de cálculo dentro de la tabla dinámica.
- `Format(int row, int column, Style)` apunta a una sola celda.
- `FormatAll(Style)` formatea toda la tabla dinámica.

## **Formatear un Área de Pivote**
El flujo de trabajo de área semántica es el enfoque recomendado cuando un resaltado debe seguir a un campo o a una región del informe.
1. Cree un `PivotArea` con `new PivotArea(pivotTable)`. El objeto describe una región semántica que pertenece a esa tabla dinámica específica.
1. Seleccione un campo por su posición basada en cero en un eje dado con `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` selecciona tanto las etiquetas como los datos del campo.
   - `PivotTableSelectionType.LabelOnly` selecciona solo las etiquetas del campo.
   - `PivotTableSelectionType.DataOnly` selecciona solo las celdas de datos del campo.
1. Seleccione un campo por nombre con `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. Cuando se selecciona un campo de fila por nombre, la región se resuelve a las celdas de valor producidas por los ítems de ese campo.
1. Cree un `Style` con `Workbook.CreateStyle()`, configure su fuente, color de primer plano y patrón de fondo sólido, y pase el estilo a `PivotTable.Format(area, style)`.
1. Cada llamada a la sobrecarga `PivotArea` agrega una entrada `PivotTableFormat` a `PivotTable.PivotFormats`.
1. Los formatos anclados a campos se pintan cuando se calculan los datos del pivote. Por lo tanto, llame a `PivotTable.CalculateData()` después de aplicar los formatos para que los estilos se vuelvan visibles.  
El siguiente ejemplo construye una pequeña tabla dinámica de ventas de frutas, aplica estilo a las etiquetas de fila `Fruit` con `PivotArea.Select` y `PivotTableSelectionType.LabelOnly`, aplica estilo a las celdas de valor producidas por ese mismo campo de fila con `PivotArea.SelectField`, y luego recalcula la tabla dinámica para que ambos estilos se pinten.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Fruit sales data
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            // Pivot table with its top-left corner at E3 (row 2, column 4)
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Bold yellow fill on the row field's label cells
            const labelStyle = workbook.createStyle();
            labelStyle.font.isBold = true;
            labelStyle.foregroundColor = AsposeCells.Color.Yellow;
            labelStyle.pattern = AsposeCells.BackgroundType.Solid;
            const labelArea = new AsposeCells.PivotArea(pivotTable);
            labelArea.select(
                AsposeCells.PivotFieldType.Row,
                0,
                AsposeCells.PivotTableSelectionType.LabelOnly
            );
            pivotTable.format(labelArea, labelStyle);
            // Light green fill on the value cells the row field produces
            const valueStyle = workbook.createStyle();
            valueStyle.foregroundColor = AsposeCells.Color.LightGreen;
            valueStyle.pattern = AsposeCells.BackgroundType.Solid;
            const valueArea = new AsposeCells.PivotArea(pivotTable);
            valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.format(valueArea, valueStyle);
            // Field-anchored formats are painted when the data is calculated
            pivotTable.calculateData();
            // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Formatear un Cell Area de la tabla dinámica**
Utilice `PivotTable.Format(CellArea, Style)` cuando la región de interés sea un rectángulo simple de hoja de cálculo y no una región semántica de pivote.  
Un `CellArea` se describe mediante los campos `startRow`, `startColumn`, `endRow` y `endColumn`. Los valores son coordenadas de hoja basadas en cero, y las coordenadas finales identifican la última fila y columna incluidas en el rectángulo, de modo que el área cubre las celdas desde la posición inicial hasta la posición final inclusive.  
A diferencia de un formato anclado a un campo, un formato `CellArea` se aplica a las celdas inmediatamente. No se necesita otra llamada a `CalculateData()` para que el estilo aparezca.  
Un rectángulo `CellArea` puede contener celdas de etiqueta y celdas de valor juntas. La siguiente sección describe cómo Aspose.Cells y Excel representan internamente ese rectángulo.  
El siguiente ejemplo formatea el rectángulo `E4:F5` de la tabla dinámica con un estilo cursiva, azul claro y guarda el libro sin necesidad de recalcular nuevamente.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Highlight the first two fruit rows (the rectangle E4:F5)
            const highlightStyle = workbook.createStyle();
            highlightStyle.font.isItalic = true;
            highlightStyle.foregroundColor = AsposeCells.Color.LightBlue;
            highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
            const rectangle = new AsposeCells.CellArea();
            rectangle.startRow = 3;
            rectangle.startColumn = 4;
            rectangle.endRow = 4;
            rectangle.endColumn = 5;
            pivotTable.format(rectangle, highlightStyle);
            // E4:F5 is italic on light blue immediately, no recalculation needed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotCellArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Cómo se asignan las áreas Pivot y Cell**
Excel almacena el formato de la tabla dinámica como registros `pivotArea` en lugar de registros ordinarios de estilo de celda de hoja de cálculo. El mismo modelo es utilizado por Aspose.Cells, de modo que una solicitud de formato se traduce en áreas de pivote cuando se registra.  
La relación entre el `CellArea` proporcionado por el usuario y las áreas de pivote almacenadas internamente es de muchos a muchos en ambas direcciones.
- Un `CellArea` puede producir varias áreas de pivote. Si el rectángulo abarca tanto celdas de etiqueta como celdas de valor, se descompone en reglas separadas de etiqueta y datos, porque el modelo de pivote trata el formato de etiquetas y el de datos de forma independiente.
- Un área de pivote puede resolverse en varias instancias `CellArea` disjuntas. Una región semántica como una fila de total general, o un campo cuyos ítems no son contiguos, puede cubrir múltiples rectángulos. Por eso `PivotArea.GetCellAreas()` devuelve una colección en lugar de un solo rectángulo.
Cada operación de formato realizada a través de `PivotTable.Format` se registra en `PivotTable.PivotFormats`. Cada entrada `PivotTableFormat` expone el `PivotArea` asociado y el `Style` que se le aplicó. La sobrecarga `PivotArea` agrega exactamente una entrada por llamada, mientras que un `CellArea` que contiene diferentes regiones semánticas puede añadir varias entradas.  
Para distinguir las regiones almacenadas, cada `PivotArea` expone los indicadores `OnlyLabel` y `OnlyData`. El ejemplo a continuación formatea un solo rectángulo que cubre tanto etiquetas como valores, inspecciona `PivotTable.PivotFormats` y muestra las coordenadas `CellArea` a las que cada área de pivote almacenada se resuelve.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat, CellArea, Color } = AsposeCells;
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                const result = document.getElementById("result");
                const downloadLink = document.getElementById("downloadLink");
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
                const years = [2024, 2024, 2025, 2025, 2024, 2025];
                const amounts = [100, 150, 120, 180, 90, 110];
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = years[i];
                    cells.get(i + 1, 2).value = amounts[i];
                }
                const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                const highlightStyle = workbook.createStyle();
                highlightStyle.font.isItalic = true;
                highlightStyle.foregroundColor = Color.LightBlue;
                highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
                // ONE rectangle in...
                const rectangle = new CellArea();
                rectangle.startRow = 3;
                rectangle.startColumn = 4;
                rectangle.endRow = 4;
                rectangle.endColumn = 5;
                // ...TWO semantic pivot areas out: the label part and the data part are stored separately
                pivotTable.format(rectangle, highlightStyle);
                const pivotFormats = pivotTable.pivotFormats;
                const outputLines = [`Stored formats: ${pivotFormats.count}`];
                for (let i = 0; i < pivotFormats.count; i++) {
                    const pivotFormat = pivotFormats.get(i);
                    const storedArea = pivotFormat.pivotArea;
                    const onlyLabel = storedArea.onlyLabel ? "True" : "False";
                    const onlyData = storedArea.onlyData ? "True" : "False";
                    outputLines.push(`Format ${i}: OnlyLabel=${onlyLabel}, OnlyData=${onlyData}`);
                    const resolvedAreas = storedArea.cellAreas;
                    for (let j = 0; j < resolvedAreas.count; j++) {
                        const resolved = resolvedAreas.get(j);
                        outputLines.push(
                            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
                        );
                    }
                }
                // This prints:
                // Stored formats: 2
                // Format 0: OnlyLabel=True, OnlyData=False
                //     rows 4-5, columns 5-5        (E4:E5, the label part)
                // Format 1: OnlyLabel=False, OnlyData=True
                //     rows 4-5, columns 6-6        (F4:F5, the data part)
                result.innerHTML =
                    `<pre>${outputLines.join("\n")}</pre>` +
                    `<p style="color: green;">Done! Click the download link to get the result file.</p>`;
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "FormatPivotAreasMap.xlsx";
                downloadLink.style.display = "block";
            });
        </script>
    </body>
</html>
```

{{% alert color="primary" %}}
Debido a que los formatos se almacenan como áreas de pivote en lugar de como estilos de celda ordinarios, sobreviven a la recalculación y actualización. Cuando la tabla dinámica se actualiza con `PivotTable.RefreshData`, se recalcula con `CalculateData`, o se guarda y vuelve a cargar, cada área de pivote almacenada se vuelve a resolver a la posición actual de su región y su estilo se vuelve a aplicar.
{{% /alert %}}

Utilice un `PivotArea` construido con `Select` o `SelectField` cuando un resaltado deba permanecer adjunto a un campo o a una región semántica a través de actualizaciones, y use un `CellArea` cuando sea suficiente formatear un rectángulo fijo en el diseño actual de la tabla dinámica. La sobrecarga de una sola celda `Format(int row, int column, Style)` apunta a una celda individual. Use `FormatAll`, cubierto en la página principal, cuando toda la tabla dinámica deba volver a estilizarse de una vez.

## **Artículos relacionados**
- [Aplicar estilo a la tabla dinámica](/cells/es/javascript-cpp/apply-style-to-pivot-table/)
- [Agregar campos de fila y columna a la tabla dinámica](/cells/es/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Administrar campos de valor en la tabla dinámica](/cells/es/javascript-cpp/manage-value-fields/)
- [Actualizar la tabla dinámica](/cells/es/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}