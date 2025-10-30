---
title: Excel dosyalarının formüllerini JavaScript ile C++ kullanarak yönetin
linktitle: Formüller
type: docs
weight: 122
url: /tr/javascript-cpp/using-formulas-or-functions-to-process-data/
description: Excel dosyalarının formüllerini nasıl yöneteceğinizi Aspose.Cells for JavaScript kullanarak C++ ile öğrenin. Aspose.Cells, Excel dosyalarının formüllerini basitçe alınabilir, ayarlanabilir ve hesaplanabilir hale getirir.
keywords: JavaScript ile C++ kullanarak formülleri nasıl hesaplayacağınızı, JavaScript kullanarak formüller ve fonksiyonlar, JavaScript ile C++ yönetilen yerleşik fonksiyonlar, JavaScript ile Eklenti fonksiyonlarını kullanmak, Dizi formüllerini kullanmak via JavaScript, JavaScript ile R1C1 formülünü kullanmak
---

## **Giriş**

Microsoft Excel'in etkileyici özelliklerinden biri, verileri formüller ve fonksiyonlar ile işleyebilme yeteneğidir. Microsoft Excel, karmaşık hesaplamaları hızlıca yapmaya yardımcı olan yerleşik fonksiyonlar ve formüller sunar. Aspose.Cells ayrıca, gelişmiş fonksiyon ve formüllerin büyük bir kümesini sağlar ve ayrıca eklenti fonksiyonlarını da destekler. Ayrıca, Aspose.Cells, dizi ve R1C1 formüllerini destekler.

## **Formüller ve Fonksiyonları Nasıl Kullanılır**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, bir [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonu sağlar. Hücreler koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfından bir nesneyi temsil eder.

Aşağıda daha detaylı olarak tartışılan [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının özellikleri ve metotları kullanılarak hücrelere formül uygulamak mümkündür.

- Yerleşik fonksiyonları kullanarak.
- Eklenti fonksiyonlarını kullanarak.
- Dizi formülleri ile çalışma.
- Bir R1C1 formülü oluşturma.

## **Yerleşik Fonksiyonları Nasıl Kullanılır**

Yerleşik fonksiyonlar veya formüller, geliştiricilerin çabalarını ve zamanı azaltmak için hazır fonksiyonlar olarak sağlanır. Aspose.Cells tarafından desteklenen yerleşik fonksiyonların [listesine](/cells/tr/javascript-cpp/supported-formula-functions/) bakın. Fonksiyonlar alfabetik sırayla listelenmiştir. Gelecekte daha fazla fonksiyon desteklenecek.

Aspose.Cells, Microsoft Excel tarafından sunulan formüllerin veya fonksiyonların çoğunu destekler. Geliştiriciler bu formülleri API veya [tasarımcı elektronik tablosu](/cells/tr/javascript-cpp/what-is-a-designer-spreadsheet/) aracılığıyla kullanabilir. Aspose.Cells, büyük bir matematiksel, dize, Boolean, tarih/zaman, istatistik, veritabanı, arama ve referans formülleri kümesi destekler.

[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) özelliğini kullanarak hücreye formül ekleyin. Örneğin **Karmaşık formüller**

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, Aspose.Cells'te de desteklenir. Bir hücreye formül uygularken, her zaman dizeye bir eşitlik işareti (=) ile başlayın (Microsoft Excel'de formül oluştururken olduğu gibi) ve bir virgül (,) kullanarak fonksiyon parametrelerini ayırın.

Aşağıdaki örnekte, bir çalışma sayfasının [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunun ilk hücresine karmaşık bir formül uygulanmıştır. Formül, Aspose.Cells tarafından sağlanan yerleşik bir **IF** fonksiyonunu kullanır.

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            worksheet.cells.get("A1").putValue(1);

            // Adding a value to "A2" cell
            worksheet.cells.get("A2").putValue(2);

            // Adding a value to "A3" cell
            worksheet.cells.get("A3").putValue(3);

            // Adding a SUM formula to "A4" cell
            worksheet.cells.get("A4").formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated A4 value: ${value}. Click the download link to get the generated file.</p>`;
        });
    </script>
</html>
```

## **Eklenti Fonksiyonlarını Nasıl Kullanılır**

Bazı kullanıcı tanımlı formüllerimiz var ve bunları bir Excel eklentisi olarak dahil etmek istiyoruz. Cell.formula fonksiyonunu ayarlarken yerleşik fonksiyonlar iyi çalışır, ancak özel fonksiyonlar veya formüllerin eklenti fonksiyonları kullanılarak ayarlanması gerekir.

Aspose.Cells, [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-) kullanarak eklenti fonksiyonlarını kaydetme özellikleri sağlar. Daha sonra, cell.formula = anyFunctionFromAddIn olarak ayarlandığında, çıktı Excel dosyası, Eklenti fonksiyonundan hesaplanan değeri içerir.

Aşağıdaki örnek kodda, eklenti fonksiyonunu kaydetmek için aşağıdaki XLAM dosyası indirilmelidir. Benzer şekilde, çıktı dosyası olan "test_udf.xlsx"yi indirerek çıktıyı kontrol edebilirsiniz.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Register Add-In Function Example</title>
    </head>
    <body>
        <h1>Register Add-In Function Example</h1>
        <p>Select the add-in file (.xlam/.xla) that contains the UDFs to register:</p>
        <input type="file" id="addInInput" accept=".xlam,.xla" />
        <button id="runExample">Register Add-In & Create Workbook</button>
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
            const fileInput = document.getElementById('addInInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an add-in file (.xlam/.xla).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const addinData = new Uint8Array(arrayBuffer);

            // Create empty workbook
            const workbook = new Workbook();

            // Register macro enabled add-in along with the function name
            const id = workbook.worksheets.registerAddInFunction(addinData, "TEST_UDF", false);

            // Register more functions in the file (if any)
            workbook.worksheets.registerAddInFunction(id, "TEST_UDF1");

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first cell
            const cell = worksheet.cells.get("A1");

            // Set formula name present in the add-in
            cell.formula = "=TEST_UDF()";

            // Save workbook to output XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_udf.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Add-in registered and formula set successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **Dizi Formülü Nasıl Kullanılır**

Dizi formüller, formülün bileşenlerine argüman olarak tek sayılar yerine dizileri alan formüllerdir. Dizi formülü gösterildiğinde, süslü parantezlerle ({}) çevrilidir.

Bazı Microsoft Excel fonksiyonları değerler dizileri döndürür. Bir dizi formülü ile birden çok sonucu hesaplamak için, diziyi formül argümanları olarak kullanarak aynı satır ve sütun sayısına sahip bir hücre aralığına girin.

Bir dizi formülünü, [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) yöntemini çağırarak bir hücreye uygulamak mümkündür. [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) yöntemi aşağıdaki parametreleri alır:

- **Dizi Formülü**, dizi formülü.
- **Satır Sayısı**, dizi formülünün sonucunu doldurmak için satır sayısı.
- **Sütun Sayısı**, dizi formülünün sonuçlarını doldurmak için sütun sayısı.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LINEST Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding values to cells
            worksheet.cells.get("A1").value = 1;
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 3;

            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 5;
            worksheet.cells.get("B3").value = 6;

            worksheet.cells.get("C1").value = 7;
            worksheet.cells.get("C2").value = 8;
            worksheet.cells.get("C3").value = 9;

            // Adding a SUM/LINEST array formula to "A6" cell
            worksheet.cells.get("A6").arrayFormula = { formula: "=LINEST(A1:A3,B1:C3,TRUE,TRUE)", rows: 5, cols: 3 };

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A6").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value: ${value}</p>`;
        });
    </script>
</html>
```

## **R1C1 Formülünü Nasıl Kullanılır**

Bir **R1C1** referans stili formülünü, [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının [**r1C1Formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#r1C1Formula--) özelliği ile bir hücreye ekleyin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set R1C1 Formula Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting an R1C1 formula on the "A11" cell,
            // Row and Column indices are relative to destination index
            const cell = worksheet.cells.get("A11");
            cell.r1C1Formula = "=SUM(R[-10]C[0]:R[-7]C[0])";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">R1C1 formula set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Öncüler ve Bağımlılar](/cells/tr/javascript-cpp/precedents-and-dependents/)
- [Formüllerde Harici Bağlantıları Ayarla](/cells/tr/javascript-cpp/set-external-links-in-formulas/)
- [Yeni satırlara veri girilirken Tablo veya List Objesinde Formülü otomatik olarak çoğaltın](/cells/tr/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Adlandırılmış Aralık için Formül Ayarlama](/cells/tr/javascript-cpp/setting-formula-for-named-range/)
- [Formülleri Ayarlama - Diğer Dilleri Kullanan Kullanıcılar İçin Uyarı](/cells/tr/javascript-cpp/setting-formulas-notice-for-non-english-users/)
- [Paylaşılan Formülü Ayarlama](/cells/tr/javascript-cpp/setting-shared-formula/)
- [Paylaşılan Formülün Maksimum Satırlarını Belirtme](/cells/tr/javascript-cpp/specify-maximum-rows-of-shared-formula/)
- [Desteklenen Excel İşlevleri](/cells/tr/javascript-cpp/supported-formula-functions/)
