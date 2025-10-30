---
title: Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma
linktitle: Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma
description: JavaScript kullanarak Aspose.Cells kütüphanesi ile hücre hizalamasını değiştirme ve mevcut biçimlendirmeyi koruma (C++ aracılığıyla)
keywords: Aspose.Cells, JavaScript kullanarak C++ aracılığıyla, Hücre hizalaması, mevcut biçimlendirmeyi koruma
type: docs
weight: 340
url: /tr/javascript-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Olası Kullanım Senaryoları**

Bazen, birden fazla hücrenin hizalamasını değiştirmek istersiniz ancak mevcut biçimlendirmeyi de korumak istersiniz. Aspose.Cells for JavaScript aracılığıyla C++, bunu [**StyleFlag.alignments(boolean)**](https://reference.aspose.com/cells/javascript-cpp/styleflag/#alignments-boolean-) yöntemi ile yapmanıza olanak tanır. Eğer **true** olarak ayarlarsanız, hizalamadaki değişiklikler gerçekleşir aksi takdirde gerçekleşmez. Lütfen, [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) nesnesinin [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-) yöntemine parametre olarak geçtiğini unutmayın, bu yöntem aslında biçimlendirmeyi bir hücre aralığına uygular.

## **Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma**

Aşağıdaki örnek kod, [örnek Excel dosyasını](67338585.xlsx) yükler, aralık oluşturur ve yatay ve dikey olarak ortalayıp mevcut biçimlendirmeyi korur. Aşağıdaki ekran görüntüsü, örnek Excel dosyasını ve [çıktı Excel dosyasını](67338586.xlsx) karşılaştırır ve hücrelerin mevcut biçimlendirmesinin aynı olduğunu ancak hücrelerin şimdi yatay ve dikey olarak merkezlenmiş olduğunu gösterir.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Cells Alignment and Keep Existing Formatting</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, TextAlignmentType, Utils } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create cells range
            const range = worksheet.cells.createRange("B2:D7");

            // Create style object
            const style = workbook.createStyle();

            // Set the horizontal and vertical alignment to center using property assignments
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            // Create style flag object
            const flag = new StyleFlag();
            flag.alignments = true; // Set style flag alignments true

            // Apply style to range of cells
            range.applyStyle(style, flag);

            // Save the workbook in XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
