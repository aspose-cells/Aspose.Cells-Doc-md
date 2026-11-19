---
title: Marcadores Inteligentes en Cabeceras y Pies de página | Aspose.Cells for Python via .NET
description: Coloque marcadores inteligentes en los encabezados y pies de página con la sintaxis de doble corchete angular y el conmutador WorkbookDesigner.enable_header_footer_markers utilizando implementaciones personalizadas de ICellsDataTable o fuentes de datos JSON, y vincule imágenes mediante URIs de datos, en Aspose.Cells for Python via .NET.
linktitle: Marcadores Inteligentes en Cabecera y Pie de página | Aspose.Cells
keywords: Aspose.Cells, Marcadores Inteligentes, encabezados, pies de página, marcadores de encabezado y pie de página, enable_header_footer_markers, WorkbookDesigner, PageSetup, set_header, set_footer, set_json_data_source, set_data_source, ICellsDataTable, tabla de datos personalizada, vinculación de datos, imagen, URI de datos, Aspose.Cells for Python via .NET
type: docs
weight: 196
url: /es/python-net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Los encabezados y pies de página generalmente contienen metadatos del informe, como el título del informe, el período de reporte, el autor y el departamento. Cuando esta información ya existe en la fuente de datos utilizada para llenar el libro de trabajo, repetirla manualmente genera duplicación innecesaria.
La sintaxis clásica de Marcador Inteligente, `&=Source.Field`, se procesa en las celdas del cuerpo de la hoja de cálculo. Si coloca un marcador clásico en un encabezado o pie de página mediante `page_setup.set_header` o `page_setup.set_footer`, permanece como texto literal porque las cadenas de encabezado y pie de página no forman parte de la cuadrícula de celdas que escanea `workbook_designer.process()`.
A partir de **Aspose.Cells for Python via .NET 26.11**, el interruptor `workbook_designer.enable_header_footer_markers`, que por defecto es `False`, permite que `process()` resuelva los marcadores escritos como `<<Source.Field>>` en las cadenas de secciones de encabezado y pie de página — configúrelo a `True` antes de llamar a `process()`. Los marcadores de encabezado y pie de página utilizan la misma fuente de datos que los marcadores del cuerpo.
Cada encabezado y pie de página contiene tres secciones direccionables:
- La sección `0` es la sección izquierda.
- La sección `1` es la sección central.
- La sección `2` es la sección derecha.
Utilice `page_setup.set_header(section, value)` y `page_setup.set_footer(section, value)` para escribir estas secciones. Después del procesamiento, use `page_setup.get_header(section)` y `page_setup.get_footer(section)` para recuperar el texto completo.

{{% alert color="primary" %}}
Un marcador como `<<Source.Field>>` inserta el valor del campo como texto en la cadena de la sección. Las imágenes se vinculan con el sufijo `(picture)` y un valor de URI de datos.
{{% /alert %}}

## **Habilitar marcadores de encabezado/pie de página con una tabla de datos personalizada**
Utilice la siguiente secuencia para resolver los marcadores de encabezado y pie de página con una fuente de datos tabular personalizada en **Aspose.Cells for Python via .NET 26.11**:
1. Cree un `Workbook` y obtenga su primera `Worksheet` en el índice `0`.
2. Escriba marcadores `<<Source.Field>>` en las secciones de encabezado y pie de página deseadas usando `page_setup.set_header` y `page_setup.set_footer`.
3. Defina una clase pequeña que implemente `ICellsDataTable` para exponer los datos tabulares de filas — los nombres de columna, la cantidad de filas y un cursor con `before_first()`, `next()` y el indexador `__getitem__` — y use un nombre de fuente que coincida con el prefijo de fuente utilizado por los marcadores. Por ejemplo, una fuente llamada `node` respalda marcadores como `<<node.Name>>`. Una clase Python simple o una lista de diccionarios NO se enlaza en esta plataforma; la implementación de `ICellsDataTable` es la fuente de datos del objeto personalizado.
4. Cree un `WorkbookDesigner` para el libro de trabajo.
5. Establezca `designer.enable_header_footer_markers` a `True` antes del procesamiento.
6. Adjunte la tabla y el nombre de fuente con `designer.set_data_source("node", table)`.
7. Llame a `designer.process()`.
8. Después del procesamiento, los marcadores ya no están presentes en el texto del encabezado o pie de página. Use `get_header` y `get_footer` para obtener las cadenas de sección completadas.

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name", "Author"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.page_setup.set_header(1, "Quarterly Report - <<node.Name>>")
worksheet.page_setup.set_footer(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
print("Footer: " + worksheet.page_setup.get_footer(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
```

## **Utilizar una fuente de datos JSON**
Puede usar JSON en lugar de un `ICellsDataTable` personalizado cuando los datos del informe ya están disponibles en formato JSON. Llame a `workbook_designer.set_json_data_source(name, json)` para adjuntar la fuente.
El argumento `name` tiene la misma función que el nombre de fuente usado con datos tabulares. Por ejemplo, el nombre `node` respalda marcadores como `<<node.Company>>` y `<<node.Title>>`.
Proporcione los datos de fila directamente a `set_json_data_source`:
- Se admite un arreglo de filas, como un arreglo JSON que contiene uno o más objetos de fila.
- También puede pasarse directamente un único objeto de fila.
- No envuelva las filas bajo una clave de nivel superior con nombre, como `{\"rows\":[...]}`. Este contenedor no corresponde a la forma de entrada orientada a filas esperada para este flujo de trabajo.
Una fuente JSON puede poblar ambos estilos de marcadores durante la misma llamada a `process()`. Puede resolver un marcador clásico `&=` en una celda del cuerpo de la hoja y marcadores de doble corchete `<<>>` en secciones de encabezado y pie de página. Aún debe habilitar `enable_header_footer_markers` para que los marcadores de encabezado y pie de página se resuelvan.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.page_setup.set_header(0, "<<node.Company>>")
worksheet.page_setup.set_header(2, "Page <<node.Title>>")
worksheet.cells.get("A1").put_value("&=node.Company")
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_json_data_source(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.page_setup.get_header(0))
print("Right: " + worksheet.page_setup.get_header(2))
print("Body: " + worksheet.cells.get("A1").string_value)
# This prints:
# Left: Aspose Pty Ltd
# Right: Page Half-Year Report
# Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx")
```

## **Semántica del conmutador y de la fuente multifila**
`enable_header_footer_markers` es `False` por defecto, y el conmutador controla solo los marcadores `<<Source.Field>>` de encabezado y pie de página. Cuando el conmutador está desactivado, `process()` aún resuelve los marcadores clásicos `&=` del cuerpo, pero un marcador `<<Source.Field>>` en un encabezado o pie de página permanece como texto literal.
Una sección de encabezado o pie de página es una única cadena, no una banda repetitiva. Si la fuente de datos contiene varias filas, la primera fila suministra los valores del encabezado y pie de página. Una vez resueltos, los valores se convierten en texto ordinario de encabezado o pie de página. Permanan en el libro de trabajo después de llamar a `save` y están presentes cuando vuelve a cargar el libro guardado.
El siguiente ejemplo crea dos libros de trabajo sobre la misma fuente de datos tabular multifila para contrastar el comportamiento deshabilitado y habilitado. El `plain_designer` deja el marcador sin cambios, mientras que el `enabled_designer` lo resuelve usando la primera fila.

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
rows = [("First Row",), ("Second Row",)]
# Without the switch the placeholder stays literal text
plain_workbook = ac.Workbook()
plain_sheet = plain_workbook.worksheets[0]
plain_sheet.page_setup.set_header(1, "<<node.Name>>")
plain_designer = ac.WorkbookDesigner(plain_workbook)
plain_designer.set_data_source("node", NodeTable(rows))
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = ac.Workbook()
enabled_sheet = enabled_workbook.worksheets[0]
enabled_sheet.page_setup.set_header(1, "<<node.Name>>")
enabled_designer = ac.WorkbookDesigner(enabled_workbook)
enabled_designer.enable_header_footer_markers = True
enabled_designer.set_data_source("node", NodeTable(rows))
enabled_designer.process()
print("Without switch: " + plain_sheet.page_setup.get_header(1))
print("With switch: " + enabled_sheet.page_setup.get_header(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
```

## **Vincular una imagen en un encabezado o pie de página**
El sufijo `(picture)` vincula una imagen en una sección de encabezado o pie de página. Escriba `<<node.logo(picture)>>` donde debe aparecer la imagen, y proporcione el valor del campo como una URI de datos — el prefijo `data:image/png;base64,` seguido del texto Base64 de los bytes de la imagen. Una cadena Base64 sin el prefijo `data:` no incrusta una imagen.
Después de `process()`:
1. El marcador se reemplaza por `&G`, el código estándar de imagen de encabezado y pie de página. Como el marcador se convierte en un código dentro de la cadena de la sección, puede estar dentro de texto más largo, por ejemplo `Logo: <<node.logo(picture)>>`.
2. Los bytes de la imagen se incrustan en el libro de trabajo como una parte multimedia adjunta a la capa de dibujo de encabezado/pie de página de esa hoja, de modo que la imagen se imprime con el encabezado o el pie de página.

```python
import aspose.cells as ac
import base64
class LogoTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["logo"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.page_setup.set_header(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    logo_data_uri = "data:image/png;base64," + base64.b64encode(image_file.read()).decode("ascii")
table = LogoTable([(logo_data_uri,)])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
```

El `&G` impreso es el código de imagen que Excel interpreta al renderizar el encabezado — los bytes de `logo.png` ahora viven dentro de `HeaderFooterPicture.xlsx`, y la imagen se imprime en lugar del código.
Para usar marcadores inteligentes en encabezados y pies de página, escriba marcadores `<<Source.Field>>` en las secciones izquierda, central y derecha del encabezado o pie de página con `set_header` y `set_footer`. Establezca `enable_header_footer_markers` a `True` en el `WorkbookDesigner` antes de llamar a `process()`, y proporcione los valores mediante `set_data_source("node", table)` con una implementación personalizada de `ICellsDataTable` o `set_json_data_source(name, json)`. Lea las secciones completadas con `get_header` y `get_footer`. La misma fuente de datos puede poblar marcadores del cuerpo y marcadores de encabezado o pie de página en una sola pasada de procesamiento. Añada el sufijo `(picture)` con un valor de URI de datos para vincular una imagen en una sección.

## Artículos relacionados
- [Renderizado de matriz de una sola celda con SmartMarker](/cells/es/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python-net" >}}