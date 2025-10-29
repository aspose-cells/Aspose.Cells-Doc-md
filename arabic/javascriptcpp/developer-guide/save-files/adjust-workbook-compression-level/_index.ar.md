---
title: تعديل مستوى ضغط دفتر العمل باستخدام جافا سكريبت عبر ++C
linktitle: ضبط مستوى ضغط ملف العمل
type: docs
weight: 180
url: /ar/javascript-cpp/adjust-workbook-compression-level/
description: تعلم كيفية تعديل مستوى ضغط دفتر العمل باستخدام سكريبت Aspose.Cells for Java عبر ++C.
---

## **ضبط مستوى ضغط الورقة العمل**

يمكن للمطورين تعديل مستوى ضغط دفتر العمل عند العمل مع دفاتر عمل أكبر. قد يفضل المطورون حجم ملف أصغر على حساب زمن المعالجة أو العكس. يوفر سكريبت Aspose.Cells for Java عبر ++C التعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype) الذي يمكنك استخدامه لتعيين مستوى ضغط دفتر العمل. يوفر التعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype) الأعضاء التالية.

- المستوي 1: أسرع ضغط ولكن أقل فعالية.  
- المستوى 2: أبطأ قليلاً، ولكن أفضل من المستوى 1.  
- المستوى 3: أبطأ قليلاً، ولكن أفضل من المستوى 2.  
- المستوى 4: أبطأ قليلاً، ولكن أفضل من المستوى 3.  
- المستوى 5: أبطأ قليلاً من المستوى 4، لكن مع ضغط أفضل.  
- المستوى 6: توازن جيد بين السرعة وكفاءة الضغط.  
- المستوى 7: ضغط جيد جدًا!  
- المستوى8: ضغط أفضل من المستوى7!  
- المستوى 9: أفضل ضغط، حيث تعني الأفضل أقل حجم لتيار البيانات المدخلة. هذا هو أيضًا أبطأ ضغط.  

يوضح الشريحة الكودية التالية استخدام تعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompressiontype) ومقارنة وقت التحويل للمستوى 1 والمستوى 6 والمستوى 9. يمكنك أيضًا مقارنة أحجام الملفات المولدة.  

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
