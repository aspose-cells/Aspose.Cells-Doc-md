---
title: Excel veya OpenOffice a Hyperlink Ekleme
linktitle: Hyperlinkleri Yönetme
type: docs
weight: 45
url: /tr/javascript-cpp/insert-hyperlinks-to-excel/
description: MS Excel olmadan JavaScript kullanarak Aspose.Cells kütüphanesi ile Excel dosyasına bağlantı (hiperlink) nasıl eklenir.
keywords: Excel’e Hiperlink Ekleme JavaScript kullanarak, Hiperlink Ekle veya Ekle JavaScript ile, URL’ye Bağlantı Ekle veya Ekle JavaScript ile, Hücreye Bağlantı Ekle veya Ekle JavaScript ile, Dış bir Dosyaya Bağlantı Ekle JavaScript ile
---

{{% alert color="primary" %}} 

Bir bağlantı, iki varlık arasında bir bağlantı oluşturmak için kullanılır. Herkes, özellikle web sitelerinde bağlantıların kullanımı hakkında bilgilidir.
Aspose.Cells kullanarak, geliştiriciler Microsoft Excel dosyalarında farklı türde bağlantılar oluşturabilir. Bu konu, Aspose.Cells tarafından desteklenen bağlantı türlerini ve bunların Excel dosyalarımızda nasıl kullanılabileceğini tartışmaktadır.

{{% /alert %}} 

## **Hyperlinkler Ekleme**
Aspose.Cells, geliştiricilerin hem API kullanarak hem de tasarımcı tabloları (manuel olarak bağlantıların oluşturulduğu ve Aspose.Cells'in diğer tablolara aktarım için kullanıldığı tablolar) ile bağlantılar eklemesine olanak tanır.

Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her sayfaya erişim sağlayan [WorksheetCollection](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) içerir. Bir sayfa, [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. Bu sınıf, Excel dosyalarına farklı hiperbağlantılar eklemek için çeşitli yöntemler sunar.
## **URL'ye Bağlantı Ekleme**
[Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, [hyperlinks](https://reference.aspose.com/cells/javascript-cpp/worksheet/#hyperlinks--) koleksiyonunu içerir. Her bir madde, [Hyperlink](https://reference.aspose.com/cells/javascript-cpp/hyperlink) nesnesini temsil eder. URL’lere hiperbağlantı eklemek için, [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection) koleksiyonunun [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) metodunu çağırın. [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) metodu aşağıdaki parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, URL adresi.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Hyperlink Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example (Create Workbook & Add Hyperlink)</button>
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

            // Obtain the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a hyperlink to a URL at "A1" cell
            worksheet.hyperlinks.add("A1", 1, 1, "http://www.aspose.com");

            // Save the Excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}} 

Yukarıdaki örnekte, bir hiper bağlantı boş bir hücre olan **A1**'e eklenir. Bu tür durumlarda, hücre boşsa, URL adresi de boş hücreye değeri olarak eklenir. Hücre dolu değilse ve bir hiper bağlantı eklenmişse, hücrenin değeri düz metin olarak görünür. Onu bir hiper bağlantı gibi görünmesini sağlamak için o hücreye uygun biçimlendirme ayarlarını uygulayın.

{{% /alert %}} 
## **Aynı Dosyadaki Bir Hücreye Bağlantı Ekleme**
Ayrıca, aynı Excel dosyasındaki hücrelere hiperbağlantı eklemek için, [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection) koleksiyonunun [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) metodunu çağırabilirsiniz. Bu metod, hem dahili hem de harici hiperbağlantıları destekler. Aşırı yüklenmiş bir metodun bir versiyonu aşağıdaki parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef hücrenin adresi.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Internal Hyperlink Example</h1>
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
            // Create a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            workbook.worksheets.add();

            // Obtaining the reference of the first (default) worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding an internal hyperlink to the "B3" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("B3", 1, 1, "Sheet2!B9");

            // Saving the Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Excel file created successfully. Click the download link to save it.</p>';
        });
    </script>
</html>
```


## **Harici Bir Dosyaya Bağlantı Ekleme**
Dış Excel dosyalarına hiperbağlantı eklemek için, [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection) koleksiyonunun [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) metodunu çağırabilirsiniz. Bu metod aşağıdaki parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef harici Excel dosyasının adresi.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <p>Select an optional Excel file to use its filename as the hyperlink target (or leave empty to use "book1.xls"):</p>
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
            let targetFileName = 'book1.xls';
            if (fileInput.files.length) {
                targetFileName = fileInput.files[0].name;
            }

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Adding an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("A5", 1, 1, targetFileName);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **Gelişmiş Konular**
- [Görüntü Bağlantılarını Eklemek](/cells/tr/javascript-cpp/add-image-hyperlinks/)
- [Bağlantı Türünü Algılamak](/cells/tr/javascript-cpp/detect-hyperlink-type/)
- [Çalışma Sayfasının Bağlantılarını Düzenleme](/cells/tr/javascript-cpp/editing-hyperlinks-of-worksheet/)
- [Aralıktaki Bağlantıları Al](/cells/tr/javascript-cpp/get-hyperlinks-in-range/)
