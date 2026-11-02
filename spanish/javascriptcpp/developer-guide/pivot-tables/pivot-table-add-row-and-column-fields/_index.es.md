---
title: Agregar campos de fila y columna de una Tabla Dinámica en Aspose.Cells for JavaScript via C++
description: Aprenda cómo agregar campos de fila y columna a una Tabla Dinámica y controlar los subtotales de los campos de la Tabla Dinámica mediante PivotField.SetSubtotals con PivotFieldSubtotalType en Aspose.Cells for JavaScript via C++.
linktitle: Campos de fila y columna
keywords: Aspose.Cells, JavaScript via C++, Tabla Dinámica, campo de fila, campo de columna, PivotField, setSubtotals, PivotFieldSubtotalType, subtotales, JavaScript, Tabla Dinámica de Excel
type: docs
weight: 220
url: /es/javascript-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Agregar un campo a la región de filas o columnas**
El método `pivotTable.addFieldToArea(fieldType, fieldName)` mueve un campo base de los datos de origen a una de las cuatro regiones de la Tabla Dinámica. El argumento `fieldType` acepta uno de los siguientes valores de `PivotFieldType`.
- `Row` — campos colocados verticalmente a la izquierda
- `Column` — campos colocados horizontalmente en la parte superior
- `Data` — campos cuyos valores se agregan
- `Page` — campos utilizados como filtros del informe
El orden de anidamiento de los campos es importante. Al agregar `Category` a la región de filas y después `Item`, se obtiene una Tabla Dinámica cuyo agrupamiento exterior es `Category` y cuyo agrupamiento interior es `Item`. Invertir el orden invierte la jerarquía.

## **Subtotales de los campos de la Tabla Dinámica**
El método `pivotField.setSubtotals(subtotalType, shown)` controla qué filas de subtotal aparecen para un campo de la Tabla Dinámica. Cada llamada activa o desactiva de forma independiente un único tipo de subtotal. Al pasar `shown = true`, se muestra el subtotal, mientras que `shown = false` lo oculta. Como cada llamada solo afecta a un tipo, invocar el método varias veces con distintos valores de `subtotalType` crea un subconjunto personalizado de subtotales.
La enumeración `PivotFieldSubtotalType` define los tipos de subtotal disponibles.
- `Automatic` — Aspose.Cells selecciona la opción predeterminada (normalmente `Sum` para los campos numéricos)
- `None` — suprime todas las filas de subtotal
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Los subtotales solo se generan cuando hay dos o más campos de la Tabla Dinámica en la región de filas (o en la región de columnas). Un único campo no ofrece ningún grupo entre el que calcular subtotales, por lo que las llamadas a `setSubtotals` no producen ningún efecto visible en ese caso. Por eso, este artículo coloca dos campos de fila (`Category` exterior, `Item` interior) en todos los ejemplos, de modo que sea visible el límite de los subtotales entre cada grupo `Category`.
{{% /alert %}}

## **Escenario 1 — Subtotales automáticos (predeterminados)**
Cuando no se invoca `setSubtotals` en absoluto, Aspose.Cells aplica la opción `Automatic` a los campos numéricos. El siguiente ejemplo confirma explícitamente este comportamiento invocando `setSubtotals(PivotFieldSubtotalType.Automatic, true)` en el campo de fila exterior `Category`.

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
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get(0, 0).value = "Category";
            cells.get(0, 1).value = "Item";
            cells.get(0, 2).value = "Year";
            cells.get(0, 3).value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTableIndex = worksheet.pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
            pivotTable.calculateData();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_automatic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Escenario 2 — Suprimir todos los subtotales (None)**
Invocar `setSubtotals(PivotFieldSubtotalType.None, true)` elimina todas las filas de subtotal de la Tabla Dinámica y deja únicamente las filas de los campos y el total general en la parte inferior. Esto resulta útil cuando se necesitan los datos agrupados sin filas de resumen.

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
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const headers = ["Category", "Item", "Year", "Amount"];
            for (let j = 0; j < headers.length; j++) {
                worksheet.cells.get(0, j).value = headers[j];
            }
            const data = [
                ["Fruit", "Apple", 2020, 100],
                ["Fruit", "Apple", 2021, 150],
                ["Fruit", "Banana", 2020, 80],
                ["Fruit", "Banana", 2021, 90],
                ["Vegetable", "Carrot", 2020, 50],
                ["Vegetable", "Carrot", 2021, 60],
                ["Vegetable", "Daikon", 2020, 40],
                ["Vegetable", "Daikon", 2021, 45]
            ];
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    worksheet.cells.get(i + 1, j).value = data[i][j];
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_none.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Escenario 3 — Subconjunto personalizado de subtotales (Sum + Average)**
No está limitado a un único tipo de subtotal. Cada llamada a `setSubtotals` opera de forma independiente sobre un tipo, por lo que invocar el método dos veces —una con `Sum` y otra con `Average`— produce un subconjunto personalizado de dos filas de subtotal para cada grupo `Category`.

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
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get("A1").value = "Category";
            cells.get("B1").value = "Item";
            cells.get("C1").value = "Year";
            cells.get("D1").value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTables = worksheet.pivotTables;
            const i = pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = pivotTables.get(i);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_custom.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Resumen**
Los tres escenarios difieren únicamente en un aspecto: las llamadas a `setSubtotals`. Todo lo demás —el conjunto de datos, los campos y las áreas en las que se asignan— es idéntico, lo que permite comparar directamente los diseños.
- **Colocación de campos.** `pivotTable.addFieldToArea(PivotFieldType.Row, fieldName)` mueve una columna de origen a una región. Dentro de una región, el orden de las llamadas es el orden de visualización, por lo que la primera llamada se convierte en el grupo más externo. Los subtotales requieren dos o más campos en la misma región: con un solo campo no hay ningún grupo intermedio sobre el que calcularlos.
- **Escenario 1 — subtotales automáticos.** No invocar `setSubtotals` deja la elección en manos de Excel, que aplica su propio subtotal predeterminado a los campos numéricos. Invocar `setSubtotals` con `PivotFieldSubtotalType.Automatic` registra esa elección explícitamente en lugar de dejarla implícita.
- **Escenario 2 — sin subtotales.** Invocar `setSubtotals` con `PivotFieldSubtotalType.None` desactiva el subtotal predeterminado, de modo que la Tabla Dinámica conserva las filas de los campos y el total general, pero elimina las filas de subtotal que Excel insertaría de otro modo entre ellas.
- **Escenario 3 — un subconjunto seleccionado.** Cada llamada activa o desactiva exactamente un tipo de subtotal, y las llamadas se acumulan en lugar de restablecerse entre sí. Por lo tanto, invocarla una vez con `PivotFieldSubtotalType.Sum` y otra con `PivotFieldSubtotalType.Average` deja ambos subtotales habilitados, y la Tabla Dinámica muestra un subtotal `Sum`, un subtotal `Average` y un total general.

{{% alert color="primary" %}}
Nada relativo a los subtotales es específico de la región de filas. Las mismas llamadas a `setSubtotals` aplicadas a un campo obtenido de `pivotTable.getColumnFields()` producen los mismos tres diseños en el eje de columnas, ya que la configuración pertenece al campo de la Tabla Dinámica y no al eje en el que se encuentra.
{{% /alert %}}

## **Artículos relacionados**
- [Campos de página en Tablas Dinámicas](/cells/es/javascript-cpp/add-page-field-in-pivot-table/)
- [Actualizar Tablas Dinámicas en Aspose.Cells for JavaScript via C++](/cells/es/javascript-cpp/refresh-pivot-table/)
- [Aplicar estilos a Tablas Dinámicas](/cells/es/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}