---
title: Cámara de Excel en Aspose.Cells for Node.js via C++
linktitle: Cámara de Excel en Aspose.Cells for Node.js via C++
description: Aprenda a usar la Cámara de Excel en Aspose.Cells for Node.js via C++ para crear una imagen dinámica vinculada a un rango de celdas que se actualiza con los datos de origen y conserva todo el formato de origen.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, Cámara de Excel, imagen dinámica, imagen vinculada, Picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /es/nodejs-cpp/excel-camera/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La Cámara de Excel es un objeto de la hoja de cálculo que renderiza una imagen en vivo de un rango de celdas y flota sobre la capa de dibujo como una imagen común. Aspose.Cells admite dos modos de creación, una imagen dinámica que se actualiza automáticamente cada vez que cambian los datos de origen y una imagen estática que captura una instantánea única de un rango. Este artículo explica ambos enfoques para que pueda elegir el que mejor se adapte a su diseño.

## ¿Qué es la Cámara de Excel?
La Cámara de Excel es esencialmente un objeto de imagen anclado a una fila y columna específicas en la capa de dibujo de la hoja de cálculo. A diferencia de una imagen insertada normal, la Cámara está vinculada a un rango de origen mediante una fórmula estilo A1, como `"A1:F10"`. Cada vez que cambia cualquier celda dentro de ese rango, la imagen de la Cámara se actualiza automáticamente para reflejar el nuevo contenido. La Cámara conserva el formato completo del área de origen (bordes, colores de fondo, fuentes y formatos de número), de modo que todo lo visible dentro de las celdas también aparece dentro de la imagen de la Cámara. Esto hace que la Cámara sea especialmente útil para paneles, resúmenes, paneles laterales y diseños de informes donde se desea una vista previa visible de una región remota sin tener que desplazarse ni repetir datos. Hay dos advertencias: debe llamar a `updateSelectedValue()` antes de guardar el libro de trabajo y el archivo se exportará a HTML o PDF, ya que esos formatos dependen de los datos de imagen incrustados en lugar de un recálculo en vivo.

## Método 1 — Agregar una imagen de Cámara dinámica
La Cámara dinámica es el enfoque más común y es el que más se acerca a la herramienta Cámara integrada de Excel. Funciona agregando una imagen sin contenido inicial y luego asignándole una `Formula` que hace referencia al rango de origen. Una vez asignada la fórmula, llamar a `updateSelectedValue()` actualiza los datos de imagen incrustados para que estén sincronizados con las celdas que refleja. La Cámara no se implementa mediante una clase dedicada, se construye completamente sobre el tipo estándar `Picture`.
Las API clave son:
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — agrega una imagen anclada en la fila y columna dadas. Pasar `null` para el parámetro `stream` crea una imagen vacía que actúa como marcador de posición para una Cámara dinámica. El método devuelve el índice de la nueva imagen.
- `pictures.get(index)` — recupera una `Picture` específica de la colección por índice.
- `Picture.formula` — una propiedad de cadena (get/set) que contiene la referencia estilo A1 al rango de origen que refleja la Cámara, como `"A1:F10"`.
- `Picture.updateSelectedValue()` — un método void que actualiza los datos de imagen incrustados a partir de las celdas referenciadas por `formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` DEBE llamarse antes de guardar cuando la salida es HTML o PDF; de lo contrario, el archivo exportado no contendrá los datos de la imagen y la Cámara aparecerá en blanco en la salida renderizada.
{{% /alert %}}

El siguiente código crea un libro de trabajo, agrega una imagen vacía anclada en la fila 10, columna 6, la vincula al rango de origen `A1:F10` mediante la propiedad `Formula`, actualiza los datos de imagen incrustados y guarda el libro de trabajo.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.Xlsx);
```

## Método 2 — Agregar una imagen de Cámara estática
La Cámara estática es esencialmente una vista previa renderizada una sola vez de un rango de celdas. En lugar de mantener un enlace en vivo, renderiza el rango a bytes de imagen una vez, envuelve esos bytes en un `Buffer` y los agrega como una imagen normal. El contenido de la imagen queda fijo en el momento de la creación y no se actualiza automáticamente cuando cambian las celdas de origen.
Las API clave son:
- `Cells.createRange(address)` — construye un objeto `Range` a partir de una dirección estilo A1 como `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — renderiza el rango a bytes de imagen. Pasar `null` usa las opciones de renderizado predeterminadas; existen sobrecargas para un control más fino de la salida.
- `new Buffer(byte[] buffer)` — envuelve los bytes de imagen renderizados en un `Buffer` que se puede pasar a `getPictures().add`.
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — agrega la imagen anclada en la fila y columna dadas, esta vez pasando el `Buffer` producido por la renderización.
El siguiente código crea un libro de trabajo, construye un `Range` para `A1:F10`, lo renderiza a bytes de imagen mediante `range.toImage(null)`, envuelve los bytes en un `Buffer`, agrega la imagen anclada en la fila 10, columna 6 y guarda el libro de trabajo.

```javascript
const aspose = require("aspose.cells");
const { MemoryStream } = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Cámara Estática: construir Range, renderizar a bytes, envolver en MemoryStream, agregar como imagen
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let stream = new MemoryStream();
stream.write(imageBytes);
let pictures = worksheet.getPictures();
pictures.add(10, 6, stream);
workbook.save("output_static.xlsx", aspose.SaveFormat.Xlsx);
```

## Elegir entre dinámica y estática
- **Cámara dinámica:** se actualiza en cada recálculo, admite exportación a HTML y PDF después de `updateSelectedValue()` y conserva el comportamiento de enlace en vivo durante toda la vida útil del archivo.
- **Cámara estática:** una renderización única que nunca se actualiza, útil cuando se desea una instantánea visual fija incrustada en el momento de la compilación en lugar de un reflejo en vivo de los datos.
Aspose.Cells admite tanto una Cámara dinámica con auto-actualización construida sobre `Picture.formula` más `updateSelectedValue()` como una Cámara estática de una sola toma construida sobre `Range.toImage` más un `Buffer`. Elija el enfoque dinámico cuando su salida necesite mantenerse sincronizada con las celdas de origen, y elija el enfoque estático cuando solo necesite una instantánea visual fija en el momento de la compilación.

{{< app/cells/assistant language="nodejs-cpp" >}}