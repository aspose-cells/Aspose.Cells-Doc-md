---
title: Büyük Veri Setlerine Sahip Büyük Dosyalarla Çalışırken Bellek Kullanımını Optimize Etme
type: docs
weight: 110
url: /tr/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Büyük veri setleriyle çalışırken veya büyük bir Microsoft Excel dosyasını okurken, işlemin alacağı toplam RAM miktarı her zaman endişe kaynağıdır. Mücadele etmek için adapte edilebilecek önlemler bulunmaktadır. Aspose.Cells, bellek kullanımını azaltmak, düşürmek ve optimize etmek için bazı ilgili seçenekler ve API çağrıları sağlar. Ayrıca, işlemin daha verimli çalışmasına ve daha hızlı çalışmasına yardımcı olabilir.

Hücre verileri için kullanılan belleği azaltmak için [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) seçeneğini kullanın. Büyük veri kümesi oluştururken, varsayılan ayar kullanmaktan daha fazla bellek tasarrufu sağlayabilir.

{{% /alert %}}

## **Bellek Kullanımını Optimize Etme**

 Aşağıdaki örnek, Aspose.Cells for JavaScript ile C++ kullanarak büyük veriyle çalışırken bellek kullanımını nasıl optimize edeceğinizi gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Optimize Memory Usage Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MemorySetting } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file or leave empty to create a new one.</p>';
                // Allow creating a new workbook even if no file selected; return only if user explicitly requires file.
            }

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // apply the setting to existing "Sheet1"
            workbook.worksheets.get(0).cells.memorySetting = MemorySetting.MemoryPreference;

            // apply the setting globally
            workbook.settings.memorySetting = MemorySetting.MemoryPreference;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Memory settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Dikkat**

Varsayılan seçenek, [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) tüm sürümler için uygulanır. Bir çalışma kitabı büyük bir veri kümesi için hücreler için bir çalışma kitabı oluşturma gibi bazı durumlarda, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) seçeneği bellek kullanımını optimize edebilir ve uygulama için bellek maliyetini azaltabilir. Ancak bu seçenek özellikle iz sürmedeki bazı özel durumlarda performansı düşürebilir.

1. **Rastgele ve Tekrarlanan Şekilde Hücrelere Erişme**: Hücre koleksiyonuna erişmek için en verimli sıralama, önce bir satırda hücre hücre, ardından satır satır erişmektir. Özellikle, [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection) ve [**Row**](https://reference.aspose.com/cells/javascript-cpp/row)'den elde edilen Numaralayıcı ile satırlara/hücrelere erişiyorsanız, performans [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) ile maksimize edilecektir.
1. **Hücreleri ve Satırları Ekleme & Silme**: Eğer Hücreler/Satırlar için birçok ekleme/silme işlemi varsa, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) modu için performans düşüşü, [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) modu ile karşılaştırıldığında belirgin olacaktır.
1. **Farklı Hücre Türlerinde İşlemler**: Eğer hücrelerin çoğu dize değerleri veya formüller içeriyorsa, bellek maliyeti [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) modu ile aynı olacaktır ancak boş hücrelerin çok olduğu veya hücre değerlerinin sayısal, bool vb. olduğu durumlarda, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) seçeneği daha iyi performans verecektir.
