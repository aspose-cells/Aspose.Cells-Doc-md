---
title: Insertar una imagen en una celda
linktitle: Insertar una imagen en una celda
description: Aspose.Cells for JavaScript via C++ es una biblioteca para trabajar con archivos de hoja de cálculo. Este artículo explica cómo ajustar una imagen exactamente a una sola celda, ya sea colocando una imagen flotante sobre la celda o incrustando la imagen directamente en la celda.
keywords: Aspose.Cells, biblioteca JavaScript via C++, hoja de cálculo, insertar imagen, incrustar imagen, imagen en una celda, ajustar una imagen a una celda, Pictures, EmbeddedImage
type: docs
weight: 80
url: /es/javascript-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece dos maneras distintas de asociar una imagen con una sola celda. Una imagen flotante es una forma situated en la capa de dibujo de la hoja de cálculo que se superpone visualmente a un rango de celdas, mientras que una imagen incrustada se almacena dentro de la celda en sí y se escala automáticamente al área de visualización de la celda. Elija el enfoque que mejor se adapte a sus requisitos de diseño.
{{% /alert %}}

## **Introducción**
Ajustar una imagen exactamente a una sola celda es un requisito común al diseñar hojas de cálculo que funcionan como informes visuales, catálogos de productos, directorios de empleados, paneles de control o listas de inventario. En lugar de estirar una imagen por varias celdas o colocarla sin ajustarla en una hoja de cálculo, es posible que necesite una imagen limpia y vinculada a la celda que permanezca alineada con la celda que la contiene.
Aspose.Cells admite este escenario de dos maneras complementarias:
- **Enfoque 1: colocar una imagen flotante sobre una celda.** Agregue un `Picture` a la hoja de cálculo, establezca su colocación mediante `picture.setPlacement(PlacementType.MoveAndSize)` y ajuste sus celdas de anclaje mediante `picture.setUpperLeftRow()`, `picture.setUpperLeftColumn()`, `picture.setLowerRightRow()` y `picture.setLowerRightColumn()` para que la imagen cubra exactamente una celda.
- **Enfoque 2: incrustar una imagen directamente en una celda.** Asigne a la celda un `Buffer` que contenga los datos de la imagen mediante `cell.setEmbeddedImage(imageBuffer)`. La imagen se escala automáticamente para ajustarse al área de visualización de la celda y permanece vinculada a ella.
El resto de este artículo explica ambos enfoques, describe las API pertinentes y muestra cómo utilizarlos en código.

## **Enfoque 1: colocar una imagen sobre una celda**
Una imagen flotante es un objeto `Picture` que reside en la capa de dibujo de la hoja de cálculo. Aunque no forma parte de ninguna celda en concreto, está anclada a un rango de celdas. Las celdas de anclaje de la imagen —sus esquinas superior izquierda e inferior derecha— determinan su extensión visual en la hoja de cálculo. De forma predeterminada, una imagen recién agregada abarca varias celdas.
Para hacer que una imagen flotante cubra **exactamente una celda**, debe:
1. Agregar la imagen mediante `worksheet.getPictures().add(row, column, imageBuffer)`, donde `imageBuffer` es un `Buffer` que contiene los datos de la imagen. Esto ancla la nueva imagen a la celda especificada.
2. Establecer los cuatro valores de anclaje para que el rectángulo delimitador de la imagen coincida con la celda de destino.
3. Llamar a `picture.setPlacement(PlacementType.MoveAndSize)` para que la imagen se mueva y cambie de tamaño junto con la celda subyacente cuando el usuario modifique el ancho de la columna o la altura de la fila.

### **Anclar la imagen a una sola celda**
El anclaje de la imagen se define mediante cuatro accesores de índice con base cero:
- `picture.getUpperLeftRow()` y `picture.setUpperLeftRow(value)`: el índice de fila del borde superior de la imagen.
- `picture.getUpperLeftColumn()` y `picture.setUpperLeftColumn(value)`: el índice de columna del borde izquierdo de la imagen.
- `picture.getLowerRightRow()` y `picture.setLowerRightRow(value)`: el índice de fila del borde inferior de la imagen. Para que el borde inferior de la imagen coincida con la parte inferior de la fila `r`, establezca este valor en `r + 1`.
- `picture.getLowerRightColumn()` y `picture.setLowerRightColumn(value)`: el índice de columna del borde derecho de la imagen. Para que el borde derecho de la imagen coincida con el lado derecho de la columna `c`, establezca este valor en `c + 1`.

{{% alert color="primary" %}}
Los índices de fila y columna en Aspose.Cells tienen **base cero**. La celda C6 tiene el índice de fila 5 y el índice de columna 2. Los errores de una unidad en el anclaje inferior derecho son la causa más común de imágenes que parecen invadir una celda adyacente.
{{% /alert %}}

### **Controlar el comportamiento de colocación**
`picture.getPlacement()` y `picture.setPlacement(value)` utilizan el enum `PlacementType` para controlar cómo se comporta la imagen cuando el usuario cambia el tamaño de la fila o la columna que se encuentra debajo. El valor recomendado para una imagen de una sola celda es `PlacementType.MoveAndSize`, que hace que la imagen se mueva y cambie de tamaño junto con la celda subyacente, conservando el ajuste exacto.

### **Instrucciones paso a paso**
1. Cree un nuevo `Workbook` o abra uno existente.
2. Acceda a la `Worksheet` de destino mediante `workbook.getWorksheets().getAt(0)`.
3. Lea el archivo de imagen del disco en un `Buffer`, por ejemplo utilizando `fs.readFileSync` de Node.js.
4. Llame a `worksheet.getPictures().add(5, 2, imageBuffer)` para agregar una imagen anclada a la celda C6. El método devuelve el índice de la nueva imagen en la colección `Pictures`; utilícelo para recuperar el `Picture` correspondiente.
5. Establezca las cuatro coordenadas de anclaje para que la imagen cubra únicamente la celda C6: `picture.setUpperLeftRow(5)`, `picture.setUpperLeftColumn(2)`, `picture.setLowerRightRow(6)` y `picture.setLowerRightColumn(3)`.
6. Llame a `picture.setPlacement(PlacementType.MoveAndSize)` para mantener la imagen alineada con C6 cuando se cambie el tamaño de la columna o de la fila.
7. Opcionalmente, agregue texto de ejemplo a las celdas circundantes para demostrar que solo la celda C6 contiene la imagen.
8. Guarde el libro de trabajo en el disco como un archivo `.xlsx`.
El siguiente código demuestra el enfoque completo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,image/png" />
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
            const fileInput = document.getElementById('fileInput');
            const file = fileInput.files[0];
            if (!file) {
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Please select a PNG image.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const imageData = new Uint8Array(await file.arrayBuffer());
            const picIndex = worksheet.pictures.add(5, 2, imageData);
            const picture = worksheet.pictures.get(picIndex);
            picture.upperLeftRow = 5;
            picture.upperLeftColumn = 2;
            picture.lowerRightRow = 6;
            picture.lowerRightColumn = 3;
            picture.placement = AsposeCells.Drawing.PlacementType.MoveAndSize;
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Enfoque 2: incrustar una imagen directamente en una celda**
Aspose.Cells también ofrece un mecanismo más sencillo para las imágenes vinculadas a celdas: el método `cell.setEmbeddedImage(imageBuffer)`. Al asignar los datos de la imagen con este método, la imagen se adjunta a la celda en sí, como si fuera contenido en línea.

### **Cómo funcionan las imágenes incrustadas**
- La imagen se almacena como parte del contenido de la celda, no como una forma en la capa de dibujo.
- La imagen se escala automáticamente para ajustarse dentro de los límites de representación de la celda. No se requieren coordenadas de anclaje ni configuraciones de colocación.
- La celda sigue siendo una celda real con una dirección real que puede ser referenciada por fórmulas, ordenarse como parte de una fila o utilizarse en otras operaciones a nivel de celda.
Esto hace que `cell.setEmbeddedImage(imageBuffer)` sea la opción más concisa cuando el objetivo es simplemente «incluir una imagen dentro de esta celda».

### **Instrucciones paso a paso**
1. Cree un nuevo `Workbook` o abra uno existente.
2. Acceda a la `Worksheet` de destino mediante `workbook.getWorksheets().getAt(0)`.
3. Lea el archivo de imagen del disco en un `Buffer`, por ejemplo utilizando `fs.readFileSync` de Node.js.
4. Obtenga una referencia a la celda de destino mediante `worksheet.getCells().get("C6")` o `worksheet.getCells().get(5, 2)`.
5. Pase el `Buffer` a la celda mediante `cell.setEmbeddedImage(imageBuffer)`.
6. Opcionalmente, ajuste el alto de la fila y el ancho de la columna de destino para dar a la imagen incrustada una apariencia más destacada.
7. Guarde el libro de trabajo en el disco como un archivo `.xlsx`.
El siguiente código demuestra el enfoque completo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,.jpg,.jpeg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const asposeReady = AsposeCells.onReady({
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
            if (!fileInput.files || fileInput.files.length === 0) {
                result.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Obtener la celda de destino C6
            const cell = worksheet.cells.get("C6");
            // Leer el archivo de imagen en un array de bytes
            const imageData = new Uint8Array(await fileInput.files[0].arrayBuffer());
            // Incrustar la imagen directamente en la celda
            cell.embeddedImage = imageData;
            // Opcionalmente, ajustar la altura de fila y el ancho de columna para que la imagen incrustada sea más visible
            worksheet.cells.setColumnWidth(2, 30); // Columna C (índice 2)
            worksheet.cells.setRowHeight(5, 100); // Fila 6 (índice 5)
            // Guardar el libro de trabajo resultante como un archivo .xlsx
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Elección del enfoque correcto**
Ambos enfoques producen una imagen que cabe dentro de una sola celda, pero difieren en la forma en que se almacena y se comporta:
- **Utilice una imagen flotante (Enfoque 1) cuando:**
  - Necesite un control más preciso sobre la colocación, las capas o la alineación con otros objetos de dibujo.
  - Desee que la imagen se comporte como una forma que pueda seleccionarse, reordenarse o agruparse con otras formas.
  - Necesite compatibilidad con código heredado que ya funciona con la colección `Pictures`, a la que se accede mediante `worksheet.getPictures()`.
  - Necesite calcular dinámicamente las coordenadas de anclaje según la distribución de la hoja de cálculo.
- **Utilice una imagen incrustada (Enfoque 2) cuando:**
  - Desee realizar la inserción de una imagen en una celda de la manera más sencilla posible.
  - La imagen deba permanecer vinculada a la celda como cualquier otro contenido de celda.

## Artículos relacionados
- [Cámara de Excel en Aspose.Cells for JavaScript via C++](/cells/es/javascript-cpp/excel-camera/)

{{< app/cells/assistant language="javascript-cpp" >}}