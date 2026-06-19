---
title: Insertar una imagen en una celda
description: Aspose.Cells es una biblioteca de Python para trabajar con archivos de hojas de cálculo. Este artículo explica cómo ajustar una imagen exactamente al tamaño de una sola celda usando dos enfoques diferentes: colocar una imagen flotante sobre la celda, o incrustar la imagen directamente en la celda.
keywords: Aspose.Cells, Python library, spreadsheet, insert image, embed image, picture in cell, fit image to cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /es/python-net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells ofrece dos formas distintas de asociar una imagen con una sola celda. Una imagen flotante es una forma en la capa de dibujo de la hoja de cálculo que se superpone visualmente a un rango de celdas, mientras que una imagen incrustada se almacena dentro de la propia celda y se escala automáticamente al área de visualización de la celda. Elija el enfoque que mejor se adapte a sus requisitos de diseño.

{{% /alert %}}

## **Introducción**

Ajustar una imagen exactamente a una sola celda es un requisito común al diseñar hojas de cálculo que actúan como informes visuales, catálogos de productos, directorios de empleados, paneles de control o listas de inventario. En lugar de estirar una imagen a lo largo de muchas celdas o colocarla de forma suelta en una hoja de cálculo, es posible que desee una imagen limpia y vinculada a la celda que permanezca alineada con la celda que la contiene.

Aspose.Cells admite este escenario de dos formas complementarias:

- **Enfoque 1: colocar una imagen flotante sobre una celda.** Añada un `Picture` a la hoja de cálculo, establezca su `placement` en `MOVE_AND_SIZE` y ajuste sus celdas de anclaje (`upper_left_row`, `upper_left_column`, `lower_right_row`, `lower_right_column`) para que la imagen cubra exactamente una celda.
- **Enfoque 2: incrustar una imagen directamente en una celda.** Asigne los bytes de la imagen a la propiedad `embedded_image` de la celda. La imagen se escala automáticamente para ajustarse al área de visualización de la celda y viaja con la celda.

El resto de este artículo recorre ambos enfoques, explica las API relevantes y muestra cómo usarlas en código.

## **Enfoque 1: colocar una imagen sobre una celda**

Una imagen flotante es un objeto `Picture` que reside en la capa de dibujo de la hoja de cálculo. Aunque no forma parte de ninguna celda individual, está anclada a un rango de celdas. Las celdas de anclaje de la imagen (sus esquinas superior izquierda e inferior derecha) determinan su extensión visual en la hoja de cálculo. Por defecto, una imagen recién añadida abarca varias celdas.

Para que una imagen flotante cubra **exactamente una celda**, necesita:

1. Añadir la imagen usando `Worksheet.pictures.add(row, column, stream)`, que ancla la nueva imagen a la celda indicada.
2. Establecer las cuatro propiedades de anclaje para que el rectángulo delimitador de la imagen coincida con la celda de destino.
3. Establecer `Picture.placement` en `PlacementType.MOVE_AND_SIZE` para que la imagen se mueva y se redimensione con la celda subyacente cuando el usuario cambie el ancho de columna o el alto de fila.

### **Anclar la imagen a una sola celda**

El ancla de la imagen se define mediante cuatro propiedades de índice basadas en cero:

- `Picture.upper_left_row` — el índice de fila del borde superior de la imagen.
- `Picture.upper_left_column` — el índice de columna del borde izquierdo de la imagen.
- `Picture.lower_right_row` — el índice de fila del borde inferior de la imagen. Para que el borde inferior de la imagen quede en la parte inferior de la fila `r`, establezca este valor en `r + 1`.
- `Picture.lower_right_column` — el índice de columna del borde derecho de la imagen. Para que el borde derecho de la imagen quede en la parte derecha de la columna `c`, establezca este valor en `c + 1`.

Por ejemplo, para ajustar la imagen exactamente a la celda **C6** (índice de fila `5`, índice de columna `2`), establezca `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6` y `lower_right_column = 3`.

{{% alert color="primary" %}}

Los índices de fila y columna en Aspose.Cells son **basados en cero**. La celda C6 tiene índice de fila 5 e índice de columna 2. Los errores de diferencia de uno en el ancla inferior derecha son la fuente más común de imágenes que parecen superponerse a una celda adyacente.

{{% /alert %}}

### **Controlar el comportamiento de colocación**

`Picture.placement` es una enumeración de tipo `PlacementType` que controla cómo se comporta la imagen cuando el usuario cambia el tamaño de la fila o columna bajo ella. El valor recomendado para una imagen de una sola celda es `PlacementType.MOVE_AND_SIZE`, que hace que la imagen se mueva y se redimensione junto con su celda subyacente, conservando el ajuste exacto.

### **Instrucciones paso a paso**

1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda al `Worksheet` de destino desde `workbook.worksheets[0]`.
3. Abra el archivo de imagen desde el disco en un flujo de archivo (o un objeto `BytesIO`) usando un bloque `with` para que el flujo se libere correctamente.
4. Llame a `worksheet.pictures.add(5, 2, stream)` para añadir una imagen anclada a la celda C6. Capture la referencia `Picture` devuelta.
5. Establezca las cuatro coordenadas de anclaje para que la imagen cubra solo la celda C6: `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, `lower_right_column = 3`.
6. Establezca `picture.placement = PlacementType.MOVE_AND_SIZE` para mantener la imagen alineada con C6 cuando se cambie el tamaño de la columna o fila.
7. Opcionalmente, añada texto de muestra a las celdas circundantes para demostrar que solo la celda C6 contiene la imagen.
8. Guarde el libro de trabajo en disco como un archivo `.xlsx`.

El siguiente código demuestra el enfoque completo.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

with open("logo.png", "rb") as fs:
    pic_index = worksheet.pictures.add(5, 2, fs)
    picture = worksheet.pictures[pic_index]
    picture.upper_left_row = 5
    picture.upper_left_column = 2
    picture.lower_right_row = 6
    picture.lower_right_column = 3
    picture.placement = ac.PlacementType.MOVE_AND_SIZE

workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Enfoque 2: incrustar una imagen directamente en una celda**

Aspose.Cells también expone un mecanismo más sencillo para imágenes vinculadas a celdas: la propiedad `Cell.embedded_image`. Asignar bytes de imagen a esta propiedad adjunta la imagen a la propia celda, como si fuera contenido en línea.

### **Cómo funcionan las imágenes incrustadas**

- La imagen se almacena como parte del contenido de la celda en lugar de como una forma en la capa de dibujo.
- La imagen se escala automáticamente para ajustarse dentro de los límites renderizados de la celda. No se requieren coordenadas de anclaje ni configuraciones de colocación.
- La celda sigue siendo una celda real con una dirección real a la que las fórmulas pueden hacer referencia, que puede ordenarse como parte de una fila o usarse en otras operaciones a nivel de celda.

Esto convierte a `Cell.embedded_image` en la opción más concisa cuando su objetivo es simplemente "una imagen que vive dentro de esta celda".

### **Instrucciones paso a paso**

1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda al `Worksheet` de destino desde `workbook.worksheets[0]`.
3. Lea el archivo de imagen desde el disco en un objeto `bytes` (por ejemplo, abriendo el archivo en modo binario y llamando a `.read()`).
4. Obtenga una referencia a la celda de destino, ya sea a través de `worksheet.cells["C6"]` o `worksheet.cells[5, 2]`.
5. Asigne el objeto de bytes a la propiedad `embedded_image` de la celda.
6. Opcionalmente, ajuste el alto de fila y el ancho de columna de la fila y columna de destino para dar a la imagen incrustada una apariencia más prominente.
7. Guarde el libro de trabajo en disco como un archivo `.xlsx`.

El siguiente código demuestra el enfoque completo.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Obtener la celda objetivo C6
cell = worksheet.cells["C6"]

# Leer el archivo de imagen en un arreglo de bytes
with open("logo.png", "rb") as f:
    imageData = f.read()

# Incrustar la imagen directamente en la celda
cell.embedded_image = imageData

# Opcionalmente ajustar la altura de la fila y el ancho de la columna para que la imagen incrustada sea más visible
worksheet.cells.set_column_width(2, 30)   # Columna C (índice 2)
worksheet.cells.set_row_height(5, 100)     # Fila 6 (índice 5)

# Guardar el libro de trabajo resultante como un archivo .xlsx
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Elegir el enfoque adecuado**

Ambos enfoques producen una imagen que se ajusta dentro de una sola celda, pero difieren en cómo se almacena la imagen y cómo se comporta:

- **Use una imagen flotante (Enfoque 1) cuando:**
  - Necesite un control más fino sobre la colocación, el orden de capas o la alineación con otros objetos de dibujo.
  - Desee que la imagen se comporte como una forma que se pueda seleccionar, reordenar o agrupar con otras formas.
  - Requiera compatibilidad heredada con código que ya trabaja con colecciones de `pictures`.
  - Necesite calcular coordenadas de anclaje dinámicamente según el diseño de la hoja de cálculo.

- **Use una imagen incrustada (Enfoque 2) cuando:**
  - Desee la inserción más sencilla posible de una imagen en una celda.
  - La imagen deba viajar con la celda como cualquier otro contenido de la celda.
  - No necesite manipular la imagen como una forma.

{{% alert color="primary" %}}

Ambos enfoques pueden coexistir en el mismo libro de trabajo. Puede colocar imágenes flotantes sobre un conjunto de celdas e incrustar imágenes directamente en otras celdas, ya que los dos mecanismos utilizan diferentes capas de almacenamiento en el archivo.

{{% /alert %}}

## **Artículos relacionados**

- [Cómo insertar una imagen en una celda](/cells/es/python-net/how-to-place-image-to-cell/)
- [Añadir hipervínculos a imágenes](/cells/es/python-net/add-image-hyperlinks/)
- [Cargar una imagen web desde una URL en una hoja de cálculo de Excel](/cells/es/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipular posición, tamaño y gráfico del diseñador](/cells/es/python-net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="python" >}}