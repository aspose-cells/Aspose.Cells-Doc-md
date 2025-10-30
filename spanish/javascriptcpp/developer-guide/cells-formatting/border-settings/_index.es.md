---
title: Configuración de bordes
linktitle: Configuración de bordes
description: Cómo usar la biblioteca Aspose.Cells en JavaScript via C++ para establecer el estilo de borde y el color de las celdas. Ajustando el ancho, estilo y color del borde, tienes más control sobre la apariencia y apariencia de las celdas.
keywords: Aspose.Cells, Configuración de Bordes de Celdas, JavaScript vía C++, Ancho del Borde, Estilo del Borde, Color del Borde
type: docs
weight: 40
url: /es/javascript-cpp/cells-border-settings/
---

## **Añadiendo Bordes a las Celdas**

Microsoft Excel permite a los usuarios dar formato a las celdas agregando bordes. El tipo de borde depende de en qué posición se añada. Por ejemplo, un borde superior se añade en la posición superior de una celda. Los usuarios también pueden modificar el estilo de línea y el color de los bordes.

Con Script Aspose.Cells for JavaScript vía C++, los desarrolladores pueden agregar bordes y personalizar su apariencia de la misma manera flexible que en Microsoft Excel.

### **Añadiendo Bordes a las Celdas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) proporciona la colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Cada elemento en la colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Aspose.Cells proporciona la propiedad [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) en la clase [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). La [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) se usa para establecer el estilo de formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) ofrece propiedades para agregar bordes a las celdas.

#### **Añadir bordes a una celda**

Los desarrolladores pueden agregar bordes a una celda usando la colección [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) del objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). El tipo de borde se pasa como índice a la colección [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--). Todos los tipos de borde están predefinidos en la enumeración [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype).

**Enumeración de Bordes**

|**Tipos de Bordes**|**Descripción**|
| :- | :- |
|BottomBorder|Una línea de borde inferior|
|DiagonalDown|Una línea diagonal de la esquina superior izquierda a la esquina inferior derecha|
|DiagonalUp|Una línea diagonal de la esquina inferior izquierda a la esquina superior derecha|
|LeftBorder|Una línea de borde izquierda|
|RightBorder|Una línea de borde derecha|
|TopBorder|Una línea de borde superior|

La colección [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) almacena todos los bordes. Cada borde en la colección [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) está representado por un objeto [**Border**](https://reference.aspose.com/cells/javascript-cpp/border) que proporciona dos propiedades, [**color**](https://reference.aspose.com/cells/javascript-cpp/border/#color-color-) y [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) para establecer el color de línea del borde y su estilo respectivamente.

Para establecer el color de línea de un borde, selecciona un color usando la enumeración Color (parte de JavaScript) y asígnalo a la propiedad color del objeto Border.

El estilo de línea del borde se establece seleccionando un estilo de línea de la enumeración [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype).

**Enumeración de Tipo de Bordes de Celda**

|**Estilos de Línea**|**Descripción**|
| :- | :- |
|DashDot|Línea fina con guiones y puntos|
|DashDotDot|Línea fina con guiones y puntos y puntos|
|Dashed|Línea discontinua|
|Dotted|Línea punteada|
|Double|Línea doble|
|Hair|Línea fina|
|MediumDashDot|Línea medianamente punteada|
|MediumDashDotDot|Línea mediana punto-punteada|
|MediumDashed|Línea mediana punteada|
|None|Sin línea|
|Medium|Línea mediana|
|SlantedDashDot|Línea oblicua medianamente punteada|
|Thick|Línea gruesa|
|Thin|Línea delgada|
Seleccione uno de los estilos de línea y luego asignarlo a la propiedad [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) del objeto [**Border**](https://reference.aspose.com/cells/javascript-cpp/border).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Borders to A1 Cell Example</h1>
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
            // This example creates a new workbook and adds borders to cell A1.
            // No try/catch is used so errors propagate for testing.

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Create a style object
            const style = cell.style;

            // Setting the line style and color of the top border
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the bottom border
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the left border
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the right border
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;

            // Apply the border styles to the cell
            cell.style = style;

            // Saving the Excel file
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

{{% alert color="primary" %}}
Debe configurar tanto el estilo de línea como el color al mismo tiempo. Las dos líneas diagonales del borde deben tener el mismo estilo y color.
{{% /alert %}}

#### **Agregar bordes a un rango de celdas**

También es posible agregar bordes a un rango de celdas en lugar de solo a una celda. Para ello, primero cree un rango de celdas llamando al método [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) de la colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Toma los siguientes parámetros:

- Primera fila, la primera fila del rango.
- Primera columna, representa la primera columna del rango.
- Número de filas, el número de filas en el rango.
- Número de columnas, el número de columnas en el rango.

El método [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) devuelve un objeto [**Range**](https://reference.aspose.com/cells/javascript-cpp/range), que contiene el rango de celdas especificado. El objeto [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) proporciona un método [**outlineBorder**](https://reference.aspose.com/cells/javascript-cpp/range/#outlineBorder-bordertype-cellbordertype-cellscolor-) que toma los siguientes parámetros para agregar un borde al rango de celdas:

- **Tipo de borde**, el tipo de borde, seleccionado de la enumeración [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype).
- **Estilo de línea**, el estilo de línea del borde, seleccionado de la enumeración [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype).
- **Color**, el color de línea, seleccionado de la enumeración Color.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Apply Borders</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, writes to A1, creates a range and applies borders, then offers the file for download.
            const workbook = new Workbook();

            const worksheet = workbook.worksheets.get(0);

            const cell = worksheet.cells.get("A1");

            cell.putValue("Hello World From Aspose");

            const range = worksheet.cells.createRange(0, 0, 1, 3);

            // Applying borders using property assignment conversions for setter methods
            range.outlineBorder = [BorderType.TopBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.BottomBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.LeftBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.RightBorder, CellBorderType.Thick, Color.Blue];

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and borders applied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
