---
title: Insertar una imagen en una celda
linktitle: Insertar una imagen en una celda
description: Aspose.Cells es una biblioteca de C++ para trabajar con archivos de hojas de cálculo. Este artículo explica cómo ajustar una imagen exactamente a una sola celda, ya sea colocando una imagen flotante sobre la celda o incrustando la imagen directamente en la celda.
keywords: Aspose.Cells, biblioteca de C++, hoja de cálculo, insertar imagen, incrustar imagen, imagen en celda, ajustar imagen a celda, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /es/cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece dos formas distintas de asociar una imagen con una sola celda. Una imagen flotante es una forma en la capa de dibujo de la hoja de cálculo que se superpone visualmente a un rango de celdas, mientras que una imagen incrustada se almacena dentro de la celda misma y se escala automáticamente al área de visualización de la celda. Elija el enfoque que mejor se adapte a sus requisitos de diseño.

## **Introducción**
Ajustar una imagen exactamente a una sola celda es un requisito común al diseñar hojas de cálculo que actúan como informes visuales, catálogos de productos, directorios de empleados, paneles de control o listas de inventario. En lugar de estirar una imagen a través de muchas celdas o colocarla de manera flexible sobre una hoja de cálculo, puede que quiera una imagen limpia y vinculada a la celda que permanezca alineada con la celda que la contiene.
Aspose.Cells admite este escenario de dos formas complementarias:
- **Enfoque 1: Coloque una imagen flotante sobre una celda.** Agregue un `Picture` a la hoja de cálculo, establezca su `Placement` en `MoveAndSize`, y ajuste sus celdas de anclaje (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) para que la imagen cubra exactamente una celda.
- **Enfoque 2: Incruste una imagen directamente en una celda.** Asigne bytes de imagen a la propiedad `EmbeddedImage` de la celda. La imagen se escala automáticamente para ajustarse al área de visualización de la celda y se desplaza junto con la celda.
El resto de este artículo recorre ambos enfoques, explica las API relevantes y muestra cómo utilizarlas en código.

## **Enfoque 1: Colocar una imagen sobre una celda**
Una imagen flotante es un objeto `Picture` que reside en la capa de dibujo de la hoja de cálculo. Aunque no forma parte de ninguna celda individual, está anclada a un rango de celdas. Las celdas de anclaje de la imagen (sus esquinas superior izquierda e inferior derecha) determinan su extensión visual en la hoja de cálculo. Por defecto, una imagen recién agregada abarca varias celdas.
Para hacer que una imagen flotante cubra **exactamente una celda**, debe:
1. Agregar la imagen usando `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)`, que ancla la nueva imagen a la celda indicada.
2. Establecer las cuatro propiedades de anclaje para que el rectángulo delimitador de la imagen coincida con la celda de destino.
3. Establecer `Picture.Placement` en `PlacementType.MoveAndSize` para que la imagen se mueva y se redimensione con la celda subyacente cuando el usuario cambie el ancho de columna o el alto de fila.

### **Anclar la imagen a una sola celda**
El anclaje de la imagen se define mediante cuatro propiedades de índice basadas en cero:
- `Picture.UpperLeftRow` — el índice de fila del borde superior de la imagen.
- `Picture.UpperLeftColumn` — el índice de columna del borde izquierdo de la imagen.
- `Picture.LowerRightRow` — el índice de fila del borde inferior de la imagen. Para que el borde inferior de la imagen quede en la parte inferior de la fila `r`, establezca esto en `r + 1`.
- `Picture.LowerRightColumn` — el índice de columna del borde derecho de la imagen. Para que el borde derecho de la imagen quede a la derecha de la columna `c`, establezca esto en `c + 1`.

{{% alert color="primary" %}}
Los índices de fila y columna en Aspose.Cells son **basados en cero**. La celda C6 tiene índice de fila 5 e índice de columna 2. Los errores de uno en uno en el ancla inferior derecha son la fuente más común de imágenes que parecen superponerse a una celda adyacente.

### **Controlar el comportamiento de colocación**
`Picture.Placement` es una enumeración de tipo `PlacementType` que controla cómo se comporta la imagen cuando el usuario cambia el tamaño de la fila o columna debajo de ella. El valor recomendado para una imagen de una sola celda es `PlacementType.MoveAndSize`, que hace que la imagen se mueva y se redimensione junto con su celda subyacente, preservando el ajuste exacto.

### **Instrucciones paso a paso**
1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda al `Worksheet` de destino desde `workbook.GetWorksheets().Get(0]`.
3. Lea el archivo de imagen del disco en un búfer de bytes `Vector<uint8_t>` para que los bytes de la imagen estén disponibles para la API.
4. Llame a `worksheet.Pictures.Add(5, 2, imageData)` para agregar una imagen anclada a la celda C6. Capture la referencia `Picture` devuelta.
5. Establezca las cuatro coordenadas de anclaje para que la imagen cubra solo la celda C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Establezca `picture.Placement = PlacementType.MoveAndSize` para mantener la imagen alineada con C6 cuando se cambie el tamaño de la columna o fila.
7. Opcionalmente, agregue texto de muestra a las celdas circundantes para demostrar que solo la celda C6 contiene la imagen.
8. Guarde el libro de trabajo en disco como un archivo `.xlsx`.
El siguiente código demuestra el enfoque completo.

```cpp
#include "Aspose.Cells.h"
#include <fstream>
#include <vector>
#include <iterator>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    std::ifstream fs("logo.png", std::ios::binary);
    std::vector<uint8_t> stdData((std::istreambuf_iterator<char>(fs)),
                                  std::istreambuf_iterator<char>());
    fs.close();
    Vector<uint8_t> imageData(reinterpret_cast<const uint8_t*>(stdData.data()),
                              static_cast<int32_t>(stdData.size()));
    int picIndex = worksheet.GetPictures().Add(5, 2, imageData);
    Picture picture = worksheet.GetPictures().Get(picIndex);
    picture.SetUpperLeftRow(5);
    picture.SetUpperLeftColumn(2);
    picture.SetLowerRightRow(6);
    picture.SetLowerRightColumn(3);
    picture.SetPlacement(PlacementType::MoveAndSize);
    workbook.Save(u"output.xlsx", SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Enfoque 2: Incrustar una imagen directamente en una celda**
Aspose.Cells también expone un mecanismo más simple para imágenes vinculadas a celdas: la propiedad `Cell.EmbeddedImage`. Asignar bytes de imagen a esta propiedad adjunta la imagen a la celda misma, como si fuera contenido en línea.

### **Cómo funcionan las imágenes incrustadas**
- La imagen se almacena como parte del contenido de la celda en lugar de como una forma en la capa de dibujo.
- La imagen se escala automáticamente para ajustarse dentro de los límites renderizados de la celda. No se requieren coordenadas de anclaje ni ajustes de colocación.
- La celda sigue siendo una celda real con una dirección real a la que se puede hacer referencia mediante fórmulas, ordenar como parte de una fila o utilizar en otras operaciones a nivel de celda.
Esto hace que `Cell.EmbeddedImage` sea la opción más concisa cuando su objetivo es simplemente «una imagen que vive dentro de esta celda».

### **Instrucciones paso a paso**
1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda al `Worksheet` de destino desde `workbook.GetWorksheets().Get(0]`.
3. Lea el archivo de imagen del disco en una matriz de bytes `Vector<uint8_t>`.
4. Obtenga una referencia a la celda de destino, ya sea mediante `worksheet.GetCells().Get("C6"])` o `worksheet.GetCells().Get(5, 2]`.
5. Asigne la matriz de bytes a la propiedad `EmbeddedImage` de la celda.
6. Opcionalmente, ajuste el alto de fila y el ancho de columna de la fila y columna de destino para dar a la imagen incrustada una apariencia más prominente.
7. Guarde el libro de trabajo en disco como un archivo `.xlsx`.
El siguiente código demuestra el enfoque completo.

```cpp
#include "Aspose.Cells.h"
#include <vector>
#include <fstream>
#include <iterator>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"C6");
    // Leer el archivo de imagen en un arreglo de bytes
    std::ifstream file("logo.png", std::ios::binary);
    std::vector<uint8_t> stdImageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();
    // Convertir std::vector a Aspose::Cells::Vector usando el constructor de puntero+tamaño
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());
    // Incrustar la imagen directamente en la celda
    cell.SetEmbeddedImage(imageData);
    // Opcionalmente ajustar la altura de la fila y el ancho de la columna para que la imagen incrustada sea más visible
    worksheet.GetCells().SetColumnWidth(2, 30);   // Columna C (índice 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // Fila 6 (índice 5)
    // Guardar el libro resultante como un archivo .xlsx
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Elección del enfoque correcto**
Ambos enfoques producen una imagen que cabe dentro de una sola celda, pero difieren en cómo se almacena la imagen y en cómo se comporta:
- **Use una imagen flotante (Enfoque 1) cuando:**
  - Necesite un control más fino sobre la colocación, el orden de capas o la alineación con otros objetos de dibujo.
  - Desee que la imagen se comporte como una forma que se pueda seleccionar, reordenar o agrupar con otras formas.
  - Requiera compatibilidad heredada con código que ya funciona con `PictureCollection`.
  - Necesite calcular las coordenadas de anclaje dinámicamente según el diseño de la hoja de cálculo.
- **Use una imagen incrustada (Enfoque 2) cuando:**
  - Desee la inserción más simple posible de una imagen en una celda.
  - La imagen deba viajar con la celda como cualquier otro contenido de la celda.
  - No necesite manipular la imagen como una forma.
{{% /alert %}}

{{% /alert %}}

## Artículos relacionados
- [Cámara de Excel en Aspose.Cells for C++](/cells/es/cpp/excel-camera/)
- [Agregar campos de filtro a una Tabla Dinámica en Aspose.Cells for C++](/cells/es/cpp/add-page-field-in-pivot-table/)
- [Aplicar estilos a Tablas Dinámicas en Aspose.Cells for C++](/cells/es/cpp/apply-style-to-pivot-table/)
- [Modificar el diseño de campos de página en una Tabla Dinámica](/cells/es/cpp/change-page-field-layout/)
- [Convertir minigráfico a imagen y HTML en Aspose.Cells for C++](/cells/es/cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="cpp" >}}