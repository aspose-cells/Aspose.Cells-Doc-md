---
title: Excel ve ODS dosyalarının Koşullu Biçimlendirmelerini ayarla
linktitle: Koşullu Biçimler
type: docs
weight: 60
url: /tr/javascript-cpp/conditional-formatting/
description: Excel ve ODS dosyalarına koşullu biçimlendirmeleri JavaScript via C++ kullanarak nasıl uygulayabilirsiniz.
keywords: Koşullu biçimlendirmeleri JavaScript via C++ kullanarak uygulayın
---

## **Giriş**

Koşullu biçimlendirme, bir hücreye veya hücre aralığına biçim uygulamanıza ve bu biçimin hücrenin değeri veya bir formülin değeri ne olursa olsun değişmesine olanak tanıyan gelişmiş bir özelliktir. Örneğin, bir hücre değeri 500'den büyük olduğunda kalın görünmesini sağlayabilirsiniz. Hücrenin değeri koşulu karşıladığında, belirtilen biçim hücreye uygulanır. Hücrenin değeri koşulu karşılamıyorsa, hücrenin varsayılan biçimi kullanılır. Microsoft Excel'de, **Biçim** seçin, ardından **Koşullu Biçimlendirme** diyaloğunu açmak için tıklayın.

Aspose.Cells, hücrelere koşullu biçimlendirme uygulamayı destekler. Bu makale, bu konuyu açıklamaktadır. Ayrıca Excel'in renk ölçeği koşullu biçimlendirme için kullandığı rengi nasıl hesapladığını açıklar.

## **Koşullu Biçimlendirme Uygulama**

Aspose.Cells, koşullu biçimlendirme uygulamayı birkaç şekilde destekler:

- Tasarımcı elek tablosu kullanarak
- Kopya yöntemi kullanarak.
- Çalışma zamanında koşullu biçimlendirme oluşturarak.

### **Tasarımcı Elek Tablosu Kullanma**

Geliştiriciler, Microsoft Excel'de koşullu biçimlendirmeler içeren bir tasarımcı elektronik tablo oluşturabilir ve ardından o elektronik tabloyu Aspose.Cells ile açabilirler. Aspose.Cells, tasarımcı elektronik tabloyu yükler ve kaydeder, herhangi bir koşullu biçimlendirme ayarını korur.

### **Kopyalama Yöntemi Kullanımı**

Aspose.Cells, geliştiricilere bir hücreden diğerine koşullu biçimlendirme ayarlarını çağırarak kopyalama imkanı sunar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get image data from the icon
            const imageData = icon.imageData;

            // Create a blob and provide download link for the image
            const blob = new Blob([imageData], { type: "image/jpeg" });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            resultDiv.innerHTML = '<p style="color: green;">Image extracted successfully! Click the download link to save the image.</p>';
        });
    </script>
</html>
```


## **Çalışma Zamanında Koşullu Biçimlendirme Uygulama**

Aspose.Cells, çalışma zamanında koşullu biçimlendirme eklemeye ve kaldırmaya olanak tanır. Aşağıdaki kod örnekleri, koşullu biçimlendirme ayarlarını nasıl yapacağınızı gösterir:

1. Bir çalışma kitabı örneği oluşturun.
1. Boş bir koşullu biçimlendirme ekleyin.
1. Biçimlendirmenin uygulanması gereken aralığı belirleyin.
1. Biçimlendirme koşullarını tanımlayın.
1. Dosyayı kaydedin.

Bu örneğin ardından, yazı tipi ayarları, kenarlık ayarları ve desen ayarları nasıl uygulanacağını gösteren birçok diğer küçük örnek gelir.

Microsoft Excel 2007, daha gelişmiş koşullu biçimlendirmeyi ekledi ve Aspose.Cells bunu da destekler. Buradaki örnekler, basit biçimlendirmeyi nasıl kullanacağınızı gösterirken, Microsoft Excel 2007 örnekleri daha gelişmiş koşullu biçimlendirme uygulamanın yollarını gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.count;
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            let ca = AsposeCells.CellArea.createCellArea(0, 0, 0, 0);
            fcs.addArea(ca);

            ca = AsposeCells.CellArea.createCellArea(1, 1, 1, 1);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "=A2", "100");

            // Adds condition.
            const conditionIndex2 = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "50", "100");

            // Sets the background color.
            const fc = fcs.get(conditionIndex);
            fc.style.backgroundColor = AsposeCells.Color.Red;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **Yazı Tipi Ayarı**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get the image data from the icon
            const imageData = icon.imageData;

            // Create a Blob and provide a download link for the image
            const blob = new Blob([imageData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            resultDiv.innerHTML = '<p style="color: green;">Image extracted successfully! Click the download link to save the image.</p>';
        });
    </script>
</html>
```



{{% alert color="primary" %}}

Yalnızca yazı tipi stili, metin rengi, altı çizili stili ve üstü çizili stili değiştirebilirsiniz.

{{% /alert %}}

### **Sınır Ayarı**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, FormatConditionType, OperatorType, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, adds conditional formatting and offers the result for download.
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.add();
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            const ca = CellArea.createCellArea(0, 0, 5, 3);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(FormatConditionType.CellValue, OperatorType.Between, "50", "100");

            // Sets the borders' line style to dashed and colors
            const fc = fcs.get(conditionIndex);
            fc.style.borders.get(BorderType.LeftBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.RightBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.TopBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Dashed;

            fc.style.borders.get(BorderType.LeftBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.RightBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.TopBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.BottomBorder).color = new Color(255, 255, 0);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Sadece ince çizgi stili sınır sınırı için kullanılabilir. Köşegen çizgiler izin verilmez.

{{% /alert %}}

### **Desen Ayarı**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Add Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const file = fileInput.files && fileInput.files.length ? fileInput.files[0] : null;

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (file) {
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.add();
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            const ca = AsposeCells.CellArea.createCellArea(0, 0, 5, 3);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "50", "100");
            const fc = fcs.get(conditionIndex);

            // Apply style using property assignments (getter/setter conversion)
            fc.style.pattern = AsposeCells.BackgroundType.ReverseDiagonalStripe;
            fc.style.foregroundColor = new AsposeCells.Color(255, 255, 0);
            fc.style.backgroundColor = new AsposeCells.Color(0, 255, 255);

            // Save workbook to browser downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting added. Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```



## **Gelişmiş Konular**  
- [2-Renkli Ölçek ve 3-Renkli Ölçek Koşullu Biçimlendirmeleri Ekle](/cells/tr/javascript-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [Çalışma Kitaplarında Koşullu Biçimlendirme Uygulamak](/cells/tr/javascript-cpp/apply-conditional-formatting-in-worksheets/)  
- [Koşullu Biçimlendirme ile Sıfır Satır ve Sütunlara Gölgelendirme Uygulamak](/cells/tr/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [Koşullu Biçimlendirme Veri Çubukları Görüntüleri Oluşturmak](/cells/tr/javascript-cpp/generate-conditional-formatting-databars-images/)  
- [Kullanılan Koşullu Biçimlendirme İkon Setleri, Veri Çubukları veya Renk Ölçekleri Nesnelerini Almak](/cells/tr/javascript-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
