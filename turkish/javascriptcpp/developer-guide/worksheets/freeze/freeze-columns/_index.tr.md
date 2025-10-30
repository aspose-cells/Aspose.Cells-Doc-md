---
title: Excel Çalışma Sayfasının Birinci Sütunu(larını) dondurma JavaScript aracılığıyla C++ kullanarak
linktitle: Sütunları Sabitle
type: docs
weight: 190
url: /tr/javascript-cpp/how-to-freeze-columns-of-excel-worksheet
description: Programatik olarak Excel Çalışma Sayfalarının sol sütunlarını dondurmayı Aspose.Cells for JavaScript kullanarak C++ ile öğrenin.
keywords: Sol sütunları dondurun, ilk sütunları dondurun, sütunu(sütunları) kilitleyin
---

## **Giriş**  

Bu makalede, sol sütunu(ları) nasıl donduracağımızı öğreneceğiz. Bir satırda büyük miktarda veri olduğunda, yatay kaydırma yaparken sol sütunları göremeyebilirsiniz. Dondurup kilitleyerek kalan veriyi kaydırırken bile dondurulmuş bölümü görebilirsiniz. Sol sütunlarda başlıkları kolayca görebilirsiniz.  

## **Excel'de Sütunları Sabitle**  

**![Excel'de sol sütunları sabitle](freeze-columns.png)**  

1. Sol sütunu(sütunları) dondurmak istiyorsanız, önce dondurulması gereken sütunun altındaki sütunu seçin.
2. Görünüm > Panoları Dondur'a tıklayın.
3. Açılır menüden İlk Sütunu Dondur'a tıklayın.
4. Aşağı kaydırırsanız, ilk sütun her zaman sol görünümde kalır.

**![Dondurulmuş sütun](frozen-columns.png)**  

Görüleceği üzere, 1. sütun dondurulmuş ve yatay kaydırırken ilk sütun her zaman görünüp sabit kalır.

Sütunları Dondurmak, uzun verinizi ilk sütunu takip etme zahmeti olmadan görüntülemenizi sağlar.

## **C++ ile Aspose.Cells for JavaScript kullanarak Sütunları Dondur**  
İlk sütunu(s) basitçe Aspose.Cells for JavaScript kullanarak C++ ile dondurmak kolaydır.  
Seçilen sütunu dondurmak için lütfen [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) metodunu kullanın.  
1. Dosyayı açmak veya boş bir dosya oluşturmak için Workbook'u oluşturun.
2. Worksheet.freezePanes() metodunu kullanarak ilk sütunu dondurun.
3. Dosyayı kaydedin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the second column on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("B1", 0, 1);

            // Saving the file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Ekli [örnek kaynak Excel dosyası](Freeze.xlsx).
