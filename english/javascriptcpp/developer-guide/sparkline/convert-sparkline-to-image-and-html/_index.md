---
title: Convert Sparkline to Image and HTML in Aspose.Cells for JavaScript via C++
description: Learn how to render Aspose.Cells sparklines to standalone images for cell embedding and export sparkline-rich worksheets to HTML using HtmlSaveOptions.
linktitle: Convert Sparkline to Image and HTML
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, sparkline, sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, render sparkline, convert sparkline to image, export sparkline to HTML
type: docs
weight: 120
url: /javascript-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines are miniature charts placed inside worksheet cells. Aspose.Cells lets you extract each sparkline as a standalone image (for embedding into another cell or an external report) and also export the entire sparkline-rich worksheet to HTML for browser-based distribution. The `cell.embeddedImage` property used in this article is available in **Aspose.Cells 26.5 and later**.
{{% /alert %}}

## **Introduction**
Sparklines are a compact way to visualize trends directly inside a worksheet. While Excel users see them in place, many real-world scenarios require a sparkline to leave the cell — for example, to be embedded into a different cell as a static picture, attached to an automated email, or rendered as part of an HTML report published to the web.
Aspose.Cells supports both of these operations. The `sparkline.toImage` method renders an individual sparkline as a `Buffer`, and the resulting bytes can be assigned to `cell.embeddedImage` so the picture is stored inside a single cell of the workbook. Separately, `HtmlSaveOptions` lets you convert the entire workbook — sparklines and all — into a self-contained HTML file. This article walks through both workflows end to end.

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**
In this workflow you will build a worksheet that contains a small range of source values, attach three different sparkline groups (Line, Column, and Stacked/Win-Loss) to that range, render each group as a PNG, and write those PNG bytes into adjacent cells as embedded images. The final result is a single `.xlsx` file that contains both the live sparklines and their rendered picture counterparts.

### **Step-by-Step Instructions**
1. Create a new `Workbook` and obtain a reference to the first `Worksheet`.
2. Populate cells `A1` through `E1` with five sample numeric values (for example, daily sales or temperature readings).
3. Add three `SparklineGroup` objects to the worksheet by calling `worksheet.getSparklineGroups().add(...)`:
   - A `SparklineType.Line` group anchored at `F1`, with data range `A1:E1`.
   - A `SparklineType.Column` group anchored at `G1`, with data range `A1:E1`.
   - A `SparklineType.Stacked` (win/loss) group anchored at `H1`, with data range `A1:E1`.
4. Build an `ImageOrPrintOptions` instance and set its `imageType` property to `ImageType.Png` so each sparkline renders as a PNG picture.
6. Save the workbook as `output_with_sparklines.xlsx`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, CellArea, ImageOrPrintOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Create a new workbook and access the first worksheet
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Populate sample data in cells A1:E1
            cells.get("A1").value = 5;
            cells.get("B1").value = -3;
            cells.get("C1").value = 8;
            cells.get("D1").value = -2;
            cells.get("E1").value = 6;
            // Add a Line sparkline group anchored at F1 (column 5, row 0)
            const lineArea = new CellArea();
            lineArea.startColumn = 5;
            lineArea.endColumn = 5;
            lineArea.startRow = 0;
            lineArea.endRow = 0;
            const lineIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Line,
                "A1:E1",
                false,
                lineArea
            );
            // Add a Column sparkline group anchored at G1 (column 6, row 0)
            const columnArea = new CellArea();
            columnArea.startColumn = 6;
            columnArea.endColumn = 6;
            columnArea.startRow = 0;
            columnArea.endRow = 0;
            const columnIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Column,
                "A1:E1",
                false,
                columnArea
            );
            // Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
            const stackedArea = new CellArea();
            stackedArea.startColumn = 7;
            stackedArea.endColumn = 7;
            stackedArea.startRow = 0;
            stackedArea.endRow = 0;
            const stackedIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Stacked,
                "A1:E1",
                false,
                stackedArea
            );
            // Configure image options for PNG output
            const imageOptions = new ImageOrPrintOptions();
            imageOptions.imageType = AsposeCells.ImageType.Png;
            // Convert the Line sparkline to image and embed it in cell F2
            const lineSp = worksheet.sparklineGroups.get(lineIdx).sparklines.get(0);
            cells.get("F2").embeddedImage = lineSp.toImage(imageOptions);
            // Convert the Column sparkline to image and embed it in cell G2
            const columnSp = worksheet.sparklineGroups.get(columnIdx).sparklines.get(0);
            cells.get("G2").embeddedImage = columnSp.toImage(imageOptions);
            // Convert the Win/Loss sparkline to image and embed it in cell H2
            const stackedSp = worksheet.sparklineGroups.get(stackedIdx).sparklines.get(0);
            cells.get("H2").embeddedImage = stackedSp.toImage(imageOptions);
            // Save the workbook to disk
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_with_sparklines.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

The code above produces a workbook where each visual representation of a sparkline exists in two forms: the live, native sparkline anchored at row 1, and a static PNG picture embedded directly into a neighboring cell on row 2. Because the pictures live inside the file itself, the workbook remains a single self-contained artifact that can be emailed or archived without breaking the embedded image references.

{{% alert color="primary" %}}
Because each sparkline group is anchored to a single cell, you can address it through the indexer `group.getSparklines()[0]` instead of enumerating the collection. This keeps the rendering code short and matches the typical "one sparkline per anchor cell" pattern. Storing the picture bytes via `cell.embeddedImage` requires Aspose.Cells 26.5 or later.
{{% /alert %}}

## **Workflow 2 — Export the Sparkline Worksheet to HTML**
Once the workbook contains live sparklines (and optionally embedded picture counterparts), the entire worksheet can be published to the web by saving it as HTML. The `HtmlSaveOptions` class exposes the knobs you need to control this export; in this workflow you will reuse the `output_with_sparklines.xlsx` file produced by Workflow 1 and convert it to a clean, single-page HTML document.

### **Step-by-Step Instructions**
1. Ensure the `output_with_sparklines.xlsx` file produced by Workflow 1 is available on disk in your working directory.
2. Load that file into a new `Workbook` instance.
3. Instantiate `HtmlSaveOptions` and set its `exportActiveWorksheetOnly` property to `true` so the resulting HTML file contains only the active worksheet rather than the entire workbook.
4. Call `workbook.save("sparklines.html", htmlOptions)` to write the HTML output to disk.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const htmlOptions = new HtmlSaveOptions();
                htmlOptions.exportActiveWorksheetOnly = true;
                const outputData = workbook.save(AsposeCells.SaveFormat.Html, htmlOptions);
                const blob = new Blob([outputData], { type: "text/html" });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "sparklines.html";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

The code above takes the sparkline-rich workbook from Workflow 1 and turns it into a portable HTML file. The sparkline groups are rendered as inline images inside the generated HTML table, so end users can view the trends in any modern browser without needing Excel installed. By setting `exportActiveWorksheetOnly` to `true`, you avoid accidentally publishing hidden sheets or auxiliary data — only the worksheet currently visible to the user is exported.

{{% alert color="primary" %}}
The `HtmlSaveOptions` class offers additional properties for fine-tuning the output, such as `exportHiddenWorksheet`, `exportImagesAsBase64`, and `encoding`. Adjust these as needed for your deployment target.
{{% /alert %}}

## **API Summary**
The workflows above rely on a small set of Aspose.Cells APIs working together.
- `SparklineGroup` and the collection accessor `worksheet.getSparklineGroups()` are used to declare the type (Line, Column, Stacked), the data range, and the anchor cell for each sparkline group. In this article each group is anchored to a single cell, so the group is reached through `worksheet.getSparklineGroups()[i]`.
- `Sparkline` and the indexer `group.getSparklines()[0]` return the individual sparkline inside a group. Because every group in the example contains exactly one sparkline, no iteration loop is required.
- `sparkline.toImage(imageOrPrintOptions)` is the rendering method that returns a picture of the sparkline as a `Buffer`. The returned bytes can be assigned directly to `cell.embeddedImage`.
- `HtmlSaveOptions.exportActiveWorksheetOnly` (a Boolean) restricts HTML export to the active worksheet. It is one of the most commonly used properties on `HtmlSaveOptions` when generating single-page reports.
- `ImageOrPrintOptions.imageType` selects the picture format (for example, `ImageType.Png`) used when rendering with `toImage` and when printing worksheets to images.

{{< app/cells/assistant language="javascript-cpp" >}}