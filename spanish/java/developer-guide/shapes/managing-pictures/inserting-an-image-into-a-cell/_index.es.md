---
title: Insertar una imagen en una celda
linktitle: Insertar una imagen en una celda
description: Aspose.Cells es una biblioteca de Java para trabajar con archivos de hojas de cálculo. Este artículo explica cómo ajustar una imagen exactamente a una sola celda, ya sea colocando una imagen flotante sobre la celda o incrustando la imagen directamente en la celda.
keywords: Aspose.Cells, biblioteca Java, hoja de cálculo, insertar imagen, incrustar imagen, imagen en celda, ajustar imagen a celda, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /es/java/inserting-an-image-into-a-cell/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece dos formas distintas de asociar una imagen con una sola celda. Una imagen flotante es una forma en la capa de dibujo de la hoja de cálculo que se superpone visualmente a un rango de celdas, mientras que una imagen incrustada se almacena dentro de la propia celda y se escala automáticamente al área de visualización de la celda. Elija el enfoque que mejor se adapte a sus requisitos de diseño.

## **Introducción**
Ajustar una imagen exactamente a una sola celda es un requisito habitual al diseñar hojas de cálculo que actúan como informes visuales, catálogos de productos, directorios de empleados, paneles de control o listas de inventario. En lugar de estirar una imagen a través de muchas celdas o colocarla de forma dispersa en una hoja de cálculo, es posible que desee una imagen limpia, vinculada a la celda, que se mantenga alineada con la celda que la contiene.
Aspose.Cells admite este escenario de dos formas complementarias:
- **Enfoque 1: colocar una imagen flotante sobre una celda.** Agregue un `Picture` a la hoja de cálculo, establezca su `Placement` en `MOVE_AND_SIZE` y ajuste sus celdas de anclaje (`getUpperLeftRow`, `getUpperLeftColumn`, `getLowerRightRow`, `getLowerRightColumn`) para que la imagen cubra exactamente una celda.
- **Enfoque 2: incrustar una imagen directamente en una celda.** Asigne bytes de imagen al setter `getEmbeddedImage()` de la celda. La imagen se escala automáticamente para ajustarse al área de visualización de la celda y viaja con la celda.
El resto de este artículo recorre ambos enfoques, explica las API relevantes y muestra cómo utilizarlas en el código.

## **Enfoque 1: colocar una imagen sobre una celda**
Una imagen flotante es un objeto `Picture` que reside en la capa de dibujo de la hoja de cálculo. Aunque no forma parte de ninguna celda individual, está anclada a un rango de celdas. Las celdas de anclaje de la imagen — sus esquinas superior izquierda e inferior derecha — determinan su extensión visual en la hoja de cálculo. De forma predeterminada, una imagen recién agregada abarca varias celdas.
Para lograr que una imagen flotante cubra **exactamente una celda**, debe:
1. Agregar la imagen usando `Worksheet.getPictures().add(int row, int column, InputStream stream)`, que ancla la nueva imagen a la celda indicada.
2. Establecer las cuatro propiedades de anclaje para que el rectángulo delimitador de la imagen coincida con la celda de destino.
3. Establecer `Picture.setPlacement()` en `PlacementType.MOVE_AND_SIZE` para que la imagen se mueva y se redimensione con la celda subyacente cuando el usuario cambie el ancho de columna o el alto de fila.

### **Anclaje de la imagen a una sola celda**
El anclaje de la imagen se define mediante cuatro propiedades de índice basadas en cero:
- `Picture.getUpperLeftRow()` — el índice de fila del borde superior de la imagen.
- `Picture.getUpperLeftColumn()` — el índice de columna del borde izquierdo de la imagen.
- `Picture.getLowerRightRow()` — el índice de fila del borde inferior de la imagen. Para que el borde inferior de la imagen se sitúe en la parte inferior de la fila `r`, establezca este valor en `r + 1`.
- `Picture.getLowerRightColumn()` — el índice de columna del borde derecho de la imagen. Para que el borde derecho de la imagen se sitúe a la derecha de la columna `c`, establezca este valor en `c + 1`.

{{% alert color="primary" %}}
Los índices de fila y columna en Aspose.Cells están **basados en cero**. La celda C6 tiene el índice de fila 5 y el índice de columna 2. Los errores off-by-one en el anclaje inferior derecho son la causa más común de imágenes que parecen superponerse en una celda adyacente.

### **Control del comportamiento de ubicación**
`Picture.getPlacement()` devuelve una enumeración de tipo `PlacementType` que controla cómo se comporta la imagen cuando el usuario cambia el tamaño de la fila o columna situada debajo de ella. El valor recomendado para una imagen de una sola celda es `PlacementType.MOVE_AND_SIZE`, lo que hace que la imagen se mueva y se redimensione junto con su celda subyacente, preservando el ajuste exacto.

### **Instrucciones paso a paso**
1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda a la `Worksheet` de destino desde `workbook.getWorksheets().get(0)`.
3. Abra el archivo de imagen desde el disco en un `InputStream` (como un `FileInputStream`) usando un bloque try-with-resources para que la secuencia se cierre correctamente.
4. Llame a `worksheet.getPictures().add(5, 2, stream)` para agregar una imagen anclada a la celda C6. Capture la referencia `Picture` devuelta.
5. Establezca las cuatro coordenadas de anclaje para que la imagen cubra únicamente la celda C6: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Establezca `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` para mantener la imagen alineada con C6 cuando se cambie el tamaño de la columna o la fila.
7. Opcionalmente, agregue texto de muestra en las celdas circundantes para demostrar que solo la celda C6 contiene la imagen.
8. Guarde el libro en disco como un archivo `.xlsx`.
El siguiente código demuestra el enfoque completo.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
try (FileInputStream fs = new FileInputStream("logo.png"))
{
    int picIndex = worksheet.getPictures().add(5, 2, fs);
    Picture picture = worksheet.getPictures().get(picIndex);
    picture.setUpperLeftRow(5);
    picture.setUpperLeftColumn(2);
    picture.setLowerRightRow(6);
    picture.setLowerRightColumn(3);
    picture.setPlacement(PlacementType.MOVE_AND_SIZE);
}
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Enfoque 2: incrustar una imagen directamente en una celda**
Aspose.Cells también expone un mecanismo más sencillo para imágenes vinculadas a celdas: el método `Cell.setEmbeddedImage(byte[])`. Asignar bytes de imagen a esta propiedad adjunta la imagen a la celda misma, como si fuera contenido en línea.

### **Cómo funcionan las imágenes incrustadas**
- La imagen se almacena como parte del contenido de la celda en lugar de como una forma en la capa de dibujo.
- La imagen se escala automáticamente para ajustarse a los límites representados de la celda. No se requieren coordenadas de anclaje ni ajustes de ubicación.
- La celda sigue siendo una celda real con una dirección real, a la que se puede hacer referencia mediante fórmulas, ordenar como parte de una fila o utilizar en otras operaciones a nivel de celda.
Esto convierte a `setEmbeddedImage()` en la opción más concisa cuando su objetivo es, sencillamente, «una imagen que reside dentro de esta celda».

### **Instrucciones paso a paso**
1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda a la `Worksheet` de destino desde `workbook.getWorksheets().get(0)`.
3. Lea el archivo de imagen desde el disco en un arreglo `byte[]` (por ejemplo, leyendo el archivo mediante `Files.readAllBytes()` desde `java.nio.file`).
4. Obtenga una referencia a la celda de destino, ya sea mediante `worksheet.getCells().get("C6")` o `worksheet.getCells().get(5, 2)`.
5. Asigne el arreglo de bytes a la celda usando `cell.setEmbeddedImage(bytes)`.
6. Opcionalmente, ajuste el alto de fila y el ancho de columna de la fila y columna de destino para dar a la imagen incrustada una apariencia más destacada.
7. Guarde el libro en disco como un archivo `.xlsx`.
El siguiente código demuestra el enfoque completo.

```java
import com.aspose.cells.*;
import java.nio.file.Files;
import java.nio.file.Paths;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Obtener la celda de destino C6
Cell cell = worksheet.getCells().get("C6");
// Leer el archivo de imagen en un arreglo de bytes
byte[] imageData = Files.readAllBytes(Paths.get("logo.png"));
// Incrustar la imagen directamente en la celda
cell.setEmbeddedImage(imageData);
// Opcionalmente ajustar la altura de la fila y el ancho de la columna para que la imagen incrustada sea más visible
worksheet.getCells().setColumnWidth(2, 30);   // Columna C (índice 2)
worksheet.getCells().setRowHeight(5, 100);     // Fila 6 (índice 5)
// Guardar el libro de trabajo resultante como un archivo .xlsx
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Cómo elegir el enfoque adecuado**
Ambos enfoques producen una imagen que cabe dentro de una sola celda, pero difieren en cómo se almacena la imagen y en cómo se comporta:
- **Utilice una imagen flotante (Enfoque 1) cuando:**
  - Necesite un control más preciso sobre la ubicación, el orden en capas o la alineación con otros objetos de dibujo.
  - Desee que la imagen se comporte como una forma que se pueda seleccionar, reordenar o agrupar con otras formas.
  - Requiera compatibilidad heredada con código que ya funciona con `PictureCollection`.
  - Necesite calcular coordenadas de anclaje dinámicamente según el diseño de la hoja de cálculo.
- **Utilice una imagen incrustada (Enfoque 2) cuando:**
  - Desee la inserción más sencilla posible de una imagen en una celda.
  - La imagen deba viajar con la celda como cualquier otro contenido de la celda.
  - No necesite manipular la imagen como una forma.
{{% /alert %}}

{{% /alert %}}

## Artículos relacionados
- [Excel Camera in Aspose.Cells for Java](/cells/es/java/excel-camera/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Java](/cells/es/java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Java](/cells/es/java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/es/java/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for Java](/cells/es/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}