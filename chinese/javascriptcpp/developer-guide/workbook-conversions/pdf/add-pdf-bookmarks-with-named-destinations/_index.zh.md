---
title: 使用JavaScript通过C++添加带有命名目标的PDF书签
linktitle: 使用命名目的地添加PDF书签
type: docs
weight: 20
url: /zh/javascript-cpp/add-pdf-bookmarks-with-named-destinations/
description: 学习如何使用Aspose.Cells for Java脚本通过C++添加带有命名目标的PDF书签，确保在更改页面后书签依然完好无损。
---

## **可能的使用场景**

命名目标是PDF中特殊类型的书签或链接，不依赖于PDF页面。这意味着，如果PDF中添加或删除页面，书签可能会失效，但命名目标将保持完整。要创建命名目标，请设置 [**PdfBookmarkEntry.destinationName**](https://reference.aspose.com/cells/javascript-cpp/pdfbookmarkentry/#destinationName--) 属性。

## **使用命名目标添加PDF书签**

请查看以下示例代码，其 [源Excel文件](50528348.xlsx)，以及 [输出PDF文件](50528349.pdf)。屏幕截图显示了输出PDF中的书签和命名目标。屏幕截图还描述了如何查看命名目标，以及您需要Acrobat Reader的专业版。

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PDF Bookmark Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PDF Bookmark Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfBookmarkEntry, PdfSaveOptions } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell C5
            let cell = worksheet.cells.get("C5");

            // Create Bookmark and Destination for this cell
            const bookmarkEntry = new PdfBookmarkEntry();
            bookmarkEntry.text = "Text";
            bookmarkEntry.destination = cell;
            bookmarkEntry.destinationName = "AsposeCells--" + cell.name;

            // Access cell G56
            cell = worksheet.cells.get("G56");

            // Create Sub-Bookmark and Destination for this cell
            const subbookmarkEntry1 = new PdfBookmarkEntry();
            subbookmarkEntry1.text = "Text1";
            subbookmarkEntry1.destination = cell;
            subbookmarkEntry1.destinationName = "AsposeCells--" + cell.name;

            // Access cell L4
            cell = worksheet.cells.get("L4");

            // Create Sub-Bookmark and Destination for this cell
            const subbookmarkEntry2 = new PdfBookmarkEntry();
            subbookmarkEntry2.text = "Text2";
            subbookmarkEntry2.destination = cell;
            subbookmarkEntry2.destinationName = "AsposeCells--" + cell.name;

            // Add Sub-Bookmarks in list
            const list = [];
            list.push(subbookmarkEntry1);
            list.push(subbookmarkEntry2);

            // Assign Sub-Bookmarks list to Bookmark Sub-Entry
            bookmarkEntry.subEntries = bookmarkEntry.subEntries || [];
            bookmarkEntry.subEntries.push(...list);

            // Create PdfSaveOptions and assign Bookmark to it
            const opts = new PdfSaveOptions();
            opts.bookmark = bookmarkEntry;

            // Save the workbook in Pdf format with given pdf save options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputPdfBookmarkEntry_DestinationName.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to download the file.</p>';
        });
    </script>
</html>
```
