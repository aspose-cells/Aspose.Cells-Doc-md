---
title: Özet Tablosunda Pivot Alanlarını Gruplandırma
linktitle: Özet Tablosunda Pivot Alanlarını Gruplandırma
description: Aspose.Cells for JavaScript via C++ kullanarak PivotField.group ve PivotFieldGroupOptions ile bir özet tablosundaki satır ve sütun pivot alanlarının aylar ve çeyreklere gibi tarih dönemlerine ve sayısal aralıklara nasıl gruplandırılacağını öğrenin.
keywords: Aspose.Cells, özet tablo, pivot alanını gruplandırma, PivotField.group, PivotFieldGroupOptions, tarih gruplandırma, sayısal gruplandırma, aylar, çeyrekler, sayısal aralık, JavaScript via C++
type: docs
weight: 80
url: /tr/javascript-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Pivot alanlarını gruplandırma, bir özet tablosunun satır veya sütun alanı çok sayıda farklı öğe içerdiğinde yararlıdır; örneğin yüzlerce tarih içeren bir tarih alanı veya çok sayıda dağınık değer içeren bir sayısal alan gibi. Gruplandırma, bu öğeleri anlamlı bölümlere dönüştürür: tarihleri aylara, çeyreklere ve yıllara; sayıları ise 0-1, 2-3 ve 4-5 gibi aralıklara. Böylece büyük özet tabloları daha kompakt olur ve analiz edilmesi kolaylaşır. Aspose.Cells bu özelliği `PivotField.group()` yöntemi (veri türüne göre otomatik gruplandırma) ve `PivotField.group(PivotFieldGroupOptions)` yöntemi (özel gruplandırma seçenekleri) aracılığıyla sunar.
- Tarih gruplandırma, bireysel tarihleri günler, aylar, çeyrekler ve yıllar gibi daha geniş dönemler hâlinde özetler ve bir zaman hiyerarşisi oluşturur (örneğin Yıllar, Çeyrekler, Aylar). Zaman içindeki eğilimler bir bakışta görünür ve her dönem düzeyi, özet tablosunun satır veya sütun bölgesinde ayrı bir pivot alanı hâline gelir.
- Gruplandırma yalnızca özet tablosunun SATIR veya SÜTUN bölgesine yerleştirilmiş alanlar için kullanılabilir. Bir veri (değer) alanı doğrudan gruplandırılamaz. Böyle bir alanı gruplandırmak için önce onu özet tablosunun satır veya sütun bölgesine eklemeniz gerekir.

## **Pivot Alanlarını Otomatik Olarak Gruplandırma**
Parametresiz `PivotField.group()` aşırı yüklemesi, alanın veri türünü inceler ve alanı otomatik olarak gruplandırır. Yalnızca tarihleri ve boş değerleri içeren bir alan aylara göre gruplandırılır. Yalnızca sayısal değerleri ve boş değerleri içeren bir alan ise otomatik bir aralık kullanılarak sayısal aralıklara gruplandırılır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Automatically</title>
    </head>
    <body>
        <h1>Auto-Group a Pivot Field</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the second worksheet and its pivot table
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the first row field automatically by its data type
                pt.rowFields.get(0).group();
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputAutoGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Özel Seçeneklerle Pivot Alanlarını Gruplandırma**
`PivotFieldGroupOptions` sınıfı özel gruplandırma yapılandırması sağlar. Tarih alanları için `startDate`, `endDate` ve `groupTypes` değerlerini ayarlayın. Sayısal alanlar için `startNumber`, `endNumber` ve `interval` değerlerini ayarlayın. `newPivotField` özelliği, gruplandırmanın özgün alanın yanında yeni pivot alanları oluşturup oluşturmadığını denetler (bu makalenin sonundaki Not bölümüne bakın).

### **Bir Tarih Alanını Aylara ve Çeyreklere Göre Gruplandırma**
Bu örnek, örnek özet tablosunun tarih satır alanını, belirtilen başlangıç ve bitiş tarihleri arasında aylara ve çeyreklere göre gruplandırır. Kod, [örnek Excel dosyasını](sampleGroupPivotFieldsInPivotTable.xlsx) yükler, gruplandırmayı gerçekleştirir, özet tablo verilerini hesaplar ve gruplandırılmış sonucu kaydeder. Ekran görüntüsü sonucu gösterir: tarih satır alanı artık çeyreklere ve aylara göre gruplandırılmıştır.

`options.groupTypes` içindeki değerlerin sırası dikkate alınmaz. Grup türleri hangi sırayla listelenirse listelensin, gruplandırılmış alanlar her zaman en büyük dönemden en küçüğe doğru gösterilir: yıllar, çeyrekler, aylar, günler, saatler, dakikalar, saniyeler. Bu örnekte aylar `options.groupTypes` içinde çeyreklerden önce listelenir; ancak çeyrekler dış düzey, aylar ise iç düzey olarak gösterilir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Date Field by Months and Quarters</title>
    </head>
    <body>
        <h1>Group a Date Pivot Field</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the date row field by months and quarters between the given dates
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startDate = new Date(2008, 1, 1);
                options.endDate = new Date(2008, 9, 5);
                options.groupTypes = [AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters];
                pt.rowFields.get(0).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputGroupPivotFieldsInPivotTable.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

![Aylar ve çeyreklere göre gruplandırılmış özet tablo](group-pivot-fields-in-the-pivot-table_1.png)

### **Sayısal Alanı Aralıklara Gruplandırma**
Örnek özet tablosunun `FieldTwo` alanı başlangıçta bir veri (değer) alanıdır. Yalnızca satır veya sütun alanları gruplandırılabildiğinden kod, önce `FieldTwo` alanını satır alanına taşımak için `PivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` çağırır. Ardından özet tabloyu yeniler ve sayısal alanı `startNumber = 0`, `endNumber = 5` ve `interval = 2` kullanarak 0-1, 2-3 ve 4-5 aralıklarına gruplandırır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Numeric Field into Ranges</title>
    </head>
    <body>
        <h1>Group a Numeric Pivot Field</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // FieldTwo is a data field: move it to the row area first,
                // because only row/column fields can be grouped
                pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
                pt.calculateData();
                // Group the numeric field into the ranges 0-1, 2-3, 4-5
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startNumber = 0;
                options.endNumber = 5;
                options.interval = 2;
                pt.rowFields.get(1).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputNumberGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Not**

{{% alert color="primary" %}}
- `PivotField.groupBy()` yöntemi aşırı yüklemeleri kullanımdan kaldırılmış ve API yüzeyinden çıkarılmıştır. Bunların yerine `PivotField.group()` ve `PivotField.group(PivotFieldGroupOptions)` kullanılır.
- Microsoft Excel'de sayısal bir alanı gruplandırmak, özgün pivot alanını gruplandırılmış aralıklarla DEĞİŞTİRİR; buna karşılık, bir tarih alanını gruplandırmak, özgün alanın yanında her grup düzeyi için bir tane YENİ PİVOT ALANI (örneğin Çeyrekler ve Aylar) OLUŞTURUR. Aspose.Cells 26.10 sürümünden başlayarak `PivotField.group()` yöntemleri Excel ile aynı davranışı izler. `PivotFieldGroupOptions.newPivotField` özelliği, önceki sürümlerle uyumluluk için mevcuttur: varsayılan değeri sayısal gruplandırmada false, tarih-saat gruplandırmasında true değeridir. Tarih gruplandırmasının özgün pivot alanını değiştirmesini ve yeni pivot alanları oluşturmamasını istiyorsanız bu değeri false olarak ayarlayın.
- `PivotFieldGroupOptions.interval` özelliği yalnızca sayısal gruplandırmada ve tarihlerin günlere göre gruplandırılmasında (örneğin tarihlerin 7 günlük dönemler hâlinde gruplandırılması) etkili olur; tarihler aylara, çeyreklere veya yıllara göre gruplandırıldığında dikkate alınmaz.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablosuna Satır ve Sütun Alanları Ekle](/cells/tr/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Özet Tablolarını Etikete veya Değere Göre Filtrele](/cells/tr/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Özet Tablosuna Sayfa Alanı Ekle](/cells/tr/javascript-cpp/add-page-field-in-pivot-table/)
- [Özet Tablosuna Biçim Uygula](/cells/tr/javascript-cpp/apply-style-to-pivot-table/)
- [Özet Tablosunu Yenile](/cells/tr/javascript-cpp/refresh-pivot-table/)
- [Özet Alanı Öğelerinin Ayrık Gruplandırılması](/cells/tr/javascript-cpp/discrete-group-pivot-fields/)

{{< app/cells/assistant language="javascript-cpp" >}}