---
title: Aplicar estilos a tablas dinámicas en Aspose.Cells for JavaScript via C++
description: Aprenda a aplicar estilos integrados y personalizados a tablas dinámicas en Aspose.Cells for JavaScript via C++, que abarcan los formatos automáticos heredados de XLS, los estilos modernos con nombre de Excel 2007+, los estilos personalizados de tabla dinámica y el atajo FormatAll.
linktitle: Aplicar estilos a tablas dinámicas
keywords: estilo de tabla dinámica de Aspose.Cells for JavaScript via C++, PivotTableStyleType, AutoFormatType, FormatAll, estilo personalizado, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /es/javascript-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite aplicar tanto los formatos automáticos heredados de tablas dinámicas (destinados a archivos `.xls`) como los estilos modernos con nombre o personalizados de tablas dinámicas (destinados a archivos `.xlsx`, `.xlsm` y `.xlsb`). La API que debe llamar depende del formato en el que se guarda el libro de trabajo, no del formato desde el que se carga.
{{% /alert %}}

## **Introducción**
Aspose.Cells expone dos API de estilos paralelas para tablas dinámicas. La elección entre ellas depende del formato en el que guarde el libro de trabajo, no del formato desde el que lo lea. Un libro de trabajo cargado desde un archivo `.xls` puede guardarse de nuevo como `.xlsx` y, en ese caso, se aplica la API de estilos modernos en lugar de la heredada.
- `pivotTable.pivotTableStyleType` selecciona uno de los estilos integrados con nombre (temas claros y oscuros, incluidos los estilos agregados en Excel 2017). Estos preajustes son de solo lectura.
- `pivotTable.pivotTableStyleName` selecciona un estilo personalizado que usted mismo define mediante `workbook.worksheets.tableStyles.addPivotTableStyle(...)`. Los estilos personalizados son necesarios siempre que necesite modificar colores, bordes o fuentes más allá de lo que ofrecen los preajustes.
Además, `pivotTable.formatAll(style)` es un atajo que aplica un único objeto `style` a todas las celdas de la tabla dinámica, anulando cualquier configuración establecida mediante cualquiera de las API de nombres de estilo anteriores. Esto resulta útil cuando se requiere una apariencia uniforme con independencia del tema subyacente.

## **Aplicar un formato automático preajustado heredado de XLS**
`pivotTable.autoFormatType` acepta un valor de la enumeración `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Los valores disponibles son `Report1` a `Report10`, `Classic` y `Table1` a `Table10`.
El siguiente ejemplo carga un libro de trabajo nuevo, llena los datos de ejemplo Fruit/Year/Amount, agrega una tabla dinámica, aplica `PivotTableAutoFormatType.Report5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}
**¿Por qué no hay campos de columna?** Los formatos automáticos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) se diseñaron en el Excel clásico para **tablas dinámicas de una sola dimensión** con campos de fila y valores únicamente, por lo que no incluyen estilos para los encabezados de los campos de columna. Si su tabla dinámica necesita campos de columna, use en su lugar los preajustes modernos `PivotTableStyleType` del [Escenario 2](#apply-a-modern-named-preset-pivot-table-style), que están diseñados para la distribución bidimensional que utiliza Excel moderno.
{{% /alert %}}

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
            // Escenario 1: Aplicar un autoformato preestablecido de XLS heredado
            // API utilizada: PivotTable.AutoFormatType
            // Formato de archivo de destino: .xls (heredado)
            // Para obtener ejemplos completos y archivos de datos, vaya a https://github.com/aspose-cells/Aspose.Cells-for-.NET
            // Crear un libro de trabajo nuevo
            const workbook = new Workbook();
            // Obtener la primera hoja de cálculo
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Poblar los datos de origen con una fila de encabezado (Fruit, Year, Amount)
            // y 9 filas de datos que abarcan uva, arándano, kiwi y cereza durante 2020 y 2021
            cells.get(0, 0).value = "Fruit";
            cells.get(0, 1).value = "Year";
            cells.get(0, 2).value = "Amount";
            cells.get(1, 0).value = "grape";
            cells.get(1, 1).value = 2020;
            cells.get(1, 2).value = 50;
            cells.get(2, 0).value = "blueberry";
            cells.get(2, 1).value = 2020;
            cells.get(2, 2).value = 30;
            cells.get(3, 0).value = "kiwi";
            cells.get(3, 1).value = 2020;
            cells.get(3, 2).value = 25;
            cells.get(4, 0).value = "cherry";
            cells.get(4, 1).value = 2020;
            cells.get(4, 2).value = 40;
            cells.get(5, 0).value = "grape";
            cells.get(5, 1).value = 2021;
            cells.get(5, 2).value = 60;
            cells.get(6, 0).value = "blueberry";
            cells.get(6, 1).value = 2021;
            cells.get(6, 2).value = 35;
            cells.get(7, 0).value = "kiwi";
            cells.get(7, 1).value = 2021;
            cells.get(7, 2).value = 28;
            cells.get(8, 0).value = "cherry";
            cells.get(8, 1).value = 2021;
            cells.get(8, 2).value = 45;
            cells.get(9, 0).value = "grape";
            cells.get(9, 1).value = 2020;
            cells.get(9, 2).value = 45;
            // Agregar una tabla dinámica en la celda de destino E3, usando el rango de origen A1:C10
            const pivotTable = sheet.pivotTables.add("=A1:C10", 2, 4);
            // Asignar campos: Fruit -> Filas, Amount -> Datos
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Aplicar el autoformato preestablecido "Report5" de XLS heredado
            // Nota: Esta propiedad solo es relevante al guardar como .xls.
            // Al guardar como .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
            // y usa lo que especifiquen PivotTableStyleType / PivotTableStyleName.
            pivotTable.autoFormatType = AsposeCells.PivotTableAutoFormatType.Report5;
            // Guardar el libro de trabajo en el formato heredado .xls
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xls";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Aplicar un estilo preajustado moderno con nombre a una tabla dinámica**
`pivotTable.pivotTableStyleType` selecciona uno de los estilos integrados con nombre que Excel 2007 introdujo para las tablas dinámicas. La enumeración `PivotTableStyleType` expone tres familias de temas: la familia clara, de `PivotTableStyleLight1` a `PivotTableStyleLight28`; la familia media, de `PivotTableStyleMedium1` a `PivotTableStyleMedium28`; y la familia oscura, de `PivotTableStyleDark1` a `PivotTableStyleDark28`. También define `None` y `Custom`. Los miembros con un número mayor de cada familia son los estilos agregados en Excel 2017.
Estos preajustes son de solo lectura. En cuanto necesite cambiar colores, bordes o fuentes más allá de lo que ofrece un preajuste, deberá definir un estilo personalizado de tabla dinámica, como se muestra en el [Escenario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**¿Por qué los preajustes modernos y no los formatos automáticos de la serie Report?** Los valores `Report1` a `Report10` y `Table1` a `Table10` de `PivotTableAutoFormatType` son anteriores a los campos de columna de las tablas dinámicas, por lo que no incluyen estilos para los encabezados de los campos de columna y Excel muestra esos encabezados sin formato. Los preajustes `PivotTableStyleType` se diseñaron para la distribución bidimensional que utiliza Excel moderno y dan formato tanto a los encabezados de los campos de fila como a los de columna.
{{% /alert %}}

Este escenario reutiliza el conjunto de datos Fruit/Year/Amount del Escenario 1, agrega `Year` al área de columnas junto con el campo de fila `Fruit` mediante `PivotFieldType.Column`, aplica el preajuste de tema oscuro `PivotTableStyleDark1` con `pivotTable.pivotTableStyleType` y guarda el resultado como `.xlsx`, el formato para el que `PivotTableStyleType` es aplicable.

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
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Escenario 2: Aplicar un estilo predefinido con nombre moderno de Excel 2007+ mediante PivotTableStyleType.
            // Formato de archivo de destino: .xlsx. La enumeración PivotTableStyleType se encuentra en el espacio de nombres Aspose.Cells
            // (no en Aspose.Cells.Pivot), por lo que no necesitamos ninguna instrucción using adicional.
            // Referencia de GitHub: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Fila de encabezado: Fruit / Year / Amount
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 9 filas de datos de Fruit / Year / Amount
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 150;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 200;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 180;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 120;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 170;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 210;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 190;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 130;
            // Agregar una tabla dinámica en E3, usando A1:C10 como origen
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // Asignar campos de tabla dinámica: Fruit -> área de filas, Year -> área de columnas, Amount -> área de datos
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Aplicar un estilo predefinido con nombre moderno de tabla dinámica de Excel 2007+.
            // PivotTableStyleType es la API correcta para archivos .xlsx / .xlsm / .xlsb; Excel ignora AutoFormatType
            // para esos formatos. PivotTableStyleDark1 pertenece a la familia de temas oscuros
            // (PivotTableStyleDark1..PivotTableStyleDark28), y la misma enumeración también expone los
            // temas más nuevos claros y oscuros de Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
            pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleDark1;
            // Guardar como .xlsx moderno, el formato para el cual PivotTableStyleType es relevante.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
        </script>
    </body>
</html>
```

## **Definir y aplicar un estilo personalizado de tabla dinámica**
Los preajustes integrados no se pueden modificar. Siempre que necesite anular colores, bordes o fuentes, deberá definir un estilo personalizado de tabla dinámica. El flujo de trabajo tiene tres pasos:
1. Agregue un estilo personalizado a la colección `tableStyles` del libro de trabajo mediante `workbook.worksheets.tableStyles.addPivotTableStyle(name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo agregando elementos (como `WholeTable` o `GrandTotalRow`) mediante `tableStyle.tableStyleElements.add(tableStyleElementType)` y luego asigne un `style` a cada elemento mediante `tableStyleElement.setElementStyle(style)`.
3. Aplique el estilo personalizado a la tabla dinámica estableciendo `pivotTable.pivotTableStyleName` al nombre del estilo. No utilice `pivotTable.pivotTableStyleType` aquí, ya que esa propiedad selecciona preajustes integrados.

{{% alert color="primary" %}}
`pivotTable.pivotTableStyleName` y `pivotTable.pivotTableStyleType` no son intercambiables. Utilice `pivotTable.pivotTableStyleType` para los preajustes integrados y `pivotTable.pivotTableStyleName` para los estilos personalizados que haya definido mediante `addPivotTableStyle`. Establecer ambos no causa problemas, pero solo se aplica el que corresponda al origen previsto.
Los valores disponibles de `TableStyleElementType` incluyen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` y `PageFieldValues`.
El siguiente ejemplo define un estilo personalizado de tabla dinámica con un borde negro fino en `WholeTable` y una fuente roja en negrita en `GrandTotalRow`, y luego lo aplica mediante `pivotTable.pivotTableStyleName` y guarda como `.xlsx`.
{{% /alert %}}

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
            const cells = worksheet.cells;
            // Completar los datos de origen: fila de encabezado + 9 filas de datos (A1:C10)
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 200;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 300;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 400;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 500;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 600;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 700;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 800;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 900;
            // Agregar una tabla dinámica con origen en A1:C10, anclada en E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Paso 1: registrar un nuevo estilo personalizado de tabla dinámica y capturar su índice
            const styleIndex = workbook.worksheets.tableStyles.addPivotTableStyle("CustomPivotStyle");
            const tableStyle = workbook.worksheets.tableStyles.get(styleIndex);
            // Paso 2: agregar un elemento WholeTable y aplicar bordes negros finos en los cuatro lados
            const wholeTableElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.WholeTable);
            const wholeTableElement = tableStyle.tableStyleElements.get(wholeTableElementIndex);
            const wholeTableStyle = workbook.createStyle();
            const topBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.TopBorder);
            topBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            topBorder.color = "black";
            const bottomBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.BottomBorder);
            bottomBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            bottomBorder.color = "black";
            const leftBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.LeftBorder);
            leftBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            leftBorder.color = "black";
            const rightBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.RightBorder);
            rightBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            rightBorder.color = "black";
            wholeTableElement.setElementStyle(wholeTableStyle);
            // Paso 3: agregar un elemento GrandTotalRow y aplicar una fuente roja en negrita
            const grandTotalElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.GrandTotalRow);
            const grandTotalElement = tableStyle.tableStyleElements.get(grandTotalElementIndex);
            const grandTotalStyle = workbook.createStyle();
            grandTotalStyle.font.isBold = true;
            grandTotalStyle.font.color = "red";
            grandTotalElement.setElementStyle(grandTotalStyle);
            // Paso 4: aplicar el estilo personalizado por nombre (NO por PivotTableStyleType, que es para los preajustes integrados)
            pivotTable.pivotTableStyleName = "CustomPivotStyle";
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Aplicar un estilo a todas las celdas de una tabla dinámica con formatAll**
`pivotTable.formatAll(style)` es un atajo que aplica un único objeto `style` a todas las celdas de la tabla dinámica, incluidos el área de datos, los encabezados de fila y columna y los totales. Lo que se haya establecido previamente mediante `pivotTable.pivotTableStyleType` o `pivotTable.pivotTableStyleName` queda anulado.

{{% alert color="primary" %}}
`formatAll` anula tanto `pivotTable.pivotTableStyleType` como `pivotTable.pivotTableStyleName`. Utilícelo solo cuando se necesite una apariencia uniforme e independiente del tema en toda la tabla dinámica.
El siguiente ejemplo crea un `style` con un relleno sólido amarillo, una fuente azul oscuro en negrita y bordes negros finos en todos los lados, y luego lo aplica con `formatAll` y guarda como `.xlsx`.
{{% /alert %}}

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
            // Escenario 4: Aplicar un único Style a todas las celdas de la tabla dinámica usando FormatAll
            // API en uso: PivotTable.FormatAll(Style)
            // Formato de destino: .xlsx
            // Referencia de GitHub: consulte el repositorio Aspose.Cells-for-.NET — ejemplos de estilo de tablas dinámicas
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Poblar los datos de origen: fila de encabezado (fila 1) + 9 filas de datos (filas 2-10)
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 5000;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 3000;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 4000;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 2000;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 6000;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 3500;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 4500;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 2500;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 5500;
            // Agregar tabla dinámica: rango de origen A1:C10, celda de destino E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // Asignar campos de la tabla dinámica: Fruit -> área de filas, Year -> área de columnas, Amount -> área de datos
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Crear un Style que se aplicará obligatoriamente a todas las celdas de la tabla dinámica
            const style = workbook.createStyle();
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            style.font.isBold = true;
            style.font.color = AsposeCells.Color.DarkBlue;
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;
            // Aplicar FormatAll: fuerza este único estilo en todas las celdas de la tabla dinámica,
            // anulando cualquier PivotTableStyleType / PivotTableStyleName previamente configurado
            pivotTable.formatAll(style);
            // Guardar el libro en el formato moderno .xlsx
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **¿Qué API de estilos debo utilizar?**
La elección de la API de estilos depende del formato de archivo en el que va a guardar. Utilice la tabla siguiente como referencia rápida.
| Formato de archivo de destino | API que debe utilizar | Notas |
|---|---|---|
| `.xls` (heredado) | `pivotTable.autoFormatType` | Valores de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (por ejemplo, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Se ignora al guardar en formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `pivotTable.pivotTableStyleType` | Valores de `Aspose.Cells.PivotTableStyleType` (temas claros/oscuros, incluidas las adiciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `pivotTable.pivotTableStyleName` + `workbook.worksheets.tableStyles.addPivotTableStyle(...)` | Utilícelo cuando los preajustes integrados no sean suficientes. Configure mediante `tableStyleElement.setElementStyle(...)`. |
| Cualquier formato (anulación uniforme) | `pivotTable.formatAll(style)` | Atajo que anula cualquier otro ajuste de estilo en toda la tabla dinámica. |
En caso de duda, guarde como `.xlsx` y utilice `pivotTable.pivotTableStyleType` para los temas integrados, o `pivotTable.pivotTableStyleName` para los temas personalizados.

{{< app/cells/assistant language="javascript-cpp" >}}