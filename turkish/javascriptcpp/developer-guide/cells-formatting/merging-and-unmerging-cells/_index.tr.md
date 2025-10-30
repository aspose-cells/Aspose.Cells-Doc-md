---
title: Hücreleri Birleştirme ve Çözme ile JavaScript kullanımı
linktitle: Hücreleri Birleştirme ve Ayırma
description: Aspose.Cells, hücreleri birleştirme ve yeniden ayırma desteği sağlayan, hücrelerle çalışma için bir JavaScript kütüphanesidir. Bu makale, Aspose.Cells kütüphanesi kullanarak hücreleri nasıl birleştirip ayıracağınızı ve birleştirilmiş hücre stili özelleştirme seçeneklerini tanıtacaktır.
keywords: Aspose.Cells, JavaScript kütüphanesi, elektronik tablo, hücreleri birleştir, hücreleri ayır, stil ayarları, özel stiller
type: docs
weight: 190
url: /tr/javascript-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells, bu özelliği destekler ve çalışsheet'lerde hücreleri birleştirebilir. Birleştirilmiş hücreleri de ayırabilir veya bölebilirsiniz. Birleştirilmiş bir hücrenin hücre referansı, orijinal seçilen aralıktaki sol üst hücrenin referansıdır.

{{% /alert %}} 
## **Giriş**
Her zaman her satır veya sütunda aynı hücre sayısını istemezsiniz. Örneğin, birkaç sütunu kapsayan bir hücreye başlık koymak isteyebilirsiniz. Veya, bir fatura oluştururken toplam için daha az sütun isteyebilirsiniz. İki veya daha fazla hücreden bir hücre yapmak için hücreleri birleştirin. Microsoft Excel, kullanıcılara dosyaları seçme ve istedikleri şekilde elektronik tabloyu yapılandırmak için birleştirmelerine izin verir.

{{% alert color="primary" %}} 

Hücreler birleştirildiğinde, yalnızca en sol üst hücredeki veri korunur. Aralıkta diğer hücrelerde veri varsa, bu veri silinir. Biçimlendirme de, aralıktaki referans hücreye göre ayarlandığından, hücreleri birleştirdiğinizde, aralıktaki sol üst hücrenin biçimlendirme ayarları birleştirilen hücreye uygulanır. Hücre bölündüğünde, yeni hücreler orijinal biçimlendirme ayarlarını korur.

{{% /alert %}} 
## **Çalışsheet'te Hücreleri Birleştirme**
### **Microsoft Excel'de Hücreleri Birleştirme**
Aşağıdaki adımlar, MS Excel kullanarak çalışsheet'te hücreleri birleştirmeyi açıklar.

1. İstenen veriyi aralıktaki en sol üst hücreye kopyalayın.
2. Birleştirmek istediğiniz hücreleri seçin.
3. Bir satır veya sütunda hücreleri birleştirmek ve hücre içeriğini ortalamak için, **Biçimlendirme** araç çubuğundaki **Birleştir ve Ortala** simgesine tıklayın.

### **Aspose.Cells ile Hücreleri Birleştirmek**
Aspose.Cells.Cells Sınıfı, görev için kullanışlı bazı yöntemler içerir. Örneğin, `merge()` yöntemi, belirli bir aralıkta hücreleri tek bir hücreye birleştirir.

Aşağıdaki örnek, bir çalışsheet'te (C6:E7) hücrelerin nasıl birleştirileceğini göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merging Cells Example</h1>
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
            // Create a Workbook.
            const wbk = new Workbook();

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Saving the Workbook and providing download link
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Hücreleri Ayırma (Birleştirmeyi Bölmek)**
### **Microsoft Excel Kullanımı**
Aşağıdaki adımlar, Microsoft Excel kullanarak birleştirilmiş hücreleri nasıl ayıracağınızı açıklar.

1. Birleştirilmiş hücreyi seçin.
   Hücreler birleştirildiğinde, **Birleştir ve Ortala**, **Biçimlendirme** araç çubuğunda seçilidir.
1. **Biçimlendirme** araç çubuğunda **Birleştir ve Ortala**'ya tıklayın.

### **Aspose.Cells Kullanımı**
Aspose.Cells.Cells sınıfında, hücreleri orijinal durumlarına ayıran `unmerge()` adlı bir yöntem vardır. Bu yöntem, hücreleri birleştirilen hücre aralığında hücrelerin referansını kullanarak ayırır.

Aşağıdaki örnek, birleştirilmiş hücreleri (C6) nasıl ayıracağınızı göstermektedir. Örnek, önceki örnekte oluşturulan dosyayı kullanır ve birleştirilmiş hücreleri ayırır.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Unmerge Cells Example</title>
    </head>
    <body>
        <h1>Unmerge Cells Example</h1>
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

            // Create a Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = workbook.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Unmerge the cells at row 5, column 2 spanning 2 rows and 3 columns
            cells.unMerge(5, 2, 2, 3);

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'unmergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cells unmerged successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Çalışsheet'teki Birleştirilmiş Hücreleri Bulma](/cells/tr/javascript-cpp/detect-merged-cells-in-a-worksheet/)
