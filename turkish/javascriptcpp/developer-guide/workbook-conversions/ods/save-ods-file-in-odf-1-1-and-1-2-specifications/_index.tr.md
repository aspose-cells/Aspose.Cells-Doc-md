---
title: JavaScript ile C++ kullanarak ODF 1.1, 1.2 ve 1.3 olarak kaydetme
linktitle: ODS Dosyasını ODF 1.1, 1.2 ve 1.3 sürümlerinde Kaydet
description: Aspose.Cells for JavaScript C++ ile ODF 1.1, 1.2 ve 1.3 spesifikasyonlarına dönüştürme
type: docs
weight: 230
url: /tr/javascript-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells, ODS dosyasını (**OpenDocument Elektronik Tablo**) ODF (**OpenDocument Format**) 1.1, 1.2 ve 1.3 spesifikasyonlara kaydetmeyi destekler. Aspose.Cells'in [**OdsSaveOptions.odfStrictVersion**](https://reference.aspose.com/cells/javascript-cpp/odssaveoptions/#odfStrictVersion--) özelliği, ODS dosyalarını kaydetmek için ODF sürümünü belirler. Bu özellik varsayılan olarak [**OpenDocumentFormatVersionType.odf12**](https://reference.aspose.com/cells/javascript-cpp/opendocumentformatversiontype/)'dir, bu yüzden bu ayar olmadan kaydedilen ODS dosyası 1.2 spesifikasyonunu kullanır.

{{% /alert %}}

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur, ilk sayfadaki A1 hücresine bazı değerler ekler ve ardından ODS dosyasını ODF 1.1, 1.2 ve 1.3 spesifikasyonlarıyla kaydeder. Varsayılan olarak, ODS dosyası ODF 1.2 spesifikasyonu ile kaydedilir.

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
