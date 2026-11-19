---
title: Smart Markers in Headers and Footers | Aspose.Cells for Node.js via Java
description: Place Smart Marker placeholders in page headers and footers with double-angle-bracket syntax and the WorkbookDesigner.setEnableHeaderFooterMarkers switch using JSON data sources, and bind pictures through data URIs, in Aspose.Cells for Node.js via Java.
linktitle: Header and Footer Smart Markers | Aspose.Cells for Node.js via Java
keywords: Aspose.Cells for Node.js via Java, Smart Markers, headers, footers, header footer markers, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, JSON rows, data binding, picture, data URI, JavaScript
type: docs
weight: 196
url: /nodejs-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Page headers and footers commonly contain report metadata such as the report title, reporting period, author, and department. When this information already exists in the data source used to populate the workbook, repeating it manually creates unnecessary duplication.
Classic Smart Marker syntax, `&=Source.Field`, is processed in worksheet body cells. If you place a classic marker in a header or footer through `PageSetup.setHeader` or `PageSetup.setFooter`, it remains literal text because header and footer strings are not part of the worksheet cell grid scanned by `WorkbookDesigner.process()`.
Starting with **Aspose.Cells for Node.js via Java 26.11**, the `WorkbookDesigner.setEnableHeaderFooterMarkers` setting, which is `false` by default, makes `process()` resolve placeholders written as `<<Source.Field>>` in header and footer section strings. Call `designer.setEnableHeaderFooterMarkers(true)` before calling `process()`. Header and footer placeholders use the same data source as body markers.
Each header and footer contains three addressable sections:
- Section `0` is the left section.
- Section `1` is the center section.
- Section `2` is the right section.
Use `PageSetup.setHeader(int section, String value)` and `PageSetup.setFooter(int section, String value)` to write these sections. After processing, use `PageSetup.getHeader(int section)` and `PageSetup.getFooter(int section)` to retrieve the completed text.

{{% alert color="primary" %}}
A placeholder such as `<<Source.Field>>` inserts the field value as text into the section string. Images are bound with the `(picture)` suffix and a data-URI value.
{{% /alert %}}

## **Enable Header/Footer Markers with JSON Row Data**
Use the following sequence to resolve header and footer placeholders with JSON row data in **Aspose.Cells for Node.js via Java 26.11**:
1. Create a `Workbook` and obtain its first `Worksheet` with `workbook.getWorksheets().get(0)`.
2. Write `<<Source.Field>>` placeholders into the desired header and footer sections with `PageSetup.setHeader` and `PageSetup.setFooter`.
3. Prepare the row data as a JSON array of row objects, and choose a source name that matches the source prefix used by the placeholders. For example, a source named `node` backs placeholders such as `<<node.Name>>`. Plain JavaScript objects and arrays passed to `setDataSource` do not bind on this platform — JSON is the supported tabular form.
4. Create a `WorkbookDesigner` for the workbook.
5. Call `designer.setEnableHeaderFooterMarkers(true)` before processing.
6. Attach the JSON with `designer.setJsonDataSource("node", '[{"Name":"...","Author":"..."}]')`.
7. Call `designer.process()`.
8. After processing, the placeholders are no longer present in the header or footer text. Use `getHeader` and `getFooter` to retrieve the completed section strings.

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

## **Use a JSON Data Source**
When the report data is already available as JSON, one `setJsonDataSource` call can feed every marker style. Call `WorkbookDesigner.setJsonDataSource(String name, String json)` to attach the source.
The `name` argument is the source name used by the placeholders. For example, the name `node` backs placeholders such as `<<node.Company>>` and `<<node.Title>>`.
Pass row data directly to `setJsonDataSource`:
- A row array, such as a JSON array containing one or more row objects, is supported.
- A single row object may also be passed directly.
- Do not wrap the rows under a named top-level key such as `{"rows":[...]}`. This wrapper is not the expected row-oriented input shape for this workflow.
One JSON source can populate both marker styles during the same `process()` call. It can resolve a classic `&=` marker in a worksheet body cell and double-angle-bracket `<<>>` placeholders in header and footer sections. You must still call `designer.setEnableHeaderFooterMarkers(true)` for the header and footer placeholders to be resolved.

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

## **Switch and Multi-Row Source Semantics**
`setEnableHeaderFooterMarkers` is `false` by default, and the setting controls only the header and footer `<<Source.Field>>` placeholders. When the switch is off, `process()` still resolves classic `&=` body markers, but a `<<Source.Field>>` placeholder in a header or footer remains literal text.
A header or footer section is one string, not a repeating band. If the data source contains several rows, the first row supplies the header and footer values. Once resolved, the values become ordinary header or footer text. They remain in the workbook after you call `save` and are present when you load the saved workbook again.
The following example creates two workbooks over the same multi-row JSON source to contrast the disabled and enabled behavior. The `plainDesigner` leaves the placeholder unchanged, while the `enabledDesigner` resolves it using the first row.

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

## **Bind a Picture into a Header or Footer**
The `(picture)` suffix binds an image into a header or footer section. Write `<<node.logo(picture)>>` where the image should appear, and supply the field value as a data URI — the prefix `data:image/png;base64,` followed by the Base64 text of the image bytes. A bare Base64 string without the `data:` prefix does not embed an image.
After `process()`:
1. The placeholder is replaced by `&G`, the standard header and footer picture code. Because the marker becomes a code inside the section string, it can sit within longer text such as `Logo: <<node.logo(picture)>>`.
2. The image bytes are embedded in the workbook as a media part attached to the header/footer drawing layer of that worksheet, so the picture prints with the header or footer.

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

The printed `&G` is the picture code Excel interprets when rendering the header — the `logo.png` bytes now live inside `HeaderFooterPicture.xlsx`, and the image prints in place of the code.
To use header and footer Smart Markers, write `<<Source.Field>>` placeholders into the left, center, and right header or footer sections with `setHeader` and `setFooter`. Call `designer.setEnableHeaderFooterMarkers(true)` before calling `process()`, and supply values through `designer.setJsonDataSource(name, json)`. Read the completed sections with `getHeader` and `getFooter`. The same data source can populate body markers and header or footer placeholders in one processing pass. Add the `(picture)` suffix with a data-URI value to bind an image into a section.

## Related Articles
- [SmartMarker Single Cell Array Rendering](/cells/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="nodejs-java" >}}