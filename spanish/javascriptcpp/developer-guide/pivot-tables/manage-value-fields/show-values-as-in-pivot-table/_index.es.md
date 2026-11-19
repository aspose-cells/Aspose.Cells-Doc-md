---
title: Mostrar valores como en tabla dinámica
linktitle: Mostrar valores como en tabla dinámica
description: Mostrar los valores de los campos de datos de una tabla dinámica como porcentaje del total, una diferencia respecto a un elemento base, totales acumulados, rangos y más con Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, tabla dinámica, mostrar valores como, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /es/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `Sum` o `Count`. La función **Mostrar valores como** de Excel reemplaza cada resultado mostrado con un cálculo secundario derivado de esa agregación —por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base seleccionado o un rango— para que pueda realizar análisis comparativo sin fórmulas auxiliares ni columnas calculadas.  
Los usos típicos incluyen análisis de participación del total, con porcentajes de una fila, columna o total general; informes acumulativos mediante un total acumulado en un campo de período; análisis de variación frente a un elemento de referencia usando diferencia o diferencia porcentual respecto a un elemento base; y clasificación de valores de menor a mayor o de mayor a menor.
En Aspose.Cells for JavaScript via C++, la enumeración `PivotShowValuesAsType` selecciona el cálculo secundario. La propiedad de solo lectura `PivotField.showValuesSetting` devuelve un objeto `PivotShowValuesSetting`, cuyas propiedades editables `showValuesAs`, `baseFieldIndex` y `baseItemIndex` configuran el comportamiento; el método de conveniencia `PivotField.showValuesAs(...)` aplica la misma configuración en una única llamada. Aplique estas configuraciones a un campo de datos o de valores obtenido de `PivotTable.dataFields`.

## **Miembros de la enumeración PivotShowValuesAsType**
El campo de datos conserva su función de agregación, como Sum o Count, mientras que Mostrar valores como transforma solo la forma en que se muestra el valor agregado.  
Además de escribir directamente las propiedades de `PivotShowValuesSetting` (ver la última sección), un método de conveniencia de una sola llamada aplica la misma configuración. Se presenta en dos formas: una que dirige el campo base y el elemento base por índice, y otra por nombre:

```html
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| Parámetro | Significado | Cuándo es requerido |
| --- | --- | --- |
| `showValuesAsType` | El cálculo secundario `PivotShowValuesAsType` a aplicar. | Siempre. |
| `baseField` | Índice basado en cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base), o —en la forma por nombre— el nombre del campo base. | Los ocho formatos relativos al base a continuación (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); pase `0` (o `null` en la forma por nombre) para cualquier otro formato. |
| `baseItem` | Índice basado en cero del elemento base, con dos sentinelas: -1 selecciona el elemento anterior y -2 el siguiente (la unión JavaScript via C++ no exporta las constantes nombradas —pase los valores literales). La forma por nombre toma la leyenda del elemento base, y `null` cuando el formato seleccionado no necesita elemento base. | Solo los tres formatos de elemento base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) evalúan el elemento base; los cinco formatos relativos al campo (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, ambos rangos) lo ignoran —pase `0` o `null`. |

| Tipo de cálculo | Comportamiento | Parámetros del elemento base |
| --- | --- | --- |
| `Normal` | No hay cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DifferenceFrom` | Muestra el valor como diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o leyenda, o el sentinela anterior/siguiente) |
| `PercentageOf` | Muestra el valor como porcentaje del valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o leyenda, o el sentinela anterior/siguiente) |
| `PercentageDifferenceFrom` | Muestra el valor como la diferencia porcentual respecto al valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o leyenda, o el sentinela anterior/siguiente) |
| `RunningTotalIn` | Muestra el valor como un total acumulado para los elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos impulsa la acumulación) |
| `PercentageOfRow` | Muestra el valor como porcentaje del total de la fila. | — |
| `PercentageOfColumn` | Muestra el valor como porcentaje del total de la columna. | — |
| `PercentageOfTotal` | Muestra el valor como porcentaje del total general. | — |
| `Index` | Muestra el valor usando la fórmula de índice de Excel ((valor * total general) / (total de fila * total de columna)). | — |
| `PercentageOfParentRowTotal` | Muestra el valor como porcentaje del total de su fila padre (para campos de fila anidados). | — |
| `PercentageOfParentColumnTotal` | Muestra el valor como porcentaje del total de su columna padre (para campos de columna anidados). | — |
| `PercentageOfParentTotal` | Muestra el valor como porcentaje de su total padre. | `baseField` (el campo padre cuyo total es la referencia) |
| `PercentageOfRunningTotalIn` | Muestra el valor como porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RankSmallestToLargest` | Clasifica el valor de menor (1) a mayor. | `baseField` (el campo cuyos elementos definen el alcance de la clasificación) |
| `RankLargestToSmallest` | Clasifica el valor de mayor (1) a menor. | `baseField` (el campo cuyos elementos definen el alcance de la clasificación) |

{{% alert color="primary" %}}
`showValuesAs(...)` escribe las propiedades del objeto `PivotShowValuesSetting` (`showValuesAs`, `baseFieldIndex` y `baseItemIndex`) —el método y el objeto de propiedad son dos formas de configurar el mismo estado, replicando los selectores de campo base y elemento base del cuadro de diálogo Mostrar valores como de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Llame al método `PivotField.showValuesAs` con `PivotShowValuesAsType.PercentageOfTotal` para convertir cada celda de campo de datos, incluido el total general, en su participación del total general. Los números mostrados se interpretan entonces como proporciones del conjunto de resultados completo. Este formato mide cada valor únicamente contra el total general, por lo que no requiere campo base ni elemento base —los argumentos finales (`0`, `0`) son marcadores que el formato ignora, según indica la tabla de parámetros anterior.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {

                // Load or create a workbook with source data
                const workbook = new Workbook();
                const dataSheet = workbook.worksheets.get(0);
                const cells = dataSheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Amount";
                const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
                const amounts = [10, 20, 30, 40, 50, 60];
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = amounts[i];
                }
                // Add a pivot table on a new worksheet
                const pivotSheetIndex = workbook.worksheets.add();
                const pivotSheet = workbook.worksheets.get(pivotSheetIndex);
                const pivotTable = pivotSheet.pivotTables.add("=Sheet1!A1:B7", 2, 2);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                // Show the Amount data field as a percentage of the grand total with the
                // one-call method; PercentageOfTotal takes no base item, so the trailing
                // base arguments (0, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
                pivotTable.calculateData();
                // Body now reads (underlying values are fractions, shown with the
                // percentage format): Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsPercentageOfTotal.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **Obtener y configurar PivotField.showValuesSetting**
Lea la configuración actual mediante `PivotField.showValuesSetting`: la propiedad de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyas propiedades describen el cálculo activo de Mostrar valores como. Para cambiar la configuración, llame al método `PivotField.showValuesAs` —escribe todas las configuraciones en una única llamada, de modo que nunca necesite asignar las propiedades una por una.  
El objeto `PivotShowValuesSetting` expone el estado que escribe `showValuesAs`:
- `showValuesAs` selecciona el cálculo secundario `PivotShowValuesAsType`.
- `baseFieldIndex` especifica el índice basado en cero del campo base dentro de los campos de pivote. Se utiliza en los formatos relativos al campo base.
- `baseItemIndex` especifica el elemento base: un índice basado en cero de un elemento de pivote específico, o uno de los dos valores sentinela — -1 para el elemento anterior, -2 para el siguiente (la unión no exporta las constantes nombradas). Se utiliza en los formatos relativos al elemento base.
- `baseFieldName` y `baseItemCaption` son vistas de solo lectura que informan el nombre del campo base resuelto y la leyenda del elemento base; por ejemplo, después de seleccionar el sentinela de elemento anterior, `baseItemCaption` devuelve `(previous)`.
Después de llamar a `showValuesAs`, invoque `PivotTable.calculateData()` nuevamente para que el cuerpo de la tabla dinámica se recalcule y se renderice con la configuración actualizada.

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
        const ready = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await ready;
                const file = document.getElementById('fileInput').files[0];
                if (!file) {
                    throw new Error("Please select ShowValuesAsPercentageOfTotal.xlsx.");
                }
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(1);
                const pivotTable = worksheet.pivotTables.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Read the current show-values settings
                const settings = dataField.showValuesSetting;
                const messages = [
                    `ShowValuesAs: ${settings.showValuesAs}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`,
                    `BaseFieldName: ${settings.baseFieldName}`,
                    `BaseItemCaption: ${settings.baseItemCaption}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                // (-1 is the previous-item sentinel; the binding does not export the constant)
                dataField.showValuesAs(
                    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    -1
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`ShowValuesAs now: ${dataField.showValuesSetting.showValuesAs}`);
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsDifferenceFrom.xlsx";
                downloadLink.style.display = "block";
            } catch (error) {
                document.getElementById('result').innerHTML =
                    `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **Artículos relacionados**
- [Administrar campos de valor en tabla dinámica](/cells/es/javascript-cpp/manage-value-fields/)
- [Actualizar tabla dinámica](/cells/es/javascript-cpp/refresh-pivot-table/)
- [Aplicar estilo a tabla dinámica](/cells/es/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}