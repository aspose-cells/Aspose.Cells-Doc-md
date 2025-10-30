---
title: JavaScript ile C++ kullanarak Paylaşılan Formüller için Maksimum Satır Sayısını Belirtin
linktitle: Paylaşılan Formülün Maksimum Satırlarını Belirtme
type: docs
weight: 40
url: /tr/javascript-cpp/specify-maximum-rows-of-shared-formula/
description: Aspose.Cells for JavaScript kullanarak C++ ile paylaşılan formüller için maksimum satır sayısını nasıl belirleyeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**  

Varsayılan olarak, paylaşılan formülün maksimum satır sayısı 64'tür. Bu herhangi bir sayı olabilir örneğin 1000 olabilir. Paylaşılan formülün performansı, satır sayısı ile değişir. Bu nedenle, Aspose.Cells, paylaşılan formülün maksimum satır sayısını belirlemek için kullanılabilecek [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--) özelliği sağlar. Paylaşılan formül toplam satır sayısı bu değerden büyükse, birkaç paylaşılan formüle bölünecektir, aşağıdaki ekran görüntüsünde gösterildiği gibi.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Paylaşılan Formülün Maksimum Satırlarını Belirtme**  

Aşağıdaki örnek kod, [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--) özelliğinin kullanımı açıklamaktadır. Paylaşılan formülün maksimum satır sayısını 5 olarak ayarlar ve D1 hücresinde 100 satır için paylaşılan formülü ekler ve sonucu [çıktı Excel dosyasına](61767856.xlsx) kaydeder. Eğer çıktı Excel dosyasının içeriğini çıkarırsanız ve *sheet1.xml* dosyasını kontrol ederseniz, paylaşılan formülün her 5 satırda bir bölündüğünü görebilirsiniz, yukarıdaki ekran görüntüsünde vurgulanmıştır.  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Maximum Rows Of Shared Formula Example</title>
    </head>
    <body>
        <h1>Specify Maximum Rows Of Shared Formula Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Set the max rows of shared formula to 5
            workbook.settings.maxRowsOfSharedFormula = 5;

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access cell D1
            const cell = ws.cells.get("D1");

            // Set the shared formula in 100 rows
            cell.sharedFormula = ["=Sum(A1:A2)", 100, 1];

            // Save the output Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyMaximumRowsOfSharedFormula.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
