---
title: Formato de celdas con JavaScript vía C++
description: Aprende cómo formatear y estilitzar celdas en Aspose.Cells for JavaScript vía C++, incluyendo formato de números, formato de fechas, estilos de fuente y otras opciones de estilo de celda. Nuestra guía te ayudará a crear hojas de cálculo atractivas y de aspecto profesional.
keywords: Aspose.Cells for JavaScript vía C++, formateo de celdas, estilización, formato de números, formato de fechas, estilo de fuente, opciones de estilo de celda, hoja de cálculo, crear, apariencia profesional, formatear filas y columnas.
linktitle: Formato de celdas
type: docs
weight: 120
url: /es/javascript-cpp/cells-formatting/
---

## **Introducción**

{{% alert color="primary" %}}

Aspose.Cells proporciona los métodos [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) y [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) de la clase [Cell](https://reference.aspose.com/cells/javascript-cpp/cell), utilizados para obtener y establecer el estilo de formato de una celda. Aspose.Cells también proporciona una clase [**Style**](https://reference.aspose.com/cells/javascript-cpp/style).

{{% /alert %}}

## **Cómo formatear celdas usando métodos de estilo**

Aplica diferentes tipos de estilos de formato en las celdas para establecer colores de fondo o primer plano, bordes, fuentes, alineaciones horizontales y verticales, nivel de sangría, dirección del texto, ángulo de rotación y mucho más.

### **Cómo usar los métodos de estilo**

Si los desarrolladores necesitan aplicar diferentes estilos de formato a distintas celdas, es mejor obtener el [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) de la celda usando el método [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--), especificar los atributos del estilo y luego aplicar el formato usando el método [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-). A continuación se muestra un ejemplo para demostrar este enfoque de aplicar varios formatos en una celda.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Styling Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Defining a Style object
            let style;

            // Get the style from A1 cell
            style = cell.style;

            // Setting the vertical alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text
            style.font.color = AsposeCells.Color.Green;

            // Setting to shrink according to the text contained in it
            style.shrinkToFit = true;

            // Setting the bottom border color to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Applying the style to A1 cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Cómo utilizar el objeto Style para dar formato a diferentes celdas**

Si los desarrolladores necesitan aplicar el mismo estilo de formato a diferentes celdas, pueden usar el objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Por favor, sigue los pasos a continuación para usar el objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style):

1. Añadir un objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) llamando al método [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--) de la clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)
2. Acceder al objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) recién añadido
3. Establecer las propiedades/atributos deseados del objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) para aplicar la configuración de formato deseada
4. Asignar el objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) configurado a tus celdas deseadas

Este enfoque puede mejorar significativamente la eficiencia de sus aplicaciones y también ahorrar memoria.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Style Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Color, BorderType, CellBorderType } = AsposeCells;

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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet to the workbook
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set value of A1
            cell.value = "Hello Aspose!";

            // Create a new style
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = TextAlignmentType.Center;
            style.horizontalAlignment = TextAlignmentType.Center;

            // Set font color
            style.font.color = Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(BorderType.BottomBorder).color = Color.Red;
            style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Medium;

            // Apply style to A1
            cell.style = style;

            // Apply same style to B1, C1, D1
            worksheet.cells.get("B1").style = style;
            worksheet.cells.get("C1").style = style;
            worksheet.cells.get("D1").style = style;

            // Save workbook to XLS format and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Cómo utilizar los estilos predefinidos de Microsoft Excel 2007**

Si necesita aplicar diferentes estilos de formato para Microsoft Excel 2007, aplique estilos usando la API de Aspose.Cells. A continuación se muestra un ejemplo para demostrar este enfoque de aplicar un estilo predefinido en una celda.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Workbook and Set Cell Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Create a style object.
            const style = workbook.createStyle();

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Input a value to A1 cell.
            cell.putValue("Test");

            // Apply the style to the cell.
            cell.style = style;

            // Saving the Excel 2007 file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



## **Cómo formatear caracteres seleccionados en una celda**

La sección sobre la configuración de fuentes explica cómo formatear texto en las celdas, pero solo explica cómo formatear todo el contenido de la celda. ¿Qué sucede si desea formatear solo caracteres seleccionados?

Aspose.Cells también soporta esta función. Este tema explica cómo usarla de manera efectiva.

### **Cómo formatear caracteres seleccionados**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene la colección [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) que permite acceder a cada hoja en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Cada elemento en la colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

La clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) proporciona el método [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-) que toma los siguientes parámetros para seleccionar un rango de caracteres dentro de una celda:

- **Índice de inicio**, el índice del carácter desde el que comienza la selección.
- **Número de caracteres**, el número de caracteres a seleccionar.

El método [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-) devuelve una instancia de la clase [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) que permite a los desarrolladores formatear los caracteres de la misma manera que una celda, como se muestra en el ejemplo de código. En el archivo generado, en la celda A1, la palabra 'Visit' estará formateada con la fuente por defecto, pero 'Aspose!' en negrita y en azul.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
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
        const { Workbook, SaveFormat } = AsposeCells;

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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the font of selected characters to bold and color to blue
            const charRange = cell.characters(6, 7);
            charRange.font.isBold = true;
            charRange.font.color = AsposeCells.Color.Blue;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Si estás interesado en formatear una porción del Texto Enriquecido en una celda, considera usar los métodos [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) & [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-). El método [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) se usa para acceder a las porciones del texto y luego se pueden hacer modificaciones usando el método [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-), mientras que el método **Get** devuelve un array de objetos [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) que pueden ser manipulados para establecer varias propiedades como nombre de la fuente, color de fuente, negrita, etc., y el método **Set** se puede usar para aplicar los cambios.

{{% /alert %}}

## **Cómo formatear filas y columnas**

A veces, los desarrolladores necesitan aplicar el mismo formato en filas o columnas. Aplicar formato en celdas una por una a menudo lleva más tiempo y no es una buena solución.
Para abordar este problema, Aspose.Cells proporciona una forma simple y rápida discutida en detalle en este artículo.

### **Formato de filas y columnas**

Aspose.Cells proporciona una clase, la [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) que permite acceder a cada hoja en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). La colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) ofrece una colección [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--).

### **Cómo dar formato a una fila**

Cada elemento en la colección [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--) representa un objeto [**Row**](https://reference.aspose.com/cells/javascript-cpp/row). El objeto [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) ofrece el método [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) que se usa para establecer el formato de fila. Para aplicar el mismo formato en una fila, usa el objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Los pasos a continuación muestran cómo usarlo.

1. Añadir un objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) a la clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) llamando a su método [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--).
2. Establecer las propiedades del objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) para aplicar la configuración de formato.
3. Activar los atributos relevantes en el objeto [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).
4. Asignar el objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) configurado al objeto [**Row**](https://reference.aspose.com/cells/javascript-cpp/row).

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
        const { Workbook, SaveFormat } = AsposeCells;

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Adding a new Style to the styles
            const style = workbook.createStyle();

            // Setting the vertical alignment of the text in the "A1" cell
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment of the text in the "A1" cell
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text in the "A1" cell
            style.font.color = AsposeCells.Color.Green;

            // Shrinking the text to fit in the cell
            style.shrinkToFit = true;

            // Setting the bottom border color of the cell to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type of the cell to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Creating StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Accessing a row from the Rows collection
            const row = worksheet.cells.rows.get(0);

            // Assigning the Style object to the Style property of the row
            row.applyStyle(style, styleFlag);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Cómo dar formato a una columna**

La colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) también proporciona una colección [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--). Cada elemento en la colección [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--) representa un objeto [**Column**](https://reference.aspose.com/cells/javascript-cpp/column). Similar a un objeto [**Row**](https://reference.aspose.com/cells/javascript-cpp/row), el objeto [**Column**](https://reference.aspose.com/cells/javascript-cpp/column) también ofrece el método [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) para formatear una columna.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Style and Column Apply Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a new Style to the styles
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Set font color
            style.font.color = AsposeCells.Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Create and configure StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Access first column and apply style
            const column = worksheet.cells.getColumns().get(0);
            column.applyStyle(style, styleFlag);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Style applied to column successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Configuración de alineación](/cells/es/javascript-cpp/cells-alignment-settings/)
- [Configuración de bordes](/cells/es/javascript-cpp/cells-border-settings/)
- [Establecer formatos condicionales de archivos de Excel y ODS.](/cells/es/javascript-cpp/conditional-formatting/)
- [Temas y colores de Excel](/cells/es/javascript-cpp/excel-themes-and-colors/)
- [Configuración de relleno](/cells/es/javascript-cpp/cells-fill-settings/)
- [Configuración de fuente](/cells/es/javascript-cpp/cells-font-settings/)
- [Dar formato a celdas de hoja de cálculo en un libro de trabajo](/cells/es/javascript-cpp/format-worksheet-cells-in-a-workbook/)
- [Implementar el sistema de fechas 1904](/cells/es/javascript-cpp/implement-1904-date-system/)
- [Combinar y descombinar celdas](/cells/es/javascript-cpp/merging-and-unmerging-cells/)
- [Configuración de números](/cells/es/javascript-cpp/cells-number-settings/)
- [Obtener y establecer estilo para celdas](/cells/es/javascript-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)
