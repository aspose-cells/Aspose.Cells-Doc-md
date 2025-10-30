---
title: Büyük Veri Kümeleri ile Çalışırken Bellek Kullanımını Optimize Etmek JavaScript ile C++ kullanarak
linktitle: Büyük Veri Setlerine Sahip Büyük Dosyalarla Çalışırken Bellek Kullanımını Optimize Etme
type: docs
weight: 180
url: /tr/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

 Büyük veri setleri ile bir çalışma kitabı oluştururken veya büyük bir Microsoft Excel dosyasını okurken, işlemin kullanacağı toplam RAM genellikle önemlidir. Bu zorlukla başa çıkmak için uyarlanabilecek önlemler vardır. Aspose.Cells for JavaScript ile C++ bazı ilgili seçenekler ve API çağrıları sağlar, bellek kullanımını azaltmak, düşürmek ve optimize etmek için. Ayrıca, işlemin daha verimli çalışmasına ve daha hızlı çalışmasına yardımcı olabilir.

Hücre verisi için bellek kullanımını optimize etmek ve genel bellek maliyetini azaltmak için [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) seçeneğini kullanın. Büyük veri setleri için hücreler oluştururken, varsayılan ayar ([**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)) kullanmaktan belirli bir miktarda bellek tasarrufu sağlayabilir.

{{% /alert %}}

## **Bellek Kullanımını Optimize Etme**

### **Büyük Excel Dosyaları Okuma**

Aşağıdaki örnek, optimize edilmiş modda büyük bir Microsoft Excel dosyasını nasıl okuyacağınızı göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - LoadOptions MemorySetting</title>
    </head>
    <body>
        <h1>LoadOptions MemorySetting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, MemorySetting, SaveFormat, Utils } = AsposeCells;

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

            // Specify the LoadOptions
            const opt = new LoadOptions();
            // Set the memory preferences (converted from setMemorySetting)
            opt.memorySetting = MemorySetting.MemoryPreference;

            // Instantiate the Workbook - load the big Excel file with options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opt);

            // Save the workbook to XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook loaded with MemoryPreference. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Büyük Excel Dosyaları Yazma**

Aşağıdaki örnek, optimize edilmiş bir modda bir çalışma sayfasına büyük bir veri seti yazmanın nasıl yapılacağını gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Memory Setting Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Memory Setting Example</h1>
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
                // If no file is selected, create a new workbook (similar to new AsposeCells.Workbook() in Node)
                // and proceed to set memory settings and populate sheets.
            }

            // Load workbook from file if provided, otherwise create empty workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Set the memory preferences on the workbook settings
            workbook.settings.memorySetting = AsposeCells.MemorySetting.MemoryPreference;

            // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook
            // To change the memory setting of existing sheets, change memory setting for them manually:
            let cells = workbook.worksheets.get(0).cells;
            cells.memorySetting = AsposeCells.MemorySetting.MemoryPreference;

            // Input large dataset into the cells of the worksheet.
            // Your code goes here.
            // Example: populate a few cells to demonstrate
            const firstCell = cells.get(0, 0);
            firstCell.value = "Sample Data 1";
            cells.get(1, 0).value = "Sample Data 2";

            // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
            const sheet2 = workbook.worksheets.add("Sheet2");
            const cells2 = sheet2.cells;
            // .........
            // Input large dataset into the cells of the worksheet.
            // Your code goes here.
            // Example: populate a few cells in Sheet2
            cells2.get(0, 0).value = "Sheet2 Data 1";
            cells2.get(1, 0).value = "Sheet2 Data 2";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Dikkat**

Varsayılan seçenek, [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) tüm sürümler için uygulanır. Bazı durumlarda, özellikle hücreler için büyük veri setleri ile çalışma kitabı oluşturulurken, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) seçeneği bellek kullanımını optimize edebilir ve uygulamanın bellek maliyetini azaltabilir. Ancak, bu seçenek bazı özel durumlarda performansı azaltabilir, örneğin aşağıdaki gibi.

1. **Hücrelere Rastgele ve Tekrarlı Erişim**: Hücre koleksiyonuna en etkili erişim sırası, satır satır hücreye erişmek ve sonra satır satır ilerlemektir. Özellikle, eğer satır/ Hücreleri [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells), [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection) ve [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) tarafından edinilen Yorumlayıcı ile erişirseniz, performans [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) ile maksimize edilir.
2. **Hücreler ve Satırların Eklenmesi ve Silinmesi**: Lütfen dikkat edin ki, hücreler/satırlar üzerinde çok sayıda ekleme/silme işlemi varsa, performans düşüşü *MemoryPreference* modunda, *Normal* moduna göre belirgin olacaktır.
3. **Farklı Hücre Tipleri Üzerinde İşlem Yapma**: Çoğu hücre string değeri veya formül içeriyorsa, bellek maliyeti *Normal* mod ile aynıdır, ancak birçok boş hücre veya hücre değeri sayısal, bool gibi ise, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) seçeneği daha iyi performans sağlayacaktır.
