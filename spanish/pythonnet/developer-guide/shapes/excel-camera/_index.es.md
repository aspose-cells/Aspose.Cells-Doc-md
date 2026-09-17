---
title: Excel Camera en Aspose.Cells for Python via .NET
linktitle: Excel Camera en Aspose.Cells for Python via .NET
description: Aprende a usar Excel Camera en Aspose.Cells for Python via .NET para crear una imagen dinámica vinculada a un rango de celdas que se actualiza con los datos de origen y conserva todo el formato de origen.
keywords: Aspose.Cells, Python, Excel Camera, imagen dinámica, imagen vinculada, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, BytesIO
type: docs
weight: 90
url: /es/python-net/excel-camera/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera es un objeto de hoja de cálculo que renderiza una imagen en vivo de un rango de celdas y flota sobre la capa de dibujo como una imagen ordinaria. Aspose.Cells admite dos modos de creación: una imagen dinámica que se actualiza automáticamente cada vez que cambian los datos de origen, y una imagen estática que captura una instantánea única de un rango. Este artículo recorre ambos enfoques para que puedas elegir el que se adapte a tu diseño.

## ¿Qué es Excel Camera?
Excel Camera es esencialmente un objeto de imagen anclado a una fila y columna específicas en la capa de dibujo de la hoja de cálculo. A diferencia de una imagen insertada normal, la Camera está vinculada a un rango de origen mediante una fórmula estilo A1, como `"A1:F10"`. Cada vez que se modifica cualquier celda dentro de ese rango, la imagen de la Camera se actualiza automáticamente para reflejar el nuevo contenido. La Camera conserva el formato completo del área de origen (bordes, colores de fondo, fuentes y formatos de número), por lo que todo lo visible dentro de las celdas también aparece dentro de la imagen de la Camera. Esto hace que la Camera sea especialmente útil para paneles de control, resúmenes, paneles laterales y diseños de informes donde se desea una vista previa visible de una región remota sin desplazarse ni repetir datos. Se aplican dos advertencias: debe invocar `update_selected_value()` antes de guardar el libro, y el archivo se exportará a HTML o PDF, ya que esos formatos dependen de los datos de imagen incrustados en lugar de un recálculo en vivo.

## Método 1 — Agregar una imagen de Camera dinámica
La Camera dinámica es el enfoque más común y es el que más se acerca a la herramienta Camera integrada en Excel. Funciona agregando una imagen sin contenido inicial y luego asignándole una `formula` que haga referencia al rango de origen. Después de asignar la fórmula, llamar a `update_selected_value()` actualiza los datos de imagen incrustados para que estén sincronizados con las celdas que refleja. La Camera no se implementa mediante una clase dedicada: se construye por completo sobre el tipo estándar `Picture`.
Las API clave son:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — agrega una imagen anclada en la fila y columna indicadas. Pasar `None` para el parámetro `stream` crea una imagen vacía que actúa como marcador de posición para una Camera dinámica. El método devuelve el índice de la nueva imagen.
- `worksheet.pictures[index]` — acceso mediante indexador para recuperar una `Picture` específica de la colección.
- `picture.formula` — una propiedad de tipo cadena (get/set) que contiene la referencia estilo A1 al rango de origen que la Camera refleja, como `"A1:F10"`.
- `picture.update_selected_value()` — un método void que actualiza los datos de imagen incrustados a partir de las celdas a las que hace referencia `formula`.

{{% alert color="primary" %}}
Se DEBE llamar a `update_selected_value()` antes de guardar cuando la salida es HTML o PDF; de lo contrario, el archivo exportado no contendrá los datos de la imagen y la Camera aparecerá en blanco en la salida renderizada.
{{% /alert %}}

El siguiente código crea un libro, agrega una imagen vacía anclada en la fila 10 columna 6, la vincula al rango de origen `A1:F10` mediante la propiedad `formula`, actualiza los datos de imagen incrustados y guarda el libro.

```python
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Cámara Dinámica: agregar una imagen vacía, vincularla mediante fórmula a A1:F10, luego actualizar
pictures = worksheet.pictures
index = pictures.add(10, 6, None)
pictures[index].formula = "A1:F10"
pictures[index].update_selected_value()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Método 2 — Agregar una imagen de Camera estática
La Camera estática es esencialmente una vista previa renderizada una sola vez de un rango de celdas. En lugar de mantener un vínculo en vivo, se renderiza el rango a bytes de imagen una vez, se envuelven esos bytes en un `BytesIO` y se agregan como una imagen normal. El contenido de la imagen queda fijado en el momento de la creación y no se actualiza automáticamente cuando cambian las celdas de origen.
Las API clave son:
- `Cells.create_range(string address)` — construye un objeto `Range` a partir de una dirección estilo A1, como `"A1:F10"`.
- `Range.to_image(ImageOrPrintOptions options)` — renderiza el rango a bytes de imagen. Pasar `None` utiliza las opciones de renderizado predeterminadas; existen sobrecargas para un control más fino de la salida.
- `BytesIO(byte[] buffer)` — envuelve los bytes de imagen renderizados en un `BytesIO` que puede proporcionarse a `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — agrega la imagen anclada en la fila y columna indicadas, esta vez pasando el `BytesIO` producido por la renderización.
El siguiente código crea un libro, construye un `Range` para `A1:F10`, lo renderiza a bytes de imagen mediante `Range.to_image(null)`, envuelve los bytes en un `BytesIO`, agrega la imagen anclada en la fila 10 columna 6 y guarda el libro.

```python
from io import BytesIO
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Cámara Estática: construir Range, renderizar a bytes, envolver en BytesIO, añadir como imagen
range_ = worksheet.cells.create_range("A1:F10")
pictures = worksheet.pictures
pictures.add(10, 6, BytesIO(range_.to_image(None)))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Elegir entre dinámica y estática
- **Camera dinámica:** se actualiza en cada recálculo, admite exportación a HTML y PDF después de `update_selected_value()`, y conserva el comportamiento de vínculo en vivo durante toda la vida útil del archivo.
- **Camera estática:** una renderización única que nunca se actualiza, útil cuando se desea una instantánea visual fija incrustada en el momento de la compilación en lugar de un reflejo en vivo de los datos.
Aspose.Cells admite tanto una Camera dinámica y autoactualizable, construida sobre `picture.formula` más `update_selected_value()`, como una Camera estática de una sola toma, construida sobre `Range.to_image` más un `BytesIO`. Elija el enfoque dinámico cuando su salida necesite mantenerse sincronizada con las celdas de origen, y elija el enfoque estático cuando solo necesite una instantánea visual fija en el momento de la compilación.

{{< app/cells/assistant language="python-net" >}}