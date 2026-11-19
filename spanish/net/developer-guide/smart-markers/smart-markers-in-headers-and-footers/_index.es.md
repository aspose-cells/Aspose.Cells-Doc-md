---
title: Marcadores Inteligentes en Encabezados y Pies de página | Aspose.Cells .NET
linktitle: Marcadores inteligentes de encabezado y pie de página | Aspose.Cells
description: Coloque marcadores inteligentes en los encabezados y pies de página con sintaxis de doble corchete angular y el conmutador WorkbookDesigner.EnableHeaderFooterMarkers, utilizando fuentes de datos DataTable o JSON, y vincule imágenes mediante URI de datos, en Aspose.Cells for .NET.
keywords: Aspose.Cells, Marcadores Inteligentes, encabezados, pies de página, marcadores de encabezado y pie de página, EnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, SetHeader, SetFooter, SetJsonDataSource, DataTable, vinculación de datos, imagen, data URI, C#
type: docs
weight: 196
url: /es/net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de Uso Posibles**
Los encabezados y pies de página suelen contener metadatos del informe, como el título del informe, el período del informe, el autor y el departamento. Cuando esta información ya existe en la fuente de datos utilizada para rellenar el libro de trabajo, repetirla manualmente crea una duplicación innecesaria.
La sintaxis clásica de Marcadores Inteligentes, `&=Source.Field`, se procesa en las celdas del cuerpo de la hoja de cálculo. Si coloca un marcador clásico en un encabezado o pie de página mediante `PageSetup.SetHeader` o `PageSetup.SetFooter`, permanecerá como texto literal porque las cadenas de encabezado y pie de página no forman parte de la cuadrícula de celdas escaneada por `WorkbookDesigner.Process()`.
A partir de **Aspose.Cells for .NET 26.11**, el interruptor `WorkbookDesigner.EnableHeaderFooterMarkers`, que por defecto es `false`, hace que `Process()` resuelva los marcadores de posición escritos como `<<Source.Field>>` en las cadenas de las secciones de encabezado y pie de página — establézcalo en `true` antes de llamar a `Process()`. Los marcadores de posición de encabezado y pie de página usan la misma fuente de datos que los marcadores del cuerpo.
Cada encabezado y pie de página contiene tres secciones direccionables:
- La sección `0` es la sección izquierda.
- La sección `1` es la sección central.
- La sección `2` es la sección derecha.
Utilice `PageSetup.SetHeader(int section, string value)` y `PageSetup.SetFooter(int section, string value)` para escribir estas secciones. Después del procesamiento, use `PageSetup.GetHeader(int section)` y `PageSetup.GetFooter(int section)` para obtener el texto completado.

{{% alert color="primary" %}}
Un marcador como `<<Source.Field>>` inserta el valor del campo como texto en la cadena de la sección. Las imágenes se vinculan con el sufijo `(picture)` y un valor de data-URI.
{{% /alert %}}

## **Habilitar Marcadores de Encabezado/Pie de Página con un DataTable**
Utilice la siguiente secuencia para resolver los marcadores de posición de encabezado y pie de página con un `DataTable` en **Aspose.Cells for .NET 26.11**:
1. Cree un `Workbook` y obtenga su primera `Worksheet` en el índice `0`.
2. Escriba marcadores de posición `<<Source.Field>>` en las secciones de encabezado y pie de página deseadas mediante `PageSetup.SetHeader` y `PageSetup.SetFooter`.
3. Cree un `DataTable` cuyo nombre de tabla coincida con el prefijo de origen usado por los marcadores de posición. Por ejemplo, una tabla llamada `node` respalda marcadores como `<<node.Name>>`.
4. Cree un `WorkbookDesigner` para el libro de trabajo.
5. Establezca `designer.EnableHeaderFooterMarkers` en `true` antes del procesamiento.
6. Adjunte la tabla con `designer.SetDataSource(table)`.
7. Llame a `designer.Process()`.
8. Después del procesamiento, los marcadores de posición ya no están presentes en el texto del encabezado o pie de página. Utilice `GetHeader` y `GetFooter` para obtener las cadenas de sección completadas.

```csharp
using System;
using System.Data;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.PageSetup.SetHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.PageSetup.SetFooter(1, "Prepared by <<node.Author>>");
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Columns.Add("Author");
table.Rows.Add("Q4 2026", "Aspose.Cells");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
Console.WriteLine("Footer: " + worksheet.PageSetup.GetFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.Save("HeaderFooterSmartMarkers.xlsx");
```

## **Usar una Fuente de Datos JSON**
Puede usar JSON en lugar de un `DataTable` cuando los datos del informe ya están disponibles en formato JSON. Llame a `WorkbookDesigner.SetJsonDataSource(string name, string json)` para adjuntar la fuente.
El argumento `name` tiene el mismo papel que el nombre del `DataTable`. Por ejemplo, el nombre `node` respalda marcadores como `<<node.Company>>` y `<<node.Title>>`.
Pase los datos de fila directamente a `SetJsonDataSource`:
- Se admite una matriz de filas, como una matriz JSON que contiene uno o más objetos de fila.
- También se puede pasar directamente un único objeto de fila.
- No envuelva las filas bajo una clave superior con nombre, como `{"rows":[...]}`. Este contenedor no es la forma de entrada orientada a filas esperada para este flujo de trabajo.
Una fuente JSON puede poblar ambos estilos de marcadores durante la misma llamada a `Process()`. Puede resolver un marcador clásico `&=` en una celda del cuerpo de la hoja y marcadores de posición de doble ángulo `<<>>` en las secciones de encabezado y pie de página. Aún debe habilitar `EnableHeaderFooterMarkers` para que los marcadores de posición de encabezado y pie de página se resuelvan.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.PageSetup.SetHeader(0, "<<node.Company>>");
worksheet.PageSetup.SetHeader(2, "Page <<node.Title>>");
worksheet.Cells["A1"].PutValue("&=node.Company");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
designer.Process();
Console.WriteLine("Left: " + worksheet.PageSetup.GetHeader(0));
Console.WriteLine("Right: " + worksheet.PageSetup.GetHeader(2));
Console.WriteLine("Body: " + worksheet.Cells["A1"].StringValue);
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.Save("HeaderFooterJsonMarkers.xlsx");
```

## **Semántica del Interruptor y Fuente Multi-fila**
`EnableHeaderFooterMarkers` es `false` por defecto, y el interruptor controla solo los marcadores de posición `<<Source.Field>>` de encabezado y pie de página. Cuando el interruptor está desactivado, `Process()` sigue resolviendo los marcadores clásicos `&=` del cuerpo, pero un marcador `<<Source.Field>>` en un encabezado o pie de página permanece como texto literal.
Una sección de encabezado o pie de página es una única cadena, no una banda repetitiva. Si la fuente de datos contiene varias filas, la primera fila proporciona los valores de encabezado y pie de página. Una vez resueltos, los valores se convierten en texto ordinario de encabezado o pie de página. Permanecen en el libro de trabajo después de llamar a `Save` y están presentes cuando vuelve a cargar el libro guardado.
El siguiente ejemplo crea dos libros de trabajo sobre el mismo `DataTable` multi-fila para contrastar el comportamiento deshabilitado y habilitado. El `plainDesigner` deja el marcador sin cambios, mientras que el `enabledDesigner` lo resuelve usando la primera fila.

```csharp
using System;
using System.Data;
using Aspose.Cells;
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Rows.Add("First Row");
table.Rows.Add("Second Row");
// Without the switch the placeholder stays literal text
Workbook plainWorkbook = new Workbook();
Worksheet plainSheet = plainWorkbook.Worksheets[0];
plainSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
plainDesigner.SetDataSource(table);
plainDesigner.Process();
// With the switch on, the FIRST row of a multi-row source wins
Workbook enabledWorkbook = new Workbook();
Worksheet enabledSheet = enabledWorkbook.Worksheets[0];
enabledSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
enabledDesigner.EnableHeaderFooterMarkers = true;
enabledDesigner.SetDataSource(table);
enabledDesigner.Process();
Console.WriteLine("Without switch: " + plainSheet.PageSetup.GetHeader(1));
Console.WriteLine("With switch: " + enabledSheet.PageSetup.GetHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.Save("HeaderFooterMarkersEnabled.xlsx");
```

## **Vincular una Imagen en un Encabezado o Pie de Página**
El sufijo `(picture)` vincula una imagen en una sección de encabezado o pie de página. Escriba `<<node.logo(picture)>>` donde debe aparecer la imagen y proporcione el valor del campo como una data URI — el prefijo `data:image/png;base64,` seguido del texto Base64 de los bytes de la imagen. Una cadena Base64 sin el prefijo `data:` no incrusta una imagen.
Después de `Process()`:
1. El marcador se reemplaza por `&G`, el código estándar de imagen de encabezado y pie de página. Como el marcador se vuelve un código dentro de la cadena de la sección, puede colocarse dentro de texto más largo, como `Logo: <<node.logo(picture)>>`.
2. Los bytes de la imagen se incrustan en el libro de trabajo como una parte multimedia adjunta a la capa de dibujo de encabezado/pie de página de esa hoja, de modo que la imagen se imprime con el encabezado o pie de página.

```csharp
using System;
using System.Data;
using System.IO;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.PageSetup.SetHeader(1, "Logo: <<node.logo(picture)>>");
DataTable table = new DataTable("node");
table.Columns.Add("logo");
table.Rows.Add("data:image/png;base64," + Convert.ToBase64String(File.ReadAllBytes("logo.png")));
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
// This prints:
// Header: Logo: &G
workbook.Save("HeaderFooterPicture.xlsx");
```

La cadena `&G` impresa es el código de imagen que Excel interpreta al renderizar el encabezado — los bytes de `logo.png` ahora residen dentro de `HeaderFooterPicture.xlsx`, y la imagen se imprime en lugar del código.
Para usar los Marcadores Inteligentes en encabezados y pies de página, escriba marcadores de posición `<<Source.Field>>` en las secciones izquierda, central y derecha del encabezado o pie de página con `SetHeader` y `SetFooter`. Establezca `EnableHeaderFooterMarkers` en `true` en el `WorkbookDesigner` antes de llamar a `Process()`, y proporcione valores mediante `SetDataSource(DataTable)` o `SetJsonDataSource`. Lea las secciones completadas con `GetHeader` y `GetFooter`. La misma fuente de datos puede poblar los marcadores del cuerpo y los marcadores de encabezado o pie de página en una sola pasada de procesamiento. Añada el sufijo `(picture)` con un valor de data-URI para vincular una imagen en una sección.

## **Artículos Relacionados**
- [Renderizado de Matriz de Marcador Inteligente en una Celda](/cells/es/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="csharp" >}}