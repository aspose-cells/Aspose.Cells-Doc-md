---
title: Microsoft Excel İleri Filtresini Kullanarak Karmaşık Kriterleri Karşılayan Kayıtları Göstermek
type: docs
weight: 280
url: /tr/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Karmaşık kriterleri karşılayan kayıtları göstermek için Microsoft Excel in gelişmiş filtresini nasıl uygulayacağınızı öğrenin, Aspose.Cells for JavaScript ile C++ API kullanarak.
keywords: Üst Düzey Filtre JavaScript’i Uygula C++ ile, Gelişmiş Filtre JavaScript’i ayarla C++ ile, Gelişmiş Filtre JavaScript’i Ekle C++, Gelişmiş Filtre JavaScript’i Oluştur C++, Bir aralığa Gelişmiş Filtre Ekleme JavaScript’i C++ ile
---

## **Olası Kullanım Senaryoları**  

Microsoft Excel, karmaşık kriterleri karşılayan kayıtları göstermek için çalışma sayfası verilerinde *Gelişmiş Filtre* uygulamanıza olanak tanır. Gelişmiş Filtre'yi *Veri > Gelişmiş* komutu ile uygulayabilirsiniz, ekran görüntüsünde gösterildiği gibi.  

![todo:image_alt_text](1.png)  

Aspose.Cells for JavaScript C++ aracılığıyla, [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-) yöntemi kullanılarak Gelişmiş Filtre uygulama imkanı sağlar. Microsoft Excel gibi, aşağıdaki parametreleri kabul eder.  

**isFilter**  

Listeyi yerinde filtrelemenin belirtilip belirtilmediğini gösterir.  

**listRange**  

Liste aralığı.  

**criteriaRange**  

Kriter aralığı.  

**copyTo**  

Verilerin kopyalanacağı aralık.  

**uniqueRecordOnly**  

Yalnızca benzersiz satırların gösterimi veya kopyalanması.  

## **Karmaşık Kriterleri Karşılayan Kayıtları Göstermek İçin Microsoft Excel'in İleri Filtresini Uygulayın**  

Aşağıdaki örnek kod, [Örnek Excel Dosyası](48496692.xlsx) üzerinde gelişmiş filtreyi uygular ve [Çıktı Excel Dosyası](48496691.xlsx) oluşturur. Ekran görüntüsü her iki dosyayı karşılaştırmak için gösterir. Ekran görüntüsü içindekileri incelediğinizde, verilerin karmaşık kriterlere göre çıktı Excel dosyası içinde filtrelendiğini görebilirsiniz.  

![todo:image_alt_text](2.png)  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Advanced Filter Example</title>
    </head>
    <body>
        <h1>Advanced Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Advanced Filter</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (sampleAdvancedFilter.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const wb = new Workbook(new Uint8Array(arrayBuffer));

            const ws = wb.worksheets.get(0);

            // Apply advanced filter on range A5:D19 with criteria A1:D2, filter in place, include all records (not unique)
            ws.advanced_Filter(true, "A5:D19", "A1:D2", "", false);

            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAdvancedFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Advanced filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
