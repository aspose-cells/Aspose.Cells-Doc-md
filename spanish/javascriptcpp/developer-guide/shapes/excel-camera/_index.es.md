---
title: Cámara de Excel en Aspose.Cells for JavaScript via C++
linktitle: Cámara de Excel en Aspose.Cells for JavaScript via C++
description: Aprenda a usar la cámara de Excel en Aspose.Cells for JavaScript via C++ para crear una imagen dinámica vinculada a un rango de celdas que se actualiza con los datos de origen y conserva todo el formato de origen.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, Cámara de Excel, imagen dinámica, imagen vinculada, picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /es/javascript-cpp/excel-camera/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La cámara de Excel es un objeto de hoja de cálculo que renderiza una imagen en vivo de un rango de celdas y se coloca en la capa de dibujo como una imagen normal. Aspose.Cells admite dos modos de creación: una imagen dinámica que se actualiza automáticamente cada vez que cambian los datos de origen y una imagen estática que captura una instantánea única de un rango. Este artículo explica ambos enfoques para que pueda elegir el que se ajuste a su diseño.

## ¿Qué es la cámara de Excel?
La cámara de Excel es, en esencia, un objeto de imagen anclado a una fila y una columna concretas de la capa de dibujo de la hoja de cálculo. A diferencia de una imagen insertada normal, la cámara se vincula a un rango de origen mediante una fórmula de estilo A1 como `"A1:F10"`. Cada vez que cambia alguna celda de ese rango, la imagen de la cámara se actualiza automáticamente para reflejar el nuevo contenido. La cámara conserva todo el formato del área de origen —los bordes, los colores de fondo, las fuentes y los formatos numéricos—, por lo que todo lo visible dentro de las celdas aparece también en la imagen de la cámara. Esto resulta especialmente útil para paneles de control, resúmenes, paneles laterales y diseños de informes en los que se desea una vista previa visible de una región remota sin desplazarse ni repetir datos. Se aplican dos advertencias: debe llamar a `updateSelectedValue()` antes de guardar el libro de trabajo y el archivo debe exportarse a HTML o PDF, porque esos formatos dependen de los datos de imagen incrustados en lugar de un recálculo en vivo.

## Método 1 — Agregar una imagen de cámara dinámica
La cámara dinámica es el enfoque más común y el que mejor se ajusta a la herramienta Cámara de Excel integrada. Funciona agregando una imagen sin contenido inicial y, a continuación, asignándole una `formula` que haga referencia al rango de origen. Después de asignar la fórmula, la llamada a `updateSelectedValue()` actualiza los datos de imagen incrustados para mantenerlos sincronizados con las celdas que refleja. La cámara no se implementa mediante una clase dedicada: se construye por completo sobre el tipo `Picture` estándar.
Las API clave son:
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, null)` — agrega una imagen anclada en la fila y la columna indicadas. Al pasar `null` para el parámetro de imagen, se crea una imagen vacía que actúa como marcador de posición para una cámara dinámica. El método devuelve el índice de la nueva imagen.
- `worksheet.getPictures().get(index)` — recupera un objeto `Picture` específico de la colección.
- `picture.formula` — propiedad de cadena que contiene la referencia en estilo A1 al rango de origen que se refleja en la cámara, como `"A1:F10"`.
- `picture.updateSelectedValue()` — método que no devuelve valor y actualiza los datos de imagen incrustados a partir de las celdas referenciadas por `formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` DEBE llamarse antes de guardar cuando la salida sea HTML o PDF; de lo contrario, el archivo exportado no contendrá los datos de la imagen y la cámara aparecerá en blanco en la salida renderizada.
El siguiente código crea un libro de trabajo, agrega una imagen vacía anclada en la fila 10 y la columna 6, la vincula al rango de origen `A1:F10` mediante la propiedad `formula`, actualiza los datos de imagen incrustados y guarda el libro de trabajo.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Cámara dinámica: agregar una imagen vacía, vincularla mediante Formula a A1:F10 y luego actualizar
            const pictures = worksheet.pictures;
            const index = pictures.add(10, 6, null);
            const picture = pictures.get(0);
            picture.formula = "A1:F10";
            picture.updateSelectedValue();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_dynamic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Método 2 — Agregar una imagen de cámara estática
La cámara estática es, en esencia, una vista previa renderizada una sola vez de un rango de celdas. En lugar de mantener un vínculo en vivo, se renderiza el rango una vez para obtener los bytes de imagen, se envuelven esos bytes en un `Buffer` y se agregan como una imagen normal. El contenido de la imagen queda fijo en el momento de su creación y no se actualiza automáticamente cuando cambian las celdas de origen.
Las API clave son:
- `cells.createRange(address)` — construye un objeto `Range` a partir de una dirección en estilo A1 como `"A1:F10"`.
- `range.toImage(options)` — renderiza el rango para obtener los bytes de imagen. Al pasar `null`, se usan las opciones de renderizado predeterminadas; existen sobrecargas que ofrecen un control más preciso de la salida.
- `Buffer.from(imageBytes)` — envuelve los bytes de imagen renderizados en un `Buffer` que se puede pasar a `worksheet.getPictures().add`.
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, imageBuffer)` — agrega la imagen anclada en la fila y la columna indicadas; en este caso, se pasa el `Buffer` generado por el renderizado.
El siguiente código crea un libro de trabajo, construye un `Range` para `A1:F10`, lo renderiza para obtener bytes de imagen mediante `range.toImage(null)`, envuelve los bytes en un `Buffer`, agrega la imagen anclada en la fila 10 y la columna 6 y guarda el libro de trabajo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Cámara estática: crear Range, renderizar a bytes, envolver en MemoryStream y agregar como imagen
            const range = worksheet.cells.createRange("A1:F10");
            const imageData = range.toImage();
            const pictures = worksheet.pictures;
            pictures.add(10, 6, imageData);
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_static.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Elección entre una cámara dinámica y una estática
- **Cámara dinámica:** se actualiza en cada recálculo, admite la exportación a HTML y PDF después de `updateSelectedValue()` y conserva el comportamiento de vínculo en vivo durante toda la vigencia del archivo.
- **Cámara estática:** es un renderizado único que nunca se actualiza; resulta útil cuando se desea una instantánea visual fija incrustada en tiempo de compilación, en lugar de una réplica en vivo de los datos.
Aspose.Cells admite tanto una cámara dinámica con actualización automática, basada en `picture.formula` más `updateSelectedValue()`, como una cámara estática de un solo uso, basada en `range.toImage` más un `Buffer`. Elija el enfoque dinámico cuando la salida deba mantenerse sincronizada con las celdas de origen y el enfoque estático cuando solo necesite una instantánea visual fija en tiempo de compilación.

## Artículos relacionados
- [Convertir una sparkline en una imagen y HTML en Aspose.Cells for JavaScript via C++](/cells/es/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Agregar campos de filtro a una tabla dinámica en Aspose.Cells for JavaScript via C++](/cells/es/javascript-cpp/add-page-field-in-pivot-table/)
- [Aplicar estilos a tablas dinámicas en Aspose.Cells for JavaScript via C++](/cells/es/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}