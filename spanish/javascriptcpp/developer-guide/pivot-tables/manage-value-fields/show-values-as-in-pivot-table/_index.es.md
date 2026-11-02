---
title: Mostrar valores como en tabla dinámica
description: Muestre los valores de los campos de datos de la tabla dinámica como un porcentaje del total, una diferencia respecto a un elemento base, totales acumulados, rangos y más con Aspose.Cells for JavaScript via C++.
linktitle: Mostrar valores como
keywords: Aspose.Cells, JavaScript via C++, tabla dinámica, mostrar valores como, formato de visualización de datos, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /es/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `Sum` o `Count`. La característica **Show Values As** de Excel reemplaza cada resultado mostrado con un cálculo secundario derivado de esa agregación —por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base elegido o un rango— para que pueda realizar análisis comparativos sin fórmulas auxiliares ni columnas calculadas.  
Los usos típicos incluyen análisis de participación del total, con porcentajes de fila, columna o total general; informes acumulativos usando un total acumulado en un campo de período; análisis de variación contra un elemento de referencia mediante diferencia o diferencia porcentual de un elemento base; y clasificación de valores de menor a mayor o de mayor a menor.  
En Aspose.Cells for JavaScript via C++, `PivotFieldDataDisplayFormat` selecciona el cálculo secundario. La propiedad de solo lectura `PivotField.showValuesSetting` devuelve un objeto `PivotShowValuesSetting`, cuyas propiedades editables `calculationType`, `baseFieldIndex`, `baseItemPositionType` y `baseItemIndex` configuran el comportamiento; el método de conveniencia `PivotField.showValuesAs(...)` aplica los mismos cuatro ajustes en una sola llamada. Aplique estas configuraciones a un campo de datos o de valores obtenido de `PivotTable.dataFields`.

## **Miembros de enumeración PivotFieldDataDisplayFormat**
El campo de datos mantiene su función de agregación, como Sum o Count, mientras que Show Values As solo transforma la forma en que se muestra el valor agregado.  
Además de escribir directamente las propiedades de `PivotShowValuesSetting` (ver la última sección), un método de conveniencia de una sola llamada aplica la misma configuración:

```html
dataField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
```

| Parámetro | Significado | Cuándo es necesario |
| --- | --- | --- |
| `displayFormat` | El cálculo secundario `PivotFieldDataDisplayFormat` que se aplicará. | Siempre. |
| `baseField` | Índice basado en cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base). | Solo para los seis formatos relativos a la base que se indican a continuación (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); los demás formatos lo ignoran. |
| `baseItemPositionType` | Cómo se elige el elemento base respecto al elemento actual: `PivotItemPositionType.Previous`, `.Next` o `.Custom`. | Solo para los tres formatos con elemento base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); los demás formatos lo ignoran. |
| `baseItem` | Índice basado en cero del elemento base. | Sólo cuando `baseItemPositionType` es `Custom` (el índice del elemento selecciona el elemento base exacto); ignorado para `Previous` / `Next` y por todos los formatos que no son de base — pase `0`. |

| Tipo de cálculo | Comportamiento | Parámetros del elemento base |
| --- | --- | --- |
| `Normal` | No hay cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DifferenceFrom` | Muestra el valor como una diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageOf` | Muestra el valor como un porcentaje del valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageDifferenceFrom` | Muestra el valor como la diferencia porcentual respecto al valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `RunningTotalIn` | Muestra el valor como un total acumulado para los elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos impulsa la acumulación) |
| `PercentageOfRow` | Muestra el valor como un porcentaje del total de la fila. | — |
| `PercentageOfColumn` | Muestra el valor como un porcentaje del total de la columna. | — |
| `PercentageOfTotal` | Muestra el valor como un porcentaje del total general. | — |
| `Index` | Muestra el valor usando la fórmula de índice de Excel ((valor * total general) / (total de fila * total de columna)). | — |
| `PercentageOfParentRowTotal` | Muestra el valor como un porcentaje del total de la fila padre (para campos de fila anidados). | — |
| `PercentageOfParentColumnTotal` | Muestra el valor como un porcentaje del total de la columna padre (para campos de columna anidados). | — |
| `PercentageOfParentTotal` | Muestra el valor como un porcentaje de su total padre. | `baseField` (el campo principal de referencia) |
| `PercentageOfRunningTotalIn` | Muestra el valor como un porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RankSmallestToLargest` | Clasifica el valor de menor (1) a mayor. | — |
| `RankLargestToSmallest` | Clasifica el valor de mayor (1) a menor. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` escribe las propiedades `PivotShowValuesSetting` (`calculationType`, `baseFieldIndex`, `baseItemPositionType`, `baseItemIndex`); el método y el objeto de propiedades son dos formas de configurar el mismo estado, replicando los selectores de campo base y elemento base del cuadro de diálogo Show Values As de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Llame al método `PivotField.showValuesAs` con `PivotFieldDataDisplayFormat.PercentageOfTotal` para convertir cada celda de campo de datos, incluido el total general, en su participación del total general. Los números mostrados, por lo tanto, se leen como proporciones del conjunto de resultados completo. Este formato mide cada valor únicamente respecto al total general, por lo que no necesita un campo base ni un elemento base — los argumentos finales (`0`, `PivotItemPositionType.Previous`, `0`) son marcadores de posición que el formato ignora, como indica la tabla de parámetros anterior.

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
                // base arguments (0, Previous, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
                    0,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
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
Lea la configuración actual mediante `PivotField.showValuesSetting`: la propiedad de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyas cuatro propiedades describen el cálculo activo de Show Values As. Para cambiar la configuración, llame al método `PivotField.showValuesAs` — escribe las cuatro configuraciones en una sola llamada, de modo que nunca necesite asignar las propiedades una por una.  
El objeto `PivotShowValuesSetting` expone las cuatro propiedades que escribe `showValuesAs`:
- `calculationType` selecciona el cálculo secundario `PivotFieldDataDisplayFormat`.
- `baseFieldIndex` especifica el índice basado en cero del campo base dentro de los campos de la tabla dinámica. Se usa en los formatos relativos a la base.
- `baseItemPositionType` determina cómo se posiciona el elemento base respecto al elemento actual y acepta `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` o `PivotItemPositionType.Custom`.
- `baseItemIndex` especifica el índice basado en cero del elemento base y se usa cuando `baseItemPositionType` es `Custom`.
Después de llamar a `showValuesAs`, invoque nuevamente `PivotTable.calculateData()` para que el cuerpo de la tabla dinámica se recalcule y vuelva a renderizarse con la configuración actualizada.

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
                    `CalculationType: ${settings.calculationType}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemPositionType: ${settings.baseItemPositionType}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`CalculationType now: ${dataField.showValuesSetting.calculationType}`);
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
- [Administrar campos de valores en tabla dinámica](/cells/es/javascript-cpp/manage-value-fields/)
- [Actualizar tabla dinámica](/cells/es/javascript-cpp/refresh-pivot-table/)
- [Aplicar estilo a tabla dinámica](/cells/es/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}