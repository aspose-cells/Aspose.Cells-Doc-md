---
title: Cámara de Excel en Aspose.Cells for .NET
description: Aprenda a usar la Cámara de Excel en Aspose.Cells for .NET para crear una imagen dinámica vinculada a un rango de celdas que se actualiza con los datos de origen y conserva todo el formato de origen.
linktitle: Cámara de Excel
keywords: Aspose.Cells, .NET, Cámara de Excel, imagen dinámica, imagen vinculada, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, MemoryStream
type: docs
weight: 90
url: /es/net/excel-camera/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La Cámara de Excel es un objeto de hoja de cálculo que renderiza una imagen en vivo de un rango de celdas y flota sobre la capa de dibujo como una imagen ordinaria. Aspose.Cells admite dos modos de creación, una imagen dinámica que se actualiza automáticamente cuando los datos de origen cambian y una imagen estática que captura una instantánea de un rango. Este artículo recorre ambos enfoques para que pueda elegir el que se adapte a su diseño.

## ¿Qué es la Cámara de Excel?
La Cámara de Excel es esencialmente un objeto de imagen anclado a una fila y columna específicas en la capa de dibujo de la hoja de cálculo. A diferencia de una imagen insertada normal, la Cámara está vinculada a un rango de origen mediante una fórmula estilo A1 como `"A1:F10"`. Cuando cualquier celda dentro de ese rango cambia, la imagen de la Cámara se actualiza automáticamente para reflejar el nuevo contenido. La Cámara conserva el formato completo del área de origen (bordes, colores de fondo, fuentes y formatos de número), por lo que todo lo visible dentro de las celdas aparece también dentro de la imagen de la Cámara. Esto hace que la Cámara sea especialmente útil para paneles, resúmenes, paneles laterales y diseños de informes donde se desea una vista previa visible de una región remota sin desplazarse ni repetir datos. Se aplican dos advertencias: debe llamar a `UpdateSelectedValue()` antes de guardar el libro de trabajo, y el archivo se exportará a HTML o PDF, ya que esos formatos dependen de los datos de imagen incrustados en lugar de un recálculo en vivo.

## Método 1: agregar una imagen de Cámara dinámica
La Cámara dinámica es el enfoque más común y es el equivalente más cercano a la herramienta de Cámara integrada en Excel. Funciona agregando una imagen sin contenido de imagen inicial y luego asignándole una `Formula` que hace referencia al rango de origen. Después de asignar la fórmula, llamar a `UpdateSelectedValue()` actualiza los datos de imagen incrustados para que estén sincronizados con las celdas que refleja. La Cámara no se implementa a través de una clase dedicada; se construye por completo sobre el tipo estándar `Picture`.
Las API clave son:
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — agrega una imagen anclada en la fila y columna dadas. Pasar `null` para el parámetro `stream` crea una imagen vacía que actúa como marcador de posición para una Cámara dinámica. El método devuelve el índice de la nueva imagen.
- `worksheet.Pictures[index]` — acceso por índice para recuperar un `Picture` específico de la colección.
- `Picture.Formula` — una propiedad de cadena (get/set) que contiene la referencia estilo A1 al rango de origen que la Cámara refleja, como `"A1:F10"`.
- `Picture.UpdateSelectedValue()` — un método void que actualiza los datos de imagen incrustados desde las celdas a las que hace referencia `Formula`.

{{% alert color="primary" %}}
Se DEBE llamar a `UpdateSelectedValue()` antes de guardar cuando la salida es HTML o PDF; de lo contrario, el archivo exportado no contendrá los datos de imagen y la Cámara aparecerá en blanco en la salida renderizada.
{{% /alert %}}

El siguiente código crea un libro de trabajo, agrega una imagen vacía anclada en la fila 10 columna 6, la vincula al rango de origen `A1:F10` mediante la propiedad `Formula`, actualiza los datos de imagen incrustados y guarda el libro de trabajo.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Cámara Dinámica: añade una imagen vacía, la vincula mediante Fórmula a A1:F10, luego actualiza
var pictures = worksheet.Pictures;
int index = pictures.Add(10, 6, (Stream)null);
pictures[0].Formula = "A1:F10";
pictures[0].UpdateSelectedValue();
workbook.Save("output_dynamic.xlsx", SaveFormat.Xlsx);
```

## Método 2: agregar una imagen de Cámara estática
La Cámara estática es esencialmente una vista previa renderizada de una sola vez de un rango de celdas. En lugar de mantener un enlace en vivo, renderiza el rango a bytes de imagen una vez, envuelve esos bytes en un `MemoryStream` y los agrega como una imagen normal. El contenido de la imagen se fija en el momento de la creación y no se actualiza automáticamente cuando cambian las celdas de origen.
Las API clave son:
- `Cells.CreateRange(string address)` — construye un objeto `Range` a partir de una dirección estilo A1 como `"A1:F10"`.
- `Range.ToImage(ImageOrPrintOptions options)` — renderiza el rango a bytes de imagen. Pasar `null` usa las opciones de renderizado predeterminadas; existen sobrecargas para un control más detallado sobre la salida.
- `new MemoryStream(byte[] buffer)` — envuelve los bytes de imagen renderizados en un `MemoryStream` que se puede alimentar a `PictureCollection.Add`.
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — agrega la imagen anclada en la fila y columna dadas, esta vez pasando el `MemoryStream` producido por la renderización.
El siguiente código crea un libro de trabajo, construye un `Range` para `A1:F10`, lo renderiza a bytes de imagen mediante `Range.ToImage(null)`, envuelve los bytes en un `MemoryStream`, agrega la imagen anclada en la fila 10 columna 6 y guarda el libro de trabajo.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Cámara Estática: construir Range, renderizar a bytes, envolver en MemoryStream, agregar como imagen
var range = workbook.Worksheets[0].Cells.CreateRange("A1:F10");
var pictures = worksheet.Pictures;
pictures.Add(10, 6, new MemoryStream(range.ToImage(null)));
workbook.Save("output_static.xlsx", SaveFormat.Xlsx);
```

## Elegir entre dinámica y estática
- **Cámara dinámica:** se actualiza en cada recálculo, admite exportación a HTML y PDF después de `UpdateSelectedValue()`, y conserva el comportamiento de enlace en vivo a lo largo de la vida útil del archivo.
- **Cámara estática:** una renderización de una sola vez que nunca se actualiza, útil cuando se desea una instantánea visual fija incrustada en tiempo de compilación en lugar de un espejo en vivo de los datos.
Aspose.Cells admite tanto una Cámara dinámica de actualización automática construida sobre `Picture.Formula` más `UpdateSelectedValue()` como una Cámara estática de una sola toma construida sobre `Range.ToImage` más un `MemoryStream`. Elija el enfoque dinámico cuando su salida necesite permanecer sincronizada con las celdas de origen, y elija el enfoque estático cuando solo necesite una instantánea visual fija en tiempo de compilación.

## Artículos relacionados
- [Convertir Sparkline en imagen y HTML en Aspose.Cells for .NET](/cells/es/net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="csharp" >}}