---
title: Import Specific HTML Tables using HtmlTableLoadOption
type: docs
weight: 130
url: /net/html-table-load-option/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

While loading an HTML file into a Workbook, Aspose.Cells imports every table it finds. With the [**HtmlTableLoadOption**](https://reference.aspose.com/cells/net/aspose.cells/htmltableloadoption/) class, you can control which tables are imported and into which worksheet each table is placed.

{{% /alert %}}

## **Possible Usage Scenarios**

Aspose.Cells exposes the [**HtmlLoadOptions.TableLoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/tableloadoptions/) property that returns an [**HtmlTableLoadOptionCollection**](https://reference.aspose.com/cells/net/aspose.cells/htmltableloadoptioncollection/) instance. The collection provides several `Add` overloads to define the tables to import:

- `Add(Int32)` – imports the table at the specified table index.
- `Add(Int32, Int32)` – imports the table at the specified table index into the worksheet with the given target index.
- `Add(HtmlTableLoadOption)` – imports a table described by an [**HtmlTableLoadOption**](https://reference.aspose.com/cells/net/aspose.cells/htmltableloadoption/) instance.

The [**HtmlTableLoadOption**](https://reference.aspose.com/cells/net/aspose.cells/htmltableloadoption/) class exposes the following properties to describe a single table:

- **Id** – the id of the table to import from HTML.
- **TableIndex** – the index of the table to import from HTML.
- **OriginalSheetIndex** – the original index of the worksheet in the HTML.
- **TargetSheetIndex** – the target index of the worksheet where the table is to be located.
- **TableToListObject** – indicates whether to generate list objects from the imported table. The default value is **false**.

If no table load option is specified, all the tables are imported. When options are added, only the referenced tables are imported. Tables that target the same worksheet are placed into it one after another in the order of the added options.

## **Sample Code**

The following sample code loads the sample HTML file twice. The first time, tables are selected by table index (`1`, `2`) and by table id (`id5`, `id6`), and all of them are imported into the first worksheet. The options are then cleared and built again, this time sending each table to a specific worksheet by using the [**TargetSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/htmltableloadoption/properties/targetsheetindex/) property. Please download the [sample HTML file](HtmlTableLoadOption.htm) used by the code.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HtmlTableLoadOption-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}