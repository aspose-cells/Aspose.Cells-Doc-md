---
title: Insertar una imagen en una celda
linktitle: Insertar una imagen en una celda
description: Aspose.Cells for Python via Java es una biblioteca para trabajar con archivos de hoja de cálculo. Este artículo explica cómo ajustar una imagen exactamente a una sola celda, ya sea colocando una imagen flotante sobre la celda o incrustando la imagen directamente en ella.
keywords: Aspose.Cells, biblioteca de Python via Java, hoja de cálculo, insertar una imagen, incrustar una imagen, imagen en una celda, ajustar una imagen a una celda, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /es/python-java/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece dos maneras distintas de asociar una imagen con una sola celda. Una imagen flotante es una forma de la capa de dibujo de la hoja de cálculo que se superpone visualmente a un rango de celdas, mientras que una imagen incrustada se almacena dentro de la celda y escala automáticamente al área de visualización de esta. Elija el enfoque que mejor se adapte a sus requisitos de diseño.
{{% /alert %}}

## **Introducción**
Ajustar una imagen exactamente a una sola celda es un requisito común al diseñar hojas de cálculo que funcionan como informes visuales, catálogos de productos, directorios de empleados, paneles de control o listas de inventario. En lugar de estirar una imagen sobre muchas celdas o colocarla de forma suelta en una hoja de cálculo, puede que necesite una imagen limpia y vinculada a la celda que permanezca alineada con la celda a la que pertenece.
Aspose.Cells admite este escenario de dos maneras complementarias:
- **Enfoque 1: colocar una imagen flotante sobre una celda.** Agregue un `Picture` a la hoja de cálculo, establezca su `setPlacement` en `MOVE_AND_SIZE` y ajuste sus celdas de anclaje (`setUpperLeftRow`, `setUpperLeftColumn`, `setLowerRightRow`, `setLowerRightColumn`) para que la imagen cubra exactamente una celda.
- **Enfoque 2: incrustar una imagen directamente en una celda.** Asigne los bytes de la imagen a la propiedad `setEmbeddedImage` de la celda. La imagen escala automáticamente para ajustarse al área de visualización de la celda y se mueve con ella.
El resto de este artículo explica ambos enfoques, describe las API pertinentes y muestra cómo utilizarlas en el código.

## **Enfoque 1: colocar una imagen flotante sobre una celda**
Una imagen flotante es un objeto `Picture` que reside en la capa de dibujo de la hoja de cálculo. Aunque no forma parte de ninguna celda en concreto, se ancla a un rango de celdas. Las celdas de anclaje de la imagen —sus esquinas superior izquierda e inferior derecha— determinan su extensión visual en la hoja de cálculo. De forma predeterminada, una imagen recién agregada abarca varias celdas.
Para hacer que una imagen flotante cubra **exactamente una celda**, debe:
1. Agregar la imagen mediante `Worksheet.getPictures().add(int row, int column, InputStream stream)`, que ancla la nueva imagen a la celda especificada.
2. Establecer las cuatro propiedades de anclaje para que el rectángulo delimitador de la imagen coincida con la celda de destino.
3. Establecer `Picture.setPlacement` en `PlacementType.MOVE_AND_SIZE` para que la imagen se mueva y cambie de tamaño junto con la celda subyacente cuando el usuario modifique el ancho de la columna o el alto de la fila.

### **Anclaje de la imagen a una sola celda**
El anclaje de la imagen se define mediante cuatro propiedades de índice con base cero:
- `setUpperLeftRow`: el índice de fila del borde superior de la imagen.
- `setUpperLeftColumn`: el índice de columna del borde izquierdo de la imagen.
- `setLowerRightRow`: el índice de fila del borde inferior de la imagen. Para que el borde inferior de la imagen se encuentre en la parte inferior de la fila `r`, establezca este valor en `r + 1`.
- `setLowerRightColumn`: el índice de columna del borde derecho de la imagen. Para que el borde derecho de la imagen se encuentre en el extremo derecho de la columna `c`, establezca este valor en `c + 1`.

{{% alert color="primary" %}}
Los índices de fila y columna en Aspose.Cells **comienzan en cero**. La celda C6 tiene el índice de fila 5 y el índice de columna 2. Los errores de una unidad en el ancla inferior derecha son la causa más común de imágenes que parecen superponerse a una celda adyacente.
{{% /alert %}}

### **Control del comportamiento de colocación**
`getPlacement` es una enumeración de tipo `PlacementType` que controla el comportamiento de la imagen cuando el usuario cambia el tamaño de la fila o la columna situ debajo de ella. El valor recomendado para una imagen vinculada a una sola celda es `PlacementType.MOVE_AND_SIZE`, que hace que la imagen se mueva y cambie de tamaño junto con la celda subyacente, conservando el ajuste exacto.

### **Instrucciones paso a paso**
1. Cree un nuevo `Workbook` o abra uno existente.
2. Acceda a la `Worksheet` de destino mediante `workbook.getWorksheets().get(0)`.
3. Abra el archivo de imagen del disco en un `InputStream`, normalmente un `FileInputStream`, para que el flujo se cierre correctamente.
4. Llame a `worksheet.getPictures().add(5, 2, stream)` para agregar una imagen anclada a la celda C6. Capture la referencia `Picture` devuelta.
5. Establezca las cuatro coordenadas de anclaje para que la imagen cubra únicamente la celda C6: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)` y `setLowerRightColumn(3)`.
6. Establezca `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` para mantener la imagen alineada con C6 cuando se cambie el tamaño de la columna o de la fila.
7. Opcionalmente, agregue texto de ejemplo a las celdas circundantes para demostrar que solo la celda C6 contiene la imagen.
8. Guarde el libro de trabajo en el disco como un archivo `.xlsx`.
El siguiente código demuestra el enfoque completo.

```python
import jpype
import asposecells
jpype.startJVM()
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
    picture.setPlacement(PlacementType.MOVE_AND_SIZE)
finally:
    fs.close()
workbook.save("output.xlsx", SaveFormat.XLSX)
jpype.shutdownJVM()
```

## **Enfoque 2: incrustar una imagen directamente en una celda**
Aspose.Cells también ofrece un mecanismo más sencillo para las imágenes vinculadas a una celda: la propiedad `Cell.setEmbeddedImage`. Al asignar bytes de imagen a esta propiedad, la imagen se adjunta a la celda como si fuera contenido en línea.

### **Funcionamiento de las imágenes incrustadas**
- La imagen se almacena como parte del contenido de la celda, en lugar de como una forma de la capa de dibujo.
- La imagen escala automáticamente para ajustarse dentro de los límites de visualización de la celda. No se requieren coordenadas de anclaje ni ajustes de colocación.
- La celda sigue siendo una celda real con una dirección real que puede ser referenciada por fórmulas, ordenarse como parte de una fila o utilizarse en otras operaciones en el nivel de la celda.
Esto hace que `Cell.setEmbeddedImage` sea la opción más concisa cuando el objetivo es simplemente «una imagen que reside dentro de esta celda».

### **Instrucciones paso a paso**
1. Cree un nuevo `Workbook` o abra uno existente.
2. Acceda a la `Worksheet` de destino mediante `workbook.getWorksheets().get(0)`.
3. Lea el archivo de imagen del disco en una matriz `byte[]`, por ejemplo, mediante una llamada `Files.readAllBytes` de `java.nio.file.Files`.
4. Obtenga una referencia a la celda de destino, ya sea mediante `worksheet.getCells().get("C6")` o `worksheet.getCells().get(5, 2)`.
5. Asigne la matriz de bytes a la propiedad `setEmbeddedImage` de la celda.
6. Opcionalmente, ajuste el alto de la fila y el ancho de la columna de destino para dar más prominencia a la imagen incrustada.
7. Guarde el libro de trabajo en el disco como un archivo `.xlsx`.
El siguiente código demuestra el enfoque completo.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Get the target cell C6
cell = worksheet.getCells().get("C6")
# Read the image file into a byte array
imageData = open("logo.png", "rb").read()
# Embed the image directly into the cell
cell.setEmbeddedImage(imageData)
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30)   # Column C (index 2)
worksheet.getCells().setRowHeight(5, 100)    # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", SaveFormat.XLSX)
jpype.shutdownJVM()
```

## **Elección del enfoque adecuado**
Ambos enfoques producen una imagen que cabe dentro de una sola celda, pero difieren en cómo se almacena y se comporta:
- **Utilice una imagen flotante (enfoque 1) cuando:**
  - Necesite un control más preciso de la colocación, las capas o la alineación con otros objetos de dibujo.
  - Desee que la imagen se comporte como una forma que se pueda seleccionar, reordenar o agrupar con otras formas.
  - Necesite compatibilidad retroactiva con el código existente que ya funciona con `PictureCollection`.
  - Necesite calcular dinámicamente las coordenadas de anclaje según el diseño de la hoja de cálculo.
- **Utilice una imagen incrustada (enfoque 2) cuando:**
  - Desee la forma más simple posible de insertar una imagen en una celda.
  - La imagen deba moverse con la celda como cualquier otro contenido de celda.

{{< app/cells/assistant language="python" >}}