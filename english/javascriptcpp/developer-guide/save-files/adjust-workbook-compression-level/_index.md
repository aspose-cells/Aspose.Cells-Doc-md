---
title: Adjust Workbook Compression Level with JavaScript via C++
linktitle: Adjust Workbook Compression Level
type: docs
weight: 180
url: /javascript-cpp/adjust-workbook-compression-level/
description: Learn how to adjust the workbook compression level in Aspose.Cells for JavaScript via C++.
---

## **Adjust Workbook Compression Level**

Developers can adjust the compression level of the workbook when working with larger workbooks. Developers may prioritize smaller file sizes over processing time or vice versa. Aspose.Cells for JavaScript via C++ provides the [**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype) enumeration which you can use to set the compression level of the workbook. The [**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype) enumeration provides the following members.

- Level 1: The fastest but least effective compression.  
- Level 2: A little slower, but better, than level 1.  
- Level 3: A little slower, but better, than level 2.  
- Level 4: A little slower, but better, than level 3.  
- Level 5: A little slower than level 4, but with better compression.  
- Level 6: A good balance of speed and compression efficiency.  
- Level 7: Pretty good compression!  
- Level 8: Better compression than Level 7!  
- Level 9: The "best" compression, where best means greatest reduction in the size of the input data stream. This is also the slowest compression.  

The following code snippet demonstrates the use of the [**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype) enumeration and compares the conversion time for Level 1, Level 6, and Level 9. You may also compare the sizes of the generated files.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save XLSB with Compression Levels</title>
    </head>
    <body>
        <h1>Save XLSB with Different Compression Levels</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none; margin-right:10px;"></a>
            <a id="downloadLink2" style="display: none; margin-right:10px;"></a>
            <a id="downloadLink3" style="display: none;"></a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XlsbSaveOptions, OoxmlCompressionType, Utils } = AsposeCells;
        
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
            const downloadLink1 = document.getElementById('downloadLink1');
            const downloadLink2 = document.getElementById('downloadLink2');
            const downloadLink3 = document.getElementById('downloadLink3');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create Xlsb save options
            const options = new XlsbSaveOptions();

            // Level 1
            let start = performance.now();
            options.compressionType = OoxmlCompressionType.Level1;
            const outputData1 = workbook.save(SaveFormat.Xlsb, options);
            let elapsedMs1 = performance.now() - start;

            const blob1 = new Blob([outputData1]);
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'LargeSampleFile_level_1_out.xlsb';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Level 1 XLSB';

            // Level 6
            start = performance.now();
            options.compressionType = OoxmlCompressionType.Level6;
            const outputData2 = workbook.save(SaveFormat.Xlsb, options);
            let elapsedMs2 = performance.now() - start;

            const blob2 = new Blob([outputData2]);
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'LargeSampleFile_level_6_out.xlsb';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Level 6 XLSB';

            // Level 9
            start = performance.now();
            options.compressionType = OoxmlCompressionType.Level9;
            const outputData3 = workbook.save(SaveFormat.Xlsb, options);
            let elapsedMs3 = performance.now() - start;

            const blob3 = new Blob([outputData3]);
            downloadLink3.href = URL.createObjectURL(blob3);
            downloadLink3.download = 'LargeSampleFile_level_9_out.xlsb';
            downloadLink3.style.display = 'inline-block';
            downloadLink3.textContent = 'Download Level 9 XLSB';

            resultDiv.innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <ul>
                    <li>Level 1 Elapsed Time: ${elapsedMs1.toFixed(2)} ms</li>
                    <li>Level 6 Elapsed Time: ${elapsedMs2.toFixed(2)} ms</li>
                    <li>Level 9 Elapsed Time: ${elapsedMs3.toFixed(2)} ms</li>
                </ul>
            `;
        });
    </script>
</html>
```