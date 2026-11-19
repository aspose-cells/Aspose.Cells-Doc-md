---
title: Smart Markers in Headers and Footers | Aspose.Cells for Python via Java
description: Place Smart Marker placeholders in page headers and footers with double-angle-bracket syntax and the WorkbookDesigner.setEnableHeaderFooterMarkers switch using tabular row or JSON data sources, and bind pictures through data URIs, in Aspose.Cells for Python via Java.
linktitle: Header and Footer Smart Markers | Aspose.Cells
keywords: Aspose.Cells, Aspose.Cells for Python via Java, Smart Markers, headers, footers, header footer markers, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, ICellsDataTable, custom data table, data binding, picture, data URI, Python via Java
type: docs
weight: 196
url: /python-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Page headers and footers commonly contain report metadata such as the report title, reporting period, author, and department. When this information already exists in the data source used to populate the workbook, repeating it manually creates unnecessary duplication.
Classic Smart Marker syntax, `&=Source.Field`, is processed in worksheet body cells. If you place a classic marker in a header or footer through `PageSetup.setHeader` or `PageSetup.setFooter`, it remains literal text because header and footer strings are not part of the worksheet cell grid scanned by `WorkbookDesigner.process()`.
Starting with **Aspose.Cells for Python via Java 26.11**, the `WorkbookDesigner.setEnableHeaderFooterMarkers` switch, which is `False` by default, makes `process()` resolve placeholders written as `<<Source.Field>>` in header and footer section strings — set it to `True` before calling `process()`. Header and footer placeholders use the same data source as body markers.
Each header and footer contains three addressable sections:
- Section `0` is the left section.
- Section `1` is the center section.
- Section `2` is the right section.
Use `PageSetup.setHeader(int section, str value)` and `PageSetup.setFooter(int section, str value)` to write these sections. After processing, use `PageSetup.getHeader(int section)` and `PageSetup.getFooter(int section)` to retrieve the completed text.

{{% alert color="primary" %}}
A placeholder such as `<<Source.Field>>` inserts the field value as text into the section string. Images are bound with the `(picture)` suffix and a data-URI value.
{{% /alert %}}

## **Enable Header/Footer Markers with a Custom Data Table**
Use the following sequence to resolve header and footer placeholders with a custom tabular data source in **Aspose.Cells for Python via Java 26.11**:
1. Create a `Workbook` and obtain its first `Worksheet` at index `0` using `workbook.getWorksheets().get(0)`.
2. Write `<<Source.Field>>` placeholders into the desired header and footer sections with `worksheet.getPageSetup().setHeader(section, value)` and `worksheet.getPageSetup().setFooter(section, value)`.
3. Define a small class that implements `ICellsDataTable` to expose the tabular row data — the column names, the row count, and a cursor with `beforeFirst()`, `next()`, and `get()` — and use a source name that matches the source prefix used by the placeholders. For example, a source named `node` backs placeholders such as `<<node.Name>>`. A plain Python class or a list of dictionaries does NOT bind on this platform; the `ICellsDataTable` implementation is the custom-object data source.
4. Create a `WorkbookDesigner` for the workbook.
5. Call `designer.setEnableHeaderFooterMarkers(True)` before processing.
6. Attach the table and source name with `designer.setDataSource("node", table)`.
7. Call `designer.process()`.
8. After processing, the placeholders are no longer present in the header or footer text. Use `worksheet.getPageSetup().getHeader(section)` and `worksheet.getPageSetup().getFooter(section)` to retrieve the completed section strings.

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

## **Use a JSON Data Source**
You can use JSON instead of a custom `ICellsDataTable` when the report data is already available in JSON format. Call `designer.setJsonDataSource(name, json)` to attach the source.
The `name` argument has the same role as the source name used with tabular data. For example, the name `node` backs placeholders such as `<<node.Company>>` and `<<node.Title>>`.
Pass row data directly to `setJsonDataSource`:
- A row array, such as a JSON array containing one or more row objects, is supported.
- A single row object may also be passed directly.
- Do not wrap the rows under a named top-level key such as `{"rows":[...]}`. This wrapper is not the expected row-oriented input shape for this workflow.
One JSON source can populate both marker styles during the same `process()` call. It can resolve a classic `&=` marker in a worksheet body cell and double-angle-bracket `<<>>` placeholders in header and footer sections. You must still enable `setEnableHeaderFooterMarkers` for the header and footer placeholders to be resolved.

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

## **Switch and Multi-Row Source Semantics**
The header and footer marker setting is `False` by default, and `designer.setEnableHeaderFooterMarkers(True)` controls only the header and footer `<<Source.Field>>` placeholders. When the switch is off, `process()` still resolves classic `&=` body markers, but a `<<Source.Field>>` placeholder in a header or footer remains literal text.
A header or footer section is one string, not a repeating band. If the data source contains several rows, the first row supplies the header and footer values. Once resolved, the values become ordinary header or footer text. They remain in the workbook after you call `workbook.save(...)` and are present when you load the saved workbook again.
The following example creates two workbooks over the same multi-row tabular data source to contrast the disabled and enabled behavior. The `plainDesigner` leaves the placeholder unchanged, while the `enabledDesigner` resolves it using the first row.

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

## **Bind a Picture into a Header or Footer**
The `(picture)` suffix binds an image into a header or footer section. Write `<<node.logo(picture)>>` where the image should appear, and supply the field value as a data URI — the prefix `data:image/png;base64,` followed by the Base64 text of the image bytes. The decoded image is handled as a `byte[]` array. A bare Base64 string without the `data:` prefix does not embed an image.
After `process()`:
1. The placeholder is replaced by `&G`, the standard header and footer picture code. Because the marker becomes a code inside the section string, it can sit within longer text such as `Logo: <<node.logo(picture)>>`.
2. The image bytes are embedded in the workbook as a media part attached to the header/footer drawing layer of that worksheet, so the picture prints with the header or footer.

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

The printed `&G` is the picture code Excel interprets when rendering the header — the `logo.png` bytes now live inside `HeaderFooterPicture.xlsx`, and the image prints in place of the code.
To use header and footer Smart Markers, write `<<Source.Field>>` placeholders into the left, center, and right header or footer sections with `setHeader` and `setFooter`. Call `designer.setEnableHeaderFooterMarkers(True)` before calling `process()`, and supply values through either `designer.setDataSource("node", table)` with a custom `ICellsDataTable` implementation or `designer.setJsonDataSource(name, json)`. Read the completed sections with `getHeader` and `getFooter`. The same data source can populate body markers and header or footer placeholders in one processing pass. Add the `(picture)` suffix with a data-URI value to bind an image into a section.

## Related Articles
- [SmartMarker Single Cell Array Rendering](/cells/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python" >}}