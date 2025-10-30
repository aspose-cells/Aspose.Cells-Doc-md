---
title: Hücre adı ve satır/sütun dizini arasında dönüştürme işlemi
linktitle: Hücre Adı ve Dizin Dönüştürme
type: docs
weight: 10
url: /tr/javascript-cpp/names-and-indices/
description: Hücre adı ve satır/sütun indeksleri arasındaki dönüşüm nasıl yapılır, C++ API üzerinden Aspose.Cells for JavaScript kullanarak öğrenin.
keywords: JavaScript ile C++ kullanarak Satır ve Sütun İndekslerinden Hücre Adı Alma, Hücre Adından Satır ve Sütun İndeksleri Alma, Güvenli çalışma yaprağı isimleri oluşturma, Güvenli çalışma sayfası isimleri ekleme
---

## **Satır ve Sütun Dizilerinden Hücre Adı Alın**
Bir hücrenin adını bulmak mümkündür, verilen satır ve sütun dizini. Bu makale açıklar.
Aspose.Cells for JavaScript C++ aracılığıyla CellsHelper.cellIndexToName metodunu sağlar, bu da geliştiricilerin satır ve sütun indekslerini vererek bir hücrenin adını almalarına olanak tanır.

{{% alert color="primary" %}} 

Microsoft Excel satır ve sütun indekslerini 1'den saymaya başlar. Microsoft Excel'in aksine, Aspose.Cells for JavaScript C++ aracılığıyla satır ve sütun indeksleri 0'dan başlar.

{{% /alert %}} 

Aşağıdaki örnek kod, bilinen satır ve sütun indeksi verildiğinde CellsHelper.cellIndexToName metodunu kullanarak hücrenin adını nasıl alacağınızı gösterir. Kod aşağıdaki çıktıyı üretir.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Original logic converted to browser JavaScript
            var row = 3;
            var column = 5;
            var name = AsposeCells.CellsHelper.cellIndexToName(row, column);
            console.log("Cell name: " + name);
            document.getElementById('result').innerHTML = '<p>Cell name: ' + name + '</p>';
        });
    </script>
</html>
```
## **Hücre Adından Satır ve Sütun Dizilerini Alın**
Bir hücrenin adından satır ve sütun dizinini bulmak mümkündür. Bu makale açıklar.
Aspose.Cells for JavaScript C++ hücrenin adıyla satır ve sütun indekslerini almak için CellsHelper.cellNameToIndex metodunu sağlar, bu da geliştiricilere imkan tanır.

{{% alert color="primary" %}} 

Microsoft Excel satır ve sütun indekslerini 1'den saymaya başlar. Microsoft Excel'in aksine, Aspose.Cells for JavaScript C++ aracılığıyla satır ve sütun indeksleri 0'dan başlar.

{{% /alert %}} 

Aşağıdaki örnek kod, CellsHelper.cellNameToIndex metodunu kullanarak hücrenin adından satır ve sütun indekslerini nasıl alacağınızı gösterir. Kod aşağıdaki çıktıyı üretir.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Row and Column from Cell Name</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <div>
            <label for="cellName">Cell Name:</label>
            <input type="text" id="cellName" value="C4" />
        </div>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

        let asposeInitialized = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeInitialized = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const name = document.getElementById('cellName').value || "C4";

            const rowCol = CellsHelper.cellNameToIndex(name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];
            console.log("Row: " + currRow + " , Column: " + currCol);

            document.getElementById('result').innerHTML = `<p>Row: ${currRow} , Column: ${currCol}</p>`;
        });
    </script>
</html>
```

## **Güvenli Çalışma Sayfası Adları Oluşturun**
Bazen çalışma sayfası adını çalışma zamanında atamak gerekebilir. Bu durumda, <>+(?” gibi ek karakterler içerebilecek sayfalar olabilir. Kullanıcı tarafından sağlanan bazı önceden ayarlanmış karakterlerle değiştirilmesi gereken, geçerli olmayan karakterler vardır. Benzer şekilde, uzunluk 31 karakterden fazla olabilir ve bu durumda kısaltılması gerekebilir. Apache POI, güvenli isimler oluşturmak için belirli özellikler sağlar, bu nedenle benzer özellikler Aspose.Cells for JavaScript C++ aracılığıyla da sunulur ve aşağıdaki örnek kod bu özelliği göstermektedir:



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Create Safe Sheet Name</title>
    </head>
    <body>
        <h1>Create Safe Sheet Name Example</h1>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Long name will be truncated to 31 characters
            var name1 = AsposeCells.CellsHelper.createSafeSheetName("this is first name which is created using CellsHelper.CreateSafeSheetName and truncated to 31 characters");

            // Any invalid character will be replaced with _
            var name2 = AsposeCells.CellsHelper.createSafeSheetName(' <> + (adj.Private ? " Private" : ")', '_');

            // Display results in the page
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p><strong>Safe Name 1:</strong> ' + name1 + '</p>' +
                                  '<p><strong>Safe Name 2:</strong> ' + name2 + '</p>';
        });
    </script>
</html>
```

Çıktı:

Bu, oluşturulmuş ilk adın kısaltıldığı ad

` <> + (adj.Private _ "Özel"
