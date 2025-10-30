---
title: Cómo crear un Gráfico Dinámico con Lista Desplegable usando JavaScript vía C++
linktitle: Cómo crear un Gráfico Dinámico con Lista Desplegable
description: Aprende cómo crear un gráfico dinámico que se actualice en función de la selección en una lista desplegable usando Aspose.Cells for JavaScript vía C++. Nuestra guía paso a paso demostrará cómo integrar una lista desplegable en tu gráfico para una visualización de datos flexible.
keywords: Aspose.Cells for JavaScript vía C++, Gráfico Dinámico, Lista Desplegable, Visualización de Datos, Integración, Visualización flexible.
type: docs
weight: 76
url: /es/javascript-cpp/create-dynamic-chart-with-dropdownlist/
---

## **Escenarios de uso posibles**
Un Gráfico Dinámico con Lista Desplegable en Excel es una herramienta poderosa que permite a los usuarios crear gráficos interactivos que pueden actualizarse dinámicamente en función de los datos seleccionados. Esta característica es particularmente útil en situaciones en las que se necesita analizar múltiples conjuntos de datos o comparar varios escenarios.

Una aplicación común de un Gráfico Dinámico con Lista Desplegable es en el análisis financiero. Por ejemplo, una empresa puede tener múltiples conjuntos de datos financieros para diferentes años o departamentos. Al utilizar una lista desplegable, los usuarios pueden seleccionar el conjunto de datos específico que desean analizar y el gráfico se actualizará automáticamente para mostrar la información correspondiente. Esto permite una fácil comparación e identificación de tendencias o patrones.

Otra aplicación está en ventas y marketing. Una empresa puede tener datos de ventas para diferentes productos o regiones. Con un Gráfico Dinámico con Lista Desplegable, los usuarios pueden elegir un producto o región específica de la lista desplegable y el gráfico se actualizará dinámicamente para mostrar el rendimiento de ventas para la opción seleccionada. Esto ayuda a identificar las áreas o productos más destacados y a tomar decisiones basadas en datos.

En resumen, un Gráfico Dinámico con Lista Desplegable en Excel proporciona una forma flexible e interactiva de visualizar y analizar datos. Es valioso en situaciones en las que se necesita comparar múltiples conjuntos de datos o explorar diferentes escenarios, convirtiéndolo en una herramienta versátil para el análisis financiero, ventas y marketing, y muchas otras aplicaciones.

## **Utiliza Aspose Cells para crear un Gráfico Dinámico con Lista Desplegable**
En los próximos párrafos, te mostraremos cómo crear un Gráfico Dinámico con Lista Desplegable usando Aspose.Cells for JavaScript vía C++. Mostraremos el código para el ejemplo, así como el archivo de Excel creado con este código.

## **Código de muestra**
El siguiente código de ejemplo generará el [Archivo de Gráfico Dinámico con Lista Desplegable](DynamicChartWithDropdownlist.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Chart with Dropdown List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, BackgroundType, Color, ChartType } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A3").putValue("Tea");
            sheet.cells.get("A4").putValue("Coffee");
            sheet.cells.get("A5").putValue("Sugar");

            // In this example, we will add 12 months of data
            sheet.cells.get("B2").putValue("Jan");
            sheet.cells.get("C2").putValue("Feb");
            sheet.cells.get("D2").putValue("Mar");
            sheet.cells.get("E2").putValue("Apr");
            sheet.cells.get("F2").putValue("May");
            sheet.cells.get("G2").putValue("Jun");
            sheet.cells.get("H2").putValue("Jul");
            sheet.cells.get("I2").putValue("Aug");
            sheet.cells.get("J2").putValue("Sep");
            sheet.cells.get("K2").putValue("Oct");
            sheet.cells.get("L2").putValue("Nov");
            sheet.cells.get("M2").putValue("Dec");
            const allMonths = 12;
            const iCount = 3;
            for (let i = 0; i < iCount; i++) {
                for (let j = 0; j < allMonths; j++) {
                    const _row = i + 2;
                    const _column = j + 1; 
                    sheet.cells.get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
                }
            }

            // This is the Dropdownlist for Dynamic Data
            const ca = CellArea.createCellArea(9, 0, 9, 0);
            const _index = sheet.validations.add(ca);
            const _va = sheet.validations.get(_index);
            _va.type = ValidationType.List;
            _va.inCellDropDown = true;
            _va.formula1 = "=$B$2:$M$2";
            sheet.cells.get("A9").putValue("Current Month");
            sheet.cells.get("A10").putValue("Jan");
            const _style = sheet.cells.get("A10").style;
            _style.font.isBold = true;
            _style.pattern = BackgroundType.Solid;
            _style.foregroundColor = Color.Yellow;
            sheet.cells.get("A10").style = _style;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtMonthData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtXLabels");
            sheets.names.get(index).refersTo = "=Sheet1!$A$3:$A$5";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Column, 8, 2, 20, 8);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("month", true);
            chart.nSeries.get(0).name = "=Sheet1!$A$10";
            chart.nSeries.get(0).values = "Sheet1!ChtMonthData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtXLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicChartWithDropdownlist.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

## **Notas**
En el archivo generado, el gráfico contará dinámicamente los datos para el mes seleccionado. Esto se hace utilizando la fórmula "OFFSET" en el código de ejemplo:
