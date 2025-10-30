---
title: JavaScript ile C++ aracılığıyla Adlandırılmış Aralıklar Oluştur ve Kopyala
linktitle: Erişim Oluştur ve Adlandırılmış Aralıkları Kopyala
type: docs
weight: 200
url: /tr/javascript-cpp/create-access-and-copy-named-ranges/
description: Excel de adlandırılmış aralıklar oluşturma, erişme ve kopyalama yöntemlerini öğrenin, Aspose.Cells for JavaScript via C++ kullanarak.
---

## **Giriş**  

 Normalde, sütun ve satır etiketleri belirli hücreleri göstermek için kullanılır. Hücreleri, hüreleri, formülleri veya sabit değerleri temsil eden açıklayıcı isimler oluşturmak mümkündür. **isim** kelimesi, hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil eden bir karakter dizisini ifade edebilir. Bir aralığa isim atamak, bu aralıktaki hücrelerin adını kullanarak erişilebilmesine olanak tanır. Anlaşılması kolay isimler kullanın, örneğin Satışlar!C20:C30 gibi karmaşık aralıklar yerine Products gibi. Etiketler, aynı sayfada veri referans alan formüllerde kullanılabilir; başka bir sayfadaki aralığı göstermek istiyorsanız, bir isim kullanabilirsiniz. *İsimlendirilmiş aralıklar, liste kontrolleri, pivot tablolar, grafikler ve benzeri kaynak aralığı olarak kullanıldığında Microsoft Excel'in en güçlü özelliklerinden biridir.*  

## **Microsoft Excel Kullanarak Adlandırılmış Aralık İle Çalışma**  

### **Adlandırılmış Aralık Oluştur**  

Aşağıdaki adımlar, **MS Excel** kullanarak hücre veya hücre aralığını nasıl adlandıracağınızı açıklar. Bu yöntem, **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000**, ve **2002** için geçerlidir.  

1. Adlandırmak istediğiniz hücre veya hücre aralığını seçin.  
2. Formül çubuğunun sol ucundaki **İsim Kutusu**na tıklayın.  
3. Hücreler için isim yazın.  
4. ENTER tuşuna basın.  

{{% alert color="primary" %}}  
Hücre içeriğini değiştirirken hücreye ad veremezsiniz.  
{{% /alert %}}  

## **Aspose.Cells Kullanarak Adlandırılmış Aralık İle Çalışma**  

Burada görevi yapmak için Aspose.Cells API'sını kullanıyoruz.  
Aspose.Cells, Microsoft Excel dosyasını temsil eden bir sınıf, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışsayfaya erişim sağlayan [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir. Bir çalışsayfa [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı bir [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonu sağlar.  

### **İsimlendirilmiş Aralık Oluştur**  

Bir adlandırılmış aralık oluşturmak, [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunun aşırı yüklenmiş [**createRange(string, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) yöntemini çağırarak mümkündür. [**createRange(string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-) yönteminin tipik bir sürümü aşağıdaki parametreleri alır:  

- Sol üst hücrenin adı, aralıktaki sol üst hücrenin adı.  
- Sağ alt hücrenin adı, aralıktaki sağ alt hücrenin adı.  

[**createRange(string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-) yöntemi çağrıldığında, yeni oluşturulan aralık, [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) sınıfının bir örneği olarak döner. Bu [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) nesnesini, isimlendirilmiş aralığı yapılandırmak için kullanın. Örneğin, [**name**](https://reference.aspose.com/cells/javascript-cpp/range/#name--) özelliğini kullanarak aralığın adını ayarlayın. Aşağıdaki örnek, B4:G14 üzerine uzanan hücrelerin adlandırılmış bir aralık oluşturmak için nasıl yapılacağını göstermektedir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Named Range Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating a named range
            const range = worksheet.cells.createRange("B4", "G14");

            // Setting the name of the named range
            range.name = "TestRange";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Adı Verilen Aralıktaki Hücrelere Veri Girişi**  

Bir aralıktaki bireysel hücrelere veri ekleyebilirsiniz. İzlenecek desen aşağıdaki gibidir  

- **JavaScript**: Range[row,sütun]  

A1:C4'ü kapsayan bir isimlendirilmiş aralığınız olduğunu düşünün. Matris 4 * 3 = 12 hücre yaratır. Bireysel aralık hücreleri ardışık olarak düzenlenir: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

Aralıktaki hücreleri tanımlamak için aşağıdaki özellikleri kullanın:  

- firstRow, adlandırılmış aralıktaki ilk satırın indeksini döndürür.  
- firstColumn, adlandırılmış aralıktaki ilk sütunun indeksini döndürür.  
- rowCount, adlandırılmış aralıktaki toplam satır sayısını döndürür.  
- columnCount, adlandırılmış aralıktaki toplam sütun sayısını döndürür.  

Aşağıdaki örnek, belirtilen bir aralıktaki hücrelere bazı değerler girmeyi gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Named Range Example</h1>
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first worksheet in the workbook.
            const worksheet1 = workbook.worksheets.get(0);

            // Create a range of cells based on H1:J4.
            const range = worksheet1.cells.createRange("H1", "J4");

            // Name the range.
            range.name = "MyRange";

            // Input some data into cells in the range.
            range.get(0, 0).value = "USA";
            range.get(0, 1).value = "SA";
            range.get(0, 2).value = "Israel";
            range.get(1, 0).value = "UK";
            range.get(1, 1).value = "AUS";
            range.get(1, 2).value = "Canada";
            range.get(2, 0).value = "France";
            range.get(2, 1).value = "India";
            range.get(2, 2).value = "Egypt";
            range.get(3, 0).value = "China";
            range.get(3, 1).value = "Philipine";
            range.get(3, 2).value = "Brazil";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'rangecells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and range populated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

### **İsimlendirilmiş Aralıktaki Hücreleri Tanımlama**  

Bir aralıktaki bireysel hücrelere veri ekleyebilirsiniz. İzlenecek desen aşağıdaki gibidir:  

- **JavaScript**: Range[row,sütun]  

Eğer A1:C4'ü kapsayan bir isimlendirilmiş aralığınız varsa, matris 4 * 3 = 12 hücre yaratır. Bireysel aralık hücreleri ardışık olarak düzenlenir: Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

Aralıktaki hücreleri tanımlamak için aşağıdaki özellikleri kullanın:  

- firstRow, adlandırılmış aralıktaki ilk satırın indeksini döndürür.  
- firstColumn, adlandırılmış aralıktaki ilk sütunun indeksini döndürür.  
- rowCount, adlandırılmış aralıktaki toplam satır sayısını döndürür.  
- columnCount, adlandırılmış aralıktaki toplam sütun sayısını döndürür.  

Aşağıdaki örnek, belirtilen bir aralıktaki hücrelere bazı değerler girmeyi gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Named Range</title>
    </head>
    <body>
        <h1>Get Named Range Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Getting the specified named range
            const range = workbook.worksheets.rangeByName("TestRange");

            if (!range) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Named range "TestRange" not found.</p>';
                return;
            }

            // Identify range cells and display properties
            const firstRow = range.firstRow;
            const firstColumn = range.firstColumn;
            const rowCount = range.rowCount;
            const columnCount = range.columnCount;

            const html = [
                `<p>First Row : ${firstRow}</p>`,
                `<p>First Column : ${firstColumn}</p>`,
                `<p>Row Count : ${rowCount}</p>`,
                `<p>Column Count : ${columnCount}</p>`
            ].join('');

            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```  

### **İsimlendirilmiş Aralıklara Eriş**  

#### **Belirli Bir Adlandırılmış Aralığa Erişme**  

Belirli bir adlandırılmış aralığa erişmek için [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) koleksiyonunun [**rangeByName(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#rangeByName-string-) yöntemini çağırın. Tipik bir [**rangeByName(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#rangeByName-string-) yöntemi, adlandırılmış aralığın adını alır ve belirtilen adlandırılmış aralığı [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) sınıfının bir örneği olarak döndürür. Aşağıdaki örnek, adına göre belirtilen bir aralığa nasıl erişileceğini göstermektedir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Named Range Example</title>
    </head>
    <body>
        <h1>Get Named Range Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Getting the specified named range
            const worksheets = workbook.worksheets;
            const range = worksheets.rangeByName("TestRange");

            if (range !== null) {
                document.getElementById('result').innerHTML = `<p>Named Range : ${range.refersTo}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">Named range "TestRange" not found.</p>';
            }
        });
    </script>
</html>
```  

#### **Bir Elektronik Tablodaki Tüm İsimlendirilmiş Aralıklara Eriş**  

Bir elektronik tabloda tüm adlandırılmış aralıkları almak için [**worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) koleksiyonunun [**namedRanges()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#namedRanges--) metodunu çağırın. [**namedRanges()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#namedRanges--) metodu, [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) koleksiyonundaki tüm adlandırılmış aralıkların dizisini döndürür.  

Aşağıdaki örnek, bir çalışma kitabındaki tüm adlandırılmış aralıklara erişmeyi gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Named Ranges</title>
    </head>
    <body>
        <h1>Get Named Ranges Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Getting all named ranges
            const ranges = workbook.worksheets.namedRanges;

            if (ranges) {
                // Some collections expose 'count', others may expose 'length'
                const total = (typeof ranges.count !== 'undefined') ? ranges.count : ranges.length;
                document.getElementById('result').innerHTML = `<p style="color: green;">Total Number of Named Ranges: ${total}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No named ranges found.</p>';
            }
        });
    </script>
</html>
```  

### **İsimlendirilmiş Aralıkları Kopyala**  

Aspose.Cells, bir hücre aralığını biçimlendirmesiyle birlikte başka bir aralığa kopyalamak için [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/range/#copy-range-pasteoptions-) yöntemi sağlar.  

Aşağıdaki örnek, kaynak hücre aralığını başka adlandırılmış bir aralığa kopyalamanın nasıl yapıldığını göstermektedir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Ranges</title>
    </head>
    <body>
        <h1>Copy Ranges Example</h1>
        <p>Select an Excel file to modify, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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

            // Instantiate a new Workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Get the first worksheet in the worksheets collection.
            const worksheet = workbook.worksheets.get(0);

            // Create a range of cells.
            const range1 = worksheet.cells.createRange("E12", "I12");

            // Name the range.
            range1.name = "MyRange";

            // Set the outline border to the range.
            range1.outlineBorder = { borderType: BorderType.TopBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.BottomBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.LeftBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.RightBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };

            // Input some data with some formattings into a few cells in the range.
            range1.get(0, 0).putValue("Test");
            range1.get(0, 4).putValue("123");

            // Create another range of cells.
            const range2 = worksheet.cells.createRange("B3", "F3");

            // Name the range.
            range2.name = "testrange";

            // Copy the first range into second range.
            range2.copy(range1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'copyranges.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
