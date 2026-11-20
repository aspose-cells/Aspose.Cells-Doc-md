---
title: Agrupación discreta de elementos de campos de tablas dinámicas
linktitle: Agrupación discreta
description: Aprenda a agrupar elementos de campos de tablas dinámicas en grupos personalizados con nombres, como frutas y verduras, mediante DiscreteGroupItem y PivotFieldGroupOptions.discreteGroupItems en Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, tabla dinámica, agrupación discreta, DiscreteGroupItem, PivotFieldGroupOptions, agrupar elementos de campos de tablas dinámicas, grupos personalizados, PivotField.group, Aspose.Cells for JavaScript via C++, tabla dinámica de Excel
type: docs
weight: 90
url: /es/javascript-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
- La agrupación automática reúne elementos según el tipo de datos, como las fechas por meses y trimestres o los números por rangos. La agrupación discreta resuelve el problema opuesto: reúne elementos específicos y no relacionados en grupos personalizados con nombres, por ejemplo, productos en grupos de frutas y verduras, tiendas en regiones o cuentas en zonas. Aspose.Cells proporciona la agrupación discreta mediante la clase `DiscreteGroupItem` y la propiedad `PivotFieldGroupOptions.discreteGroupItems`.
- Un `DiscreteGroupItem` contiene un nombre de grupo y los elementos que pertenecen a él. Los elementos pueden identificarse de dos maneras: por sus nombres (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) o por sus posiciones en los datos de origen, con índices que comienzan en cero (`new DiscreteGroupItem("fruit", [0, 3])`). Ambas formas producen el mismo resultado.
- La agrupación discreta se aplica a un campo del área de filas o columnas de la tabla dinámica al pasar las opciones a `PivotField.group(PivotFieldGroupOptions)`.

## **Agrupar elementos de campos de tablas dinámicas según sus nombres**
El siguiente ejemplo crea una pequeña lista de ventas (producto, fecha e importe), genera una tabla dinámica a partir de ella con `product` en el área de filas, `date` en el área de columnas y `amount` en el área de datos, y después define dos grupos personalizados según los nombres de sus elementos: frutas (uva, cereza) y verduras (zanahoria, patata). El resultado muestra una estructura de filas de dos niveles, con el nombre del grupo en el nivel exterior y los elementos originales anidados debajo, lo que permite analizar las tendencias por grupo personalizado y por elemento.

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            const { Workbook, DiscreteGroupItem, PivotFieldGroupOptions } = AsposeCells;
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType =
                    AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // Group specific items into custom groups by item names
                const fruit = new DiscreteGroupItem("fruit", ["grape", "cherry"]);
                const vegetable = new DiscreteGroupItem("vegetable", ["carrot", "potato"]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

Después de `calculateData()`, el área de filas de la tabla dinámica muestra frutas (uva 50, cereza 80) y verduras (zanahoria 60, patata 70), con un total general de 260, mientras que las etiquetas de las columnas conservan las cuatro fechas (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Agrupar elementos de campos de tablas dinámicas según sus índices**
Cuando los nombres de los elementos son largos o están traducidos, el segundo constructor de `DiscreteGroupItem` los identifica por índice. Los índices son las posiciones de los elementos en los datos de origen, numeradas desde cero y en el orden en que aparecen, no en orden alfabético. En los datos de ejemplo anteriores, la uva es el elemento 0, la zanahoria es el elemento 1, la patata es el elemento 2 y la cereza es el elemento 3; por lo tanto, el grupo de frutas es `{ 0, 3 }` y el de verduras es `{ 1, 2 }`. El resultado es idéntico al del ejemplo basado en nombres.

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            const {
                Workbook,
                SaveFormat,
                DiscreteGroupItem,
                PivotFieldGroupOptions
            } = AsposeCells;
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
                // (zero-based positions in the order the items appear in the source data)
                const fruit = new DiscreteGroupItem("fruit", [0, 3]);
                const vegetable = new DiscreteGroupItem("vegetable", [1, 2]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotFieldByIndex.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

## **Nota**

{{% alert color="primary" %}}
- Los elementos que no se asignan a ningún grupo personalizado no se pierden. Se mantienen en la tabla dinámica en el mismo nivel que los grupos personalizados, cada uno en una entrada individual. En el ejemplo anterior, al definir solo el grupo de frutas, la zanahoria y la patata permanecen en el área de filas como entradas independientes junto al grupo de frutas.
- La propiedad `PivotFieldGroupOptions.newPivotField` controla la estructura de la agrupación discreta. De forma predeterminada, es `true`, lo que añade el campo agrupado como un nuevo campo exterior junto al original y produce la estructura de dos niveles mostrada anteriormente (`rowFields` pasa a contener 2 elementos). Si se establece en `false`, el campo agrupado sustituye al original; entonces, el área de filas muestra un único nivel que contiene únicamente los nombres de los grupos con sus valores agregados: frutas 130 (50 + 80) y verduras 130 (60 + 70).
- Los constructores de `DiscreteGroupItem` basados en nombres e índices pueden combinarse dentro de la misma matriz `discreteGroupItems`.
{{% /alert %}}

## **Artículos relacionados**
- [Agrupar campos en la tabla dinámica](/cells/es/javascript-cpp/group-pivot-fields-in-the-pivot-table/)
- [Agregar campos de fila y columna a una tabla dinámica](/cells/es/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Aplicar estilo a la tabla dinámica](/cells/es/javascript-cpp/apply-style-to-pivot-table/)
- [Actualizar la tabla dinámica](/cells/es/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}