---
title: Modificar un estilo existente
linktitle: Modificar un estilo existente
description: Aspose.Cells es una biblioteca para JavaScript vía C++ para trabajar con archivos de hojas de cálculo que permite modificar estilos existentes en las celdas. Este artículo introducirá cómo modificar un estilo de celda existente con la biblioteca Aspose.Cells para que los usuarios puedan cambiar la apariencia de las celdas según sus necesidades.
keywords: Modificar estilos existentes, personalizar la apariencia de su aplicación, guías, tutoriales, documentación de ayuda, documentación de desarrollo, referencias de API, código de muestra, descargas, soporte.
type: docs
weight: 90
url: /es/javascript-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Para aplicar las mismas opciones de formateo a las celdas, cree un nuevo objeto de estilo de formateo. Un objeto de estilo de formateo es una combinación de características de formateo, como la fuente, el tamaño de la fuente, la indentación, el número, los bordes, los patrones, etc., nombrados y almacenados como un conjunto. Cuando se aplica, se aplican todas las características de formato en ese estilo.

También puede utilizar un estilo existente, guardarlo con el libro de trabajo y usarlo para formatear la información con los mismos atributos.

Cuando las celdas no tienen formato explícito, se aplica el **Estilo Normal** (el estilo predeterminado del libro). Microsoft Excel predefine varios estilos además del estilo Normal, incluyendo Coma, Moneda y Porcentaje.

Aspose.Cells permite modificar cualquiera de estos estilos u cualquier otro estilo que defina con las características deseadas.

{{% /alert %}}

## **Usar Microsoft Excel**

Para actualizar un estilo en Microsoft Excel 97-2003:

1. En el menú **Formato**, haga clic en **Estilo**.
1. Seleccione el estilo que desea modificar de la lista **Nombre del estilo**.
1. Haga clic en **Modificar**.
1. Seleccione las opciones de estilo que desee utilizando las pestañas en el cuadro de diálogo Formato de celdas.
1. Haz clic en **Aceptar**.
1. En **El estilo incluye**, especifique las características del estilo que desee.
1. Haga clic en **Aceptar** para guardar el estilo y aplicarlo al rango seleccionado.

## **Usando Aspose.Cells for JavaScript vía C++**

Los siguientes ejemplos muestran cómo usar el método [**Style.update()**](https://reference.aspose.com/cells/javascript-cpp/style/#update--).

### **Creación y Modificación de un Estilo**

Este ejemplo crea un objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style), lo aplica a un rango de celdas y modifica el objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Las modificaciones se aplican automáticamente a la celda y al rango al que se aplicó el estilo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Style Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a new style object.
            const style = workbook.createStyle();

            // Set the number format.
            style.number = 14;

            // Set the font color to red color.
            style.font.color = AsposeCells.Color.Red;

            // Name the style.
            style.name = "Date1";

            // Get the first worksheet cells.
            const cells = workbook.worksheets.get(0).cells;

            // Specify the style (described above) to A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.style = style;

            // Create a range (B1:D1).
            const range = cells.createRange("B1", "D1");

            // Initialize styleflag object.
            const flag = new AsposeCells.StyleFlag();

            // Set all formatting attributes on.
            flag.all = true;

            // Apply the style (described above) to the range.
            range.applyStyle(style, flag);

            // Modify the style (described above) and change the font color from red to black.
            style.font.color = AsposeCells.Color.Black;

            // Done! Since the named style (described above) has been set to a cell and range, 
            // The change would be reflected(new modification is implemented) to cell(A1) and 
            // Range (B1:D1).
            style.update();

            // Save the excel file. 
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book_styles.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **Modificación de un Estilo Existente**

Este ejemplo utiliza un archivo de Excel de plantilla simple en el que ya se ha aplicado un estilo llamado Porcentaje a un rango. El ejemplo:

1. obtiene el estilo,
1. crea un objeto de estilo y
1. modifica el formato del estilo.

Las modificaciones se aplican automáticamente al rango al que se aplicó el estilo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Named Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, Utils } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the named style "Percent" via the styles collection
            const style = workbook.styles.get("Percent");

            // Change the number format to "0.00%".
            style.number = 11;

            // Set the font color.
            style.font.color = Color.Red;

            // Update the style so ranges using this named style are updated.
            style.update();

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book2.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Style updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
