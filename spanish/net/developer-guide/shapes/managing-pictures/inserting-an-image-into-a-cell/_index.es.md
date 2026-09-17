---
title: Insertar una imagen en una celda
linktitle: Insertar una imagen en una celda
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo. Este artículo explica cómo ajustar una imagen exactamente a una sola celda, ya sea colocando una imagen flotante sobre la celda o incrustando la imagen directamente en la celda.
keywords: Aspose.Cells, biblioteca NET, hoja de cálculo, insertar imagen, incrustar imagen, imagen en celda, ajustar imagen a celda, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /es/net/inserting-an-image-into-a-cell/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece dos formas distintas de asociar una imagen con una sola celda. Una imagen flotante es una forma en la capa de dibujo de la hoja de cálculo que se superpone visualmente a un rango de celdas, mientras que una imagen incrustada se almacena dentro de la propia celda y se escala automáticamente al área de visualización de la celda. Elija el enfoque que mejor se adapte a sus requisitos de diseño.

## **Introducción**
Ajustar una imagen exactamente a una sola celda es un requisito común al diseñar hojas de cálculo que actúan como informes visuales, catálogos de productos, directorios de empleados, paneles de control o listas de inventario. En lugar de extender una imagen a lo largo de muchas celdas o colocarla de forma dispersa en una hoja de cálculo, es posible que desee una imagen limpia y vinculada a la celda que permanezca alineada con la celda a la que pertenece.
Aspose.Cells admite este escenario de dos formas complementarias:
- **Enfoque 1 — Colocar una imagen flotante sobre una celda.** Agregue un `Picture` a la hoja de cálculo, establezca su `Placement` en `MoveAndSize` y ajuste sus celdas de anclaje (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) para que la imagen cubra exactamente una celda.
- **Enfoque 2 — Incrustar una imagen directamente en una celda.** Asigne bytes de imagen a la propiedad `EmbeddedImage` de la celda. La imagen se escala automáticamente para ajustarse al área de visualización de la celda y viaja con la celda.
El resto de este artículo recorre ambos enfoques, explica las API relevantes y muestra cómo utilizarlos en el código.

## **Enfoque 1: Colocar una imagen sobre una celda**
Una imagen flotante es un objeto `Picture` que vive en la capa de dibujo de la hoja de cálculo. Aunque no forma parte de ninguna celda individual, está anclada a un rango de celdas. Las celdas de anclaje de la imagen (sus esquinas superior izquierda e inferior derecha) determinan su extensión visual en la hoja de cálculo. Por defecto, una imagen recién agregada abarca varias celdas.
Para hacer que una imagen flotante cubra **exactamente una celda**, debe:
1. Agregue la imagen usando `Worksheet.Pictures.Add(int row, int column, Stream stream)`, que ancla la nueva imagen a la celda indicada.
2. Establezca las cuatro propiedades de anclaje para que el rectángulo delimitador de la imagen coincida con la celda de destino.
3. Establezca `Picture.Placement` en `PlacementType.MoveAndSize` para que la imagen se mueva y cambie de tamaño junto con la celda subyacente cuando el usuario cambie el ancho de columna o la altura de fila.

### **Anclar la imagen a una sola celda**
El ancla de la imagen está definida por cuatro propiedades de índice basadas en cero:
- `Picture.UpperLeftRow` — el índice de fila del borde superior de la imagen.
- `Picture.UpperLeftColumn` — el índice de columna del borde izquierdo de la imagen.
- `Picture.LowerRightRow` — el índice de fila del borde inferior de la imagen. Para que el borde inferior de la imagen se sitúe en la parte inferior de la fila `r`, establezca este valor en `r + 1`.
- `Picture.LowerRightColumn` — el índice de columna del borde derecho de la imagen. Para que el borde derecho de la imagen se sitúe en el lado derecho de la columna `c`, establezca este valor en `c + 1`.

{{% alert color="primary" %}}
Los índices de fila y columna en Aspose.Cells están **basados en cero**. La celda C6 tiene índice de fila 5 e índice de columna 2. Los errores de uno en uno en el ancla inferior derecha son la fuente más común de imágenes que parecen superponerse a una celda adyacente.

### **Controlar el comportamiento de ubicación**
`Picture.Placement` es una enumeración de tipo `PlacementType` que controla cómo se comporta la imagen cuando el usuario cambia el tamaño de la fila o columna debajo de ella. El valor recomendado para una imagen de una sola celda es `PlacementType.MoveAndSize`, que hace que la imagen se mueva y cambie de tamaño junto con su celda subyacente, conservando el ajuste exacto.

### **Instrucciones paso a paso**
1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda a la `Worksheet` de destino desde `workbook.Worksheets[0]`.
3. Abra el archivo de imagen desde disco en un `FileStream` utilizando un bloque `using` para que el flujo se libere correctamente.
4. Llame a `worksheet.Pictures.Add(5, 2, stream)` para agregar una imagen anclada a la celda C6. Capture la referencia `Picture` devuelta.
5. Establezca las cuatro coordenadas de anclaje para que la imagen cubra solo la celda C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Establezca `picture.Placement = PlacementType.MoveAndSize` para mantener la imagen alineada con C6 cuando se cambie el tamaño de la columna o fila.
7. Opcionalmente, agregue texto de muestra a las celdas circundantes para demostrar que solo la celda C6 contiene la imagen.
8. Guarde el libro en disco como un archivo `.xlsx`.
El siguiente código demuestra el enfoque completo.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Drawing;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
using (FileStream fs = new FileStream("logo.png", FileMode.Open, FileAccess.Read))
{
    int picIndex = worksheet.Pictures.Add(5, 2, fs);
    Picture picture = worksheet.Pictures[picIndex];
    picture.UpperLeftRow = 5;
    picture.UpperLeftColumn = 2;
    picture.LowerRightRow = 6;
    picture.LowerRightColumn = 3;
    picture.Placement = PlacementType.MoveAndSize;
}
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Enfoque 2: Incrustar una imagen directamente en una celda**
Aspose.Cells también expone un mecanismo más simple para imágenes vinculadas a celdas: la propiedad `Cell.EmbeddedImage`. Asignar bytes de imagen a esta propiedad adjunta la imagen a la celda misma, como si fuera contenido en línea.

### **Cómo funcionan las imágenes incrustadas**
- La imagen se almacena como parte del contenido de la celda en lugar de como una forma en la capa de dibujo.
- La imagen se escala automáticamente para ajustarse a los límites representados de la celda. No se requieren coordenadas de anclaje ni ajustes de ubicación.
- La celda sigue siendo una celda real con una dirección real a la que se puede hacer referencia mediante fórmulas, ordenar como parte de una fila o usar en otras operaciones a nivel de celda.
Esto hace que `Cell.EmbeddedImage` sea la opción más concisa cuando su objetivo es simplemente "una imagen que vive dentro de esta celda".

### **Instrucciones paso a paso**
1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda a la `Worksheet` de destino desde `workbook.Worksheets[0]`.
3. Lea el archivo de imagen desde disco en un arreglo `byte[]` (por ejemplo, usando `File.ReadAllBytes`).
4. Obtenga una referencia a la celda de destino, ya sea mediante `worksheet.Cells["C6"]` o `worksheet.Cells[5, 2]`.
5. Asigne el arreglo de bytes a la propiedad `EmbeddedImage` de la celda.
6. Opcionalmente, ajuste la altura de fila y el ancho de columna de la fila y columna de destino para dar a la imagen incrustada una apariencia más prominente.
7. Guarde el libro en disco como un archivo `.xlsx`.
El siguiente código demuestra el enfoque completo.

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// Obtener la celda objetivo C6
var cell = worksheet.Cells["C6"];
// Leer el archivo de imagen en un arreglo de bytes
byte[] imageData = File.ReadAllBytes("logo.png");
// Incrustar la imagen directamente en la celda
cell.EmbeddedImage = imageData;
// Opcionalmente ajustar la altura de la fila y el ancho de la columna para que la imagen incrustada sea más visible
worksheet.Cells.SetColumnWidth(2, 30);   // Columna C (índice 2)
worksheet.Cells.SetRowHeight(5, 100);     // Fila 6 (índice 5)
// Guardar el libro resultante como un archivo .xlsx
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Elegir el enfoque correcto**
Ambos enfoques producen una imagen que cabe dentro de una sola celda, pero difieren en cómo se almacena la imagen y cómo se comporta:
- **Use una imagen flotante (Enfoque 1) cuando:**
  - Necesita un control más fino sobre la ubicación, las capas o la alineación con otros objetos de dibujo.
  - Desea que la imagen se comporte como una forma que se pueda seleccionar, reordenar o agrupar con otras formas.
  - Requiere compatibilidad heredada con código que ya funciona con `PictureCollection`.
  - Necesita calcular coordenadas de anclaje dinámicamente según el diseño de la hoja de cálculo.
- **Use una imagen incrustada (Enfoque 2) cuando:**
  - Desea la inserción más simple posible de una imagen en una celda.
  - La imagen debe viajar con la celda como cualquier otro contenido de celda.
  - No necesita manipular la imagen como una forma.
{{% /alert %}}

{{% /alert %}}

## Artículos relacionados
- [Cámara de Excel en Aspose.Cells for .NET](/cells/es/net/excel-camera/)
- [Agregar campos de filtro a una tabla dinámica en Aspose.Cells for .NET](/cells/es/net/add-page-field-in-pivot-table/)
- [Aplicar estilos a tablas dinámicas en Aspose.Cells for .NET](/cells/es/net/apply-style-to-pivot-table/)
- [Modificar el diseño del campo de página en una tabla dinámica](/cells/es/net/change-page-field-layout/)
- [Convertir minigráfico a imagen y HTML en Aspose.Cells for .NET](/cells/es/net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="csharp" >}}