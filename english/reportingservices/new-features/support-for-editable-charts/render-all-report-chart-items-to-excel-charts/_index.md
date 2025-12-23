---
title: Render All Report Chart Items to Excel Charts
linktitle: Render All Report Charts
type: docs
weight: 10
url: /reportingservices/render-all-report-chart-items-to-excel-charts/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}
**Quick tip:** To render **all** chart items in a report as editable Excel charts, update the `<Chart>` element in **Aspose.Cells.ReportingServices.xml** to use the value `all`.

```xml
<Chart value="all" />
```

When the `value` attribute is set to `all`, every chart defined in the report is exported as an editable Excel chart rather than a static image.

**Result in Excel**

![Editable Excel chart rendered from a report](render-all-report-chart-items-to-excel-charts_1.png)
{{% /alert %}}

{{% alert color="primary" %}}

## How It Works

Aspose.Cells for Reporting Services uses the **Aspose.Cells.ReportingServices.xml** configuration file to control how chart objects are exported. By default only selected charts are converted to native Excel chart objects; the rest are rendered as images. Changing the `<Chart>` node to `value="all"` instructs the engine to treat *every* chart as a native Excel chart.

## Step‑by‑Step Configuration

1. **Locate the configuration file**  
   The file is typically found in the Reporting Services installation folder, e.g.:

   ```text
   C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer\Aspose.Cells.ReportingServices.xml
   ```

or

   ```text
   C:\Program Files\Aspose\Aspose.Cells for Reporting Services\Aspose.Cells.ReportingServices.xml
   ```

1. **Open the file in a text editor** (Notepad, VS Code, etc.).

2. **Find the `<Chart>` element**.  
   It may look like this by default:

   ```xml
   <Chart value="selected" />
   ```

3. **Replace the value** with `all`:

   ```xml
   <Chart value="all" />
   ```

4. **Save the file** and restart the Reporting Services service (or recycle the application pool) so the changes take effect.

5. **Export your report** to Excel. All chart items will now appear as fully editable Excel charts.
