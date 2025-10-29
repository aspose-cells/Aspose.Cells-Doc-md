---
title: حفظ كملف ODF 1.1، 1.2 و 1.3 باستخدام جافا سكريبت عبر C++
linktitle: حفظ ملف ODS بصيغة ODF 1.1 و 1.2 و 1.3
description: تحويل إكسل إلى مواصفات ODF 1.1، 1.2 و 1.3 باستخدام Aspose.Cells for JavaScript عبر C++.
type: docs
weight: 230
url: /ar/javascript-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells حفظ ملف ODS (**جداول بيانات المستند المفتوح**) بصيغة ODF (**صيغة المستند المفتوح**) وفقًا لمواصفات 1.1 و 1.2 و 1.3. لدى Aspose.Cells خاصية [**OdsSaveOptions.odfStrictVersion**](https://reference.aspose.com/cells/javascript-cpp/odssaveoptions/#odfStrictVersion--) التي تحدد إصدار ODF لحفظ ملفات ODS. القيمة الافتراضية لهذه الخاصية هي [**OpenDocumentFormatVersionType.odf12**](https://reference.aspose.com/cells/javascript-cpp/opendocumentformatversiontype/)، لذلك الملف ODS المحفوظ بدون ضبط هذه الخاصية يستخدم مواصفات 1.2.

{{% /alert %}}

يفترض الكود النموذجي أدناه إنشاء كائن عمل، يضيف قيمة إلى الخلية A1 في الورقة الأولى ثم يقوم بحفظ ملف ODS وفقًا لمواصفات ODF 1.1 و 1.2 و 1.3. بشكل افتراضي، يتم حفظ ملف ODS بمواصفات ODF 1.2.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells ODS Save Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ODS Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv,.ods" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none;"></a><br/>
            <a id="downloadLink2" style="display: none;"></a><br/>
            <a id="downloadLink3" style="display: none;"></a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OdsSaveOptions, OpenDocumentFormatVersionType, Utils } = AsposeCells;

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

            if (fileInput.files.length > 0) {
                // If a file is provided, it will be loaded. Otherwise a new workbook will be created.
            }

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some value in cell A1
            const cell = worksheet.cells.get("A1");
            cell.putValue("Welcome to Aspose!");

            // Save ODS in ODF 1.2 version which is default
            const options = new OdsSaveOptions();
            const outputData1 = workbook.save(SaveFormat.Ods, options);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'ODF1.2_out.ods';
            downloadLink1.style.display = 'block';
            downloadLink1.textContent = 'Download ODF 1.2 File';

            // Save ODS in ODF 1.1 version
            options.odfStrictVersion = OpenDocumentFormatVersionType.Odf11;
            const outputData2 = workbook.save(SaveFormat.Ods, options);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'ODF1.1_out.ods';
            downloadLink2.style.display = 'block';
            downloadLink2.textContent = 'Download ODF 1.1 File';

            // Save ODS in ODF 1.3 version
            options.odfStrictVersion = OpenDocumentFormatVersionType.Odf13;
            const outputData3 = workbook.save(SaveFormat.Ods, options);
            const blob3 = new Blob([outputData3]);
            const downloadLink3 = document.getElementById('downloadLink3');
            downloadLink3.href = URL.createObjectURL(blob3);
            downloadLink3.download = 'ODF1.3_out.ods';
            downloadLink3.style.display = 'block';
            downloadLink3.textContent = 'Download ODF 1.3 File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Files are ready. Click the download links to save them.</p>';
        });
    </script>
</html>
```
