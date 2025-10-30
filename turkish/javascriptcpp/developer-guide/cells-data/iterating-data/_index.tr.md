---
title: JavaScript ile C++ kullanarak Anketler, Gözat noktaları ve kullanımı için nerelerde ve nasıl kullanılır
linktitle: Verileri Yinele
type: docs
weight: 55
url: /tr/javascript-cpp/how-and-where-to-use-enumerators/
description: C++ API üzerinden Aspose.Cells for JavaScript ile Enumerators kullanmayı öğrenin.
keywords: C++, Cells Enumerator JavaScript kullanımı, C++ üzerinden Rows Enumerator JavaScript kullanımı, C++ üzerinden Columns Enumerator JavaScript kullanımı
---

{{% alert color="primary" %}}  

Bir enumerator, bir konteyner veya koleksiyon içinde gezinme yeteneği sağlayan bir nesnedir. Enumerators, koleksiyondaki verileri okumak için kullanılabilir, ancak temel koleksiyonu değiştirmek için kullanılamaz, Array ise `enumerator` adlı bir yöntemi tanımlayan bir arayüzdür ve bu yöntem bir `IEnumerator` arayüzü döner, bu da koleksiyon üzerinde salt okunur erişim sağlar.  

Aspose.Cells API'ları bir dizi numaralandırıcı sağlar, ancak bu makale genellikle aşağıda listelenen üç türü tartışmaktadır.  

1. Hücreler Numaralandırıcı  
1. Satırlar Numaralandırıcı  
1. Sütunlar Numaralandırıcı  

{{% /alert %}}  

## **Numaralandırıcıları Nasıl Kullanılır**  

### **Hücreler Numaralandırıcı**  

Hücreler Numaralandırıcısına erişmenin çeşitli yolları vardır ve uygulama gereksinimlerine bağlı olarak bu yöntemlerden herhangi biri kullanılabilir. İşte hücreler numaralandırıcısını döndüren yöntemler.  

1. [**Cells.enumerator**](https://reference.aspose.com/cells/javascript-cpp/cells/#enumerator--)  
1. [**Row.enumerator**](https://reference.aspose.com/cells/javascript-cpp/row/#enumerator--)  
1. [**Range.enumerator**](https://reference.aspose.com/cells/javascript-cpp/range/#enumerator--)  

Yukarıda bahsedilen tüm yöntemler, başlatılmış hücre koleksiyonunu gezinmeyi sağlayan numaralandırıcıyı döndürür.  

{{% alert color="primary" %}}  

Hücreleri gezinirken koleksiyon değiştirilmemelidir (bir hücreyi yeni bir şekilde oluşturan işlemler veya var olan bir hücreyi sildiren işlemler). Aksi takdirde, numaralandırıcı tüm hücreleri doğru bir şekilde gezinemeyebilir (bazı öğeler tekrarlanabilir veya atlanabilir).  

{{% /alert %}}  

Aşağıdaki kod örneği, bir Hücreler koleksiyonunun `IEnumerator` arayüzü uygulamasını göstermektedir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Values</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            const resultLines = [];

            // Iterate over all cells in the worksheet
            const cellsEnumerator = worksheet.cells.getEnumerator();
            for (const cell of cellsEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            // Iterate over the first row's cells
            const firstRowEnumerator = worksheet.cells.rows.get(0).getEnumerator();
            for (const cell of firstRowEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            // Iterate over a specific range A1:B10
            const rangeEnumerator = worksheet.cells.createRange("A1:B10").getEnumerator();
            for (const cell of rangeEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            document.getElementById('result').innerHTML = `<pre>${resultLines.join('\n')}</pre>`;
        });
    </script>
</html>
```  

### **Satırlar Numaralandırıcı**  

Satır Sayıcı (Rows Enumerator), [**RowCollection.enumerator**](https://reference.aspose.com/cells/javascript-cpp/rowcollection/#enumerator--) yöntemi kullanılırken erişilebilir. Aşağıdaki kod örneği, [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection) için `IEnumerator` arayüzünün uygulanmasını gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - List Row Indexes</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get RowCollection and iterate using index
            const rows = workbook.worksheets.get(0).cells.rows;
            const rowCount = rows.count;

            // Traverse rows in the collection and display indexes
            let output = '<p>Row indexes:</p><ul>';
            for (let i = 0; i < rowCount; i++) {
                const row = rows.get(i);
                output += `<li>${row.index}</li>`;
                console.log(row.index);
            }
            output += '</ul>';
            document.getElementById('result').innerHTML = output;
        });
    </script>
</html>
```  

### **Sütunlar Numaralandırıcı**  

Sütun Sayıcı (Columns Enumerator), [**ColumnCollection.enumerator**](https://reference.aspose.com/cells/javascript-cpp/columncollection) yöntemi kullanılırken erişilebilir. Aşağıdaki kod örneği, [**ColumnCollection**](https://reference.aspose.com/cells/javascript-cpp/columncollection) için `IEnumerator` arayüzünün uygulanmasını gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Columns Indexes Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get columns collection from first worksheet
            const columns = workbook.worksheets.get(0).cells.columns;
            // Traverse columns using index
            const count = columns.count;
            let html = '<p>Columns indexes:</p><ul>';
            for (let i = 0; i < count; i++) {
                const col = columns.get(i);
                html += `<li>${col.index}</li>`;
                console.log(col.index);
            }
            html += '</ul>';
            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```  

## **Numaralandırıcıları Nerede Kullanılacağı**  

Dizicilerin avantajlarını tartışmak için gerçek zamanlı bir örnek ele alalım.  

**Senaryo**  

Bir uygulamanın gereksinimlerinden biri, belirli bir [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) içindeki tüm hücreleri gezinerek değerlerini okumaktır. Bu amacı gerçekleştirmek için birkaç yöntem gösterilmiştir.  

### **Görüntü Aralığı Kullanarak**  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Max Display Range Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection of first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Get the MaxDisplayRange
            const displayRange = cells.maxDisplayRange;

            // Loop over all cells in the MaxDisplayRange
            let outputLines = [];
            for (let row = displayRange.firstRow; row < displayRange.rowCount; row++) {
                for (let col = displayRange.firstColumn; col < displayRange.columnCount; col++) {
                    // Read the Cell value (stringValue property)
                    const cell = displayRange.get(row, col);
                    outputLines.push(cell.stringValue);
                    console.log(cell.stringValue);
                }
            }

            resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```  

### **MaxDataRow & MaxDataColumn Kullanarak**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #result { margin-top: 15px; max-height: 400px; overflow: auto; border: 1px solid #ddd; padding: 10px; }
            .cell-value { padding: 2px 0; border-bottom: 1px dashed #eee; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>Read Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;

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

        function escapeHtml(text) {
            if (text === null || text === undefined) return '';
            return String(text)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p class="error">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection of first worksheet
            const cells2 = workbook.worksheets.get(0).cells;
            const maxDataRow = cells2.maxDataRow;
            const maxDataColumn = cells2.maxDataColumn;

            const outputLines = [];
            // Loop over all cells
            for (let row = 0; row <= maxDataRow; row++) {
                for (let col = 0; col <= maxDataColumn; col++) {
                    // Read the Cell value
                    const currentCell = cells2.checkCell(row, col);
                    if (currentCell) {
                        const cellText = currentCell.stringValue;
                        outputLines.push('<div class="cell-value">' + escapeHtml(cellText) + '</div>');
                        console.log(cellText);
                    }
                }
            }

            if (outputLines.length === 0) {
                resultDiv.innerHTML = '<p>No cell values found.</p>';
            } else {
                resultDiv.innerHTML = outputLines.join('');
            }
        });
    </script>
</html>
```  

Yukarıda bahsedilen her iki yaklaşımın da, tüm hücreleri döngü içinde dolaşarak hücre değerlerini okuma mantığına daha veya daha az benzer olduğunu gözlemleyebilirsiniz. Bu, aşağıda tartışılan birçok nedenden biri olabilir.  

1. [**maxRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxRow--), [**maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--), [**maxColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxColumn--), [**maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) ve [**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--) gibi API'ler, ilgili istatistikleri toplamak için ekstra zaman gerektirir. Veri matrisi (satırlar x sütunlar) büyükse, bu API'leri kullanmak performans düşüşüne neden olabilir.  
1. Çoğu durumda, verilen bir aralıktaki tüm hücreler oluşturulmamıştır. Bu tür durumlarda, matristeki her hücreyi kontrol etmek, yalnızca başlatılmış hücreleri kontrol etmekten daha verimli değildir.  
1. Hücreye döngü içinde Cells satır, sütun olarak erişmek, bir aralıktaki tüm hücre nesnelerinin oluşturulmasına neden olabilir, bu da sonunda OutOfMemoryException'a neden olabilir.  

## **Sonuç**  

Yukarıda belirtilen gerçeklere dayanarak, aşağıdakiler, numaralandırıcıların kullanılması gereken olası senaryolarıdır.  

1. Yalnızca hücre koleksiyonunun salt okunur erişimi gereklidir, yani; gereksinim yalnızca hücreleri incelemektir.  
1. Birçok hücrenin dolaşılması gereklidir.  
1. Yalnızca başlatılmış hücreler/satırlar/sütunlar dolaşılmalıdır.
