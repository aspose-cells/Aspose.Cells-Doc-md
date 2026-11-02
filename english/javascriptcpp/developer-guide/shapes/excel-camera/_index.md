---
title: Excel Camera in Aspose.Cells for JavaScript via C++
description: Learn how to use Excel Camera in Aspose.Cells for JavaScript via C++ to create a dynamic picture linked to a cell range that refreshes with the source data and preserves all source formatting.
linktitle: Excel Camera
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, Excel Camera, dynamic picture, linked picture, picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /javascript-cpp/excel-camera/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera is a worksheet object that renders a live image of a cell range and floats on the drawing layer like an ordinary picture. Aspose.Cells supports two creation modes, a dynamic picture that auto-refreshes whenever the source data changes and a static picture that captures a one-time snapshot of a range. This article walks through both approaches so you can pick the one that fits your layout.

## What Is Excel Camera?
The Excel Camera is essentially a picture object anchored to a specific row and column on the worksheet's drawing layer. Unlike a regular inserted picture, the Camera is linked to a source range through an A1-style formula such as `"A1:F10"`. Whenever any cell inside that range changes, the Camera's image is refreshed automatically to reflect the new content. The Camera preserves the full formatting of the source area — borders, background colors, fonts, and number formats — so everything visible inside the cells appears inside the Camera's image as well. This makes the Camera especially useful for dashboards, summaries, side panels, and report layouts where you want a visible preview of a remote region without scrolling or repeating data. Two caveats apply: you must call `updateSelectedValue()` before saving the workbook, and the file will be exported to HTML or PDF, because those formats rely on the embedded image data rather than a live recalculation.

## Method 1 — Add a Dynamic Camera Picture
The dynamic Camera is the most common approach and is the closest match to Excel's built-in Camera tool. It works by adding a picture with no initial image content, then assigning it a `formula` that references the source range. After the formula is assigned, calling `updateSelectedValue()` refreshes the embedded image data so it is in sync with the cells it mirrors. The Camera is not implemented through a dedicated class — it is built entirely on the standard `Picture` type.
The key APIs are:
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, null)` — adds a picture anchored at the given row and column. Passing `null` for the image parameter creates an empty picture that acts as the placeholder for a dynamic Camera. The method returns the index of the new picture.
- `worksheet.getPictures().get(index)` — retrieves a specific `Picture` from the collection.
- `picture.formula` — a string property holding the A1-style reference to the source range that the Camera mirrors, such as `"A1:F10"`.
- `picture.updateSelectedValue()` — a void method that refreshes the embedded image data from the cells referenced by `formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` MUST be called before saving when the output is HTML or PDF; otherwise the exported file will not contain the picture data and the Camera will appear blank in the rendered output.
The following code creates a workbook, adds an empty picture anchored at row 10 column 6, links it to the source range `A1:F10` through the `formula` property, refreshes the embedded image data, and saves the workbook.
{{% /alert %}}

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
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
            const pictures = worksheet.pictures;
            const index = pictures.add(10, 6, null);
            const picture = pictures.get(0);
            picture.formula = "A1:F10";
            picture.updateSelectedValue();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_dynamic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Method 2 — Add a Static Camera Picture
The static Camera is essentially a one-time rendered preview of a cell range. Instead of maintaining a live link, you render the range to image bytes once, wrap those bytes in a `Buffer`, and add them as a regular picture. The image content is then fixed at the moment of creation and does not auto-refresh when source cells change.
The key APIs are:
- `cells.createRange(address)` — builds a `Range` object from an A1-style address such as `"A1:F10"`.
- `range.toImage(options)` — renders the range to image bytes. Passing `null` uses the default rendering options; overloads exist for finer control over output.
- `Buffer.from(imageBytes)` — wraps the rendered image bytes in a `Buffer` that can be fed into `worksheet.getPictures().add`.
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, imageBuffer)` — adds the picture anchored at the given row and column, this time passing the `Buffer` produced by the render.
The following code creates a workbook, builds a `Range` for `A1:F10`, renders it to image bytes through `range.toImage(null)`, wraps the bytes in a `Buffer`, adds the picture anchored at row 10 column 6, and saves the workbook.

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
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Static Camera: build Range, render to bytes, wrap in MemoryStream, add as picture
            const range = worksheet.cells.createRange("A1:F10");
            const imageData = range.toImage();
            const pictures = worksheet.pictures;
            pictures.add(10, 6, imageData);
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_static.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Choosing Between Dynamic and Static
- **Dynamic Camera:** updates on every recalculation, supports HTML and PDF export after `updateSelectedValue()`, and preserves the live-link behavior across the file's lifetime.
- **Static Camera:** a one-time render that never updates, useful when you want a fixed visual snapshot embedded at build time rather than a live mirror of the data.
Aspose.Cells supports both a dynamic, auto-refreshing Camera built on `picture.formula` plus `updateSelectedValue()` and a static, one-shot Camera built on `range.toImage` plus a `Buffer`. Choose the dynamic approach when your output needs to stay in sync with the source cells, and choose the static approach when you only need a fixed visual snapshot at build time.

## Related Articles
- [Convert Sparkline to Image and HTML in Aspose.Cells for JavaScript via C++](/cells/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for JavaScript via C++](/cells/javascript-cpp/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for JavaScript via C++](/cells/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}