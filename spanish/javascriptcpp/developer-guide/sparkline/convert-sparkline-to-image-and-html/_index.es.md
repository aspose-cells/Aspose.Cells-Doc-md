---
title: Convertir un minigráfico en una imagen y exportar a HTML con Aspose.Cells for JavaScript via C++
linktitle: Convertir un minigráfico en una imagen y exportar a HTML con Aspose.Cells for JavaScript via C++
description: Aprenda a renderizar los minigráficos de Aspose.Cells como imágenes independientes que pueden incrustarse en celdas y a exportar a HTML hojas de cálculo con minigráficos mediante HtmlSaveOptions.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, minigráfico, sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, renderizado de minigráficos, conversión de minigráficos a imágenes, exportación de minigráficos a HTML
type: docs
weight: 120
url: /es/javascript-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Los minigráficos son gráficos en miniatura que se colocan dentro de las celdas de una hoja de cálculo. Aspose.Cells permite extraer cada minigráfico como una imagen independiente (para incrustarla en otra celda o en un informe externo) y también exportar a HTML la hoja de cálculo completa con sus minigráficos para facilitar su distribución en el navegador. La propiedad `cell.embeddedImage` utilizada en este artículo está disponible en **Aspose.Cells 26.5 y versiones posteriores**.
{{% /alert %}}

## **Introducción**
Los minigráficos ofrecen una forma compacta de visualizar tendencias directamente dentro de una hoja de cálculo. Aunque los usuarios de Excel los ven directamente en su ubicación, muchos escenarios del mundo real requieren que un minigráfico se extraiga de la celda; por ejemplo, para incrustarlo en otra celda como imagen estática, adjuntarlo a un correo electrónico automatizado o renderizarlo como parte de un informe HTML publicado en la web.
Aspose.Cells admite ambas operaciones. El método `sparkline.toImage` renderiza un minigráfico individual como `Buffer`, y los bytes resultantes pueden asignarse a `cell.embeddedImage` para que la imagen quede almacenada dentro de una sola celda del libro de trabajo. Por otro lado, `HtmlSaveOptions` permite convertir el libro de trabajo completo, con todos sus minigráficos, en un archivo HTML autocontenido. Este artículo explica ambos flujos de trabajo de principio a fin.

## **Flujo de trabajo 1: renderizar minigráficos como imágenes e incrustarlos en celdas**
En este flujo de trabajo se creará una hoja de cálculo con un rango pequeño de valores de origen, se asociarán tres grupos de minigráficos distintos (línea, columna y apilado/victoria-derrota) a ese rango, cada grupo se renderizará como PNG y los bytes resultantes se escribirán en celdas adyacentes como imágenes incrustadas. El resultado final es un único archivo `.xlsx` que contiene tanto los minigráficos activos como sus imágenes estáticas correspondientes.

### **Instrucciones paso a paso**
1. Cree un nuevo `Workbook` y obtenga una referencia al primer `Worksheet`.
2. Rellene las celdas `A1` a `E1` con cinco valores numéricos de muestra (por ejemplo, ventas diarias o lecturas de temperatura).
3. Agregue tres objetos `SparklineGroup` a la hoja de cálculo llamando a `worksheet.getSparklineGroups().add(...)`:
   - Un grupo `SparklineType.Line` anclado en `F1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.Column` anclado en `G1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.Stacked` (victoria/derrota) anclado en `H1`, con rango de datos `A1:E1`.
4. Cree una instancia de `ImageOrPrintOptions` y establezca su propiedad `imageType` en `ImageType.Png` para que cada minigráfico se represente como una imagen PNG.
5. Guarde el libro de trabajo como `output_with_sparklines.xlsx`.

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
        const { Workbook, CellArea, ImageOrPrintOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Crear un nuevo libro de trabajo y acceder a la primera hoja de cálculo
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Rellenar las celdas A1:E1 con datos de ejemplo
            cells.get("A1").value = 5;
            cells.get("B1").value = -3;
            cells.get("C1").value = 8;
            cells.get("D1").value = -2;
            cells.get("E1").value = 6;
            // Agregar un grupo de minigráficos de línea anclado en F1 (columna 5, fila 0)
            const lineArea = new CellArea();
            lineArea.startColumn = 5;
            lineArea.endColumn = 5;
            lineArea.startRow = 0;
            lineArea.endRow = 0;
            const lineIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Line,
                "A1:E1",
                false,
                lineArea
            );
            // Agregar un grupo de minigráficos de columna anclado en G1 (columna 6, fila 0)
            const columnArea = new CellArea();
            columnArea.startColumn = 6;
            columnArea.endColumn = 6;
            columnArea.startRow = 0;
            columnArea.endRow = 0;
            const columnIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Column,
                "A1:E1",
                false,
                columnArea
            );
            // Agregar un grupo de minigráficos Ganador/Perdedor (Apilado) anclado en H1 (columna 7, fila 0)
            const stackedArea = new CellArea();
            stackedArea.startColumn = 7;
            stackedArea.endColumn = 7;
            stackedArea.startRow = 0;
            stackedArea.endRow = 0;
            const stackedIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Stacked,
                "A1:E1",
                false,
                stackedArea
            );
            // Configurar las opciones de imagen para la salida PNG
            const imageOptions = new ImageOrPrintOptions();
            imageOptions.imageType = AsposeCells.ImageType.Png;
            // Convertir el minigráfico de línea en una imagen e incrustarla en la celda F2
            const lineSp = worksheet.sparklineGroups.get(lineIdx).sparklines.get(0);
            cells.get("F2").embeddedImage = lineSp.toImage(imageOptions);
            // Convertir el minigráfico de columna en una imagen e incrustarla en la celda G2
            const columnSp = worksheet.sparklineGroups.get(columnIdx).sparklines.get(0);
            cells.get("G2").embeddedImage = columnSp.toImage(imageOptions);
            // Convertir el minigráfico Ganador/Perdedor en una imagen e incrustarla en la celda H2
            const stackedSp = worksheet.sparklineGroups.get(stackedIdx).sparklines.get(0);
            cells.get("H2").embeddedImage = stackedSp.toImage(imageOptions);
            // Guardar el libro de trabajo en el disco
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_with_sparklines.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

El código anterior produce un libro de trabajo en el que cada representación visual de un minigráfico existe en dos formas: el minigráfico nativo y activo, anclado en la fila 1, y una imagen PNG estática incrustada directamente en una celda contigua de la fila 2. Como las imágenes están contenidas en el propio archivo, el libro de trabajo sigue siendo un único artefacto autocontenido que puede enviarse por correo electrónico o archivarse sin invalidar las referencias a las imágenes incrustadas.

{{% alert color="primary" %}}
Como cada grupo de minigráficos está anclado en una sola celda, puede acceder a su minigráfico mediante el indexador `group.getSparklines()[0]` en lugar de enumerar la colección. Esto mantiene corto el código de renderizado y coincide con el patrón típico de «un minigráfico por celda de anclaje». El almacenamiento de los bytes de la imagen mediante `cell.embeddedImage` requiere Aspose.Cells 26.5 o una versión posterior.
{{% /alert %}}

## **Flujo de trabajo 2: exportar la hoja de cálculo con minigráficos a HTML**
Una vez que el libro de trabajo contiene minigráficos activos (y, opcionalmente, sus imágenes incrustadas correspondientes), se puede publicar toda la hoja de cálculo en la web guardándola como HTML. La clase `HtmlSaveOptions` expone las opciones necesarias para controlar esta exportación; en este flujo de trabajo se reutilizará el archivo `output_with_sparklines.xlsx` producido en el Flujo de trabajo 1 y se convertirá en un documento HTML limpio de una sola página.

### **Instrucciones paso a paso**
1. Asegúrese de que el archivo `output_with_sparklines.xlsx` producido en el Flujo de trabajo 1 esté disponible en el disco, en el directorio de trabajo.
2. Cargue ese archivo en una nueva instancia de `Workbook`.
3. Cree una instancia de `HtmlSaveOptions` y establezca su propiedad `exportActiveWorksheetOnly` en `true` para que el archivo HTML resultante contenga solo la hoja de cálculo activa en lugar de todo el libro de trabajo.
4. Llame a `workbook.save("sparklines.html", htmlOptions)` para escribir la salida HTML en el disco.

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
        const { Workbook, HtmlSaveOptions } = AsposeCells;
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
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const htmlOptions = new HtmlSaveOptions();
                htmlOptions.exportActiveWorksheetOnly = true;
                const outputData = workbook.save(AsposeCells.SaveFormat.Html, htmlOptions);
                const blob = new Blob([outputData], { type: "text/html" });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "sparklines.html";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

El código anterior toma el libro de trabajo con minigráficos del Flujo de trabajo 1 y lo convierte en un archivo HTML portátil. Los grupos de minigráficos se renderizan como imágenes en línea dentro de la tabla HTML generada, por lo que los usuarios finales pueden ver las tendencias en cualquier navegador moderno sin necesidad de tener Excel instalado. Al establecer `exportActiveWorksheetOnly` en `true`, se evita publicar accidentalmente hojas ocultas o datos auxiliares; solo se exporta la hoja de cálculo visible actualmente para el usuario.

{{% alert color="primary" %}}
La clase `HtmlSaveOptions` ofrece propiedades adicionales para ajustar con precisión la salida, como `exportHiddenWorksheet`, `exportImagesAsBase64` y `encoding`. Ajústelas según las necesidades de su entorno de despliegue.
{{% /alert %}}

## **Resumen de la API**
Los flujos de trabajo anteriores dependen de un pequeño conjunto de API de Aspose.Cells que funcionan conjuntamente.
- `SparklineGroup` y el método de acceso a la colección `worksheet.getSparklineGroups()` se utilizan para declarar el tipo (línea, columna y apilado), el rango de datos y la celda de anclaje de cada grupo de minigráficos. En este artículo, cada grupo está anclado en una sola celda, por lo que se accede al grupo mediante `worksheet.getSparklineGroups()[i]`.
- `Sparkline` y el indexador `group.getSparklines()[0]` devuelven el minigráfico individual incluido en un grupo. Como cada grupo del ejemplo contiene exactamente un minigráfico, no es necesario ningún bucle de iteración.
- `sparkline.toImage(imageOrPrintOptions)` es el método de renderizado que devuelve una imagen del minigráfico como `Buffer`. Los bytes devueltos pueden asignarse directamente a `cell.embeddedImage`.
- `HtmlSaveOptions.exportActiveWorksheetOnly` (un valor booleano) restringe la exportación HTML a la hoja de cálculo activa. Es una de las propiedades más utilizadas de `HtmlSaveOptions` al generar informes de una sola página.
- `ImageOrPrintOptions.imageType` selecciona el formato de imagen (por ejemplo, `ImageType.Png`) que se utiliza al renderizar con `toImage` y al imprimir hojas de cálculo como imágenes.

{{< app/cells/assistant language="javascript-cpp" >}}