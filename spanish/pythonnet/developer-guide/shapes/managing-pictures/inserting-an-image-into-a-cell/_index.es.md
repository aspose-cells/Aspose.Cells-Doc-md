---
title: Insertar una imagen en una celda
linktitle: Insertar una imagen en una celda
description: Aspose.Cells es una biblioteca de Python para trabajar con archivos de hojas de cálculo. Este artículo explica cómo ajustar una imagen a una sola celda exactamente, ya sea colocando una imagen flotante sobre la celda o incrustando la imagen directamente en la celda.
keywords: Aspose.Cells, biblioteca de Python, hoja de cálculo, insertar imagen, incrustar imagen, imagen en celda, ajustar imagen a celda, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /es/python-net/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece dos formas distintas de asociar una imagen a una sola celda. Una imagen flotante es una forma en la capa de dibujo de la hoja de cálculo que se superpone visualmente a un rango de celdas, mientras que una imagen incrustada se almacena dentro de la propia celda y se escala automáticamente al área de visualización de la celda. Elija el enfoque que mejor se adapte a sus requisitos de diseño.
{{% /alert %}}

## **Introduction**
Ajustar una imagen exactamente a una sola celda es un requisito común al diseñar hojas de cálculo que actúan como informes visuales, catálogos de productos, directorios de empleados, paneles de control o listas de inventario. En lugar de estirar una imagen a través de muchas celdas o colocarla sin anclarla en una hoja de cálculo, es posible que desee una imagen limpia y vinculada a una celda que permanezca alineada con la celda a la que pertenece.
Aspose.Cells admite este escenario de dos formas complementarias:
- **Enfoque 1: Colocar una imagen flotante sobre una celda.** Agregue un `Picture` a la hoja de cálculo, establezca su `placement` en `MOVE_AND_SIZE` y ajuste sus celdas de anclaje (`upper_left_row`, `upper_left_column`, `lower_right_row`, `lower_right_column`) para que la imagen cubra exactamente una celda.
- **Enfoque 2: Incrustar una imagen directamente en una celda.** Asigne bytes de imagen a la propiedad `embedded_image` de la celda. La imagen se escala automáticamente para ajustarse al área de visualización de la celda y viaja con la celda.
El resto de este artículo recorre ambos enfoques, explica las API relevantes y muestra cómo usarlos en código.

## **Approach 1: Place a Picture Over a Cell**
Una imagen flotante es un objeto `Picture` que reside en la capa de dibujo de la hoja de cálculo. Aunque no forma parte de ninguna celda individual, está anclada a un rango de celdas. Las celdas de anclaje de la imagen (sus esquinas superior izquierda e inferior derecha) determinan su extensión visual en la hoja de cálculo. Por defecto, una imagen recién agregada abarca varias celdas.
Para hacer que una imagen flotante cubra **exactamente una celda**, debe:
1. Agregar la imagen usando `Worksheet.pictures.add(row, column, stream)`, que ancla la nueva imagen a la celda indicada.
2. Establecer las cuatro propiedades de anclaje para que el rectángulo delimitador de la imagen coincida con la celda de destino.
3. Establecer `Picture.placement` en `PlacementType.MOVE_AND_SIZE` para que la imagen se mueva y se redimensione con la celda subyacente cuando el usuario cambie el ancho de columna o la altura de fila.

### **Anchoring the Picture to a Single Cell**
El ancla de la imagen está definida por cuatro propiedades de índice basado en cero:
- `Picture.upper_left_row` — el índice de fila del borde superior de la imagen.
- `Picture.upper_left_column` — el índice de columna del borde izquierdo de la imagen.
- `Picture.lower_right_row` — el índice de fila del borde inferior de la imagen. Para que el borde inferior de la imagen quede en la parte inferior de la fila `r`, establezca este valor en `r + 1`.
- `Picture.lower_right_column` — el índice de columna del borde derecho de la imagen. Para que el borde derecho de la imagen quede a la derecha de la columna `c`, establezca este valor en `c + 1`.

{{% alert color="primary" %}}
Los índices de filas y columnas en Aspose.Cells están **basados en cero**. La celda C6 tiene índice de fila 5 e índice de columna 2. Los errores de desviación por uno en el ancla inferior derecha son la causa más común de imágenes que parecen superponerse a una celda adyacente.
{{% /alert %}}

### **Controlling Placement Behavior**
`Picture.placement` es una enumeración de tipo `PlacementType` que controla cómo se comporta la imagen cuando el usuario cambia el tamaño de la fila o columna debajo de ella. El valor recomendado para una imagen de una sola celda es `PlacementType.MOVE_AND_SIZE`, que hace que la imagen se mueva y cambie de tamaño junto con su celda subyacente, preservando el ajuste exacto.

### **Step-by-Step Instructions**
1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda al `Worksheet` de destino desde `workbook.worksheets[0]`.
3. Abra el archivo de imagen desde el disco en un flujo de archivo (o un objeto `BytesIO`) usando un bloque `with` para que el flujo se libere correctamente.
4. Llame a `worksheet.pictures.add(5, 2, stream)` para agregar una imagen anclada a la celda C6. Capture la referencia `Picture` devuelta.
5. Establezca las cuatro coordenadas de anclaje para que la imagen cubra solo la celda C6: `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, `lower_right_column = 3`.
6. Establezca `picture.placement = PlacementType.MOVE_AND_SIZE` para mantener la imagen alineada con C6 cuando se cambie el tamaño de la columna o fila.
7. Opcionalmente, agregue texto de muestra a las celdas circundantes para demostrar que solo la celda C6 contiene la imagen.
8. Guarde el libro de trabajo en el disco como un archivo `.xlsx`.
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

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cells también expone un mecanismo más simple para imágenes vinculadas a celdas: la propiedad `Cell.embedded_image`. Asignar bytes de imagen a esta propiedad adjunta la imagen a la celda misma, como si fuera contenido en línea.

### **How Embedded Images Work**
- La imagen se almacena como parte del contenido de la celda en lugar de como una forma en la capa de dibujo.
- La imagen se escala automáticamente para ajustarse dentro de los límites renderizados de la celda. No se requieren coordenadas de anclaje ni configuraciones de ubicación.
- La celda sigue siendo una celda real con una dirección real a la que se puede hacer referencia mediante fórmulas, ordenar como parte de una fila o usar en otras operaciones a nivel de celda.
Esto hace que `Cell.embedded_image` sea la opción más concisa cuando su objetivo es simplemente «una imagen que reside dentro de esta celda».

### **Step-by-Step Instructions**
1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda al `Worksheet` de destino desde `workbook.worksheets[0]`.
3. Lea el archivo de imagen desde el disco en un objeto `bytes` (por ejemplo, abriendo el archivo en modo binario y llamando a `.read()`).
4. Obtenga una referencia a la celda de destino, ya sea a través de `worksheet.cells["C6"]` o `worksheet.cells[5, 2]`.
5. Asigne el objeto bytes a la propiedad `embedded_image` de la celda.
6. Opcionalmente, ajuste la altura de fila y el ancho de columna de la fila y columna de destino para dar a la imagen incrustada una apariencia más prominente.
7. Guarde el libro de trabajo en el disco como un archivo `.xlsx`.
El siguiente código demuestra el enfoque completo.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Get the target cell C6
cell = worksheet.cells["C6"]
# Read the image file into a byte array
with open("logo.png", "rb") as f:
    imageData = f.read()
# Embed the image directly into the cell
cell.embedded_image = imageData
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.cells.set_column_width(2, 30)   # Column C (index 2)
worksheet.cells.set_row_height(5, 100)     # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Choosing the Right Approach**
Ambos enfoques producen una imagen que cabe dentro de una sola celda, pero difieren en cómo se almacena la imagen y cómo se comporta:
- **Use una imagen flotante (Enfoque 1) cuando:**
  - Necesite un control más fino sobre la ubicación, el orden de apilamiento o la alineación con otros objetos de dibujo.
  - Desee que la imagen se comporte como una forma que se pueda seleccionar, reordenar o agrupar con otras formas.
  - Requiera compatibilidad heredada con código que ya funciona con colecciones de `pictures`.
  - Necesite calcular coordenadas de anclaje dinámicamente según el diseño de la hoja de cálculo.
- **Use una imagen incrustada (Enfoque 2) cuando:**
  - Desee la inserción más simple posible de una imagen en una celda.
  - La imagen deba viajar con la celda como cualquier otro contenido de la celda.

## Related Articles
- [Cámara de Excel en Aspose.Cells for Python via .NET](/cells/es/python-net/excel-camera/)
- [Agregar campos de filtro a una Tabla Dinámica en Aspose.Cells for Python via .NET](/cells/es/python-net/add-page-field-in-pivot-table/)
- [Aplicar estilos a Tablas Dinámicas en Aspose.Cells for Python via .NET](/cells/es/python-net/apply-style-to-pivot-table/)
- [Modificar el diseño del campo de página en una Tabla Dinámica](/cells/es/python-net/change-page-field-layout/)
- [Convertir minigráfico a imagen y HTML en Aspose.Cells for Python via .NET](/cells/es/python-net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="python" >}}