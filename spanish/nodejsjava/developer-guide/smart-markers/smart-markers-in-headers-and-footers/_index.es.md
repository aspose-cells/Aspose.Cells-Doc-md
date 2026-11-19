---
title: Marcadores Inteligentes en Encabezados y Pies de Página | Aspose.Cells for Node.js via Java
description: Coloque marcadores inteligentes en los encabezados y pies de página con sintaxis de doble signo angular y el interruptor WorkbookDesigner.setEnableHeaderFooterMarkers usando fuentes de datos JSON, y vincule imágenes mediante URIs de datos, en Aspose.Cells for Node.js via Java.
linktitle: Marcadores Inteligentes en Encabezado y Pie de Página | Aspose.Cells for Node.js via Java
keywords: Aspose.Cells for Node.js via Java, Marcadores Inteligentes, encabezados, pies de página, marcadores de encabezado y pie de página, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, filas JSON, vinculación de datos, imagen, URI de datos, JavaScript
type: docs
weight: 196
url: /es/nodejs-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de Uso Posibles**
Los encabezados y pies de página normalmente contienen metadatos del informe, como el título del informe, el período del informe, el autor y el departamento. Cuando esta información ya existe en la fuente de datos utilizada para rellenar el libro de trabajo, repetirla manualmente genera duplicación innecesaria.
La sintaxis clásica de Marcador Inteligente, `&=Source.Field`, se procesa en las celdas del cuerpo de la hoja de cálculo. Si coloca un marcador clásico en un encabezado o pie de página mediante `PageSetup.setHeader` o `PageSetup.setFooter`, permanecerá como texto literal porque las cadenas de encabezado y pie de página no forman parte de la cuadrícula de celdas escaneada por `WorkbookDesigner.process()`.
A partir de **Aspose.Cells for Node.js via Java 26.11**, la configuración `WorkbookDesigner.setEnableHeaderFooterMarkers`, que por defecto es `false`, hace que `process()` resuelva los marcadores escritos como `<<Source.Field>>` en las cadenas de secciones de encabezado y pie de página. Llame a `designer.setEnableHeaderFooterMarkers(true)` antes de invocar `process()`. Los marcadores de encabezado y pie de página utilizan la misma fuente de datos que los marcadores del cuerpo.
Cada encabezado y pie de página contiene tres secciones direccionables:
- La sección `0` es la sección izquierda.
- La sección `1` es la sección central.
- La sección `2` es la sección derecha.
Utilice `PageSetup.setHeader(int section, String value)` y `PageSetup.setFooter(int section, String value)` para escribir estas secciones. Después del procesamiento, use `PageSetup.getHeader(int section)` y `PageSetup.getFooter(int section)` para obtener el texto completado.

{{% alert color="primary" %}}
Un marcador como `<<Source.Field>>` inserta el valor del campo como texto en la cadena de la sección. Las imágenes se vinculan con el sufijo `(picture)` y un valor URI de datos.
{{% /alert %}}

## **Habilitar Marcadores de Encabezado y Pie con Datos de Filas JSON**
1. Cree un `Workbook` y obtenga su primera `Worksheet` con `workbook.getWorksheets().get(0)`.
2. Escriba marcadores `<<Source.Field>>` en las secciones de encabezado y pie de página deseadas con `PageSetup.setHeader` y `PageSetup.setFooter`.
3. Prepare los datos de filas como una matriz JSON de objetos fila, y elija un nombre de fuente que coincida con el prefijo de fuente utilizado por los marcadores. Por ejemplo, una fuente llamada `node` respalda marcadores como `<<node.Name>>`. Los objetos y matrices JavaScript simples pasados a `setDataSource` no se vinculan en esta plataforma — JSON es la forma tabular admitida.
4. Cree un `WorkbookDesigner` para el libro de trabajo.
5. Llame a `designer.setEnableHeaderFooterMarkers(true)` antes del procesamiento.
6. Adjunte el JSON con `designer.setJsonDataSource("node", '[{"Name":"...","Author":"..."}]')`.
7. Llame a `designer.process()`.
8. Después del procesamiento, los marcadores ya no aparecen en el texto del encabezado o pie de página. Use `getHeader` y `getFooter` para obtener las cadenas de sección completadas.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource(
  "node",
  '[{"Name":"Q4 2026","Author":"Aspose.Cells"}]'
);
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
console.log("Footer: " + worksheet.getPageSetup().getFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx");
```

## **Utilizar una Fuente de Datos JSON**
Cuando los datos del informe ya están disponibles como JSON, una llamada a `setJsonDataSource` puede alimentar todos los estilos de marcadores. Llame a `WorkbookDesigner.setJsonDataSource(String name, String json)` para adjuntar la fuente.
El argumento `name` es el nombre de la fuente utilizada por los marcadores. Por ejemplo, el nombre `node` respalda marcadores como `<<node.Company>>` y `<<node.Title>>`.
Pase los datos de fila directamente a `setJsonDataSource`:
- Se admite una matriz de filas, como una matriz JSON que contiene uno o más objetos fila.
- También se puede pasar directamente un único objeto fila.
- No envuelva las filas bajo una clave de nivel superior con nombre como `{"rows":[...]}`. Este contenedor no es la forma de entrada orientada a filas esperada para este flujo de trabajo.
Una sola fuente JSON puede poblar ambos estilos de marcadores durante la misma llamada a `process()`. Puede resolver un marcador clásico `&=` en una celda del cuerpo de la hoja de cálculo y marcadores de doble signo angular `<<>>` en las secciones de encabezado y pie de página. Aún debe llamar a `designer.setEnableHeaderFooterMarkers(true)` para que los marcadores de encabezado y pie se resuelvan.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
worksheet.getCells().get("A1").putValue("&=node.Company");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]');
designer.process();
console.log("Left: " + worksheet.getPageSetup().getHeader(0));
console.log("Right: " + worksheet.getPageSetup().getHeader(2));
console.log("Body: " + worksheet.getCells().get("A1").getStringValue());
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx");
```

## **Semántica del Interruptor y Fuente Multi-fila**
`setEnableHeaderFooterMarkers` es `false` por defecto, y la configuración controla solo los marcadores `<<Source.Field>>` de encabezado y pie de página. Cuando el interruptor está desactivado, `process()` todavía resuelve los marcadores clásicos `&=` del cuerpo, pero un marcador `<<Source.Field>>` en un encabezado o pie de página permanece como texto literal.
Una sección de encabezado o pie de página es una única cadena, no una banda repetitiva. Si la fuente de datos contiene varias filas, la primera fila suministra los valores del encabezado y pie de página. Una vez resueltos, los valores se convierten en texto de encabezado o pie de página ordinario. Permanecen en el libro de trabajo después de llamar a `save` y están presentes cuando vuelva a cargar el libro guardado.
El siguiente ejemplo crea dos libros de trabajo a partir de la misma fuente JSON multi-fila para contrastar el comportamiento desactivado y activado. El `plainDesigner` deja el marcador sin cambios, mientras que el `enabledDesigner` lo resuelve usando la primera fila.

```javascript
const AsposeCells = require("aspose.cells");
const table = '[{"Name":"First Row"},{"Name":"Second Row"}]';
// Without the switch the placeholder stays literal text
const plainWorkbook = new AsposeCells.Workbook();
const plainSheet = plainWorkbook.getWorksheets().get(0);
plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const plainDesigner = new AsposeCells.WorkbookDesigner(plainWorkbook);
plainDesigner.setJsonDataSource("node", table);
plainDesigner.process();
// With the switch on, the FIRST row of a multi-row source wins
const enabledWorkbook = new AsposeCells.Workbook();
const enabledSheet = enabledWorkbook.getWorksheets().get(0);
enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const enabledDesigner = new AsposeCells.WorkbookDesigner(enabledWorkbook);
enabledDesigner.setEnableHeaderFooterMarkers(true);
enabledDesigner.setJsonDataSource("node", table);
enabledDesigner.process();
console.log("Without switch: " + plainSheet.getPageSetup().getHeader(1));
console.log("With switch: " + enabledSheet.getPageSetup().getHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
```

## **Vincular una Imagen en un Encabezado o Pie de Página**
El sufijo `(picture)` vincula una imagen en una sección de encabezado o pie de página. Escriba `<<node.logo(picture)>>` donde debe aparecer la imagen, y proporcione el valor del campo como una URI de datos — el prefijo `data:image/png;base64,` seguido del texto Base64 de los bytes de la imagen. Una cadena Base64 sin el prefijo `data:` no incrusta una imagen.
Después de `process()`:
1. El marcador se reemplaza por `&G`, el código estándar de imagen para encabezado y pie de página. Como el marcador se convierte en un código dentro de la cadena de la sección, puede estar incrustado en texto más largo como `Logo: <<node.logo(picture)>>`.
2. Los bytes de la imagen se incrustan en el libro de trabajo como una parte multimedia adjunta a la capa de dibujo de encabezado/pie de la hoja de cálculo, por lo que la imagen se imprime con el encabezado/pie.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
const table = [
    {
        logo: "data:image/png;base64," + fs.readFileSync("logo.png").toString("base64")
    }
];
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", JSON.stringify(table));
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
// This prints:
// Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx");
```

El `&G` impreso es el código de imagen que Excel interpreta al renderizar el encabezado — los bytes de `logo.png` ahora están dentro de `HeaderFooterPicture.xlsx`, y la imagen se imprime en lugar del código.
Para usar Marcadores Inteligentes en encabezados y pies de página, escriba marcadores `<<Source.Field>>` en las secciones izquierda, central y derecha del encabezado o pie de página con `setHeader` y `setFooter`. Llame a `designer.setEnableHeaderFooterMarkers(true)` antes de llamar a `process()`, y proporcione los valores mediante `designer.setJsonDataSource(name, json)`. Lea las secciones completadas con `getHeader` y `getFooter`. La misma fuente de datos puede poblar los marcadores del cuerpo y los marcadores de encabezado o pie de página en una sola pasada de procesamiento. Añada el sufijo `(picture)` con un valor URI de datos para vincular una imagen en una sección.

## **Artículos Relacionados**
- [Renderizado de Matriz de Celda Única con SmartMarker](/cells/es/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="nodejs-java" >}}