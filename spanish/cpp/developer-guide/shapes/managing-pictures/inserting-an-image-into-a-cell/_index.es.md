---
title: Insertar una imagen en una celda
description: Aspose.Cells es una biblioteca de C++ para trabajar con archivos de hojas de cálculo. Este artículo explica cómo ajustar una imagen exactamente al tamaño de una sola celda utilizando dos enfoques diferentes: colocar una imagen flotante sobre la celda o incrustar la imagen directamente en la celda.
keywords: Aspose.Cells, C++ library, spreadsheet, insert image, embed image, picture in cell, fit image to cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /es/cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells ofrece dos formas distintas de asociar una imagen con una sola celda. Una imagen flotante es una forma en la capa de dibujo de la hoja de cálculo que se superpone visualmente a un rango de celdas, mientras que una imagen incrustada se almacena dentro de la propia celda y se escala automáticamente al área de visualización de la celda. Elija el enfoque que mejor se adapte a sus requisitos de diseño.

{{% /alert %}}

## **Introducción**

Ajustar una imagen exactamente a una sola celda es un requisito común al diseñar hojas de cálculo que actúan como informes visuales, catálogos de productos, directorios de empleados, paneles de control o listas de inventario. En lugar de estirar una imagen a través de muchas celdas o colocarla de forma imprecisa en una hoja de cálculo, es posible que desee una imagen limpia, vinculada a la celda y alineada con la celda a la que pertenece.

Aspose.Cells admite este escenario de dos formas complementarias:

- **Enfoque 1 — Colocar una imagen flotante sobre una celda.** Añada un `Picture` a la hoja de cálculo, establezca su `Placement` en `MoveAndSize`, y ajuste sus celdas de anclaje (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) para que la imagen cubra exactamente una celda.
- **Enfoque 2 — Incrustar una imagen directamente en una celda.** Asigne los bytes de la imagen a la propiedad `EmbeddedImage` de la celda. La imagen se escala automáticamente para ajustarse al área de visualización de la celda y se desplaza con ella.

El resto de este artículo explica ambos enfoques, describe las API relevantes y muestra cómo utilizarlas en código.

## **Enfoque 1: Colocar una imagen sobre una celda**

Una imagen flotante es un objeto `Picture` que reside en la capa de dibujo de la hoja de cálculo. Aunque no forma parte de ninguna celda individual, está anclado a un rango de celdas. Las celdas de anclaje de la imagen —sus esquinas superior izquierda e inferior derecha— determinan su extensión visual en la hoja de cálculo. Por defecto, una imagen recién añadida abarca varias celdas.

Para que una imagen flotante cubra **exactamente una celda**, debe:

1. Añadir la imagen usando `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)`, que ancla la nueva imagen a la celda indicada.
2. Establecer las cuatro propiedades de anclaje para que el rectángulo delimitador de la imagen coincida con la celda de destino.
3. Establecer `Picture.Placement` en `PlacementType.MoveAndSize` para que la imagen se mueva y cambie de tamaño junto con la celda subyacente cuando el usuario modifique el ancho de columna o la altura de fila.

### **Anclar la imagen a una sola celda**

El anclaje de la imagen se define mediante cuatro propiedades de índice basadas en cero:

- `Picture.UpperLeftRow` — el índice de fila del borde superior de la imagen.
- `Picture.UpperLeftColumn` — el índice de columna del borde izquierdo de la imagen.
- `Picture.LowerRightRow` — el índice de fila del borde inferior de la imagen. Para que el borde inferior de la imagen quede en la parte inferior de la fila `r`, establezca este valor en `r + 1`.
- `Picture.LowerRightColumn` — el índice de columna del borde derecho de la imagen. Para que el borde derecho de la imagen quede en la parte derecha de la columna `c`, establezca este valor en `c + 1`.

Por ejemplo, para ajustar la imagen exactamente a la celda **C6** (índice de fila `5`, índice de columna `2`), establezca `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6` y `LowerRightColumn = 3`.

{{% alert color="primary" %}}

Los índices de fila y columna en Aspose.Cells están **basados en cero**. La celda C6 tiene índice de fila 5 e índice de columna 2. Los errores de diferencia de uno (off-by-one) en el anclaje inferior derecho son la fuente más común de imágenes que parecen superponerse a una celda adyacente.

{{% /alert %}}

### **Controlar el comportamiento de ubicación**

`Picture.Placement` es una enumeración de tipo `PlacementType` que controla cómo se comporta la imagen cuando el usuario cambia el tamaño de la fila o columna situada debajo. El valor recomendado para una imagen de una sola celda es `PlacementType.MoveAndSize`, que hace que la imagen se mueva y cambie de tamaño junto con su celda subyacente, preservando el ajuste exacto.

### **Instrucciones paso a paso**

1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda al `Worksheet` de destino desde `workbook.Worksheets[0]`.
3. Lea el archivo de imagen del disco en un búfer de bytes `Vector<uint8_t>` para que los bytes de la imagen estén disponibles para la API.
4. Llame a `worksheet.Pictures.Add(5, 2, imageData)` para añadir una imagen anclada a la celda C6. Capture la referencia `Picture` devuelta.
5. Establezca las cuatro coordenadas de anclaje para que la imagen cubra solo la celda C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Establezca `picture.Placement = PlacementType.MoveAndSize` para mantener la imagen alineada con C6 cuando se cambie el tamaño de la columna o la fila.
7. Opcionalmente, añada texto de muestra a las celdas circundantes para demostrar que solo la celda C6 contiene la imagen.
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

Aspose.Cells también expone un mecanismo más sencillo para imágenes vinculadas a celdas: la propiedad `Cell.EmbeddedImage`. Asignar bytes de imagen a esta propiedad adjunta la imagen a la propia celda, como si fuera contenido en línea.

### **Cómo funcionan las imágenes incrustadas**

- La imagen se almacena como parte del contenido de la celda en lugar de como una forma en la capa de dibujo.
- La imagen se escala automáticamente para ajustarse a los límites representados de la celda. No se requieren coordenadas de anclaje ni ajustes de ubicación.
- La celda sigue siendo una celda real con una dirección real a la que pueden hacer referencia fórmulas, puede ordenarse como parte de una fila o usarse en otras operaciones a nivel de celda.

Esto hace que `Cell.EmbeddedImage` sea la opción más concisa cuando su objetivo es simplemente "una imagen que vive dentro de esta celda".

### **Instrucciones paso a paso**

1. Cree un nuevo `Workbook` (o abra uno existente).
2. Acceda al `Worksheet` de destino desde `workbook.Worksheets[0]`.
3. Lea el archivo de imagen del disco en un arreglo de bytes `Vector<uint8_t>`.
4. Obtenga una referencia a la celda de destino —ya sea a través de `worksheet.Cells["C6"]` o `worksheet.Cells[5, 2]`.
5. Asigne el arreglo de bytes a la propiedad `EmbeddedImage` de la celda.
6. Opcionalmente, ajuste la altura de fila y el ancho de columna de la fila y columna de destino para dar a la imagen incrustada una apariencia más prominente.
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

    // Convertir std::vector a Aspose::Cells::Vector usando el constructor puntero+tamaño
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());

    // Incrustar la imagen directamente en la celda
    cell.SetEmbeddedImage(imageData);

    // Opcionalmente ajustar la altura de la fila y el ancho de la columna para que la imagen incrustada sea más visible
    worksheet.GetCells().SetColumnWidth(2, 30);   // Columna C (índice 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // Fila 6 (índice 5)

    // Guardar el libro de trabajo resultante como un archivo .xlsx
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Elegir el enfoque adecuado**

Ambos enfoques producen una imagen que se ajusta dentro de una sola celda, pero difieren en cómo se almacena la imagen y cómo se comporta:

- **Use una imagen flotante (Enfoque 1) cuando:**
  - Necesite un control más preciso sobre la ubicación, las capas o la alineación con otros objetos de dibujo.
  - Desee que la imagen se comporte como una forma que pueda seleccionarse, reordenarse o agruparse con otras formas.
  - Requiera compatibilidad heredada con código que ya trabaja con `PictureCollection`.
  - Necesite calcular coordenadas de anclaje dinámicamente según el diseño de la hoja de cálculo.

- **Use una imagen incrustada (Enfoque 2) cuando:**
  - Desee la inserción más sencilla posible de una imagen en una celda.
  - La imagen deba viajar con la celda como cualquier otro contenido de la celda.
  - No necesite manipular la imagen como una forma.

{{% alert color="primary" %}}

Ambos enfoques pueden coexistir en el mismo libro de trabajo. Puede colocar imágenes flotantes sobre un conjunto de celdas e incrustar imágenes directamente en otras celdas, ya que los dos mecanismos utilizan diferentes capas de almacenamiento en el archivo.

{{% /alert %}}

## **Artículos relacionados**

- [Cómo insertar una imagen en una celda](/cells/es/cpp/how-to-place-image-to-cell/)
- [Añadir hipervínculos a imágenes](/cells/es/cpp/add-image-hyperlinks/)
- [Cargar una imagen web desde una URL en una hoja de cálculo de Excel](/cells/es/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipular posición, tamaño y gráfico del diseñador](/cells/es/cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="cpp" >}}