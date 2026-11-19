---
title: Smart Markers in Headers and Footers | Aspose.Cells for Python via .NET
description: Place Smart Marker placeholders in page headers and footers with double-angle-bracket syntax and the WorkbookDesigner.enable_header_footer_markers switch using custom ICellsDataTable implementations or JSON data sources, and bind pictures through data URIs, in Aspose.Cells for Python via .NET.
linktitle: Header and Footer Smart Markers | Aspose.Cells
keywords: Aspose.Cells, Smart Markers, headers, footers, header footer markers, enable_header_footer_markers, WorkbookDesigner, PageSetup, set_header, set_footer, set_json_data_source, set_data_source, ICellsDataTable, custom data table, data binding, picture, data URI, Aspose.Cells for Python via .NET
type: docs
weight: 196
url: /python-net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Page headers and footers commonly contain report metadata such as the report title, reporting period, author, and department. When this information already exists in the data source used to populate the workbook, repeating it manually creates unnecessary duplication.
Classic Smart Marker syntax, `&=Source.Field`, is processed in worksheet body cells. If you place a classic marker in a header or footer through `page_setup.set_header` or `page_setup.set_footer`, it remains literal text because header and footer strings are not part of the worksheet cell grid scanned by `workbook_designer.process()`.
Starting with **Aspose.Cells for Python via .NET 26.11**, the `workbook_designer.enable_header_footer_markers` switch, which is `False` by default, makes `process()` resolve placeholders written as `<<Source.Field>>` in header and footer section strings — set it to `True` before calling `process()`. Header and footer placeholders use the same data source as body markers.
Each header and footer contains three addressable sections:
- Section `0` is the left section.
- Section `1` is the center section.
- Section `2` is the right section.
Use `page_setup.set_header(section, value)` and `page_setup.set_footer(section, value)` to write these sections. After processing, use `page_setup.get_header(section)` and `page_setup.get_footer(section)` to retrieve the completed text.

{{% alert color="primary" %}}
A placeholder such as `<<Source.Field>>` inserts the field value as text into the section string. Images are bound with the `(picture)` suffix and a data-URI value.
{{% /alert %}}

## **Enable Header/Footer Markers with a Custom Data Table**
Use the following sequence to resolve header and footer placeholders with a custom tabular data source in **Aspose.Cells for Python via .NET 26.11**:
1. Create a `Workbook` and obtain its first `Worksheet` at index `0`.
2. Write `<<Source.Field>>` placeholders into the desired header and footer sections with `page_setup.set_header` and `page_setup.set_footer`.
3. Define a small class that implements `ICellsDataTable` to expose the tabular row data — the column names, the row count, and a cursor with `before_first()`, `next()`, and the `__getitem__` indexer — and use a source name that matches the source prefix used by the placeholders. For example, a source named `node` backs placeholders such as `<<node.Name>>`. A plain Python class or a list of dictionaries does NOT bind on this platform; the `ICellsDataTable` implementation is the custom-object data source.
4. Create a `WorkbookDesigner` for the workbook.
5. Set `designer.enable_header_footer_markers` to `True` before processing.
6. Attach the table and source name with `designer.set_data_source("node", table)`.
7. Call `designer.process()`.
8. After processing, the placeholders are no longer present in the header or footer text. Use `get_header` and `get_footer` to retrieve the completed section strings.

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

## **Use a JSON Data Source**
You can use JSON instead of a custom `ICellsDataTable` when the report data is already available in JSON format. Call `workbook_designer.set_json_data_source(name, json)` to attach the source.
The `name` argument has the same role as the source name used with tabular data. For example, the name `node` backs placeholders such as `<<node.Company>>` and `<<node.Title>>`.
Pass row data directly to `set_json_data_source`:
- A row array, such as a JSON array containing one or more row objects, is supported.
- A single row object may also be passed directly.
- Do not wrap the rows under a named top-level key such as `{"rows":[...]}`. This wrapper is not the expected row-oriented input shape for this workflow.
One JSON source can populate both marker styles during the same `process()` call. It can resolve a classic `&=` marker in a worksheet body cell and double-angle-bracket `<<>>` placeholders in header and footer sections. You must still enable `enable_header_footer_markers` for the header and footer placeholders to be resolved.

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

## **Switch and Multi-Row Source Semantics**
`enable_header_footer_markers` is `False` by default, and the switch controls only the header and footer `<<Source.Field>>` placeholders. When the switch is off, `process()` still resolves classic `&=` body markers, but a `<<Source.Field>>` placeholder in a header or footer remains literal text.
A header or footer section is one string, not a repeating band. If the data source contains several rows, the first row supplies the header and footer values. Once resolved, the values become ordinary header or footer text. They remain in the workbook after you call `save` and are present when you load the saved workbook again.
The following example creates two workbooks over the same multi-row tabular data source to contrast the disabled and enabled behavior. The `plain_designer` leaves the placeholder unchanged, while the `enabled_designer` resolves it using the first row.

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

## **Bind a Picture into a Header or Footer**
The `(picture)` suffix binds an image into a header or footer section. Write `<<node.logo(picture)>>` where the image should appear, and supply the field value as a data URI — the prefix `data:image/png;base64,` followed by the Base64 text of the image bytes. A bare Base64 string without the `data:` prefix does not embed an image.
After `process()`:
1. The placeholder is replaced by `&G`, the standard header and footer picture code. Because the marker becomes a code inside the section string, it can sit within longer text such as `Logo: <<node.logo(picture)>>`.
2. The image bytes are embedded in the workbook as a media part attached to the header/footer drawing layer of that worksheet, so the picture prints with the header or footer.

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

The printed `&G` is the picture code Excel interprets when rendering the header — the `logo.png` bytes now live inside `HeaderFooterPicture.xlsx`, and the image prints in place of the code.
To use header and footer Smart Markers, write `<<Source.Field>>` placeholders into the left, center, and right header or footer sections with `set_header` and `set_footer`. Set `enable_header_footer_markers` to `True` on the `WorkbookDesigner` before calling `process()`, and supply values through `set_data_source("node", table)` with a custom `ICellsDataTable` implementation or `set_json_data_source(name, json)`. Read the completed sections with `get_header` and `get_footer`. The same data source can populate body markers and header or footer placeholders in one processing pass. Add the `(picture)` suffix with a data-URI value to bind an image into a section.

## Related Articles
- [SmartMarker Single Cell Array Rendering](/cells/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python-net" >}}