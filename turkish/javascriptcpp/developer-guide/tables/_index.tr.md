---
title: JavaScript ile C++ kullanarak Microsoft Excel dosyalarının tablolarını oluşturun ve yönetin
linktitle: Tablolar
type: docs
weight: 150
url: /tr/javascript-cpp/create-and-format-table/
description: Excel dosyalarının tablolarını ekleyin, yeniden boyutlandırın, düzenleyin, silin ve biçimlendirin Aspose.Cells for JavaScript ile C++ kullanarak.
---

## **Tablo Oluştur**

Hesap tablolarının avantajlarından biri, telefon listeleri, görev listeleri, işlemler, varlıklar veya borçlar gibi farklı tiplerde listeler oluşturmanıza olanak tanımalarıdır. Çeşitli kullanıcılar birden fazla listeyi kullanmak, oluşturmak ve yönetmek için birlikte çalışabilir.

Aspose.Cells, listeler oluşturmayı ve yönetmeyi destekler.

### **Liste Nesnesi Avantajları**

Veri listesini gerçek bir Liste Nesnesine dönüştürdüğünüzde birkaç avantaj bulunmaktadır

- Yeni satır ve sütunlar otomatik olarak dahil edilir.
- Listenizin altından toplam satırı SUM, AVERAGE, COUNT vb. göstermek için kolayca ekleyebilirsiniz.
- Sağa eklenen sütunlar otomatik olarak List nesnesine dahil edilir.
- Satırlar ve sütunlara dayalı grafikler otomatik olarak genişletilecektir.
- Satırlara ve sütunlara atanan adlandırılmış aralıklar otomatik olarak genişletilir.
- Liste kazara satır ve sütun silme işlemlerine karşı korunur.

### **Microsoft Excel Kullanarak Bir Liste Nesnesi Oluşturma**

- Liste nesnesi oluşturmak için veri aralığını seçme
- Bu, Liste Oluştur iletişim kutusunu görüntüler.
- Veri için Liste nesnesini uygula ve toplam satırını belirtin (**Veri** > **Liste** > **Toplam Satır**) seçin.

### **Aspose.Cells API'si Kullanımı**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir çalışma sayfasında [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) oluşturmak için, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının [**listObjects**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#listObjects--) koleksiyon özelliğini kullanın. Her [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/), aslında [**ListObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/) sınıfının bir nesnesidir ve ek olarak [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/#add-number-number-number-number-boolean-) yöntemi ile Liste nesnesi ekleme ve hücre aralığını belirleme sağlar.

Belirtilen hücre aralığına göre, Aspose.Cells tarafından Liste nesnesi oluşturulur. Listeyi kontrol etmek için [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) sınıfının attribute'leri (örneğin, [**showTotals**](https://reference.aspose.com/cells/javascript-cpp/listobject/#showTotals--), [**listColumns**](https://reference.aspose.com/cells/javascript-cpp/listobject/#listColumns--) vb.) kullanın.

Aşağıdaki örnekte, yukarıdaki bölümde Microsoft Excel kullanarak oluşturduğumuzla aynı [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) nesnesini Aspose.Cells API kullanarak oluşturduk.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells ListObjects Example</title>
    </head>
    <body>
        <h1>ListObjects Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TotalsCalculation } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const listObjects = workbook.worksheets.get(0).listObjects;

            listObjects.add(1, 1, 7, 5, true);

            const firstList = listObjects.get(0);
            firstList.showTotals = true;

            firstList.listColumns.get(4).totalsCalculation = TotalsCalculation.Sum;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">List created and totals calculated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Tabloyu Biçimlendir**

İlgili veri grubunu yönetmek ve analiz etmek için, hücre aralığını bir liste nesnesine (aynı zamanda bir Excel tablosu olarak da bilinir) dönüştürmek mümkündür. Bir tablo, ilişkili verileri içeren bir dizi satır ve sütun, diğer satır ve sütunlardaki veriden bağımsız olarak yönetilir. Varsayılan olarak, tablodaki her sütunun başlık satırında filtreleme etkinleştirilir, böylece listeniz nesnesi verilerinizi hızlı bir şekilde filtreleyebilir veya sıralayabilir. Listeniz nesnesine (sayısal verilerle çalışmak için faydalı olan bir listede özel bir satır) toplam satır ekleyebilirsiniz. Bu toplam satırın her hücresi için bir toplama işlevlerinin açılır menüsünü sağlayan özel bir satır. Aspose.Cells, listelerin (veya tabloların) oluşturulması ve yönetilmesi için seçenekler sunar.

### **Liste Nesnesini Biçimlendirme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş özellik ve yöntemler sağlar. Bir çalışma sayfasında [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) oluşturmak için, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının [**listObjects**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#listObjects--) koleksiyon özelliğini kullanın. Her [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/), aslında [**ListObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/) sınıfının bir nesnesidir ve ek olarak [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/#add-number-number-number-number-boolean-) yöntemi ile bir Liste nesnesi ekleyip kapsaması gereken hücre aralığını belirler. Belirtilen hücre aralığına göre, Aspose.Cells çalışma sayfasında [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) oluşturur. Formata uygun hale getirmek için [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) sınıfının [**TableStyleType**](https://reference.aspose.com/cells/javascript-cpp/tablestyletype/) attribute'lerini kullanın.

Aşağıdaki örnek, çalışma sayfasına örnek veri ekler, bir [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) ekler ve varsayılan stilleri uygular. [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) stilleri, Microsoft Excel 2007/2010 tarafından desteklenir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // This example does not require an input file; it creates a new workbook
            const workbook = new Workbook();

            // Obtaining the reference of the default(first) worksheet
            const sheet = workbook.worksheets.get(0);

            // Obtaining Worksheet's cells collection
            const cells = sheet.cells;

            // Setting the value to the cells (converted putValue -> value)
            cells.get(1, 1).value = "Employee";
            cells.get(1, 2).value = "Quarter";
            cells.get(1, 3).value = "Product";
            cells.get(1, 4).value = "Continent";
            cells.get(1, 5).value = "Country";
            cells.get(1, 6).value = "Sale";

            cells.get(2, 1).value = "David";
            cells.get(3, 1).value = "David";
            cells.get(4, 1).value = "David";
            cells.get(5, 1).value = "David";
            cells.get(6, 1).value = "James";
            cells.get(7, 1).value = "James";
            cells.get(8, 1).value = "James";
            cells.get(9, 1).value = "James";
            cells.get(10, 1).value = "James";
            cells.get(11, 1).value = "Miya";
            cells.get(12, 1).value = "Miya";
            cells.get(13, 1).value = "Miya";
            cells.get(14, 1).value = "Miya";
            cells.get(15, 1).value = "Miya";
            cells.get(2, 2).value = 1;
            cells.get(3, 2).value = 2;
            cells.get(4, 2).value = 3;
            cells.get(5, 2).value = 4;
            cells.get(6, 2).value = 1;
            cells.get(7, 2).value = 2;
            cells.get(8, 2).value = 3;
            cells.get(9, 2).value = 4;
            cells.get(10, 2).value = 4;
            cells.get(11, 2).value = 1;
            cells.get(12, 2).value = 1;
            cells.get(13, 2).value = 2;
            cells.get(14, 2).value = 2;
            cells.get(15, 2).value = 2;

            cells.get(2, 3).value = "Maxilaku";
            cells.get(3, 3).value = "Maxilaku";
            cells.get(4, 3).value = "Chai";
            cells.get(5, 3).value = "Maxilaku";
            cells.get(6, 3).value = "Chang";
            cells.get(7, 3).value = "Chang";
            cells.get(8, 3).value = "Chang";
            cells.get(9, 3).value = "Chang";
            cells.get(10, 3).value = "Chang";
            cells.get(11, 3).value = "Geitost";
            cells.get(12, 3).value = "Chai";
            cells.get(13, 3).value = "Geitost";
            cells.get(14, 3).value = "Geitost";
            cells.get(15, 3).value = "Geitost";

            cells.get(2, 4).value = "Asia";
            cells.get(3, 4).value = "Asia";
            cells.get(4, 4).value = "Asia";
            cells.get(5, 4).value = "Asia";
            cells.get(6, 4).value = "Europe";
            cells.get(7, 4).value = "Europe";
            cells.get(8, 4).value = "Europe";
            cells.get(9, 4).value = "Europe";
            cells.get(10, 4).value = "Europe";
            cells.get(11, 4).value = "America";
            cells.get(12, 4).value = "America";
            cells.get(13, 4).value = "America";
            cells.get(14, 4).value = "America";
            cells.get(15, 4).value = "America";

            cells.get(2, 5).value = "China";
            cells.get(3, 5).value = "India";
            cells.get(4, 5).value = "Korea";
            cells.get(5, 5).value = "India";
            cells.get(6, 5).value = "France";
            cells.get(7, 5).value = "France";
            cells.get(8, 5).value = "Germany";
            cells.get(9, 5).value = "Italy";
            cells.get(10, 5).value = "France";
            cells.get(11, 5).value = "U.S.";
            cells.get(12, 5).value = "U.S.";
            cells.get(13, 5).value = "Brazil";
            cells.get(14, 5).value = "U.S.";
            cells.get(15, 5).value = "U.S.";

            cells.get(2, 6).value = 2000;
            cells.get(3, 6).value = 500;
            cells.get(4, 6).value = 1200;
            cells.get(5, 6).value = 1500;
            cells.get(6, 6).value = 500;
            cells.get(7, 6).value = 1500;
            cells.get(8, 6).value = 800;
            cells.get(9, 6).value = 900;
            cells.get(10, 6).value = 500;
            cells.get(11, 6).value = 1600;
            cells.get(12, 6).value = 600;
            cells.get(13, 6).value = 2000;
            cells.get(14, 6).value = 500;
            cells.get(15, 6).value = 900;

            // Adding a new List Object to the worksheet
            const index = sheet.listObjects.add("A1", "F15", true);

            const listObject = sheet.listObjects.get(index);

            // Adding Default Style to the table (converted setter -> property)
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium10;

            // Show Total
            listObject.showTotals = true;

            // Set the Quarter field's calculation type (converted getter/setter -> property)
            listObject.listColumns.get(1).totalsCalculation = AsposeCells.TotalsCalculation.Count;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and table added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Tabloyu ODS'ye Dönüştür](/cells/tr/javascript-cpp/convert-table-to-ods/)
- [Dış Veri Bağlantılarıyla İlgili Sorgu Tablolarını ve List Obje Bulma](/cells/tr/javascript-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Sorgu Tablosu Veri Kaynağı ile Tablo Okuma ve Yazma](/cells/tr/javascript-cpp/read-and-write-table-with-query-table-data-source/)
- [Çalışma Sayfası içinde Masa veya Liste Nesnesi Yorumunu Ayarlayın](/cells/tr/javascript-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tablolar ve Aralıklar](/cells/tr/javascript-cpp/tables-and-ranges/)
