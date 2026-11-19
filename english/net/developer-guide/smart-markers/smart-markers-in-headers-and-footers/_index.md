---
title: Smart Markers in Headers and Footers | Aspose.Cells .NET
description: Place Smart Marker placeholders in page headers and footers with double-angle-bracket syntax and the WorkbookDesigner.EnableHeaderFooterMarkers switch using DataTable or JSON data sources, and bind pictures through data URIs, in Aspose.Cells for .NET.
linktitle: Header and Footer Smart Markers | Aspose.Cells
keywords: Aspose.Cells, Smart Markers, headers, footers, header footer markers, EnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, SetHeader, SetFooter, SetJsonDataSource, DataTable, data binding, picture, data URI, C#
type: docs
weight: 196
url: /net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Page headers and footers commonly contain report metadata such as the report title, reporting period, author, and department. When this information already exists in the data source used to populate the workbook, repeating it manually creates unnecessary duplication.
Classic Smart Marker syntax, `&=Source.Field`, is processed in worksheet body cells. If you place a classic marker in a header or footer through `PageSetup.SetHeader` or `PageSetup.SetFooter`, it remains literal text because header and footer strings are not part of the worksheet cell grid scanned by `WorkbookDesigner.Process()`.
Starting with **Aspose.Cells for .NET 26.11**, the `WorkbookDesigner.EnableHeaderFooterMarkers` switch, which is `false` by default, makes `Process()` resolve placeholders written as `<<Source.Field>>` in header and footer section strings — set it to `true` before calling `Process()`. Header and footer placeholders use the same data source as body markers.
Each header and footer contains three addressable sections:
- Section `0` is the left section.
- Section `1` is the center section.
- Section `2` is the right section.
Use `PageSetup.SetHeader(int section, string value)` and `PageSetup.SetFooter(int section, string value)` to write these sections. After processing, use `PageSetup.GetHeader(int section)` and `PageSetup.GetFooter(int section)` to retrieve the completed text.

{{% alert color="primary" %}}
A placeholder such as `<<Source.Field>>` inserts the field value as text into the section string. Images are bound with the `(picture)` suffix and a data-URI value.
{{% /alert %}}

## **Enable Header/Footer Markers with a DataTable**
Use the following sequence to resolve header and footer placeholders with a `DataTable` in **Aspose.Cells for .NET 26.11**:
1. Create a `Workbook` and obtain its first `Worksheet` at index `0`.
2. Write `<<Source.Field>>` placeholders into the desired header and footer sections with `PageSetup.SetHeader` and `PageSetup.SetFooter`.
3. Create a `DataTable` whose table name matches the source prefix used by the placeholders. For example, a table named `node` backs placeholders such as `<<node.Name>>`.
4. Create a `WorkbookDesigner` for the workbook.
5. Set `designer.EnableHeaderFooterMarkers` to `true` before processing.
6. Attach the table with `designer.SetDataSource(table)`.
7. Call `designer.Process()`.
8. After processing, the placeholders are no longer present in the header or footer text. Use `GetHeader` and `GetFooter` to retrieve the completed section strings.

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

## **Use a JSON Data Source**
You can use JSON instead of a `DataTable` when the report data is already available in JSON format. Call `WorkbookDesigner.SetJsonDataSource(string name, string json)` to attach the source.
The `name` argument has the same role as the `DataTable` name. For example, the name `node` backs placeholders such as `<<node.Company>>` and `<<node.Title>>`.
Pass row data directly to `SetJsonDataSource`:
- A row array, such as a JSON array containing one or more row objects, is supported.
- A single row object may also be passed directly.
- Do not wrap the rows under a named top-level key such as `{"rows":[...]}`. This wrapper is not the expected row-oriented input shape for this workflow.
One JSON source can populate both marker styles during the same `Process()` call. It can resolve a classic `&=` marker in a worksheet body cell and double-angle-bracket `<<>>` placeholders in header and footer sections. You must still enable `EnableHeaderFooterMarkers` for the header and footer placeholders to be resolved.

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

## **Switch and Multi-Row Source Semantics**
`EnableHeaderFooterMarkers` is `false` by default, and the switch controls only the header and footer `<<Source.Field>>` placeholders. When the switch is off, `Process()` still resolves classic `&=` body markers, but a `<<Source.Field>>` placeholder in a header or footer remains literal text.
A header or footer section is one string, not a repeating band. If the data source contains several rows, the first row supplies the header and footer values. Once resolved, the values become ordinary header or footer text. They remain in the workbook after you call `Save` and are present when you load the saved workbook again.
The following example creates two workbooks over the same multi-row `DataTable` to contrast the disabled and enabled behavior. The `plainDesigner` leaves the placeholder unchanged, while the `enabledDesigner` resolves it using the first row.

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

## **Bind a Picture into a Header or Footer**
The `(picture)` suffix binds an image into a header or footer section. Write `<<node.logo(picture)>>` where the image should appear, and supply the field value as a data URI — the prefix `data:image/png;base64,` followed by the Base64 text of the image bytes. A bare Base64 string without the `data:` prefix does not embed an image.
After `Process()`:
1. The placeholder is replaced by `&G`, the standard header and footer picture code. Because the marker becomes a code inside the section string, it can sit within longer text such as `Logo: <<node.logo(picture)>>`.
2. The image bytes are embedded in the workbook as a media part attached to the header/footer drawing layer of that worksheet, so the picture prints with the header or footer.

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

The printed `&G` is the picture code Excel interprets when rendering the header — the `logo.png` bytes now live inside `HeaderFooterPicture.xlsx`, and the image prints in place of the code.
To use header and footer Smart Markers, write `<<Source.Field>>` placeholders into the left, center, and right header or footer sections with `SetHeader` and `SetFooter`. Set `EnableHeaderFooterMarkers` to `true` on the `WorkbookDesigner` before calling `Process()`, and supply values through either `SetDataSource(DataTable)` or `SetJsonDataSource`. Read the completed sections with `GetHeader` and `GetFooter`. The same data source can populate body markers and header or footer placeholders in one processing pass. Add the `(picture)` suffix with a data-URI value to bind an image into a section.

## Related Articles
- [SmartMarker Single Cell Array Rendering](/cells/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="csharp" >}}