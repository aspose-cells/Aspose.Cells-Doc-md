---
title: JavaScript ve C++ ile Gelişmiş Koruma Ayarları Excel XP’den itibaren
linktitle: Excel XP den beri Gelişmiş Koruma Ayarları
type: docs
weight: 30
url: /tr/javascript-cpp/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

2002 veya XP sürümüyle birlikte, Microsoft birçok gelişmiş koruma ayarı eklemiştir.

{{% /alert %}}


## **Giriş**

Bu koruma ayarları, kullanıcıların aşağıdakileri kısıtlamasına veya izin vermesini sağlar:

- Satırları veya sütunları sil.
- İçeriği, nesneleri veya senaryoları düzenle.
- Hücreleri, satırları veya sütunları biçimlendir.
- Satırları, sütunları veya köprüleri ekle.
- Kilitli veya kilitsiz hücreleri seç.
- Özet tabloları ve çok daha fazlasını kullanın.

Aspose.Cells for JavaScript kullanılarak C++ ile Excel XP veya daha sonraki sürümler tarafından sunulan tüm gelişmiş koruma ayarları desteklenmektedir.

### **Excel XP'de bulunan koruma ayarlarını görüntülemek için:**

**Araçlar** menüsünden **Koruma** ardından **Sayfayı Koru**'yu seçin.

1. **Araçlar** menüsünden **Koruma** ve ardından **Çalışma Sayfası Koru** seçin. Bir iletişim kutusu görüntülenecektir.

Excel 2016'daki koruma ayarlarını görüntülemek için:

1. **Dosya** menüsünden **Çalışma Kitabını Koru** ve ardından **Mevcut Sayfayı Koru** seçin.
1. **İncele** menüsünde **Çalışma Sayfası Koru** seçin.

Yukarıdaki adımları takip etmek, çalışma sayfasında özellikleri izin verme veya kısıtlama ya da parola uygulama diyaloğunu gösterecektir.

### **Gelişmiş Koruma Ayarları Aspose.Cells for JavaScript kullanılarak C++ ile**

Aspose.Cells for JavaScript kullanılarak C++ ile tüm gelişmiş koruma ayarları desteklenmektedir.

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim izni veren bir [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı tarafından temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, bu gelişmiş koruma ayarlarını uygulamak için kullanılan [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) özelliğini sağlar. Aslında, [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) özelliği, engelleme veya kısıtlamaları etkinleştirmek veya devre dışı bırakmak için birkaç Boolean özelliği kapsayan [**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection) sınıfından bir nesnedir.

Aşağıda küçük bir örnek uygulama bulunmaktadır. Bir Excel dosyası açar ve Excel XP ve sonraki sürümler tarafından desteklenen gelişmiş koruma ayarlarının çoğunu kullanır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Worksheet Protection Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const protection = worksheet.protection;

            // Restricting users to delete columns of the worksheet
            protection.allowDeletingColumn = false;

            // Restricting users to delete row of the worksheet
            protection.allowDeletingRow = false;

            // Restricting users to edit contents of the worksheet
            protection.allowEditingContent = false;

            // Restricting users to edit objects of the worksheet
            protection.allowEditingObject = false;

            // Restricting users to edit scenarios of the worksheet
            protection.allowEditingScenario = false;

            // Restricting users to filter
            protection.allowFiltering = false;

            // Allowing users to format cells of the worksheet
            protection.allowFormattingCell = true;

            // Allowing users to format rows of the worksheet
            protection.allowFormattingRow = true;

            // Allowing users to insert columns in the worksheet
            protection.allowFormattingColumn = true;

            // Allowing users to insert hyperlinks in the worksheet
            protection.allowInsertingHyperlink = true;

            // Allowing users to insert rows in the worksheet
            protection.allowInsertingRow = true;

            // Allowing users to select locked cells of the worksheet
            protection.allowSelectingLockedCell = true;

            // Allowing users to select unlocked cells of the worksheet
            protection.allowSelectingUnlockedCell = true;

            // Allowing users to sort
            protection.allowSorting = true;

            // Allowing users to use pivot tables in the worksheet
            protection.allowUsingPivotTable = true;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protection settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Lütfen [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) özelliğini kullanırken [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) metodunu çağırmayın. Ayrıca, dosyayı Excel97'den 2003'e veya Xlsx formatında kaydedin çünkü gelişmiş koruma ayarları yalnızca Excel XP ve daha yeni sürümler tarafından desteklenir.

{{% /alert %}}

### **Hücre Kilitleme Sorunu**

Kullanıcıların hücreleri düzenlemesini engellemek istiyorsanız, hücreler herhangi bir koruma ayarı uygulanmadan önce kilitlenmiş olmalıdır. Aksi takdirde, çalışma sayfası korunsa bile hücreler düzenlenebilir. Microsoft Excel XP'de hücreler aşağıdaki iletişim kutusu aracılığıyla kilitlenebilir:

|**Excel XP'de Hücreleri Kilitlme İletişim Kutusu**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Aspose.Cells API kullanarak da hücreler kilitlenebilir. Her hücre, [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) biçimlendirmeyi alan ve bir Boolean özellik [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) içeren [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) özelliğine sahip olabilir. Hücreyi kilitlemek veya kilidini açmak için [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) özelliğini **doğru** veya **yanlış** olarak ayarlayın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Lock cell A1 by setting the style property
            const cell = worksheet.cells.get("A1");
            cell.style.isLocked = true;

            // Protect the sheet now.
            worksheet.protect(ProtectionType.All);

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
