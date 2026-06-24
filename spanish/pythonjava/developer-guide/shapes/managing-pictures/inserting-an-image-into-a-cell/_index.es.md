---
title: Insertar una imagen en una celda
description: Aspose.Cells for Python via Java es una biblioteca para trabajar con archivos de hojas de cálculo. Este artículo explica cómo ajustar una imagen exactamente al tamaño de una sola celda usando dos enfoques diferentes, colocar una imagen flotante sobre la celda o incrustar la imagen directamente en la celda.
keywords: Aspose.Cells, Python via Java library, spreadsheet, insert image, embed image, picture in cell, fit image to cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /es/python-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells ofrece dos formas distintas de asociar una imagen con una sola celda. Una imagen flotante es una forma en la capa de dibujo de la hoja de cálculo que se superpone visualmente a un rango de celdas, mientras que una imagen incrustada se almacena dentro de la propia celda y se escala automáticamente al área de visualización de la celda. Elija el enfoque que mejor se adapte a sus requisitos de diseño.

{{% /alert %}}

## **Introducción**

Ajustar una imagen exactamente a una sola celda es un requisito común al diseñar hojas de cálculo que actúan como informes visuales, catálogos de productos, directorios de empleados, paneles de control o listas de inventario. En lugar de estirar una imagen a lo largo de muchas celdas o colocarla de forma suelta en una hoja de cálculo, es posible que desee una imagen limpia y vinculada a una celda que se mantenga alineada con la celda a la que pertenece.

Aspose.Cells admite este escenario de dos formas complementarias:

- **Enfoque 1 — Colocar una imagen flotante sobre una celda.** Añada un `Picture` a la hoja de cálculo, establezca su `setPlacement` en `MOVE_AND_SIZE`, y ajuste sus celdas de anclaje (`setUpperLeftRow`, `setUpperLeftColumn`, `setLowerRightRow`, `setLowerRightColumn`) para que la imagen cubra exactamente una celda.
- **Enfoque 2 — Incrustar una imagen directamente en una celda.** Asigne bytes de imagen a la propiedad `setEmbeddedImage` de la celda. La imagen se escala automáticamente para ajustarse al área de visualización de la celda y viaja con la celda.

El resto de este artículo recorre ambos enfoques, explica las API relevantes y muestra cómo usarlas en el código.

## **Enfoque 1: Colocar una imagen sobre una celda**

Una imagen flotante es un objeto `Picture` que reside en la capa de dibujo de la hoja de cálculo. Aunque no forma parte de ninguna celda individual, está anclada a un rango de celdas. Las celdas de anclaje de la imagen —sus esquinas superior izquierda e inferior derecha— determinan su extensión visual en la hoja de cálculo. Por defecto, una imagen recién añadida abarca varias celdas.

Para hacer que una imagen flotante cubra **exactamente una celda**, necesita:

1. Añadir la imagen usando `Worksheet.getPictures().add(int row, int column, InputStream stream)`, que ancla la nueva imagen a la celda indicada.
2. Establecer las cuatro propiedades de anclaje para que el rectángulo delimitador de la imagen coincida con la celda de destino.
3. Establecer `Picture.setPlacement` en `PlacementType.MOVE_AND_SIZE` para que la imagen se mueva y cambie de tamaño con la celda subyacente cuando el usuario modifique el ancho de columna o la altura de fila.

### **Anclaje de la imagen a una sola celda**

El anclaje de la imagen se define mediante cuatro propiedades de índice basadas en cero:

- `setUpperLeftRow` — el índice de fila del borde superior de la imagen.
- `setUpperLeftColumn` — el índice de columna del borde izquierdo de la imagen.
- `setLowerRightRow` — el índice de fila del borde inferior de la imagen. Para hacer que el borde inferior de la imagen se sitúe en la parte inferior de la fila `r`, establezca este valor en `r + 1`.
- `setLowerRightColumn` — el índice de columna del borde derecho de la imagen. Para hacer que el borde derecho de la imagen se sitúe en la parte derecha de la columna `c`, establezca este valor en `c + 1`.

Por ejemplo, para ajustar la imagen exactamente en la celda **C6** (índice de fila `5`, índice de columna `2`), establezca `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)` y `setLowerRightColumn(3)`.

{{% alert color="primary" %}}

Los índices de fila y columna en Aspose.Cells son **basados en cero**. La celda C6 tiene índice de fila 5 e índice de columna 2. Los errores de desfase por uno en el anclaje inferior derecho son la fuente más común de imágenes que parecen superponerse a una celda adyacente.

{{% /alert %}}

### **Control del comportamiento de colocación**

`getPlacement` es una enumeración de tipo `PlacementType` que controla cómo se comporta la imagen cuando el usuario cambia el tamaño de la fila o columna debajo de ella. El valor recomendado para una imagen de una sola celda es `PlacementType.MOVE_AND_SIZE`, que hace que la imagen se mueva y cambie de tamaño junto con su celda subyacente, preservando el ajuste exacto.

### **Instrucciones paso a paso**

1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda a la `Worksheet` de destino desde `workbook.getWorksheets().get(0)`.
3. Abra el archivo de imagen desde el disco en un `InputStream` (normalmente un `FileInputStream`) para que el flujo se cierre correctamente.
4. Llame a `worksheet.getPictures().add(5, 2, stream)` para añadir una imagen anclada a la celda C6. Capture la referencia `Picture` devuelta.
5. Establezca las cuatro coordenadas de anclaje para que la imagen cubra solo la celda C6: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Establezca `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` para mantener la imagen alineada con C6 cuando se cambie el tamaño de la columna o fila.
7. Opcionalmente, añada texto de muestra a las celdas circundantes para demostrar que solo la celda C6 contiene la imagen.
8. Guarde el libro de trabajo en disco como un archivo `.xlsx`.

El siguiente código demuestra el enfoque completo.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat, PlacementType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

FileInputStream = jpype.JClass("java.io.FileInputStream")
fs = FileInputStream("logo.png")
try:
    picIndex = worksheet.getPictures().add(5, 2, fs)
    picture = worksheet.getPictures().get(picIndex)
    picture.setUpperLeftRow(5)
    picture.setUpperLeftColumn(2)
    picture.setLowerRightRow(6)
    picture.setLowerRightColumn(3)
    picture.setPlacement(PlacementType.MoveAndSize)
finally:
    fs.close()

workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **Enfoque 2: Incrustar una imagen directamente en una celda**

Aspose.Cells también expone un mecanismo más simple para imágenes vinculadas a celdas: la propiedad `Cell.setEmbeddedImage`. Asignar bytes de imagen a esta propiedad adjunta la imagen a la celda misma, como si fuera contenido en línea.

### **Cómo funcionan las imágenes incrustadas**

- La imagen se almacena como parte del contenido de la celda en lugar de como una forma en la capa de dibujo.
- La imagen se escala automáticamente para ajustarse dentro de los límites renderizados de la celda. No se requieren coordenadas de anclaje ni configuraciones de colocación.
- La celda sigue siendo una celda real con una dirección real a la que pueden hacer referencia las fórmulas, que se puede ordenar como parte de una fila o usar en otras operaciones a nivel de celda.

Esto hace que `Cell.setEmbeddedImage` sea la opción más concisa cuando su objetivo es simplemente "una imagen que vive dentro de esta celda".

### **Instrucciones paso a paso**

1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda a la `Worksheet` de destino desde `workbook.getWorksheets().get(0)`.
3. Lea el archivo de imagen desde el disco en un arreglo `byte[]` (por ejemplo, usando una llamada a `Files.readAllBytes` de `java.nio.file.Files`).
4. Obtenga una referencia a la celda de destino —ya sea mediante `worksheet.getCells().get("C6")` o `worksheet.getCells().get(5, 2)`.
5. Asigne el arreglo de bytes a la propiedad `setEmbeddedImage` de la celda.
6. Opcionalmente, ajuste la altura de fila y el ancho de columna de la fila y columna de destino para dar a la imagen incrustada una apariencia más prominente.
7. Guarde el libro de trabajo en disco como un archivo `.xlsx`.

El siguiente código demuestra el enfoque completo.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# código portado aquí
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Obtener la celda objetivo C6
cell = worksheet.getCells().get("C6")

# Leer el archivo de imagen en un arreglo de bytes
imageData = open("logo.png", "rb").read()

# Incrustar la imagen directamente en la celda
cell.setEmbeddedImage(imageData)

# Opcionalmente ajustar la altura de fila y el ancho de columna para que la imagen incrustada sea más visible
worksheet.getCells().setColumnWidth(2, 30)   # Columna C (índice 2)
worksheet.getCells().setRowHeight(5, 100)    # Fila 6 (índice 5)

# Guardar el libro de trabajo resultante como un archivo .xlsx
workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **Elección del enfoque adecuado**

Ambos enfoques producen una imagen que cabe dentro de una sola celda, pero difieren en cómo se almacena la imagen y cómo se comporta:

- **Use una imagen flotante (Enfoque 1) cuando:**
  - Necesite un control más fino sobre la colocación, el orden de capas o la alineación con otros objetos de dibujo.
  - Desee que la imagen se comporte como una forma que se pueda seleccionar, reordenar o agrupar con otras formas.
  - Requiera compatibilidad heredada con código que ya trabaja con `PictureCollection`.
  - Necesite calcular coordenadas de anclaje dinámicamente según el diseño de la hoja de cálculo.

- **Use una imagen incrustada (Enfoque 2) cuando:**
  - Desee la inserción más simple posible de una imagen en una celda.
  - La imagen deba viajar con la celda como cualquier otro contenido de la celda.
  - No necesite manipular la imagen como una forma.

{{% alert color="primary" %}}

Ambos enfoques pueden coexistir en el mismo libro de trabajo. Puede colocar imágenes flotantes sobre un conjunto de celdas e incrustar imágenes directamente en otras celdas, ya que los dos mecanismos usan diferentes capas de almacenamiento en el archivo.

{{% /alert %}}



{{< app/cells/assistant language="python" >}}