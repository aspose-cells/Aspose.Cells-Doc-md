---
title: JavaScript ile C++ kullanarak Çalışma Sayfası Görünümleri
linktitle: Sayfa Görünümleri
type: docs
weight: 40
url: /tr/javascript-cpp/worksheet-views/
description: Bu makale, JavaScript ve JavaScript API sini kullanarak Excel çalışma kitabı ve çalışma sayfalarının sayfa kırma önizlemesiyle nasıl etkileşim kurulacağını anlatacaktır. Bölünmüş panolar, dondurulmuş panolar ve yakınlaştırma faktörü ile çalışın.
---

## **Sayfa Kesme Önizleme**

Tüm çalışma sayfaları iki modda görüntülenebilir:

- Normal görünüm.
- Sayfa kesme önizlemesi.

Normal görünüm, bir çalışma sayfasının varsayılan görünümüdür. Sayfa kırma önizlemesi, bir çalışma sayfasını yazdırılacak gibi gösteren düzenleme görünümüdür. Sayfa kırma önizlemesi, her sayfada hangi verilerin olacağını gösterir böylece yazdırma alanını ve sayfa kırıklarını ayarlayabilirsiniz. C++ aracılığıyla Aspose.Cells for JavaScript kullanılarak, geliştiriciler normal veya sayfa kırma önizleme modlarını etkinleştirebilir.

### **Görünüm Modlarını Kontrol Etme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı sunar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Normal veya sayfa görünümü önizlemesi modlarını etkinleştirmek için [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) özelliğini kullanın. [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--), yalnızca bir **true** ya da **false** değerini depolayabilen bir Boolean özelliğidir.

#### **Normal Görünümü Etkinleştirme**

Normal görünüm için çalışma sayfasını, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) özelliğini **false** olarak ayarlayarak belirleyin.

#### **Sayfa Kesme Önizlemesini Etkinleştirme**

Herhangi bir çalışma sayfasını sayfa görünümü önizlemesi için [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) özelliğini **true** olarak ayarlayarak belirleyin. Bunu yapmak, çalışma sayfasını normal görünümden sayfa görünümü önizlemesine geçirir.

Aşağıda, bir Excel dosyasının ilk çalışma sayfası için sayfa görünümü önizleme modunu etkinleştirmek için [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) özelliğini nasıl kullanacağını gösteren tam bir örnek verilmiştir.

book1.xls dosyası, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının bir örneği oluşturularak açılır. İlk çalışma sayfası için görünüm, [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) özelliğinin **true** olarak ayarlanmasıyla sayfa görünümü önizlemesi olarak değiştirilir. Değiştirilmiş dosya, çıktı.xls olarak kaydedilir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Break Preview</title>
    </head>
    <body>
        <h1>Page Break Preview Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Displaying the worksheet in page break preview
            worksheet.isPageBreakPreview = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Yakınlaştırma Faktörü**

### **Microsoft Excel Kullanımı**

Microsoft Excel, kullanıcılara bir çalışma tablosunun yakınlaştırma veya ölçekleme faktörünü ayarlamalarına izin veren bir özellik sağlar. Bu özellik, kullanıcıların çalışma tablosu içeriğini daha küçük veya daha büyük görüntülemelerine yardımcı olur. Kullanıcılar yakınlaştırma faktörünü herhangi bir değere ayarlayabilirler.

### **Aspose.Cells ve Yakınlaştırma Faktörü**

Aspose.Cells, geliştiricilere çalışma sayfası yakınlaştırma faktörünü ayarlama olanağı tanır.
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıfı içeren bir özelliktir. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir çalışma sayfasının yakınlaştırma faktörünü ayarlamak için, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) özelliğini kullanın. Yakınlaştırma faktörü, [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) özelliğine sayısal (tamsayı) bir değer atayarak ayarlanır.

Aşağıda, Excel dosyasının ilk çalışma sayfasının yakınlaştırma faktörünü ayarlamak için [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) özelliğini kullanmayı gösteren tam bir örnek verilmiştir.

Book1.xls dosyası, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının bir örneğini oluşturarak açılır. İlk çalışma sayfasının yakınlaştırma faktörü 75 olarak ayarlanır ve değiştirilmiş dosya output.xls olarak kaydedilir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Set Worksheet Zoom Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the zoom factor of the worksheet to 75
            worksheet.zoom = 75;

            // Saving the modified Excel file (Excel97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Zoom set to 75 successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Pencereyi Dondurma**

### **Microsoft Excel Kullanımı**

Pencerelerin dondurulmasını sağlayan bir özellik, Microsoft Excel tarafından sağlanır. Pencereyi dondurma, bir çalışma tablosunda kaydırma yaparken görünmesini istediğiniz verileri seçmenize olanak tanır.

### **Aspose.Cells & Pencereleri Dondurma**

Aspose.Cells, çalışma sayfalarına çalışma zamanında sabit panolar uygulamak için geliştiricilere olanak tanır.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıfı içeren bir özelliktir. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sunar. Dondurulmuş panelleri yapılandırmak için, Worksheet sınıfının [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) yöntemini çağırın. [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) yöntemi aşağıdaki parametreleri alır:

- **Satır**, dondurulmanın başlayacağı hücrenin satır indeksi.
- **Sütun**, dondurulmanın başlayacağı hücrenin sütun indeksi.
- **Dondurulan satırlar**, üst bölmedeki görünür satır sayısı.
- **Donuk sütunlar**, sol panelde görünür sütunların sayısı.

Book1.xls dosyası, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının yapılandırıcısını çağırarak açılır ve ilk çalışma sayfasında birkaç satır ve sütun sabitlenir. Değiştirilmiş dosya output.xls olarak kaydedilir.

Aşağıdaki tam örnek, bir Excel dosyasının ilk çalışma sayfasının (0 dizininden başlayarak 4. satır ve 3. sütunu temsil eden C4'ten başlayarak) satır ve sütunları sabitlemek için [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) yönteminin nasıl kullanılacağını gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Applying freeze panes settings: topRows = 3, leftColumns = 2, top = 3, left = 2
            worksheet.freezePanes(3, 2, 3, 2);

            // Saving the modified Excel file in Excel97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/octet-stream" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Bölmeler**

Aynı çalışma tablosunda farklı görünümler elde etmek için ekranı bölmek istemeniz durumunda bölmeler. Microsoft Excel, çalışma sayfanızın kopyasını birden fazla görüntülemenize ve her bir pencerede bağımsız olarak kaydırmanıza izin veren çok kullanışlı bir özellik sunar: bölmeler.

Pencereler aynı anda çalışır. Birinde değişiklik yaparsanız, değişiklik diğerinde aynı anda görünür. Aspose.Cells, kullanıcılar için bölme bölmeleri özelliği sağlar.

### **Bölmelerin Uygulanması ve Kaldırılması**

#### **Bölmeleri Böleme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıfı içeren bir özelliktir. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, bir Excel dosyasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bölünmüş görünümleri uygulamak için, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--) özelliğini kullanın. Bölünmüş panoları kaldırmak için, [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--) yöntemini kullanın.

Örnekte, basit bir şablon dosyası kullanılır, ardından ilk çalışma sayfasındaki bir hücreye bölme bölmeleri özelliği uygulanır. Güncellenmiş dosya kaydedilir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Split Window Example</title>
    </head>
    <body>
        <h1>Split Worksheet Window Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new workbook and open the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Set the active cell (converted from setActiveCell -> activeCell)
            sheet.activeCell = "A20";

            // Split the worksheet window
            sheet.split();

            // Save the excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet window split and active cell set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Yukarıdaki kodu çalıştırdıktan sonra, oluşturulan dosyanın bölünmüş bir görünüme sahip olacağı.

#### **Pencereleri Kaldırma**

Bölme panolarını [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--) yöntemiyle kaldırın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Remove Split Example</h1>
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

            // Instantiate a new workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Set the active cell
            worksheet.activeCell = "A20";

            // Split the worksheet window - remove any existing split
            worksheet.removeSplit();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Çalışma Sayfasında Sıfır Değerlerinin Görüntüsünü Gizleme](/cells/tr/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Çalışma Sayfası Sekme Rengini Ayarlama](/cells/tr/javascript-cpp/set-worksheet-tab-color/)
- [Kılavuz Çizgilerini ve Satır Sütun Başlıklarını Gösterme ve Gizleme](/cells/tr/javascript-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [Satır Sütun ve Kaydırma Çubuklarını Gösterme ve Gizleme](/cells/tr/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [Çalışma Sayfalarını ve Sekmeleri Gösterme ve Gizleme](/cells/tr/javascript-cpp/show-and-hide-worksheets-and-tabs/)
- [Çalışma Sayfasında Değerlerin Yerine Formülleri Gösterme](/cells/tr/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [Hata Kontrol Seçeneklerini Kullan](/cells/tr/javascript-cpp/use-error-checking-options/)
