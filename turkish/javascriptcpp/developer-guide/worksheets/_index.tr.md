---
title: Microsoft Excel dosyalarının Sayfa Çalışma Sayfalarını JavaScript ile C++ üzerinden Yönetme
linktitle: Çalışma Sayfaları
type: docs
weight: 90
url: /tr/javascript-cpp/manage-worksheets/
description: C++ üzerinden Aspose.Cells for JavaScript kullanarak çalışma sayfaları ekleme, kaldırma ve etkinleştirme.
---

{{% alert color="primary" %}}
Geliştiriciler, Aspose.Cells'in esnek API'sini kullanarak Microsoft Excel dosyalarında programlı olarak çalışma sayfaları eklemek ve kaldırmak için yaklaşımlar sağlar. Bu konu, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir {2} koleksiyonuna sahip olan bir {0} temsil eden bir Aspose.Cells sınıfını açıklar.
{{% /alert %}}

Aspose.Cells, Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her sayfaya erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sunar.

## **Yeni bir Excel Dosyasına Çalışsayfalar Ekleme**

Programlı olarak yeni bir Excel dosyası oluşturmak için:

1. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının bir nesnesini oluşturun.  
2. [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) sınıfının [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#add-sheettype-) yöntemini çağırın. Boş bir çalışma sayfası otomatik olarak Excel dosyasına eklenir. Yeni çalışma sayfasının sayfa indeksini [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonuna geçerek referans alabilirsiniz.  
3. Bir çalışma sayfası referansı edinin.  
4. Çalışma sayfalarında çalışma yapın.  
5. Yeni çalışma sayfalarıyla yeni Excel dosyasını kaydedin, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) yöntemini çağırarak.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Worksheet Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Get current worksheet count (converted from getWorksheets().getCount())
            const i = workbook.worksheets.count;

            // Add a new worksheet (converted from getWorksheets().add())
            workbook.worksheets.add();

            // Obtain the newly added worksheet by index (converted from getWorksheets().get(i))
            const worksheet = workbook.worksheets.get(i);

            // Set the name of the newly added worksheet (converted from setName)
            worksheet.name = "My Worksheet";

            // Save the workbook to XLS format and prepare download
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Tasarımcı Çalışsayfalara Çalışsayfalar Ekleme**

Tasarımcı çalışma sayfasına sayfa ekleme işlemi, yeni bir çalışma sayfası ekleme ile aynıdır; ancak, Excel dosyası zaten mevcut olmalı ve eklemeden önce açılmalıdır. Tasarımcı çalışma sayfası, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı kullanılarak açılabilir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Worksheet</title>
    </head>
    <body>
        <h1>Add Worksheet Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Setting the name of the newly added worksheet
            worksheet.name = "My Worksheet";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sayfa Adını Kullanarak Çalışsayfalara Erişme**

Adını veya dizinini belirterek herhangi bir çalışma sayfasına erişin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example: Read Cell Value</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing a worksheet using its sheet name
            const worksheet = workbook.worksheets.get("Sheet1");
            const cell = worksheet.cells.get("A1");

            console.log(cell.value);
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.value}</p>`;
        });
    </script>
</html>
```

## **Sayfa Adını Kullanarak Çalışsayfaları Kaldırma**

Bir dosyadan çalışma sayfalarını kaldırmak için, [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) sınıfının [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-) yöntemini çağırın. Belirli bir sayfayı kaldırmak için, sayfa adını [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-) yöntemine geçirin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Removing a worksheet using its sheet name
            workbook.worksheets.removeAt("Sheet1");

            // Save workbook
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sayfa Dizinini Kullanarak Çalışma Sayfalarını Kaldırma**

Sayfa adını kullanarak sayfaları kaldırmak, sayfa adını bildiğiniz zaman iyi çalışır. Sayfa adını bilmiyorsanız, sayfa indeksini alan [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-) yönteminin aşırı yüklenmiş versiyonunu kullanın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Remove First Worksheet</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Removing a worksheet using its sheet index
            workbook.worksheets.removeAt(0);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sayfaları Etkinleştirme ve Çalışma Sayfasında Aktif Bir Hücre Yapma**

Bazen, bir kullanıcının Microsoft Excel dosyasını Excel'de açtığında belirli bir çalışma sayfasının aktif ve görüntülenebilir olması gerekir. Benzer şekilde, belirli bir hücreyi etkinleştirmek ve kaydırma çubuklarını etkin hücreyi gösterecek şekilde ayarlamak isteyebilirsiniz. Aspose.Cells bu görevleri yapabilir.

Bir **etkin sayfa**, üzerinde çalıştığınız bir sayfadır: sekmelerdeki etkin sayfanın adı varsayılan olarak kalın harfle yazılıdır.

Bir **etkin hücre**, seçilen hücredir, verinin başlatıldığı hücredir. Aynı zamanda yalnızca bir hücre etkindir. Etkin hücre, kalın bir kenarlıkla vurgulanır.

### **Sayfaları Aktifleştirme ve Bir Hücreyi Etkin Yapma**

Aspose.Cells, bir sayfayı ve bir hücreyi etkinleştirmek için özel API çağrıları sağlar. Örneğin, [**WorksheetCollection.activeSheetIndex**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#activeSheetIndex--) özelliği, çalışma kitabında etkin sayfayı ayarlamak için kullanışlıdır. Benzer şekilde, [**Worksheet.activeCell**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#activeCell--) özelliği, bir çalışma sayfasında etkin hücreyi ayarlamak ve almak için kullanılır.

Yatay veya dikey kaydırma çubuklarının, belirli verileri göstermek istediğiniz satır ve sütun konumunda olduğundan emin olmak için [**Worksheet.firstVisibleRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#firstVisibleRow--) ve [**Worksheet.firstVisibleColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#firstVisibleColumn--) özelliklerini kullanın.

Aşağıdaki örnek, bir çalışma sayfasını etkinleştirmenin ve üzerinde etkin bir hücre oluşturmanın nasıl yapıldığını gösterir. Oluşturulan çıktıda, kaydırmalı çubuklar, ilk görünür satır ve sütun olarak 2. satır ve 2. sütunu yapmak için kaydırılır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Add a worksheet if collection is empty
            const worksheets = workbook.worksheets;
            if (worksheets.count === 0) {
                worksheets.add();
            }

            // Get the first worksheet in the workbook.
            const worksheet1 = worksheets.get(0);

            // Get the cells in the worksheet.
            const cells = worksheet1.cells;

            // Input data into B2 cell.
            const cell = cells.get(1, 1);
            cell.value = "Hello World!";

            // Set the first sheet as an active sheet.
            worksheets.activeSheetIndex = 0;

            // Set B2 cell as an active cell in the worksheet.
            worksheet1.activeCell = "B2";

            // Set the B column as the first visible column in the worksheet.
            worksheet1.firstVisibleColumn = 1;

            // Set the 2nd row as the first visible row in the worksheet.
            worksheet1.firstVisibleRow = 1;

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Çalışma Sayfalarını Kopyalama ve Taşıma](/cells/tr/javascript-cpp/copying-and-moving-worksheets/)  
- [Çalışma Sayfasındaki Hücre Sayısını Sayma](/cells/tr/javascript-cpp/count-number-of-cells-in-the-worksheet/)  
- [Boş Çalışma Sayfalarını Algılama](/cells/tr/javascript-cpp/detecting-empty-worksheets/)  
- [Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma](/cells/tr/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [Çalışma sayfası benzersiz kimliğini alın](/cells/tr/javascript-cpp/get-worksheet-unique-id/)  
- [Çalışma Sayfalarından Senaryo Oluşturma, Hareketlendirme veya Kaldırma](/cells/tr/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [Sayfa Sonlarını Yönetme](/cells/tr/javascript-cpp/managing-page-breaks/)  
- [Sayfa Ayarı Özellikleri](/cells/tr/javascript-cpp/page-setup-features/)  
- [Aspose.Cells üzerinde Sheet.SheetId özelliğini kullanarak OpenXml'in faydalanılması](/cells/tr/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [Çalışma Sayfası Görünümleri](/cells/tr/javascript-cpp/worksheet-views/)
