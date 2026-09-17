---
title: Cámara de Excel en Aspose.Cells for Python via Java
linktitle: Cámara de Excel en Aspose.Cells for Python via Java
description: Aprenda a usar la Cámara de Excel en Aspose.Cells for Python via Java para crear una imagen dinámica vinculada a un rango de celdas que se actualiza con los datos de origen y conserva todo el formato de origen.
keywords: Aspose.Cells, Python via Java, Cámara de Excel, imagen dinámica, imagen vinculada, Picture.formula, updateSelectedValue, createRange, toImage, matriz byte[]
type: docs
weight: 90
url: /es/python-java/excel-camera/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La Cámara de Excel es un objeto de hoja de cálculo que muestra una imagen en vivo de un rango de celdas y flota sobre la capa de dibujo como una imagen ordinaria. Aspose.Cells for Python via Java admite dos modos de creación, una imagen dinámica que se actualiza automáticamente cada vez que cambian los datos de origen y una imagen estática que captura una instantánea única de un rango. Este artículo recorre ambos enfoques para que pueda elegir el que mejor se adapte a su diseño.

## ¿Qué es la Cámara de Excel?
La Cámara de Excel es esencialmente un objeto de imagen anclado a una fila y columna específicas en la capa de dibujo de la hoja de cálculo. A diferencia de una imagen insertada normal, la Cámara está vinculada a un rango de origen mediante una fórmula estilo A1 como `"A1:F10"`. Cada vez que cambia cualquier celda dentro de ese rango, la imagen de la Cámara se actualiza automáticamente para reflejar el nuevo contenido. La Cámara conserva el formato completo del área de origen —bordes, colores de fondo, fuentes y formatos de número— de modo que todo lo visible dentro de las celdas también aparece dentro de la imagen de la Cámara. Esto hace que la Cámara sea especialmente útil para paneles de control, resúmenes, paneles laterales y diseños de informes donde se desea una vista previa visible de una región remota sin desplazarse ni repetir datos. Se aplican dos advertencias: debe llamar a `updateSelectedValue()` antes de guardar el libro, y el archivo se exportará a HTML o PDF, porque esos formatos dependen de los datos de imagen incrustados en lugar de un recálculo en vivo.

## Método 1 — Agregar una Imagen de Cámara Dinámica
La Cámara dinámica es el enfoque más común y es el más cercano a la herramienta Cámara integrada de Excel. Funciona agregando una imagen sin contenido de imagen inicial y luego asignándole una fórmula que hace referencia al rango de origen. Después de asignar la fórmula, llamar a `updateSelectedValue()` actualiza los datos de imagen incrustados para que estén sincronizados con las celdas que refleja. La Cámara no se implementa mediante una clase dedicada —se construye completamente sobre el tipo `Picture` estándar.
Las API clave son:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — agrega una imagen anclada en la fila y columna indicadas. Pasar `None` para el parámetro `stream` crea una imagen vacía que actúa como marcador de posición para una Cámara dinámica. El método devuelve el índice de la nueva imagen.
- `worksheet.getPictures().get(index)` — descriptor de acceso para recuperar una `Picture` específica de la colección.
- `Picture.getFormula()` / `Picture.setFormula()` — obtiene/establece la referencia estilo A1 al rango de origen que refleja la Cámara, como `"A1:F10"`.
- `Picture.updateSelectedValue()` — un método void que actualiza los datos de imagen incrustados desde las celdas referenciadas por la fórmula.

{{% alert color="primary" %}}
`updateSelectedValue()` DEBE llamarse antes de guardar cuando la salida es HTML o PDF; de lo contrario, el archivo exportado no contendrá los datos de la imagen y la Cámara aparecerá en blanco en la salida renderizada.
{{% /alert %}}

El siguiente código crea un libro, agrega una imagen vacía anclada en la fila 10 columna 6, la vincula al rango de origen `A1:F10` mediante el método `setFormula`, actualiza los datos de imagen incrustados y guarda el libro.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Cámara Dinámica: agregar una imagen vacía, vincularla mediante Fórmula a A1:F10, luego actualizar
pictures = worksheet.getPictures()
index = pictures.add(10, 6, None)
pictures.get(index).setFormula("A1:F10")
pictures.get(index).updateSelectedValue()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Método 2 — Agregar una Imagen de Cámara Estática
La Cámara estática es esencialmente una vista previa renderizada una sola vez de un rango de celdas. En lugar de mantener un enlace en vivo, renderiza el rango a bytes de imagen una vez, envuelve esos bytes en una matriz `byte[]` y los agrega como una imagen normal. El contenido de la imagen se fija en el momento de la creación y no se actualiza automáticamente cuando cambian las celdas de origen.
Las API clave son:
- `Cells.createRange(String address)` — construye un objeto `Range` a partir de una dirección estilo A1 como `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — renderiza el rango a bytes de imagen. Pasar `None` usa las opciones de renderizado predeterminadas; existen sobrecargas para un control más fino de la salida.
- `byte[] array(byte[] buffer)` — envuelve los bytes de imagen renderizados en una matriz `byte[] array` que se puede alimentar a `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — agrega la imagen anclada en la fila y columna indicadas, esta vez pasando la matriz `byte[] array` producida por el renderizado.
El siguiente código crea un libro, construye un `Range` para `A1:F10`, lo renderiza a bytes de imagen mediante `Range.toImage(None)`, envuelve los bytes en una matriz `byte[]`, agrega la imagen anclada en la fila 10 columna 6 y guarda el libro.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Cámara Estática: construir Range, renderizar a bytes, envolver en ByteArrayInputStream, agregar como imagen
range_ = worksheet.getCells().createRange("A1:F10")
image_bytes = range_.toImage(None)
pictures = worksheet.getPictures()
pictures.add(10, 6, jpype.JArray(jpype.JByte)(image_bytes))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Elección entre Dinámica y Estática
- **Cámara Dinámica:** se actualiza en cada recálculo, admite la exportación a HTML y PDF después de `updateSelectedValue()` y conserva el comportamiento de enlace en vivo durante toda la vida útil del archivo.
- **Cámara Estática:** un renderizado único que nunca se actualiza, útil cuando se desea una instantánea visual fija incrustada en tiempo de compilación en lugar de un espejo en vivo de los datos.
Aspose.Cells for Python via Java admite tanto una Cámara dinámica y de actualización automática construida sobre `setFormula` más `updateSelectedValue()` como una Cámara estática de un solo uso construida sobre `toImage` más una matriz `byte[]`. Elija el enfoque dinámico cuando su salida necesite permanecer sincronizada con las celdas de origen, y elija el enfoque estático cuando solo necesite una instantánea visual fija en tiempo de compilación.

{{< app/cells/assistant language="python" >}}