---
title: 使用JavaScript通过C++调整工作簿压缩级别
linktitle: 调整工作簿压缩级别
type: docs
weight: 180
url: /zh/javascript-cpp/adjust-workbook-compression-level/
description: 学习如何在Aspose.Cells for JavaScript中通过C++调整工作簿的压缩级别。
---

## **调整工作簿压缩级别**

开发人员在处理较大的工作簿时，可以调整工作簿的压缩级别。开发人员可以优先考虑更小的文件大小或处理时间。Aspose.Cells for JavaScript通过C++提供了[**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype)枚举，可用于设置工作簿的压缩级别。[**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype)枚举包含以下成员。

- Level1：速度最快，但压缩效果最差。  
- Level2：比级别1略慢，但效果更好。  
- Level3：比级别2略慢，效果更佳。  
- Level4：比级别3略慢，效果更佳。  
- Level5: 比级别4略慢，但压缩效果更好。  
- Level6: 速度和压缩效率的良好平衡。  
- Level7：压缩效果非常不错！  
- Level8: 比Level7压缩更好！  
- Level9：最"佳"压缩，这里的"佳"意味着最大程度地减小输入数据流的大小。这也是最慢的压缩方式。  

以下代码片段演示了使用 [**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype) 枚举，并比较了 Level1、Level6 和 Level9 的转换时间。 您还可以比较生成文件的大小。  

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
