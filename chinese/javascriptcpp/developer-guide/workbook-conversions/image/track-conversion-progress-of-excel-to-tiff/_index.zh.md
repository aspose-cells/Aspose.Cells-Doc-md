---
title: 用 JavaScript 通过 C++ 追踪 Excel 转换为 TIFF 的进度
linktitle: 跟踪Excel转换为TIFF的进度
type: docs
weight: 190
url: /zh/javascript-cpp/track-conversion-progress-of-excel-to-tiff/
description: 学习如何用 Aspose.Cells for JavaScript 通过 C++ 追踪 Excel 文件转换为 TIFF 的过程。在转换过程中提升用户体验。
---

## **可能的使用场景**

有时候转换大型 Excel 文件可能需要一些时间。在此期间，您可能希望显示文档转换的进度，而不是加载屏幕，从而提升应用的易用性。Aspose.Cells for JavaScript 通过 C++ 支持追踪文档转换过程，提供 [**IPageSavingCallback**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback) 接口。[**IPageSavingCallback**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback) 接口提供 [**pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) 和 [**pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-) 方法，您可以在自定义类中实现它们。您还可以控制哪些页面被渲染，方法可参考 *TestPageSavingCallback* 自定义类的示例。

## **跟踪Excel转换为TIFF的进度**

下面的代码示例加载了【源 Excel 文件】(95584311.xlsx)，并使用实现了 [**IPageSavingCallback**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback) 接口的 *TestPageSavingCallback* 自定义类在控制台打印其转换进度。生成的输出文件已附上供您参考。

[Output File](95584312.tiff)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to TIFF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="convertTiff">Convert to TIFF</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, WorkbookRender, ImageType, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('convertTiff').addEventListener('click', async () => {
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

                // Create ImageOrPrintOptions and configure for TIFF conversion
                const opts = new ImageOrPrintOptions();

                // Define TestTiffPageSavingCallback
                class TestTiffPageSavingCallback {
                    // Implement pageSaving as a no-op handler; Aspose.Cells may call this during TIFF generation
                    pageSaving(args) {
                        // No-op: default behavior will be used for page saving
                        // If needed, args (like args.imageStream) can be modified here
                    }
                }

                // Assign callback and image type using property assignment (converted from setters)
                opts.pageSavingCallback = new TestTiffPageSavingCallback();
                opts.imageType = ImageType.Tiff;

                // Create WorkbookRender and generate the TIFF image
                const wr = new WorkbookRender(workbook, opts);
                const outputData = wr.toImage();

                // Create a Blob and provide a download link for the generated TIFF
                const blob = new Blob([outputData], { type: 'image/tiff' });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'DocumentConversionProgressForTiff_out.tiff';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download TIFF File';

                resultDiv.innerHTML = '<p style="color: green;">Conversion completed. Click the download link to save the TIFF.</p>';
            });
        });
    </script>
</html>
```

以下是 *TestTiffPageSavingCallback* 自定义类的代码。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - TIFF Page Saving Callback</title>
    </head>
    <body>
        <h1>TIFF Page Saving Callback Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Save as TIFF with Page Callback</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

        class TestTiffPageSavingCallback {
            pageStartSaving(args) {
                console.log(`Start saving page index ${args.pageIndex} of pages ${args.pageCount}`);

                // Don't output pages before page index 2.
                if (args.pageIndex < 2) {
                    args.isToOutput = false;
                }
            }

            pageEndSaving(args) {
                console.log(`End saving page index ${args.pageIndex} of pages ${args.pageCount}`);

                // Don't output pages after page index 8.
                if (args.pageIndex >= 8) {
                    args.hasMorePages = false;
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create TIFF save options and assign the page saving callback
            const tiffOptions = new AsposeCells.TiffSaveOptions();
            tiffOptions.pageSavingCallback = new TestTiffPageSavingCallback();

            // Save the workbook as TIFF using the save options
            const outputData = workbook.save(SaveFormat.Tiff, tiffOptions);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TIFF saved successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **控制台输出**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
