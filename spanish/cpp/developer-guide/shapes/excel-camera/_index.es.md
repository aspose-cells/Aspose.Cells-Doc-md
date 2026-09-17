---
title: Cámara de Excel en Aspose.Cells for C++
linktitle: Cámara de Excel en Aspose.Cells for C++
description: Aprenda a usar la Cámara de Excel en Aspose.Cells for C++ para crear una imagen dinámica vinculada a un rango de celdas que se actualiza con los datos de origen y conserva todo el formato de origen.
keywords: Aspose.Cells, C++, Cámara de Excel, imagen dinámica, imagen vinculada, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Vector
type: docs
weight: 90
url: /es/cpp/excel-camera/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La Cámara de Excel es un objeto de la hoja de cálculo que representa una imagen en vivo de un rango de celdas y flota sobre la capa de dibujo como una imagen ordinaria. Aspose.Cells admite dos modos de creación: una imagen dinámica que se actualiza automáticamente cada vez que cambian los datos de origen, y una imagen estática que captura una instantánea única de un rango. Este artículo explica ambos enfoques para que pueda elegir el que mejor se adapte a su diseño.

## ¿Qué es la Cámara de Excel?
La Cámara de Excel es esencialmente un objeto de imagen anclado a una fila y columna específicas en la capa de dibujo de la hoja de cálculo. A diferencia de una imagen insertada normal, la Cámara está vinculada a un rango de origen mediante una fórmula en estilo A1, como `"A1:F10"`. Cada vez que cambia cualquier celda dentro de ese rango, la imagen de la Cámara se actualiza automáticamente para reflejar el nuevo contenido. La Cámara conserva el formato completo del área de origen: bordes, colores de fondo, fuentes y formatos numéricos, de modo que todo lo visible dentro de las celdas también aparece dentro de la imagen de la Cámara. Esto hace que la Cámara sea especialmente útil para paneles de control, resúmenes, paneles laterales y diseños de informes donde se desea una vista previa visible de una región remota sin tener que desplazarse ni repetir datos. Se aplican dos advertencias: debe llamar a `UpdateSelectedValue()` antes de guardar el libro, y el archivo se exportará a HTML o PDF, ya que esos formatos dependen de los datos de imagen incrustados en lugar de un recálculo en vivo.

## Método 1: agregar una imagen de Cámara dinámica
La Cámara dinámica es el enfoque más común y es el equivalente más cercano a la herramienta Cámara integrada de Excel. Funciona agregando una imagen sin contenido inicial y luego asignándole un `Formula` que haga referencia al rango de origen. Una vez asignada la fórmula, llamar a `UpdateSelectedValue()` actualiza los datos de imagen incrustados para que estén sincronizados con las celdas que refleja. La Cámara no se implementa mediante una clase específica: se construye completamente sobre el tipo estándar `Picture`.
Las API clave son:
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — agrega una imagen anclada en la fila y columna indicadas. Pasar un `Vector<uint8_t>()` vacío crea una imagen vacía que actúa como marcador de posición para una Cámara dinámica. El método devuelve el índice de la nueva imagen.
- `worksheet.GetPictures().Get(int index)` — recupera una `Picture` específica de la colección por índice.
- `Picture.SetFormula(U16String value)` — establece la referencia en estilo A1 al rango de origen que refleja la Cámara, como `U16String("A1:F10")`.
- `Picture.UpdateSelectedValue()` — actualiza los datos de imagen incrustados a partir de las celdas a las que hace referencia `Formula`.

{{% alert color="primary" %}}
Se DEBE llamar a `UpdateSelectedValue()` antes de guardar cuando la salida es HTML o PDF; de lo contrario, el archivo exportado no contendrá los datos de la imagen y la Cámara aparecerá en blanco en la salida renderizada.
{{% /alert %}}

El siguiente código crea un libro, agrega una imagen vacía anclada en la fila 10 columna 6, la vincula al rango de origen `A1:F10` mediante la propiedad `Formula`, actualiza los datos de imagen incrustados y guarda el libro.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Cámara Dinámica: agregar una imagen vacía, vincularla mediante Fórmula a A1:F10, luego actualizar
    int index = worksheet.GetPictures().Add(10, 6, Vector<uint8_t>());
    Picture picture = worksheet.GetPictures().Get(index);
    picture.SetFormula(U16String("A1:F10"));
    picture.UpdateSelectedValue();
    workbook.Save(U16String("output_dynamic.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Método 2: agregar una imagen de Cámara estática
La Cámara estática es esencialmente una vista previa renderizada una sola vez de un rango de celdas. En lugar de mantener un enlace en vivo, se renderiza el rango a un búfer de bytes `Vector<uint8_t>` una vez y se pasa ese búfer directamente a `Pictures.Add(row, col, data)`. El contenido de la imagen queda fijo en el momento de la creación y no se actualiza automáticamente cuando cambian las celdas de origen.
Las API clave son:
- `Cells.CreateRange(U16String address)` — construye un objeto `Range` a partir de una dirección en estilo A1, como `U16String("A1:F10")`.
- `Range.ToImage(ImageOrPrintOptions options)` — renderiza el rango a un búfer de bytes `Vector<uint8_t>`. Pasar `nullptr` usa las opciones de renderizado predeterminadas; existen sobrecargas para un control más fino de la salida.
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — agrega la imagen anclada en la fila y columna indicadas, esta vez pasando el búfer de bytes producido por `Range.ToImage`.
El siguiente código crea un libro, construye un `Range` para `A1:F10`, lo renderiza a bytes de imagen mediante `Range.ToImage(nullptr)`, agrega la imagen anclada en la fila 10 columna 6 y guarda el libro.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Cámara estática: construir Rango, renderizar a bytes, agregar como imagen
    Range range = worksheet.GetCells().CreateRange(U16String("A1:F10"));
    Vector<uint8_t> imageBytes = range.ToImage(nullptr);
    worksheet.GetPictures().Add(10, 6, imageBytes);
    workbook.Save(U16String("output_static.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Elegir entre dinámica y estática
- **Cámara dinámica:** se actualiza en cada recálculo, admite exportación a HTML y PDF después de `UpdateSelectedValue()` y conserva el comportamiento de enlace en vivo durante toda la vida útil del archivo.
- **Cámara estática:** un renderizado único que nunca se actualiza, útil cuando se desea una instantánea visual fija incrustada en tiempo de compilación en lugar de un reflejo en vivo de los datos.
Aspose.Cells admite tanto una Cámara dinámica de actualización automática basada en `Picture.Formula` más `UpdateSelectedValue()`, como una Cámara estática de un solo disparo basada en `Range.ToImage` más `Vector<uint8_t>`. Elija el enfoque dinámico cuando su salida necesite mantenerse sincronizada con las celdas de origen, y elija el enfoque estático cuando solo necesite una instantánea visual fija en tiempo de compilación.

{{< app/cells/assistant language="cpp" >}}