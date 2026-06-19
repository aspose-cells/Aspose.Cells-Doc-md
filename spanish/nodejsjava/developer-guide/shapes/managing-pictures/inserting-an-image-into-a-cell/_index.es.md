---
title: Insertar una imagen en una celda
description: Aspose.Cells es una biblioteca de Node.js vía Java para trabajar con archivos de hojas de cálculo. Este artículo explica cómo ajustar una imagen exactamente al tamaño de una sola celda utilizando dos enfoques diferentes: colocar una imagen flotante sobre la celda o incrustar la imagen directamente en la celda.
keywords: Aspose.Cells, biblioteca Node.js vía Java, hoja de cálculo, insertar imagen, incrustar imagen, imagen en celda, ajustar imagen a celda, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /es/nodejs-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells ofrece dos formas distintas de asociar una imagen con una sola celda. Una imagen flotante es una forma en la capa de dibujo de la hoja de cálculo que se superpone visualmente a un rango de celdas, mientras que una imagen incrustada se almacena dentro de la propia celda y se escala automáticamente al área de visualización de la celda. Elija el enfoque que mejor se adapte a sus requisitos de diseño.

{{% /alert %}}

## **Introducción**

Ajustar una imagen exactamente a una sola celda es un requisito común al diseñar hojas de cálculo que actúan como informes visuales, catálogos de productos, directorios de empleados, paneles de control o listas de inventario. En lugar de estirar una imagen a través de muchas celdas o colocarla de forma suelta en una hoja de cálculo, es posible que desee una imagen limpia y vinculada a la celda que permanezca alineada con la celda a la que pertenece.

Aspose.Cells admite este escenario de dos formas complementarias:

- **Enfoque 1 — Colocar una imagen flotante sobre una celda.** Agregue una `Picture` a la hoja de cálculo, establezca su `Placement` en `MoveAndSize`, y ajuste las celdas de anclaje (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) para que la imagen cubra exactamente una celda.
- **Enfoque 2 — Incrustar una imagen directamente en una celda.** Asigne bytes de imagen a la propiedad `EmbeddedImage` de la celda. La imagen se escala automáticamente para ajustarse al área de visualización de la celda y se desplaza con ella.

El resto de este artículo recorre ambos enfoques, explica las API relevantes y muestra cómo utilizarlos en código.

## **Enfoque 1: Colocar una imagen sobre una celda**

Una imagen flotante es un objeto `Picture` que reside en la capa de dibujo de la hoja de cálculo. Aunque no forma parte de ninguna celda individual, está anclada a un rango de celdas. Las celdas de anclaje de la imagen — sus esquinas superior izquierda e inferior derecha — determinan su extensión visual en la hoja de cálculo. Por defecto, una imagen recién agregada abarca varias celdas.

Para que una imagen flotante cubra **exactamente una celda**, necesita:

1. Agregar la imagen usando `worksheet.getPictures().add(int row, int column, InputStream stream)`, que ancla la nueva imagen a la celda indicada.
2. Establecer las cuatro propiedades de anclaje para que el rectángulo delimitador de la imagen coincida con la celda de destino.
3. Establecer `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` para que la imagen se mueva y se redimensione con la celda subyacente cuando el usuario cambie el ancho de columna o la altura de fila.

### **Anclar la imagen a una sola celda**

El anclaje de la imagen se define mediante cuatro propiedades de índice basadas en cero:

- `picture.setUpperLeftRow(int)` — el índice de fila del borde superior de la imagen.
- `picture.setUpperLeftColumn(int)` — el índice de columna del borde izquierdo de la imagen.
- `picture.setLowerRightRow(int)` — el índice de fila del borde inferior de la imagen. Para que el borde inferior de la imagen se ubique en la parte inferior de la fila `r`, establezca este valor en `r + 1`.
- `picture.setLowerRightColumn(int)` — el índice de columna del borde derecho de la imagen. Para que el borde derecho de la imagen se ubique a la derecha de la columna `c`, establezca este valor en `c + 1`.

Por ejemplo, para ajustar la imagen exactamente en la celda **C6** (índice de fila `5`, índice de columna `2`), establezca `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, y `LowerRightColumn = 3`.

{{% alert color="primary" %}}

Los índices de fila y columna en Aspose.Cells están **basados en cero**. La celda C6 tiene índice de fila 5 e índice de columna 2. Los errores de desfase por uno en el anclaje inferior derecho son la fuente más común de imágenes que parecen superponerse a una celda adyacente.

{{% /alert %}}

### **Controlar el comportamiento de ubicación**

`Picture.Placement` es una enumeración de tipo `PlacementType` que controla cómo se comporta la imagen cuando el usuario cambia el tamaño de la fila o columna debajo de ella. El valor recomendado para una imagen de una sola celda es `PlacementType.MoveAndSize`, que hace que la imagen se mueva y se redimensione junto con su celda subyacente, conservando el ajuste exacto.

### **Instrucciones paso a paso**

1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda al `Worksheet` de destino desde `workbook.getWorksheets().get(0)`.
3. Abra el archivo de imagen desde el disco en un `InputStream` (por ejemplo, usando `FileInputStream`) para que el flujo se cierre correctamente.
4. Llame a `worksheet.getPictures().add(5, 2, stream)` para agregar una imagen anclada a la celda C6. Capture la referencia `Picture` devuelta.
5. Establezca las cuatro coordenadas de anclaje para que la imagen cubra solo la celda C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Establezca `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` para mantener la imagen alineada con C6 cuando se cambie el tamaño de la columna o la fila.
7. Opcionalmente, agregue texto de muestra a las celdas circundantes para demostrar que solo la celda C6 contiene la imagen.
8. Guarde el libro de trabajo en disco como un archivo `.xlsx`.

El siguiente código demuestra el enfoque completo.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

var picIndex = worksheet.getPictures().add(5, 2, "logo.png");
var picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);

workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Enfoque 2: Incrustar una imagen directamente en una celda**

Aspose.Cells también expone un mecanismo más simple para imágenes vinculadas a celdas: la propiedad `Cell.EmbeddedImage`. Asignar bytes de imagen a esta propiedad adjunta la imagen a la celda misma, como si fuera contenido en línea.

### **Cómo funcionan las imágenes incrustadas**

- La imagen se almacena como parte del contenido de la celda en lugar de como una forma en la capa de dibujo.
- La imagen se escala automáticamente para ajustarse dentro de los límites renderizados de la celda. No se requieren coordenadas de anclaje ni configuraciones de ubicación.
- La celda sigue siendo una celda real con una dirección real que puede ser referenciada por fórmulas, ordenada como parte de una fila, o utilizada en otras operaciones a nivel de celda.

Esto hace que `Cell.EmbeddedImage` sea la opción más concisa cuando su objetivo es simplemente "una imagen que vive dentro de esta celda".

### **Instrucciones paso a paso**

1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda al `Worksheet` de destino desde `workbook.getWorksheets().get(0)`.
3. Lea el archivo de imagen desde el disco en un arreglo de bytes (por ejemplo, usando `Files.readAllBytes` de `java.nio.file.Files`).
4. Obtenga una referencia a la celda de destino, ya sea a través de `worksheet.getCells().get("C6")` o `worksheet.getCells().get(5, 2)`.
5. Asigne el arreglo de bytes a la propiedad `EmbeddedImage` de la celda mediante `cell.setEmbeddedImage(bytes)`.
6. Opcionalmente, ajuste la altura de fila y el ancho de columna de la fila y columna de destino para dar a la imagen incrustada una apariencia más prominente.
7. Guarde el libro de trabajo en disco como un archivo `.xlsx`.

El siguiente código demuestra el enfoque completo.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Obtener la celda objetivo C6
var cell = worksheet.getCells().get("C6");

// Leer el archivo de imagen en un arreglo de bytes
var imageData = fs.readFileSync("logo.png");

// Incrustar la imagen directamente en la celda
cell.setEmbeddedImage(imageData);

// Opcionalmente ajustar la altura de la fila y el ancho de la columna para que la imagen incrustada sea más visible
worksheet.getCells().setColumnWidth(2, 30);   // Columna C (índice 2)
worksheet.getCells().setRowHeight(5, 100);     // Fila 6 (índice 5)

// Guardar el libro de trabajo resultante como un archivo .xlsx
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Elegir el enfoque adecuado**

Ambos enfoques producen una imagen que se ajusta dentro de una sola celda, pero difieren en cómo se almacena la imagen y cómo se comporta:

- **Use una imagen flotante (Enfoque 1) cuando:**
  - Necesite un control más fino sobre la ubicación, el ordenamiento en capas o la alineación con otros objetos de dibujo.
  - Desee que la imagen se comporte como una forma que se pueda seleccionar, reordenar o agrupar con otras formas.
  - Requiera compatibilidad heredada con código que ya trabaja con `PictureCollection`.
  - Necesite calcular coordenadas de anclaje dinámicamente según el diseño de la hoja de cálculo.

- **Use una imagen incrustada (Enfoque 2) cuando:**
  - Desee la inserción más simple posible de una imagen en una celda.
  - La imagen deba viajar con la celda como cualquier otro contenido de celda.
  - No necesite manipular la imagen como una forma.

{{% alert color="primary" %}}

Ambos enfoques pueden coexistir en el mismo libro de trabajo. Puede colocar imágenes flotantes sobre un conjunto de celdas e incrustar imágenes directamente en otras celdas, ya que los dos mecanismos utilizan diferentes capas de almacenamiento en el archivo.

{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}