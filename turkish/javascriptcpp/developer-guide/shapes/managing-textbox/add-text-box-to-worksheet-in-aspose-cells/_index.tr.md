---
title: JavaScript kullanarak Çalışma Sayfasına Metin Kutusu Ekleme/İçine Yazma C++ ile
linktitle: Çalışma Sayfasına Metin Kutusu Ekle
type: docs
weight: 10
url: /tr/javascript-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: C++ kullanarak Aspose.Cells for JavaScript ile Çalışma Sayfasına Metin Kutusu nasıl eklenir/yapıştırılır.
keywords: C++ ile Aspose JavaScript kullanarak Çalışma Sayfasına Metin Kutusu Ekleme/Güncelleme
---

## Excel'de Çalışma Sayfasına Metin Kutusu Ekle

Excel programında (sürüm 07 ve üzeri), metin kutusu ekebileceğiniz iki yer vardır. Biri 'insert-shapes' içinde, diğeri ise 'Insert' seçeneğinin sağ üst menüsündedir.

### yöntem biri:

![1](1.png)

### yöntem iki:

![2](2.png)

## Nasıl oluşturulur

Metin Kutusu, yatay veya dikey metinle oluşturulabilir.

- Karşılık gelen seçeneği seçin (yatay veya dikey)
- Sayfada sol tuşa basın.
- Sol tuşa basılı tutun ve sayfada bir mesafe sürükleyin.
- Sol tuşu bırakın.

Şimdi bir metin kutusuna sahipsiniz.

## C++ kullanarak Çalışma Sayfasına Metin Kutusu Ekleme Aspose.Cells for JavaScript ile

İş sayfasına toplu olarak TextBox eklemeniz gerektiğinde, manuel ekleme yöntemi açıkça bir felakettir. Eğer bu sizi rahatsız ediyorsa, bu belgenin size yardımcı olacağını düşünüyorum. [Aspose.Cells](https://products.aspose.com/cells/) size kodunuzda toplu eklemeleri kolayca yapmanızı sağlayan bir API sunar.

Aşağıdaki örnek kod bir metin kutusu oluşturur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add TextBox</title>
    </head>
    <body>
        <h1>Add TextBox to Workbook</h1>
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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the TextBox to the worksheet
            sheet.textBoxes.add(6, 10, 100, 200);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TextBox added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Benzer bir dosya alacaksınız [sonuç dosyası](result.xlsx). Dosyada aşağıdakileri göreceksiniz:

![](52449.png)
