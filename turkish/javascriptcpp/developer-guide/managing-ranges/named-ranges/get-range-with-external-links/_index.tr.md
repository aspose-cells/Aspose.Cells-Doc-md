---
title: Dış Bağlantılı Aralıkları JavaScript ile C++ kullanarak alın
linktitle: Harici Bağlantıları İçeren Menzil Al
type: docs
weight: 120
url: /tr/javascript-cpp/get-range-with-external-links/
description: Aspose.Cells for JavaScript via C++ kullanarak dış bağlantıları olan aralıkları nasıl alacağınızı öğrenin. Farklı Excel dosyalarından verileri verimli şekilde alın.
---

## **Harici Bağlantıları Olan Aralığı Al**

Birçok zaman, Excel dosyaları diğer Excel dosyalarına dış bağlantılar kullanarak veri erişir. Aspose.Cells for JavaScript via C++ bu dış bağlantıları [**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-) yöntemi ile almanızı sağlar. [**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-) yöntemi [**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea) türünde bir dizi döner. [**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea) sınıfı, dış dosyanın adını döndüren [**ReferredArea.externalFileName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#externalFileName--) özelliği sağlar. [**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea) sınıfı ise aşağıdaki üyeleri gösterir.

- [**ReferredArea.endColumn**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#endColumn--): Bölgenin son sütunu
- [**ReferredArea.endRow**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#endRow--): Bölgenin son satırı
- [**ReferredArea.externalFileName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#externalFileName--): Bu dış referanssa, dış dosya adını al
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#isArea--): Bu, bir alan mı gösterir
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#isExternalLink--): Bu, dış bağlantı mı gösterir
- [**ReferredArea.sheetName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#sheetName--): Bu, hangi sayfada olduğunu gösterir
- [**ReferredArea.startColumn**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#startColumn--): Bölgenin başlangıç sütunu
- [**ReferredArea.startRow**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#startRow--): Bölgenin başlangıç satırı

Aşağıda verilen örnek kod, Dış Bağlantılı Aralıkları almak için [**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-) metodunun kullanımını gösterir.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - External References</title>
    </head>
    <body>
        <h1>Sample External References</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (SampleExternalReferences.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing named ranges via worksheets.names
            const names = workbook.worksheets.names;
            const namesCount = names.count;
            const outputLines = [];
            outputLines.push(`<p>Processing file: ${file.name}</p>`);
            outputLines.push(`<p>Named Ranges Count: ${namesCount}</p>`);

            for (let i = 0; i < namesCount; i++) {
                const namedRange = names.get(i);
                outputLines.push(`<h3>Named Range ${i}: ${namedRange.name || ('Index ' + i)}</h3>`);

                // Get referred areas (including external references)
                const referredAreas = namedRange.referredAreas(true);
                if (referredAreas) {
                    referredAreas.forEach((referredArea, idx) => {
                        outputLines.push(`<h4>Referred Area ${idx}</h4>`);
                        outputLines.push(`<ul>`);
                        outputLines.push(`<li>IsExternalLink: ${referredArea.isExternalLink}</li>`);
                        outputLines.push(`<li>IsArea: ${referredArea.isArea}</li>`);
                        outputLines.push(`<li>SheetName: ${referredArea.sheetName}</li>`);
                        outputLines.push(`<li>ExternalFileName: ${referredArea.externalFileName}</li>`);
                        outputLines.push(`<li>StartColumn: ${referredArea.startColumn}</li>`);
                        outputLines.push(`<li>StartRow: ${referredArea.startRow}</li>`);
                        outputLines.push(`<li>EndColumn: ${referredArea.endColumn}</li>`);
                        outputLines.push(`<li>EndRow: ${referredArea.endRow}</li>`);
                        outputLines.push(`</ul>`);
                    });
                } else {
                    outputLines.push(`<p>No referred areas for this named range.</p>`);
                }
            }

            resultDiv.innerHTML = outputLines.join('');
        });
    </script>
</html>
```
