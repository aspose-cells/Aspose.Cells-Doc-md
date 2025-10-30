---
title: Cómo crear un Gráfico de Rodamiento Dinámico con JavaScript a través de C++
linktitle: Cómo crear un Gráfico Dinámico Continuo
description: Aprenda a crear un gráfico de rodamiento dinámico usando Aspose.Cells for JavaScript via C++. Nuestra guía demostrará cómo implementar transiciones suaves de datos y promedios rodantes en su gráfico para una visualización continua y actualizada.
keywords: Aspose.Cells for JavaScript via C++, Gráfico de Rodamiento Dinámico, Transiciones de Datos, Promedios Suaves, Pantalla Continua, Visualización Actualizada.
type: docs
weight: 74
url: /es/javascript-cpp/create-dynamic-rolling-chart/
---

## **Escenarios de uso posibles**
Un gráfico de desplazamiento dinámico se refiere a una representación gráfica que muestra puntos de datos en constante cambio y actualización a lo largo del tiempo. Es un tipo de gráfico que se actualiza continuamente, mostrando una ventana en tiempo real de los puntos de datos más recientes mientras descarta los puntos de datos antiguos a medida que ingresan nuevos.

Los gráficos de desplazamiento dinámico se utilizan comúnmente para visualizar tendencias y patrones en datos en tiempo real o en streaming. Son particularmente útiles en escenarios donde los aspectos temporales y los cambios a lo largo del tiempo son críticos, como análisis del mercado de valores, monitoreo del clima o seguimiento de actuaciones en vivo.

Estos gráficos suelen emplear mecanismos de animación o desplazamiento automático para garantizar que la información más actualizada siempre se presente. La longitud de la ventana de desplazamiento se puede personalizar para mostrar un período de tiempo específico, como la última hora, día o semana.

En resumen, un gráfico de desplazamiento dinámico es una representación gráfica actualizada continuamente que muestra los últimos puntos de datos mientras descarta los antiguos, lo que permite a los usuarios observar tendencias y patrones en tiempo real.

## **Use Aspose Cells para crear un gráfico de desplazamiento dinámico**
En los siguientes párrafos, le mostraremos cómo crear un gráfico de desplazamiento dinámico usando Aspose.Cells. Le mostraremos el código del ejemplo, así como el archivo de Excel creado con este código.

## **Código de muestra**
El siguiente código de ejemplo generará el [Archivo de Gráfico de Desplazamiento Dinámico](DynamicRollingChart.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Rolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Utils } = AsposeCells;

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
            sheet.cells.get("A1").value = "Month";
            sheet.cells.get("A2").value = 1;
            sheet.cells.get("A3").value = 2;
            sheet.cells.get("A4").value = 3;
            sheet.cells.get("A5").value = 4;
            sheet.cells.get("A6").value = 5;
            sheet.cells.get("A7").value = 6;
            sheet.cells.get("A8").value = 7;

            sheet.cells.get("B1").value = "Sales";
            sheet.cells.get("B2").value = 50;
            sheet.cells.get("B3").value = 45;
            sheet.cells.get("B4").value = 55;
            sheet.cells.get("B5").value = 60;
            sheet.cells.get("B6").value = 55;
            sheet.cells.get("B7").value = 65;
            sheet.cells.get("B8").value = 70;

            // Set the dynamic range for the chart's data source.
            let index = sheets.names.add("Sheet1!ChtData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)";

            // Set the dynamic range for the chart's data labels.
            index = sheets.names.add("Sheet1!ChtLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 10, 3, 25, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicRollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Notas**
En el archivo generado, puedes seguir agregando datos en las columnas A y B, mientras que el gráfico cuenta dinámicamente los últimos 5 conjuntos de datos. Esto se hace usando la fórmula "OFFSET" en el código de muestra:
