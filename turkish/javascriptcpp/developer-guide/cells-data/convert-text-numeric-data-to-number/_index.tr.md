---
title: Metin Sayısal Verileri Sayıya Dönüştür
type: docs
weight: 900
url: /tr/javascript-cpp/convert-text-numeric-data-to-number/
description: Excel de sayısal olarak saklanan metni sayıya dönüştürmek için Aspose.Cells for JavaScript C++ API kullanımıyla ilgili detayları öğrenin.
keywords: excel metni sayıya dönüştür, excel metni sayıya dönüştür JavaScript kodu, excel metin sayısal veriyi sayıya dönüştür, excel metin sayısal veriyi sayıya dönüştür JavaScript kodu, excel sayısal metni sayıya dönüştür, excel sayısal metni sayıya dönüştür JavaScript kodu, excel sayısal metni JavaScript kodu ile sayıya dönüştür, excel de sayısal metni JavaScript koduyla sayıya dönüştür, excel de sayısal metni JavaScript koduyla sayıya dönüştür, excel de sayısal dizgiyi sayıya dönüştür JavaScript kodu, excel metni sayısal veriyi sayıya dönüştür JavaScript kodu, excel de sayısal dizgiye JavaScript koduyla dönüşüm
---

## **Olası Kullanım Senaryoları**
Bazen, metin olarak girilen sayısal verileri sayıya dönüştürmek istersiniz. Microsoft Excel'de sayıları metin olarak girerken bir apostrof önüne koyabilirsiniz, örneğin **'12345**. Excel then sayıyı string olarak kabul eder. Aspose.Cells for JavaScript C++ ile dizeleri sayıya dönüştürebilirsiniz.


## Excel'de metin olarak depolanan sayıları sayılara dönüştürme
Birkaç basit adımı izleyerek metin olarak depolanan sayıları sayılara dönüştürebilirsiniz.
1. Sol üst köşede bir hata göstergesi bulunan herhangi bir tek hücre veya hücre aralığını seçin.
1. Seçili hücre veya hücre aralığının yanına, ortaya çıkan hata düğmesine tıklayın. Menüde, Sayıya Dönüştür üzerine tıklayın. 
<br>
<img src="4.png" width=70% />
1. Uyarı düğmesi kullanılabilir değilse, Bu sorunu yaşayan bir sütun seçin. Tüm sütunu dönüştürmek istemiyorsanız, bunun yerine bir veya daha fazla hücre seçebilirsiniz. Seçtiğiniz hücrelerin aynı sütunda olduğundan emin olun, aksi halde bu işlem çalışmaz. Bir sütunu bölme için genellikle Metin Bölme düğmesi kullanılır, ancak aynı zamanda bir sütun metnini sayılara dönüştürmek için de kullanılabilir. Veri sekmesinde, Metin Bölme'ye tıklayın.
<br>
<img src="1.png" width=70% />
1. Açılır pencerede Tamam düğmesine tıklayın.
<br>
<img src="2.png" width=70% />
1. Metin olarak depolanan sayılar sayılara dönüştürülür.
<br>
<img src="3.png" width=70% />

## Aspose.Cells for JavaScript C++ kullanarak metin olarak saklanan sayıları sayıya dönüştürme yolları
Aspose.Cells for JavaScript C++ [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) metodunu sağlar, bu metod tüm dizgi veya metin ile saklanan sayısal verileri sayıya dönüştürmek için kullanılabilir.

Aşağıdaki ekran görüntüsü, hücrelerdeki string sayıları **A1:A17** göstermektedir. Dize sayıları sola hizalanmıştır.
<br>
<img src="5.png" width=70% />

Bu string sayılar aşağıdaki ekran görüntüsünde [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) kullanılarak sayılara dönüştürülmüştür. Görebileceğiniz gibi, şimdi sağa hizalanmış durumdadırlar.
<br>
<img src="6.png" width=70% />

## Dize sayılarını gerçek sayılara dönüştürmek için JavaScript kodu

Aşağıdaki örnek kod, tüm çalışma sayfalarındaki dize sayısal verileri gerçek sayılara dönüştürmenin nasıl yapıldığını göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Strings to Numeric Values in All Sheets</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook object with the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;
            const sheetcount = sheets.count;

            // Iterate through all worksheets and convert strings to numeric values
            for (let i = 0; i < sheetcount; i++) {
                const sheet = sheets.get(i);
                sheet.cells.convertStringToNumericValue();
            }

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
