---
title: Boş veya Boş olmayanları Filtreleme
type: docs
weight: 85
url: /tr/javascript-cpp/how-to-filter-blanks-and-non-blanks/
description: Boş Hücreleri ve Boş Olmayan Hücreleri filtreleme hakkında bilgi edinin, Aspose.Cells for JavaScript via C++ API kullanarak.
keywords: Boşları Filtrele, Boş Olmayanları Filtrele, Çalışma sayfasında Boşları Filtrele, Çalışma sayfasında Boş Olmayanları Filtrele, Excel de Boşları Filtrele, Excel de Boş Olmayanları Filtrele, Excel de Boşları ve Boş Olmayanları Filtreleme
---

## **Olası Kullanım Senaryoları**
Excel'de veri filtreleme, kullanıcıların kriterlerine dayalı olarak belirli veri alt kümelerine odaklanmalarını sağlayarak veri analizini, keşfini ve sunumunu geliştiren değerli bir araçtır, bu da genel veri işleme ve yorum sürecini daha verimli ve etkili hale getirir.

## **Excel'de Boş veya Boş Olmayanları Filtreleme**
Excel'de, filtreleme seçeneklerini kullanarak kolayca boş veya boş olmayanları filtreleyebilirsiniz. Bunu nasıl yapabileceğinizi aşağıda bulabilirsiniz:

### **Excel'de Boşları Filtreleme**
1. Aralığı Seçin: Tüm sütunu seçmek için sütun başlığının harfine tıklayın veya boşları filtrelemek istediğiniz aralığı seçin.
1. Filtre Menüsünü Açın: Kurdeledeki "Veri" sekmesine gidin.
<br>
<image src="1.png" width="70%" />
1. Filtre Seçenekleri: "Filtre" düğmesine tıklayın. Bu, seçilen aralığa filtre oklarını ekleyecektir.
1. Boşları Filtrele: Boşları filtrelemek istediğiniz sütundaki filtre okuna tıklayın. "Boşlar" hariç tüm seçenekleri seçmeyin ve Tamam'a tıklayın. Bu, o sütundaki yalnızca boş hücreleri gösterecektir.
<br>
<image src="2.png" width="70%" />
1. Sonuç aşağıdaki gibidir:
<br>
<image src="3.png" width="70%" />

### **Excel'de Boş Olmayanları Filtreleme**
1. Aralığı Seçin: Tüm sütunu seçmek için sütun başlığının harfine tıklayın veya boş olmayanları filtrelemek istediğiniz aralığı seçin.
1. Filtre Menüsünü Açın: Kurdeledeki "Veri" sekmesine gidin.
<br>
<image src="1.png" width="70%" />
1. Filtre Seçenekleri: "Filtre" düğmesine tıklayın. Bu, seçilen aralığa filtre oklarını ekleyecektir.
1. Boş Olmayanları Filtrele: Boş olmayanları filtrelemek istediğiniz sütundaki filtre okuna tıklayın. "Boş olmayanlar" veya "Özel" dışındaki tüm seçenekleri kaldırın ve koşulları ayarlayın. Tamam'a tıklayın. Bu, o sütundaki yalnızca boş olmayan hücreleri gösterecektir.
<br>
<image src="4.png" width="70%" />
1. Sonuç aşağıdaki gibidir:
<br>
<image src="5.png" width="70%" />

## **Boş Hücreleri Aspose.Cells for JavaScript aracılığıyla C++ kullanarak nasıl filtrelerim**
Bir sütunda çok az hücre boş ise ve sadece boş hücrelerin olduğu satırları seçmek gerekiyorsa, [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchBlanks-number-) ve [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#addFilter-number-string-) fonksiyonları aşağıda gösterildiği gibi kullanılabilir. 

Lütfen aşağıdaki örnek kodu inceleyin, bu örnek Excel dosyasından (örnek.xlsx) bazı sahte veriler içeren dosyayı yükler. Örnek kod, boşları filtrelemek için üç yöntem kullanır. Daha sonra çalışma kitabını [çıktı Excel dosyası](FiltrelenmişBoşlar.xlsx) olarak kaydeder. 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Filter for Blank Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.autoFilter.addFilter(1, null);
            worksheet.autoFilter.refresh();

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download FilteredBlanks.xlsx';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied and file ready for download.</p>';
        });
    </script>
</html>
```


## **Boş Olmayan Hücreleri Aspose.Cells for JavaScript aracılığıyla C++ kullanarak nasıl filtrelerim**

Aşağıdaki örnek kodu inceleyin; bu kod, bazı sahte verilerin bulunduğu örnek Excel dosyasını yükler, yükledikten sonra boş olmayan verileri filtrelemek için [AutoFilter.matchNonBlanks(number)] fonksiyonunu çağırır ve sonunda çalışma kitabını [Çıktı Excel Dosyası](FilteredNonBlanks.xlsx) olarak kaydeder. 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter NonBlanks Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchNonBlanks function to apply the filter
            worksheet.autoFilter.matchNonBlanks(1);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNonBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
