---
title: İconları Çalışma Sayfasına Ekleme JavaScript ve C++ ile
linktitle: Simgeleri Yönetme
type: docs
weight: 100
url: /tr/javascript-cpp/insert-svg-to-excel/
---

## Aspose.Cells for JavaScript kullanarak Çalışma Sayfasına İkonlar Ekleme in C++

Eğer bir Excel dosyasına 'simgeler' eklemek için [Aspose.Cells](https://products.aspose.com/cells/) kullanmanız gerekiyorsa, bu belge size bazı yardımlar sağlayabilir.

Ekle simgesine karşılık gelen Excel arayüzü aşağıdaki gibidir:

![](1.png)

- Çalışma sayfasına eklemek istediğiniz simgenin konumunu seçin
- *Ekle*->*Simgeler*ü tıklayın
- Açılan pencerede, yukarıdaki resimde kırmızı dikdörtgen içindeki simgeyi seçin
- Sol tıklama *Ekle* seçimine tıklayın, Excel dosyasına eklenecektir.

Efekt aşağıdaki gibidir:

![](2.png)

Burada, simgeleri [Aspose.Cells](https://products.aspose.com/cells/) kullanarak eklemenize yardımcı olacak *örnek kod* hazırlandı. Ayrıca gerekli [örnek dosya](sample.xlsx) ve bir ikon [kaynak dosyası](icon.zip) bulunmaktadır. Aynı görüntü efektini vermek için Excel arayüzünü kullanarak, [kaynak dosyası](icon.zip) içinden bir ikon ekledik ve [örnek dosya](sample.xlsx).

### JavaScript

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Icon to Worksheet Example</h1>
        <p>Select an Excel file and an SVG icon file, then click "Run Example".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="iconInput" accept=".svg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            const iconInput = document.getElementById('iconInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!iconInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an SVG icon file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const iconFile = iconInput.files[0];

            const arrayBuffer = await file.arrayBuffer();
            const iconArrayBuffer = await iconFile.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the icon to the worksheet
            const iconBytes = new Uint8Array(iconArrayBuffer);
            sheet.shapes.addIcons(3, 0, 7, 0, 100, 100, iconBytes, null);

            // Set a prompt message
            const c = sheet.cells.get(8, 7);
            c.value = "Insert via Aspose.Cells";
            const s = c.style;
            s.font.color = Color.Blue;
            c.style = s;

            // Save and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Icon added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Yukarıdaki kodu projenizde çalıştırdığınızda aşağıdaki sonuçları elde edersiniz:

![](3.png)
