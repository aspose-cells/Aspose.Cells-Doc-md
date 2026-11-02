---
title: Conversión de Excel al formato OFD
linktitle: Conversión de Excel al formato OFD
description: Aspose.Cells for JavaScript via C++ es una biblioteca de JavaScript para trabajar con archivos de hoja de cálculo que permite convertir libros de trabajo de Excel al formato OFD (documento de diseño fijo). Este artículo demuestra cómo crear contenido de Excel y exportarlo como OFD, así como cómo convertir archivos de Excel existentes a OFD mediante Aspose.Cells.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, biblioteca de JavaScript, hoja de cálculo, Excel a OFD, conversión a OFD, SaveFormat.Ofd, documento de diseño fijo, exportación de libros de trabajo
type: docs
weight: 195
url: /es/javascript-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells permite convertir directamente libros de trabajo de Excel al formato OFD (documento de diseño fijo) mediante el valor de la enumeración `SaveFormat.Ofd`. El documento OFD resultante conserva la disposición visible, el contenido, las celdas combinadas, los anchos de columna, las alturas de fila, las fuentes, los colores, los bordes y los formatos numéricos del libro de trabajo. Esto hace que Aspose.Cells sea adecuado para flujos de trabajo de archivado, impresión, presentación ante organismos reguladores y envío a la administración pública, cuando se requiere una salida de diseño fijo.
{{% /alert %}}

## **Introducción**
OFD (documento de diseño fijo) es un estándar nacional chino (GB/T 33190-2016) para representar documentos digitales con una disposición fija basada en páginas. Desempeña un papel similar al de PDF en casos de uso en los que la apariencia visual del documento de origen debe conservarse exactamente tal como se creó. OFD se utiliza ampliamente para envíos a la administración pública, presentaciones ante organismos reguladores, facturas electrónicas y el archivado a largo plazo en la República Popular China.
La conversión de libros de trabajo de Excel a OFD es un requisito habitual en situaciones en las que el contenido de una hoja de cálculo debe distribuirse como un artefacto de solo lectura con la disposición bloqueada, en lugar de como una hoja de cálculo editable. Entre los ejemplos se incluyen enviar una factura finalizada a un cliente, archivar un informe financiero trimestral o presentar una hoja de cálculo de presupuesto a una autoridad reguladora. Aspose.Cells cubre esta necesidad mediante el valor de la enumeración `SaveFormat.Ofd`, que permite guardar el libro de trabajo directamente en formato OFD sin necesidad de un paso de conversión intermedio. La salida OFD conserva los valores de las celdas, los rangos combinados, las fuentes, los colores, los bordes, los formatos numéricos y las opciones de configuración de página definidas en el libro de trabajo.

{{% alert color="primary" %}}
La salida OFD generada por Aspose.Cells conserva la disposición visible del libro de trabajo de origen, incluidos el contenido de las celdas, las celdas combinadas, los anchos de columna y las alturas de fila. El formato de las celdas, como las fuentes, los colores, los bordes, la alineación y los formatos numéricos, también se representa en la salida de diseño fijo. Las opciones de configuración de página establecidas en la hoja de cálculo, como el tamaño del papel, la orientación y el área de impresión, influyen en la disposición del documento OFD resultante.
{{% /alert %}}

## **Creación de un libro de trabajo de Excel y guardado como OFD**
Aspose.Cells permite crear un libro de trabajo de forma programática, llenarlo con datos y guardarlo directamente en formato OFD mediante el valor de la enumeración `SaveFormat.Ofd`. El siguiente ejemplo crea una factura desde cero. Añade el logotipo de una empresa, información de encabezado, una sección de datos de facturación, líneas de detalle y totales calculados; a continuación, exporta el libro de trabajo a un documento OFD.

### **Creación de una factura con un logotipo**
El ejemplo construye una hoja de cálculo para una factura. Para ello, inserta una imagen del logotipo en el área superior izquierda, rellena el nombre de la empresa y los datos de contacto, añade un título "INVOICE" en celdas combinadas, registra el número y la fecha de la factura, indica el cliente al que se factura, crea una tabla de líneas de detalle con columnas de descripción, cantidad, precio unitario y total, y calcula el subtotal, el impuesto y el total general mediante fórmulas en las celdas. Se aplican elementos de formato, como los encabezados en negrita, el formato de moneda de los precios, los bordes y los anchos de columna, mediante los objetos `Style` y `Font`. Por último, el libro de trabajo se guarda con la extensión `.ofd` mediante `SaveFormat.Ofd`.

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
        const { Workbook, Color } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                // Crear un nuevo libro de trabajo
                const workbook = new Workbook();
                // Obtener la primera hoja de cálculo
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Establecer los anchos de las columnas
                cells.setColumnWidth(0, 5);
                cells.setColumnWidth(1, 35);
                cells.setColumnWidth(2, 12);
                cells.setColumnWidth(3, 15);
                cells.setColumnWidth(4, 15);
                cells.setColumnWidth(5, 5);
                // Insertar el logotipo de la empresa
                // Crear un PNG en memoria porque el navegador no tiene una ruta del sistema de archivos.
                const logoCanvas = document.createElement("canvas");
                logoCanvas.width = 100;
                logoCanvas.height = 30;
                const logoContext = logoCanvas.getContext("2d");
                logoContext.fillStyle = "#000080";
                logoContext.fillRect(0, 0, logoCanvas.width, logoCanvas.height);
                logoContext.fillStyle = "#FFFFFF";
                logoContext.font = "bold 18px Arial";
                logoContext.fillText("ACME", 16, 21);
                const logoBlob = await new Promise(resolve => logoCanvas.toBlob(resolve, "image/png"));
                if (!logoBlob) {
                    throw new Error("Unable to create the company logo.");
                }
                const logoData = new Uint8Array(await logoBlob.arrayBuffer());
                worksheet.pictures.add(1, 1, logoData);
                // Nombre de la empresa y datos de contacto
                cells.get("B3").value = "Acme Corporation";
                cells.get("B4").value = "123 Business Street";
                cells.get("B5").value = "City, State 12345";
                cells.get("B6").value = "Phone: (555) 123-4567";
                // Título de la factura: combinar celdas
                cells.merge(7, 1, 2, 4);
                const titleCell = cells.get("B8");
                titleCell.value = "INVOICE";
                const titleStyle = workbook.createStyle();
                titleStyle.font.isBold = true;
                titleStyle.font.size = 20;
                titleStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                titleCell.style = titleStyle;
                // Número de factura y fecha
                cells.get("B11").value = "Invoice Number:";
                cells.get("C11").value = "INV-2024-001";
                cells.get("B12").value = "Date:";
                const now = new Date();
                const invoiceDate = [
                    now.getFullYear(),
                    String(now.getMonth() + 1).padStart(2, "0"),
                    String(now.getDate()).padStart(2, "0")
                ].join("-");
                cells.get("C12").value = invoiceDate;
                // Sección de facturación
                cells.get("B14").value = "Bill To:";
                cells.get("B15").value = "Client Name";
                cells.get("B16").value = "Client Address";
                cells.get("B17").value = "Client City, State";
                // Encabezado de las líneas de detalle
                const headerDesc = cells.get("B19");
                const headerQty = cells.get("C19");
                const headerPrice = cells.get("D19");
                const headerTotal = cells.get("E19");
                headerDesc.value = "Description";
                headerQty.value = "Quantity";
                headerPrice.value = "Unit Price";
                headerTotal.value = "Total";
                const headerStyle = workbook.createStyle();
                headerStyle.font.isBold = true;
                headerStyle.font.color = Color.fromArgb(255, 255, 255);
                headerStyle.foregroundColor = Color.fromArgb(0, 0, 128);
                headerStyle.pattern = AsposeCells.BackgroundType.Solid;
                headerStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                headerStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerDesc.style = headerStyle;
                headerQty.style = headerStyle;
                headerPrice.style = headerStyle;
                headerTotal.style = headerStyle;
                // Estilo de moneda con bordes
                const currencyStyle = workbook.createStyle();
                currencyStyle.custom = '"$"#,##0.00';
                currencyStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // Estilo de borde simple para celdas de descripción/cantidad
                const borderStyle = workbook.createStyle();
                borderStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // Filas de las líneas de detalle
                const lineItems = [
                    ["Product A - Widget", 2, 50.00],
                    ["Product B - Gadget", 3, 75.00],
                    ["Product C - Service", 1, 100.00]
                ];
                for (let i = 0; i < lineItems.length; i++) {
                    const row = 20 + i;
                    const descCell = cells.get(row, 1);
                    const qtyCell = cells.get(row, 2);
                    const priceCell = cells.get(row, 3);
                    const totalCell = cells.get(row, 4);
                    descCell.value = lineItems[i][0];
                    qtyCell.value = lineItems[i][1];
                    priceCell.value = lineItems[i][2];
                    totalCell.formula = "C" + (row + 1) + "*D" + (row + 1);
                    descCell.style = borderStyle;
                    qtyCell.style = borderStyle;
                    priceCell.style = currencyStyle;
                    totalCell.style = currencyStyle;
                }
                // Subtotal, impuesto y total general
                cells.get("B24").value = "Subtotal:";
                const subtotalCell = cells.get("E24");
                subtotalCell.formula = "SUM(E21:E23)";
                cells.get("B25").value = "Tax (10%):";
                const taxCell = cells.get("E25");
                taxCell.formula = "E24*0.1";
                cells.get("B26").value = "Grand Total:";
                const grandTotalCell = cells.get("E26");
                grandTotalCell.formula = "E24+E25";
                // Estilo de negrita y moneda para los valores totales
                const totalStyle = workbook.createStyle();
                totalStyle.font.isBold = true;
                totalStyle.custom = '"$"#,##0.00';
                subtotalCell.style = totalStyle;
                taxCell.style = totalStyle;
                grandTotalCell.style = totalStyle;
                // Estilo de negrita para las etiquetas de totales
                const boldStyle = workbook.createStyle();
                boldStyle.font.isBold = true;
                cells.get("B24").style = boldStyle;
                cells.get("B25").style = boldStyle;
                cells.get("B26").style = boldStyle;
                // Guardar el libro de trabajo como un archivo OFD
                const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "Invoice.ofd";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
        </script>
    </body>
</html>
```

## **Conversión de un archivo de Excel existente a OFD**
Aspose.Cells también puede cargar un libro de trabajo de Excel existente desde el disco y exportarlo directamente al formato OFD. Esto resulta útil para procesos de conversión por lotes, flujos de archivado y situaciones en las que el libro de trabajo de origen se creó con otra herramienta y solo necesita volver a generarse como un artefacto de diseño fijo. El siguiente ejemplo carga un libro de trabajo `.xlsx` existente, lee datos de sus celdas, aplica ajustes opcionales en la configuración de página y guarda el resultado como un documento OFD.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, CellsHelper } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            function formatTimestamp(date) {
                const pad = value => String(value).padStart(2, "0");
                return date.getFullYear() + "-" +
                    pad(date.getMonth() + 1) + "-" +
                    pad(date.getDate()) + " " +
                    pad(date.getHours()) + ":" +
                    pad(date.getMinutes()) + ":" +
                    pad(date.getSeconds());
            }
            function escapeHtml(value) {
                const entities = {
                    "&": "&amp;",
                    "<": "&lt;",
                    ">": "&gt;",
                    '"': "&quot;",
                    "'": "&#39;"
                };
                return String(value).replace(/[&<>"']/g, character => entities[character]);
            }
            runButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an Excel file first.</p>';
                        return;
                    }
                    runButton.disabled = true;
                    downloadLink.style.display = "none";
                    downloadLink.removeAttribute("href");
                    // Abrir un libro de Excel existente desde el disco
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // (1) Leer y mostrar los valores de las celdas seleccionadas para confirmar que el archivo se cargó
                    const firstSheet = workbook.worksheets.get(0);
                    const cells = firstSheet.cells;
                    const output = [];
                    output.push("First sheet name: " + firstSheet.name);
                    output.push("Cell A1: " + cells.get("A1").stringValue);
                    output.push("Cell B1: " + cells.get("B1").stringValue);
                    output.push("Cell C1: " + cells.get("C1").stringValue);
                    // (2) Recorrer la colección Worksheets para enumerar las hojas disponibles
                    output.push("");
                    output.push("Available worksheets:");
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const ws = workbook.worksheets.get(i);
                        output.push("  [" + i + "] " + ws.name);
                    }
                    // (3) Opcionalmente, actualizar una celda de marca de tiempo para reflejar la conversión
                    cells.get("A1").value = "Converted on: " + formatTimestamp(new Date());
                    // Agregar una fila de encabezado de resumen en la parte superior del bloque de datos
                    cells.insertRow(0);
                    cells.get("A1").value = "Conversion Summary";
                    cells.get("A2").value = "Generated: " + formatTimestamp(new Date());
                    // (4) Configurar las propiedades de PageSetup en la hoja de cálculo
                    const pageSetup = firstSheet.pageSetup;
                    pageSetup.orientation = AsposeCells.PageOrientationType.Landscape;
                    pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
                    pageSetup.fitToPagesTall = 1;
                    pageSetup.fitToPagesWide = 1;
                    // (5) Opcionalmente, establecer el área de impresión para la salida OFD
                    const lastRow = cells.maxDataRow;
                    const lastCol = cells.maxDataColumn;
                    const lastColLetter = CellsHelper.columnIndexToName(lastCol);
                    const printArea = "A1:" + lastColLetter + (lastRow + 1);
                    pageSetup.printArea = printArea;
                    output.push("");
                    output.push("Print area set to: " + printArea);
                    // (6) Guardar el libro como un archivo OFD
                    const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                    const blob = new Blob([outputData]);
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "SampleBook.ofd";
                    downloadLink.textContent = "Download SampleBook.ofd";
                    downloadLink.style.display = "block";
                    output.push("");
                    output.push("File successfully converted to OFD format: SampleBook.ofd");
                    result.innerHTML =
                        '<pre style="white-space: pre-wrap;">' +
                        escapeHtml(output.join("\n")) +
                        "</pre>" +
                        '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    const message = error && error.message ? error.message : String(error);
                    result.innerHTML = '<p style="color: red;">Error: ' + escapeHtml(message) + "</p>";
                } finally {
                    runButton.disabled = false;
                }
            });
        </script>
    </body>
</html>
```

## **Artículos relacionados**
- [Inserción de una imagen en una celda](/cells/es/javascript-cpp/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="javascript-cpp" >}}