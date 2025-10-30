---
title: Çalışma Sayfasının Hücrelerine Erişme
type: docs
weight: 10
url: /tr/javascript-cpp/accessing-cells-of-a-worksheet/
description: Bu makale, çalışma sayfasının maksimum görüntüleme aralığını almayı ve hücrelere erişimi C++ API ile gösterir.
keywords: Hücre nesnesine erişme, Hücrelere Erişme, Çalışma sayfasının maksimum görüntüleme aralığını alın. 
---

{{% alert color="primary" %}}

Tüm çalışma sayfalarının temel olarak hücrelerde saklanan verileri içerdiğini biliyoruz (bir çalışma sayfası hücrelerden oluşur). Bir hücre, tüm çalışma sayfasını satırlar ve sütunlar dizisi olarak inşa etmek için kullanılan temel bir parçadır. Bir çalışma sayfasından veri almadan önce, hücrelerine erişim sağlamamız gerekir. Bu konuda, çalışma sayfası hücrelerine çalışma zamanında erişebilmek için bazı temel yaklaşımları tartışacağız.

{{% /alert %}}

## **Hücrelere Nasıl Erişilir**

C++ ile Script, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir sınıf sağlar, bu sınıf bir Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) adlı bir nesne içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonu sağlar.

[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonu kullanarak çalışma sayfasındaki hücrelere erişebiliriz. C++ ile Script, çalışma sayfasındaki hücrelere erişmek için üç temel yaklaşım sağlar:

1. Hücre adını kullanarak.
2. Bir hücrenin satır ve sütun indisini kullanarak.
1. [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunda hücre indeksini kullanarak

 3. yaklaşımın en hızlı, 1. yaklaşımın ise en yavaş olduğunu belirttik. Yaklaşımlar arasındaki performans farkı çok küçüktür, bu nedenle hangi yaklaşımı kullanırsanız kullanın performans düşüşü konusunda endişelenmeyin.

### **Hücre Nesnesini Hücre Adıyla Nasıl Alınır**

Geliştiriciler, hücrenin adını [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonuna indeks olarak geçirerek herhangi bir belirli hücreye erişebilirler.

Başlangıçta boş bir çalışma sayfası oluşturursanız, [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunun sayısı sıfırdır. Bu yöntemi kullanarak bir hücreye erişirken, bu hücrenin koleksiyonda olup olmadığını kontrol eder. Evet ise, koleksiyondaki hücre nesnesini döner, değilse yeni bir [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) nesnesi oluşturur, nesneyi [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonuna ekler ve sonra nesneyi döner. Bu yöntem, Microsoft Excel'e aşina olanlar için en kolay yoldur, ancak diğer yaklaşımlara göre en yavaş olanıdır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Read Cell Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("A1");

            // Output the cell's string value to the page
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **Hücrenin Satır ve Sütun İndisine Göre Hücre Nesnesi Nasıl Alınır**

Geliştiriciler, satır ve sütun indekslerini [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonuna geçirerek herhangi bir belirli hücreye erişebilirler.

Bu yaklaşım, ilk yaklaşımın çalışma şekliyle aynı şekilde çalışır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Value</h1>
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

            // Using the first worksheet in workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column (A1 -> 0,0)
            const cell = worksheet.cells.get(0, 0);

            // Printing the string value of the cell
            const value = cell.stringValue;
            console.log(value);
            resultDiv.innerHTML = `<p>Cell A1 value: ${value}</p>`;
        });
    </script>
</html>
```

### **Hücre Endeksindeki Hücre Nesnesi Nasıl Alınır**

Bir hücreye, hücrenin sayısal indeksini [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonuna geçirerek de erişilebilir.

Bu yaklaşımla hücrelere erişirken, hücrenin sayısal indeksi aralıktan dışarsa, bir istisna oluşabilir. Bu yöntem, hücrelere en hızlı şekilde erişmenin yoludur, ancak önemli bir bilgi şu ki, bu yöntemi kullanarak bir hücre nesnesine erişirseniz, sayısal indeks, yeni hücreler eklendikçe değişebilir. [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonundaki hücre nesneleri içsel olarak satır ve sütun indekslerine göre sıralanmıştır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell String Value</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the Sheet 1 in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column.
            const cell = worksheet.cells.get(0, 0);

            // Output the string value of the cell
            console.log(cell.stringValue);
            resultDiv.innerHTML = `<p>Cell (0,0) string value: <strong>${cell.stringValue}</strong></p>`;
        });
    </script>
</html>
```

## **Çalışsayının Maksimum Görüntü Aralığını Nasıl Alınır**

C++ ile Script, geliştiricilerin çalışma sayfasının maksimum görüntüleme alanına erişmesine olanak sağlar. Maksimum görüntüleme alanı — içerik bulunan ilk ve son hücreler arasındaki hücreler arası alan —, tüm çalışma sayfasını kopyalamak, seçmek veya görüntülemek gerektiğinde faydalıdır.

Bir çalışma sayfasının maksimum görüntüleme alanına [**Cells.maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--) kullanarak erişebilirsiniz. Aşağıdaki örnek kod, [**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--) özelliğine nasıl erişileceğini gösterir.

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Ensure Aspose.Cells is initialized
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the Maximum Display Range
            const range = worksheet.cells.maxDisplayRange;

            // Print / display the Maximum Display Range RefersTo property
            const refersTo = range.refersTo;
            resultDiv.innerHTML = `<p style="color: green;">Maximum Display Range: ${refersTo}</p>`;
        });
    </script>
</html>
```
