---
title: JavaScript経由でC++を使用してワークブックの圧縮レベルを調整する
linktitle: Workbookの圧縮レベルを調整
type: docs
weight: 180
url: /ja/javascript-cpp/adjust-workbook-compression-level/
description: C++を使用してAspose.Cells for JavaScriptでワークブックの圧縮レベルを調整する方法を学びます。
---

## **ワークブックの圧縮レベルを調整する**

開発者は、大きなワークブックを扱う際にワークブックの圧縮レベルを調整できます。ファイルサイズを小さくすることを優先するか、処理時間を優先するかを選択できます。Aspose.Cells for JavaScriptは、ワークブックの圧縮レベルを設定するために[**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype)列挙体を提供しています。[**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype)列挙体は以下のメンバーを提供します。

- Level1：最速ですがあまり効果的でない圧縮。  
- Level2：少し遅くなりますが、Level1より優れています。  
- Level3：少し遅くなりますが、Level2より優れています。  
- Level4：少し遅くなりますが、Level3より優れています。  
- レベル5：レベル4よりもやや遅く、より効果的な圧縮。  
- レベル6：速度と圧縮効率の良いバランス。  
- Level7：かなり良い圧縮！  
- レベル8：レベル7よりも優れた圧縮！  
- Level9：「最良」の圧縮です。ここでの最良は入力データストリームのサイズを最も小さくすることを意味します。これはまた、最も遅い圧縮でもあります。  

次のコードスニペットは、[**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype)列挙型の使用を示し、Level1、Level6、Level9の変換時間を比較します。また、生成されたファイルのサイズを比較することもできます。  

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
