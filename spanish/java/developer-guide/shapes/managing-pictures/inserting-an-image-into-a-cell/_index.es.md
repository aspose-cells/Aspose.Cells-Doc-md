---
title: Insertar una imagen en una celda
linktitle: Insertar una imagen en una celda
description: Aspose.Cells es una biblioteca de Java para trabajar con archivos de hoja de cálculo. Este artículo explica cómo ajustar exactamente una imagen a una sola celda, ya sea colocando una imagen flotante sobre la celda o incrustando la imagen directamente en ella.
keywords: Aspose.Cells, biblioteca de Java, hoja de cálculo, insertar imagen, incrustar imagen, imagen en una celda, ajustar imagen a la celda, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /es/java/inserting-an-image-into-a-cell/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece dos formas distintas de asociar una imagen con una sola celda. Una imagen flotante es una forma de la capa de dibujo de la hoja de cálculo que se superpone visualmente a un rango de celdas, mientras que una imagen incrustada se almacena dentro de la propia celda y se escala automáticamente para ajustarse al área de visualización de la celda. Elija el enfoque que mejor se adapte a sus requisitos de diseño.
{{% /alert %}}

## **Introducción**
Ajustar una imagen exactamente a una sola celda es un requisito común al diseñar hojas de cálculo que funcionan como informes visuales, catálogos de productos, directorios de empleados, paneles de control o listas de inventario. En lugar de estirar una imagen por muchas celdas o colocarla sin precisión en una hoja de cálculo, es posible que necesite una imagen limpia y vinculada a la celda que permanezca alineada con la celda propietaria.
Aspose.Cells admite este escenario de dos formas complementarias:
- **Enfoque 1: colocar una imagen flotante sobre una celda.** Agregue un `Picture` a la hoja de cálculo, defina su `Placement` en `MOVE_AND_SIZE` y ajuste sus celdas de anclaje (`getUpperLeftRow`, `getUpperLeftColumn`, `getLowerRightRow`, `getLowerRightColumn`) para que la imagen cubra exactamente una celda.
- **Enfoque 2: incrustar una imagen directamente en una celda.** Asigne los bytes de la imagen al método de asignación `getEmbeddedImage()` de la celda. La imagen se escala automáticamente para ajustarse al área de visualización de la celda y se mueve con ella.
El resto de este artículo explica ambos enfoques, describe las API pertinentes y muestra cómo utilizarlas en código.

## **Enfoque 1: colocar una imagen sobre una celda**
Una imagen flotante es un objeto `Picture` que reside en la capa de dibujo de la hoja de cálculo. Aunque no forma parte de ninguna celda concreta, se ancla a un rango de celdas. Las celdas de anclaje de la imagen, es decir, sus esquinas superior izquierda e inferior derecha, determinan su extensión visual en la hoja de cálculo. De forma predeterminada, una imagen recién agregada se extiende por varias celdas.
Para hacer que una imagen flotante cubra **exactamente una celda**, debe:
1. Agregar la imagen mediante `Worksheet.getPictures().add(int row, int column, InputStream stream)`, que ancla la nueva imagen a la celda indicada.
2. Establecer las cuatro propiedades de anclaje para que el rectángulo delimitador de la imagen coincida con la celda de destino.
3. Definir `Picture.setPlacement()` en `PlacementType.MOVE_AND_SIZE` para que la imagen se mueva y cambie de tamaño junto con la celda subyacente cuando el usuario cambie el ancho de la columna o la altura de la fila.

### **Anclar la imagen a una sola celda**
El anclaje de la imagen se define mediante cuatro propiedades de índice con base cero:
- `Picture.getUpperLeftRow()`: el índice de fila del borde superior de la imagen.
- `Picture.getUpperLeftColumn()`: el índice de columna del borde izquierdo de la imagen.
- `Picture.getLowerRightRow()`: el índice de fila del borde inferior de la imagen. Para que el borde inferior de la imagen quede en la parte inferior de la fila `r`, establezca este valor en `r + 1`.
- `Picture.getLowerRightColumn()`: el índice de columna del borde derecho de la imagen. Para que el borde derecho de la imagen quede en el extremo derecho de la columna `c`, establezca este valor en `c + 1`.

{{% alert color="primary" %}}
Los índices de fila y columna en Aspose.Cells son **base cero**. La celda C6 tiene el índice de fila 5 y el índice de columna 2. Los errores de una unidad en el ancla inferior derecha son la causa más común de que las imágenes parezcan invadir una celda adyacente.
{{% /alert %}}

### **Control del comportamiento de colocación**
`Picture.getPlacement()` devuelve un valor de enumeración de tipo `PlacementType` que controla cómo se comporta la imagen cuando el usuario cambia el tamaño de la fila o columna subyacente. El valor recomendado para una imagen ajustada a una sola celda es `PlacementType.MOVE_AND_SIZE`, que hace que la imagen se mueva y cambie de tamaño junto con la celda subyacente, manteniendo el ajuste exacto.

### **Instrucciones paso a paso**
1. Cree un nuevo `Workbook` o abra uno existente.
2. Acceda a la `Worksheet` de destino mediante `workbook.getWorksheets().get(0)`.
3. Abra el archivo de imagen del disco en un `InputStream`, como `FileInputStream`, mediante un bloque try-with-resources para que el flujo se cierre correctamente.
4. Llame a `worksheet.getPictures().add(5, 2, stream)` para agregar una imagen anclada a la celda C6. Conserve la referencia `Picture` devuelta.
5. Establezca las cuatro coordenadas de anclaje para que la imagen cubra únicamente la celda C6: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Defina `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` para mantener la imagen alineada con C6 cuando se cambie el tamaño de la columna o de la fila.
7. Opcionalmente, agregue texto de ejemplo a las celdas circundantes para demostrar que solo la celda C6 contiene la imagen.
8. Guarde el `Workbook` en el disco como un archivo `.xlsx`.
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
Aspose.Cells también ofrece un mecanismo más sencillo para imágenes vinculadas a celdas: el método `Cell.setEmbeddedImage(byte[])`. Al asignar los bytes de la imagen a esta propiedad, la imagen se adjunta a la propia celda como si fuera contenido insertado en línea.

### **Cómo funcionan las imágenes incrustadas**
- La imagen se almacena como parte del contenido de la celda, no como una forma de la capa de dibujo.
- La imagen se escala automáticamente para ajustarse dentro de los límites representationados de la celda. No se requieren coordenadas de anclaje ni ajustes de colocación.
- La celda sigue siendo una celda real con una dirección real que se puede referenciar mediante fórmulas, ordenar como parte de una fila o utilizar en otras operaciones a nivel de celda.
Esto hace que `setEmbeddedImage()` sea la opción más concisa cuando el objetivo es simplemente «una imagen que reside dentro de esta celda».

### **Instrucciones paso a paso**
1. Cree un nuevo `Workbook` o abra uno existente.
2. Acceda a la `Worksheet` de destino mediante `workbook.getWorksheets().get(0)`.
3. Lea el archivo de imagen del disco en una matriz `byte[]`, por ejemplo, leyendo el archivo mediante `Files.readAllBytes()` desde `java.nio.file`.
4. Obtenga una referencia a la celda de destino, ya sea mediante `worksheet.getCells().get("C6")` o `worksheet.getCells().get(5, 2)`.
5. Asigne la matriz de bytes a la celda mediante `cell.setEmbeddedImage(bytes)`.
6. Opcionalmente, ajuste el alto de la fila y el ancho de la columna de destino para dar a la imagen incrustada una apariencia más prominente.
7. Guarde el `Workbook` en el disco como un archivo `.xlsx`.
El siguiente código demuestra el enfoque completo.

```java
import com.aspose.cells.*;
import java.nio.file.Files;
import java.nio.file.Paths;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Obtener la celda objetivo C6
Cell cell = worksheet.getCells().get("C6");
// Leer el archivo de imagen en un array de bytes
byte[] imageData = Files.readAllBytes(Paths.get("logo.png"));
// Incrustar la imagen directamente en la celda
cell.setEmbeddedImage(imageData);
// Opcionalmente, ajustar el alto de la fila y el ancho de la columna para que la imagen incrustada sea más visible
worksheet.getCells().setColumnWidth(2, 30);   // Columna C (índice 2)
worksheet.getCells().setRowHeight(5, 100);     // Fila 6 (índice 5)
// Guardar el libro de trabajo resultante como un archivo .xlsx
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Elección del enfoque adecuado**
Ambos enfoques producen una imagen que se ajusta a una sola celda, pero difieren en cómo se almacena y se comporta:
- **Utilice una imagen flotante (enfoque 1) cuando:**
  - Necesite un control más preciso de la colocación, el orden de capas o la alineación con otros objetos de dibujo.
  - Desee que la imagen se comporte como una forma que pueda seleccionarse, reordenarse o agruparse con otras formas.
  - Necesite compatibilidad con código heredado que ya funciona con `PictureCollection`.
  - Necesite calcular dinámicamente las coordenadas de anclaje según la disposición de la hoja de cálculo.
- **Utilice una imagen incrustada (enfoque 2) cuando:**
  - Desee realizar la inserción de una imagen en una celda de la manera más sencilla posible.
  - La imagen deba moverse con la celda como cualquier otro contenido de esta.

## Artículos relacionados
- [Cámara de Excel en Aspose.Cells for Java](/cells/es/java/excel-camera/)

{{< app/cells/assistant language="java" >}}