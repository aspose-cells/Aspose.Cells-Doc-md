---
title: C++ ile JavaScript kullanarak Excel Çalışma Sayfasının Üst Satır(ları)nı Dondurun
linktitle: Satırları Sabitle
type: docs
weight: 190
url: /tr/javascript-cpp/how-to-freeze-rows-of-excel-worksheet
description: Bu yazıda, JavaScript kütüphanesi ve C++ API kullanarak Excel Çalışma Sayfalarının üst satırlarını programatik olarak nasıl donduracağınızı öğreneceksiniz.
keywords: Üst satırları dondurun, JavaScript ile Üst satırını dondurma C++ kullanarak.
---

## **Giriş**

Bu makalede, üst satır(lar)ı nasıl donduracağımızı öğreneceğiz. Ortak başlık altında büyük miktarda veri olduğunda, aşağı kaydırırken başlıkları göremeyebilirsiniz. Üst satır(ları) dondurup kilitleyerek, kalan veriyi kaydırırken bile o kısmı görebilirsiniz. Üst satırlarda başlıkları kolayca görebilirsiniz.

## **Excel'de Satırları Dondur**

![Excel'de üst satır(ları) dondur](Freeze-Rows.png)

1. Üst satır(lar)ı dondurmak istiyorsanız, önce dondurulması gereken satırın altındaki satırı seçin.
2. Görünüm > Panoları Dondur'a tıklayın.
3. Açılır menüden Üst Satırı Dondur'a tıklayın.
4. Aşağı kaydırırsanız, ilk satır her zaman üst görünümde kalır.

**![Dondurulmuş satır](Frozen-Row.png)**

Görüleceği üzere, 1. satır dondurulmuştur; ilk satır aşağı kaydırırken her zaman görüntüde üstte kalır.

Satırları Dondurun, büyük verinizi satır etiketiyle ilgilenmeden görüntülemenizi sağlar.

## **Aspose.Cells for JavaScript kullanarak Satırları Dondur C++ ile**
C++ ile Aspose.Cells for JavaScript kullanarak satır(ları)nı dondurmak basittir. 
Lütfen seçilen satırda satır(lar)ı dondurmak için [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) metodunu kullanın.
1. Dosyayı açmak veya boş bir dosya oluşturmak için Workbook'u oluşturun.
2. Worksheet.freezePanes() yöntemiyle ilk satırı dondurun.
3. Dosyayı kaydedin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Freeze Panes</title>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the cell B2 on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("A2", 1, 0);

            // Saving the file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
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

Ekli [örnek kaynak Excel dosyası](../Freeze.xlsx).
