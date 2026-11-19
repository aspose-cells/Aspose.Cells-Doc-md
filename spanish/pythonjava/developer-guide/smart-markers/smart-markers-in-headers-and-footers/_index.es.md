---
title: Marcadores Inteligentes en Encabezados y Pies de Página | Aspose.Cells for Python via Java
description: Coloque marcadores inteligentes en los encabezados y pies de página con sintaxis de doble corchete angular y el interruptor WorkbookDesigner.setEnableHeaderFooterMarkers usando fuentes de datos tabulares de filas o JSON, y vincule imágenes mediante URI de datos, en Aspose.Cells for Python via Java.
linktitle: Marcadores Inteligentes en Encabezados y Pies de Página | Aspose.Cells
keywords: Aspose.Cells, Aspose.Cells for Python via Java, Marcadores Inteligentes, encabezados, pies de página, marcadores de encabezado y pie de página, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, ICellsDataTable, tabla de datos personalizada, enlace de datos, imagen, URI de datos, Python via Java
type: docs
weight: 196
url: /es/python-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de Uso Posibles**
Los encabezados y pies de página suelen contener metadatos del informe, como el título del informe, el período de reporte, el autor y el departamento. Cuando esta información ya existe en la fuente de datos utilizada para rellenar el libro de trabajo, repetirla manualmente genera duplicación innecesaria.  
La sintaxis clásica de Smart Marker, `&=Source.Field`, se procesa en las celdas del cuerpo de la hoja de cálculo. Si coloca un marcador clásico en un encabezado o pie de página mediante `PageSetup.setHeader` o `PageSetup.setFooter`, permanecerá como texto literal porque las cadenas de encabezado y pie de página no forman parte de la cuadrícula de celdas que escanea `WorkbookDesigner.process()`.  
A partir de **Aspose.Cells for Python via Java 26.11**, el conmutador `WorkbookDesigner.setEnableHeaderFooterMarkers`, que por defecto es `False`, hace que `process()` resuelva los marcadores escritos como `<<Source.Field>>` en las cadenas de encabezado y pie de página — configúrelo en `True` antes de llamar a `process()`. Los marcadores de encabezado y pie de página utilizan la misma fuente de datos que los marcadores del cuerpo.  
Cada encabezado y pie de página contiene tres secciones direccionables:
- La sección `0` es la sección izquierda.
- La sección `1` es la sección central.
- La sección `2` es la sección derecha.  
Utilice `PageSetup.setHeader(int section, str value)` y `PageSetup.setFooter(int section, str value)` para escribir en estas secciones. Después del procesamiento, use `PageSetup.getHeader(int section)` y `PageSetup.getFooter(int section)` para obtener el texto completado.

{{% alert color="primary" %}}
Un marcador como `<<Source.Field>>` inserta el valor del campo como texto en la cadena de la sección. Las imágenes se vinculan con el sufijo `(picture)` y un valor de URI de datos.  
{{% /alert %}}

## **Activar Marcadores de Encabezado/Pie de Página con una Tabla de Datos Personalizada**
Utilice la siguiente secuencia para resolver los marcadores de encabezado y pie de página con una fuente de datos tabular personalizada en **Aspose.Cells for Python via Java 26.11**:
1. Cree un `Workbook` y obtenga su primera `Worksheet` en el índice `0` mediante `workbook.getWorksheets().get(0)`.
2. Escriba marcadores `<<Source.Field>>` en las secciones de encabezado y pie de página deseadas con `worksheet.getPageSetup().setHeader(section, value)` y `worksheet.getPageSetup().setFooter(section, value)`.
3. Defina una pequeña clase que implemente `ICellsDataTable` para exponer los datos tabulares: los nombres de columna, el recuento de filas y un cursor con `beforeFirst()`, `next()` y `get()`. Use un nombre de fuente que coincida con el prefijo usado por los marcadores. Por ejemplo, una fuente llamada `node` respalda marcadores como `<<node.Name>>`. Una clase Python sencilla o una lista de diccionarios NO funciona en esta plataforma; la implementación de `ICellsDataTable` es la fuente de datos personalizada.
4. Cree un `WorkbookDesigner` para el libro de trabajo.
5. Llame a `designer.setEnableHeaderFooterMarkers(True)` antes del procesamiento.
6. Adjunte la tabla y el nombre de fuente con `designer.setDataSource("node", table)`.
7. Llame a `designer.process()`.
8. Después del procesamiento, los marcadores ya no estarán presentes en el texto del encabezado o pie de página. Use `worksheet.getPageSetup().getHeader(section)` y `worksheet.getPageSetup().getFooter(section)` para obtener las cadenas de sección completadas.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name", "Author"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>")
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
print("Footer: " + worksheet.getPageSetup().getFooter(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
jpype.shutdownJVM()
```

## **Usar una Fuente de Datos JSON**
Puede utilizar JSON en lugar de un `ICellsDataTable` personalizado cuando los datos del informe ya están disponibles en formato JSON. Llame a `designer.setJsonDataSource(name, json)` para adjuntar la fuente.  
El argumento `name` desempeña la misma función que el nombre de fuente usado con datos tabulares. Por ejemplo, el nombre `node` respalda marcadores como `<<node.Company>>` y `<<node.Title>>`.  
Pase los datos de fila directamente a `setJsonDataSource`:
- Se admite una matriz de filas, como un arreglo JSON que contiene uno o más objetos de fila.
- También se puede pasar un único objeto de fila directamente.
- No envuelva las filas bajo una clave superior con nombre, como `{"rows":[...]}`. Este contenedor no corresponde a la forma de entrada orientada a filas esperada para este flujo de trabajo.  
Una fuente JSON puede rellenar ambos estilos de marcadores durante la misma llamada a `process()`. Puede resolver un marcador clásico `&=` en una celda del cuerpo y marcadores de doble corchete `<<>>` en secciones de encabezado y pie de página. Aún debe habilitar `setEnableHeaderFooterMarkers` para que se resuelvan los marcadores en encabezado y pie de página.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>")
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>")
worksheet.getCells().get("A1").putValue("&=node.Company")
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setJsonDataSource(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.getPageSetup().getHeader(0))
print("Right: " + worksheet.getPageSetup().getHeader(2))
print("Body: " + worksheet.getCells().get("A1").getStringValue())
workbook.save("HeaderFooterJsonMarkers.xlsx")
jpype.shutdownJVM()
```

## **Conmutador y Semántica de Fuente Multi-Fila**
La configuración del marcador de encabezado/pie de página es `False` por defecto, y `designer.setEnableHeaderFooterMarkers(True)` controla únicamente los marcadores `<<Source.Field>>` en encabezado y pie de página. Cuando el conmutador está desactivado, `process()` sigue resolviendo los marcadores clásicos `&=` del cuerpo, pero un marcador `<<Source.Field>>` en un encabezado o pie de página permanece como texto literal.  
Una sección de encabezado o pie de página es una única cadena, no una banda repetitiva. Si la fuente de datos contiene varias filas, la primera fila proporciona los valores del encabezado y pie de página. Una vez resueltos, los valores se convierten en texto ordinario de encabezado o pie de página. Permanecen en el libro de trabajo después de llamar a `workbook.save(...)` y están presentes al cargar nuevamente el libro guardado.  
El siguiente ejemplo crea dos libros de trabajo sobre la misma fuente de datos tabular multi-fila para contrastar el comportamiento desactivado y activado. El `plainDesigner` deja el marcador sin cambios, mientras que el `enabledDesigner` lo resuelve usando la primera fila.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
table = NodeTable([
    ("First Row",),
    ("Second Row",),
])
# Without the switch the placeholder stays literal text
plain_workbook = Workbook()
plain_sheet = plain_workbook.getWorksheets().get(0)
plain_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
plain_designer = WorkbookDesigner(plain_workbook)
plain_designer.setDataSource("node", table)
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = Workbook()
enabled_sheet = enabled_workbook.getWorksheets().get(0)
enabled_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
enabled_designer = WorkbookDesigner(enabled_workbook)
enabled_designer.setEnableHeaderFooterMarkers(True)
enabled_designer.setDataSource("node", table)
enabled_designer.process()
print("Without switch: " + plain_sheet.getPageSetup().getHeader(1))
print("With switch: " + enabled_sheet.getPageSetup().getHeader(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
jpype.shutdownJVM()
```

## **Vincular una Imagen en un Encabezado o Pie de Página**
El sufijo `(picture)` vincula una imagen a una sección de encabezado o pie de página. Escriba `<<node.logo(picture)>>` donde debería aparecer la imagen y proporcione el valor del campo como una URI de datos — el prefijo `data:image/png;base64,` seguido del texto Base64 de los bytes de la imagen. La imagen decodificada se maneja como una matriz `byte[]`. Una cadena Base64 sin el prefijo `data:` no incrusta una imagen.  
Después de `process()`:
1. El marcador se reemplaza por `&G`, el código estándar de imagen de encabezado y pie de página. Como el marcador se convierte en un código dentro de la cadena de la sección, puede coexistir con texto más largo, por ejemplo `Logo: <<node.logo(picture)>>`.
2. Los bytes de la imagen se incrustan en el libro de trabajo como una parte multimedia adjunta a la capa de dibujo de encabezado/pie de página de esa hoja, de modo que la imagen se imprime con el encabezado o pie de página.

```python
import base64
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["logo"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    image_bytes = image_file.read()
logo_data = "data:image/png;base64," + base64.b64encode(image_bytes).decode("ascii")
table = NodeTable([(logo_data,)])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
jpype.shutdownJVM()
```

El `&G` impreso es el código de imagen que Excel interpreta al renderizar el encabezado — los bytes de `logo.png` ahora viven dentro de `HeaderFooterPicture.xlsx`, y la imagen se imprime en lugar del código.  
Para usar marcadores inteligentes en encabezados y pies de página, escriba marcadores `<<Source.Field>>` en las secciones izquierda, central y derecha con `setHeader` y `setFooter`. Llame a `designer.setEnableHeaderFooterMarkers(True)` antes de `process()`, y proporcione valores mediante `designer.setDataSource("node", table)` con una implementación personalizada de `ICellsDataTable` o `designer.setJsonDataSource(name, json)`. Lea las secciones completadas con `getHeader` y `getFooter`. La misma fuente de datos puede rellenar marcadores del cuerpo y marcadores de encabezado o pie de página en una única pasada de procesamiento. Añada el sufijo `(picture)` con un valor de URI de datos para incrustar una imagen en una sección.

## **Artículos Relacionados**
- [Renderizado de Matriz de Celda Única con SmartMarker](/cells/es/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python" >}}