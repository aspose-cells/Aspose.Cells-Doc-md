---
title: Configuración de relleno
linktitle: Configuración de relleno
description: Aprende a personalizar los ajustes de relleno, fondo y estilo de las celdas utilizando la biblioteca Aspose.Cells para JavaScript vía C++.
keywords: Aspose.Cells, Celdas, Configuración de Relleno, Fondo, Estilo, JavaScript vía C++
type: docs
weight: 50
url: /es/javascript-cpp/cells-fill-settings/
---

## **Colores y patrones de fondo**

Microsoft Excel puede establecer los colores de primer plano (contorno) y fondo (relleno) de las celdas y los patrones de fondo.

Aspose.Cells también admite estas características de manera flexible. En este tema, aprenderemos a usar estas características utilizando Aspose.Cells.

### **Estableciendo colores y patrones de fondo**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Cada elemento en la colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

La [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) tiene la propiedad [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) que se usa para obtener y establecer el formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) proporciona propiedades para configurar los colores de primer plano y fondo de las celdas. Aspose.Cells ofrece una enumeración [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype) que contiene un conjunto de tipos predefinidos de patrones de fondo que se muestran a continuación.

|**Patrones de fondo**|**Descripción**|
| :- | :- |
|DiagonalCrosshatch|Representa un patrón de entrecruzado diagonal|
|DiagonalStripe|Representa un patrón de rayas diagonales|
|Gray6|Representa un patrón gris del 6.25%|
|Gray12|Representa un patrón gris del 12.5%|
|Gray25|Representa un patrón gris del 25%|
|Gray50|Representa un patrón gris del 50%|
|Gray75|Representa un patrón gris del 75%|
|HorizontalStripe|Representa un patrón de rayas horizontales|
|None|Representa ningún fondo|
|ReverseDiagonalStripe|Representa un patrón de rayas diagonales inversas|
|Solid|Representa un patrón sólido|
|ThickDiagonalCrosshatch|Representa un patrón de entrecruzado diagonal grueso|
|ThinDiagonalCrosshatch|Representa un patrón de entrecruzado diagonal delgado|
|ThinDiagonalStripe|Representa un patrón de rayas diagonales delgado|
|ThinHorizontalCrosshatch|Representa un patrón de entrecruzado horizontal delgado|
|ThinHorizontalStripe|Representa un patrón de rayas horizontales delgado|
|ThinReverseDiagonalStripe|Representa un patrón de rayas diagonales inversas delgado|
|ThinVerticalStripe|Representa un patrón de rayas verticales delgado|
|VerticalStripe|Representa un patrón de rayas verticales|

En el ejemplo a continuación, el color de primer plano de la celda A1 está establecido pero A2 está configurada para tener tanto el color de primer plano como el color de fondo con un patrón de fondo de rayas verticales.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Define a Style and get the A1 cell style
            let style = worksheet.cells.get("A1").style;

            // Setting the foreground color to yellow
            style.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A1 cell
            worksheet.cells.get("A1").style = style;

            // Get the A2 cell style
            style = worksheet.cells.get("A2").style;

            // Setting the foreground color to blue
            style.foregroundColor = AsposeCells.Color.Blue;

            // Setting the background color to yellow
            style.backgroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A2 cell
            worksheet.cells.get("A2").style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```


### **Importante saber**

{{% alert color="primary" %}}

- Para establecer el color de primer plano o de fondo de una celda, utilice las propiedades [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) o [**backgroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundColor-color-) del objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Ambos tendrán efecto solo si la propiedad [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) del objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) está configurada.
- La propiedad [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) establece el color de sombra de la celda. La propiedad [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) especifica el tipo de patrón de fondo utilizado para el color de primer plano o fondo. Aspose.Cells proporciona una enumeración, [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype), que contiene un conjunto de tipos predefinidos de patrones de fondo.
- Si selecciona el valor *BackgroundType.None* en la enumeración [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype), el color de primer plano no se aplica. Asimismo, el color de fondo no se aplica si selecciona los valores *BackgroundType.None* o *BackgroundType.Solid*.
- Al recuperar el color de sombreado de la celda, si [**style.pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) es *BackgroundType.None*, [**style.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor--) devolverá *Color.Empty*.

{{% /alert %}}

### **Aplicar efectos de relleno de degradado**

Para aplicar efectos de relleno de gradiente deseados a la celda, use la propiedad [**twoColorGradient**](https://reference.aspose.com/cells/javascript-cpp/style/#twoColorGradient-color-color-gradientstyletype-number-) del objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) en consecuencia.

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
        const { Workbook, SaveFormat, Color, GradientStyleType, TextAlignmentType } = AsposeCells;

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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.get(2, 1).putValue("test");

            const style = worksheet.cells.get("B3").style;

            style.isGradient = true;
            style.twoColorGradient = [ new Color(255, 255, 255), new Color(79, 129, 189), GradientStyleType.Horizontal, 1 ];
            style.font.color = Color.Red;
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            worksheet.cells.get("B3").style = style;

            worksheet.cells.rowHeightPixel = [2, 53];

            worksheet.cells.merge(2, 1, 1, 2);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Colores y paleta**

Una paleta es el número de colores disponibles para utilizar en la creación de una imagen. El uso de una paleta estandarizada en una presentación permite al usuario crear un aspecto consistente. Cada archivo de Microsoft Excel (97-2003) tiene una paleta de 56 colores que se pueden aplicar a celdas, fuentes, líneas de cuadrícula, objetos gráficos, rellenos y líneas en un gráfico.

Con Aspose.Cells es posible no solo utilizar los colores existentes de la paleta, sino también colores personalizados. Antes de utilizar un color personalizado, agréguelo primero a la paleta.

Este tema trata sobre cómo agregar colores personalizados a la paleta.

### **Agregar colores personalizados a la paleta**

Aspose.Cells soporta la paleta de colores de Microsoft Excel con 56 colores. Para utilizar un color personalizado que no está definido en la paleta, agregue el color a la paleta.

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) proporciona un método [**changePalette**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-) que recibe los siguientes parámetros para agregar un color personalizado y modificar la paleta:

- Color personalizado, el color personalizado que se agregará.
- Índice, el índice del color en la paleta que el color personalizado reemplazará. Debe estar entre 0-55.

El siguiente ejemplo agrega un color personalizado (Orchid) a la paleta antes de aplicarlo a una fuente.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(AsposeCells.Color.Orchid, 55);

            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining new Style object
            const styleObject = workbook.createStyle();
            // Setting the Orchid (custom) color to the font
            styleObject.font.color = workbook.colors[55];

            // Applying the style to the cell
            cell.style = styleObject;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

La paleta solo contiene 56 colores. Cuando agrega un color personalizado a la paleta, la paleta cambia y cualquier elemento en el archivo formateado con el color anterior cambia. Por lo tanto, tenga mucho cuidado al cambiar la paleta. Además, esta es una limitación solo en el formato de archivo XLS (Excel 97 - 2003) ya que no hay tal limitación para formatos de archivo XLSX o más avanzados de MS Excel (2007/2010 o 2013).

{{% /alert %}}
