---
title: Insertar imágenes y formas en archivos de Excel con JavaScript a través de C++  
linktitle: Formas  
type: docs  
weight: 140  
url: /es/javascript-cpp/insert-shapes/  
description: Gestionar imágenes, objetos OLE y formas en archivos de Excel usando Aspose.Cells for JavaScript a través de C++.  
---  

{{% alert color="primary" %}}  
A veces necesitas insertar algunas formas necesarias en la hoja de cálculo. Es posible que necesites insertar la misma forma en diferentes posiciones de la hoja. O que necesites insertar en lote formas en la hoja.  
¡No te preocupes! [Aspose.Cells](https://products.aspose.com/cells/) soporta todas estas operaciones.  
{{% /alert %}}  

Las formas en Excel se dividen principalmente en los siguientes tipos:  
- **Imágenes**  
- **OleObjects**  
- **Líneas**  
- **Rectángulos**  
- **Formas Básicas**  
- **Flechas en Bloque**  
- **Formas de Ecuaciones**  
- **Diagramas de Flujo**  
- **Estrellas y Banderas**  
- **Llamadas**  

Este documento guía seleccionará una o dos formas de cada tipo para hacer muestras. A través de estos ejemplos, aprenderá cómo usar [Aspose.Cells](https://products.aspose.com/cells/) para insertar la forma especificada en la hoja de cálculo.  

## **Agregar imágenes en la hoja de cálculo de Excel usando JavaScript**  

Agregar imágenes a una hoja de cálculo es muy fácil. Solo toma unas pocas líneas de código:  
Simplemente llama al método [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-) de la colección [**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection) (encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). El método [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-) toma los siguientes parámetros:  

- **Índice de fila superior izquierda**, el índice de la fila superior izquierda.  
- **Índice de columna superior izquierda**, el índice de la columna superior izquierda.  
- **Nombre del archivo de imagen**, el nombre del archivo de imagen, completo con la ruta.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Picture to Workbook Example</h1>
        <p>
            Optional: select an existing Excel file to modify, or leave empty to create a new workbook.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>
            Select an image to insert into the worksheet (required):
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // If an Excel file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const arrayBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Add a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read the selected image file as Uint8Array
            const imageFile = imageInput.files[0];
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(imageArrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            worksheet.pictures.add(5, 5, imageBytes);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Insertar objetos OLE en la hoja de cálculo de Excel usando JavaScript**  

Aspose.Cells soporta agregar, extraer y manipular objetos OLE en hojas de cálculo. Por esta razón, Aspose.Cells tiene la clase [**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection), utilizada para agregar un nuevo objeto OLE a la lista de colección. Otra clase, [**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject), representa un objeto OLE. Tiene algunos miembros importantes:  

- La propiedad [**OleObject.imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--) especifica los datos de la imagen (ícono) de tipo arreglo de bytes. La imagen se mostrará para mostrar el objeto OLE en la hoja de cálculo.  
- La propiedad [**OleObject.objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--) especifica los datos del objeto en forma de un arreglo de bytes. Estos datos se mostrarán en su programa relacionado cuando hagas doble clic en el ícono del objeto OLE.  

El siguiente ejemplo muestra cómo agregar un objeto(s) OLE a una hoja de cálculo.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Insert OLE Object Example</h1>
        <p>
            Select an image to display as the OLE object's icon and an Excel file to embed as the OLE object.
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <input type="file" id="excelInput" accept=".xls,.xlsx" />
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
            const imageInput = document.getElementById('imageInput');
            const excelInput = document.getElementById('excelInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file for the OLE icon.</p>';
                return;
            }
            if (!excelInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file to embed.</p>';
                return;
            }

            const imageFile = imageInput.files[0];
            const excelFile = excelInput.files[0];

            // Read files as ArrayBuffers
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const excelArrayBuffer = await excelFile.arrayBuffer();

            // Convert to Uint8Array for Aspose.Cells
            const imageData = new Uint8Array(imageArrayBuffer);
            const objectData = new Uint8Array(excelArrayBuffer);

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Add an Ole object into the worksheet with the image shown in MS Excel.
            sheet.oleObjects.add(14, 3, 200, 220, imageData);

            // Set embedded ole object data.
            sheet.oleObjects.get(0).objectData = objectData;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">OLE object embedded successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Insertar una línea en la hoja de Excel usando JavaScript**  

La forma de la línea pertenece a la categoría **líneas**.  

*  

- Selecciona la celda donde deseas insertar la línea  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona la línea de 'Formas usadas recientemente' o 'Líneas'  

![](line.png)  

***Usando Aspose.Cells***  

Puedes utilizar el siguiente método para insertar una línea en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
El método devuelve un objeto [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar una línea en una hoja de cálculo.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Line Example</h1>
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
            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Create workbook from uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Access first worksheet from the collection
                const sheet = workbook.worksheets.get(0);

                // Add the line to the worksheet
                sheet.shapes.addLine(2, 0, 2, 0, 100, 300);

                // Save workbook to XLSX format and create download link
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'sample.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Line added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](line2.png)  

## **Insertar una flecha de línea en la hoja de Excel usando JavaScript**  

La forma de la flecha de línea pertenece a la categoría **Líneas**. Es un caso especial de línea.  

*  

- Seleccione la celda donde desea insertar la flecha de línea  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona la flecha de línea de 'Formas usadas recientemente' o 'Líneas'  

![](line_arrow1.png)  

***Usando Aspose.Cells***  

Puede utilizar el siguiente método para insertar una flecha de línea en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
El método devuelve un objeto [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar una flecha de línea en una hoja de cálculo.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Line Arrow Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains shapes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the line arrow to the worksheet
            let s = sheet.shapes.addLine(2, 0, 2, 0, 100, 300); // method 1
            // let s = sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
            // let s = sheet.shapes.addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

            // add a arrow at the line begin
            s.line.beginArrowheadStyle = AsposeCells.MsoArrowheadStyle.Arrow; // arrow type
            s.line.beginArrowheadWidth = AsposeCells.MsoArrowheadWidth.Wide; // arrow width
            s.line.beginArrowheadLength = AsposeCells.MsoArrowheadLength.Short; // arrow length

            // add a arrow at the line end
            s.line.endArrowheadStyle = AsposeCells.MsoArrowheadStyle.ArrowOpen; // arrow type
            s.line.endArrowheadWidth = AsposeCells.MsoArrowheadWidth.Narrow; // arrow width
            s.line.endArrowheadLength = AsposeCells.MsoArrowheadLength.Long; // arrow length

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.with_arrow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Arrow';

            document.getElementById('result').innerHTML = '<p style="color: green;">Arrow added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](line_arrow2.png)  

## **Insertar un rectángulo en la hoja de Excel usando JavaScript**  

La forma del rectángulo pertenece a la categoría **Rectángulos**.  

*  

- Selecciona la celda donde deseas insertar el rectángulo  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona el rectángulo de 'Formas usadas recientemente' o 'Rectángulos'  

![](rectangle.png)  

***Usando Aspose.Cells***  

Puedes utilizar el siguiente método para insertar un rectángulo en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
El método devuelve un objeto [RectangleShape](https://reference.aspose.com/cells/javascript-cpp/rectangleshape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar un rectángulo en una hoja de cálculo.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Rectangle</title>
    </head>
    <body>
        <h1>Add Rectangle to Worksheet</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the rectangle to the worksheet
            sheet.shapes.addRectangle(2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Rectangle added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](rectangle2.png)  

## **Insertar un cubo en la hoja de Excel usando JavaScript**  

La forma del cubo pertenece a la categoría **Formas Básicas**.  

*  

- Selecciona la celda donde deseas insertar el cubo  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona el Cubo en **Formas Básicas**  

![](cube.png)  

***Usando Aspose.Cells***  

Puede utilizar el siguiente método para insertar un cubo en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
El método devuelve un objeto [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar un cubo en una hoja de cálculo.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Cube</title>
    </head>
    <body>
        <h1>Add Cube to Worksheet</h1>
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
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the cube to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Cube added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](cube2.png)  

## **Insertar una llamada de cuádruple flecha en la hoja de Excel usando JavaScript**  

La forma de la flecha de cuadro de llamada pertenece a la categoría **Flechas de Bloques**.  

*  

- Seleccione la celda donde desea insertar la flecha de cuadro de referencia  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona la flecha de cuadro de llamada en **Flechas de Bloques**  

![](callout_quad_arrow.png)  

***Usando Aspose.Cells***  

Puede utilizar el siguiente método para insertar una flecha de cuadro de referencia en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
El método devuelve un objeto [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar una flecha de cuadro de llamada en una hoja de cálculo.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Callout Quad Arrow</title>
    </head>
    <body>
        <h1>Add Callout Quad Arrow Shape</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const sheet = workbook.worksheets.get(0);

            sheet.shapes.addAutoShape(AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](callout_quad_arrow2.png)  

## **Insertar un signo de multiplicación en la hoja de cálculo de Excel usando JavaScript**  

La forma del signo de multiplicación pertenece a la categoría **Formas de Ecuación**.  

*  

- Seleccione la celda donde desea insertar el signo de multiplicación  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona el signo de multiplicación en **Formas de Ecuación**  

![](multiplication_sign.png)  

***Usando Aspose.Cells***  

Puede utilizar el siguiente método para insertar un signo de multiplicación en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
El método devuelve un objeto [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar un signo de multiplicación en una hoja de cálculo.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Multiply Sign</title>
    </head>
    <body>
        <h1>Add Multiplication Sign to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multiplication sign to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Multiplication sign added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](multiplication_sign2.png)  

## **Insertar un documento multidocumento en la hoja de cálculo de Excel usando JavaScript**  

La forma del multidocumento pertenece a la categoría **Diagramas de Flujo**.  

*  

- Seleccione la celda donde desea insertar el multidocumento  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona el multidocumento en **Diagramas de Flujo**  

![](multidocument.png)  

***Usando Aspose.Cells***  

Puedes usar el siguiente método para insertar un multidocumento en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
El método devuelve un objeto [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar un multidocumento en una hoja de cálculo.  

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
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multidocument to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](multidocument2.png)  

## **Insertar una estrella de cinco puntas en la hoja de cálculo de Excel usando JavaScript**  

La forma de la estrella de cinco puntas pertenece a la categoría **Estrellas y Banderas**.  

*  

- Selecciona la celda donde desees insertar la estrella de cinco puntas  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona la estrella de cinco puntas en **Estrellas y Banderas**  

![](star_5_points.png)  

***Usando Aspose.Cells***  

Puedes usar el siguiente método para insertar una estrella de cinco puntas en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
El método devuelve un objeto [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar una estrella de cinco puntas en una hoja de cálculo.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Star Shape</title>
    </head>
    <body>
        <h1>Add Five-Pointed Star to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Add the Five-pointed star to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Star shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](star_5_points2.png)  

## **Insertar una burbuja de pensamiento en la hoja de cálculo de Excel usando JavaScript**  

La forma de la nube de burbuja de pensamiento pertenece a la categoría **Comentarios**.  

*  

- Seleccione la celda donde desea insertar el globo de pensamiento  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona la nube de burbuja de pensamiento en **Comentarios**  

![](thought_bubble_cloud.png)  

***Usando Aspose.Cells***  

Puede utilizar el siguiente método para insertar un globo de pensamiento en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
El método devuelve un objeto [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar una nube de burbujas en un globo de pensamiento en una hoja de cálculo.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Cloud Callout Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the thought bubble cloud to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cloud callout added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](thought_bubble_cloud2.png)  

## **Temas avanzados**  
- [Cambiar los valores de ajuste de la forma](/cells/es/javascript-cpp/change-adjustment-values-of-the-shape/)  
- [Copiar formas entre hojas de cálculo](/cells/es/javascript-cpp/copy-shapes-between-worksheets/)  
- [Datos en Forma No Primitiva](/cells/es/javascript-cpp/data-in-non-primitive-shape/)  
- [Encontrar la Posición Absoluta de la Forma dentro de la Hoja de Trabajo](/cells/es/javascript-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [Obtener Puntos de Conexión de la Forma](/cells/es/javascript-cpp/get-connection-points-from-shape/)  
- [Gestionar Controles](/cells/es/javascript-cpp/managing-controls/)  
- [Agregar Iconos a la Hoja de Trabajo](/cells/es/javascript-cpp/insert-svg-to-excel/)  
- [Gestionar Objetos OLE](/cells/es/javascript-cpp/managing-ole-objects/)  
- [Gestionar Imágenes](/cells/es/javascript-cpp/managing-pictures/)  
- [Gestionar SmartArt](/cells/es/javascript-cpp/managing-smartart/)  
- [Gestionar Cuadro de Texto](/cells/es/javascript-cpp/managing-textbox-of-excel/)  
- [Agregar WordArt como Marca de Agua a la Hoja de Trabajo](/cells/es/javascript-cpp/add-wordart-watermark-to-worksheet/)  
- [Actualizar Valores de Formas Vinculadas](/cells/es/javascript-cpp/refresh-values-of-linked-shapes/)  
- [Enviar Forma al Frente o Atrás Dentro de la Hoja de Trabajo](/cells/es/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [Gestionar Opciones de la Forma](/cells/es/javascript-cpp/managing-shape-options/)  
- [Gestionar Opciones de Texto de la Forma](/cells/es/javascript-cpp/managing-shape-text-options/)  
- [Extensiones Web - Complementos de Office](/cells/es/javascript-cpp/web-extensions-office-add-ins/)
