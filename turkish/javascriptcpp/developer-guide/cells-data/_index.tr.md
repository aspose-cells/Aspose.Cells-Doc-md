---
title: Excel dosyalarının verilerini yönetme
linktitle: Hücre Verileri
type: docs
weight: 110
url: /tr/javascript-cpp/view-and-edit-excel-data/
description: Bu makale, Aspose.Cells kütüphanesi kullanarak Excel dosyasındaki verileri görüntüleme ve düzenleme yöntemlerini anlatır.
keywords: Aspose.Cells JavaScript ile C++ aracılığıyla, Excel dosyası verilerini yönetme, veri ekleme, veriyi alma, Veri ekleme verimliliğini artırma, hücre verilerini yönetme, hücreleri güncelleme, hücreleri alma, hücreleri ekleme yöntemleri
---

{{% alert color="primary" %}}

 [Bir Çalışma Sayfasının Hücrelerine Erişme](/cells/tr/javascript-cpp/accessing-cells-of-a-worksheet/) konusunda, bir çalışma sayfasında hücrelere erişmek için temel yaklaşımları tartışmıştık. Bu makale, bu yaklaşımlardan birini kullanarak hücrelere farklı türde veriler eklemektedir.

{{% /alert %}}

## **Hücrelere Veri Ekleme**

Aspose.Cells for JavaC++ aracılığıyla Script, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfıyla temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ise bir [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonunu sağlar. [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonundaki her öğe, bir [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfı nesnesini temsil eder.

Aspose.Cells, geliştiricilerin [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) metodunu çağırarak hücrelere veri eklemesine olanak tanır. Aspose.Cells, farklı veri türlerini hücrelere eklemeyi sağlayan [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) metodunun aşırı yüklenmiş sürümlerini de sunar. Bu aşırı yüklenmiş metodları kullanarak, hücreye Boolean, dize, double, tam sayı veya tarih/zaman gibi değerler ekleyebilirsiniz.

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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding values to cells
            const cells = worksheet.cells;
            const cellA1 = cells.get("A1");
            cellA1.value = "Hello World";

            const cellA2 = cells.get("A2");
            cellA2.value = 20.5;

            const cellA3 = cells.get("A3");
            cellA3.value = 15;

            const cellA4 = cells.get("A4");
            cellA4.value = true;

            const cellA5 = cells.get("A5");
            cellA5.value = new Date();

            // Setting the display format of the date
            let style = cellA5.style;
            style.number = 15;
            cellA5.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **Verimliliği Nasıl Arttırılır**

Eğer [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) metodunu kullanarak büyük miktarda veri bir çalışma sayfasına yerleştiriyorsanız, verileri önce satır satır, sonra sütun sütun ekmek uygulamanız, uygulamanızın verimliliğini büyük ölçüde artıracaktır.

## **Hücrelerden Veri Almak**

Aspose.Cells for JavaScript C++ aracılığıyla, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) Microsoft Excel dosyasını temsil eden bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, dosyadaki çalışma sayfalarına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, bir [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonu sunar. [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının bir nesnesini temsil eder.

[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfı, geliştiricilerin hücrelerin değerlerini veri türlerine göre almak için kullanabilecekleri birkaç özellik sağlar. Bu özellikler şunları içerir:

- [**stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--): hücrenin dize değerini döndürür.
- [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--): hücrenin çift değerini döndürür.
- [**boolValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#boolValue--): hücrenin boolean değerini döndürür.
- [**dateTimeValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#dateTimeValue--): hücrenin tarih/zaman değerini döndürür.
- [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--): hücrenin float değerini döndürür.
- [**intValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#intValue--): hücrenin tam sayı değerini döndürür.

Bir alan doldurulmadığında, [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--) veya [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--) ile işaretlenmiş hücreler istisna fırlatır.

Bir hücrede bulunan verinin tipi, [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) metodu kullanılarak da kontrol edilebilir. Aslında, [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) metodu, aşağıda listelenen önceden tanımlı değerlere sahip [**CellValueType**](https://reference.aspose.com/cells/javascript-cpp/cellvaluetype) enum'ına dayanmaktadır:

|**Hücre Değer Türleri**|**Açıklama**|
| :- | :- |
|IsBool| Hücre değerinin Boolean olduğunu belirtir.
|IsDateTime| Hücre değerinin tarih/saat olduğunu belirtir.
|IsNull| Boş bir hücreyi temsil eder.
|IsNumeric| Hücre değerinin sayısal olduğunu belirtir.
|IsString| Hücre değerinin bir dize olduğunu belirtir.
|IsUnknown| Hücre değerinin bilinmeyen olduğunu belirtir.

Yukarıdaki önceden tanımlanmış hücre değeri türlerini, her hücrede bulunan veri türüyle karşılaştırmak için kullanabilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Cell Values Example</h1>
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

            // Opening an existing workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing first worksheet
            const worksheet = workbook.worksheets.get(0);

            var cells = worksheet.cells;
            var maxRow = cells.maxRow;
            var maxColumn = cells.maxColumn;
            let logs = [];
            for (let i = 0; i <= maxRow; i++) {
                for (let j = 0; j <= maxColumn; j++) 
                {
                    const cell1 = cells.get(i, j);
                    if (!cell1) {
                        continue;
                    }
                    // Variables to store values of different data types
                    let stringValue;
                    let doubleValue;
                    let boolValue;
                    let dateTimeValue;

                    // Passing the type of the data contained in the cell for evaluation
                    switch (cell1.type) {
                        // Evaluating the data type of the cell data for string value
                        case AsposeCells.CellValueType.IsString:
                            stringValue = cell1.stringValue;
                            console.log("String Value: " + stringValue);
                            logs.push("String Value: " + stringValue);
                            break;

                        // Evaluating the data type of the cell data for double value
                        case AsposeCells.CellValueType.IsNumeric:
                            doubleValue = cell1.doubleValue;
                            console.log("Double Value: " + doubleValue);
                            logs.push("Double Value: " + doubleValue);
                            break;

                        // Evaluating the data type of the cell data for boolean value
                        case AsposeCells.CellValueType.IsBool:
                            boolValue = cell1.boolValue;
                            console.log("Bool Value: " + boolValue);
                            logs.push("Bool Value: " + boolValue);
                            break;

                        // Evaluating the data type of the cell data for date/time value
                        case AsposeCells.CellValueType.IsDateTime:
                            dateTimeValue = cell1.dateTimeValue;
                            console.log("DateTime Value: " + dateTimeValue);
                            logs.push("DateTime Value: " + dateTimeValue);
                            break;

                        // Evaluating the unknown data type of the cell data
                        case AsposeCells.CellValueType.IsUnknown:
                            stringValue = cell1.stringValue;
                            console.log("Unknown Value: " + stringValue);
                            logs.push("Unknown Value: " + stringValue);
                            break;

                        // Terminating the type checking of type of the cell data is null
                        case AsposeCells.CellValueType.IsNull:
                            break;
                    }
                }
            }

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! See console for detailed cell values.</p><pre>${logs.join("\n")}</pre>`;
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Çalışma sayfaları üzerinde çalışırken kullanıcılar hücrelere farklı veri türleri ekleyebilir. Bu veri türleri Boolean, tam sayı, ondalıklı sayı, metin veya tarih/zaman değerleri içerebilir. Aspose.Cells ile, hücrelerin veri türlerine göre uygun değerleri alabilirsiniz.

{{% /alert %}}

## **Gelişmiş Konular**
- [Bir Çalışma Sayfasının Hücrelerine Erişme](/cells/tr/javascript-cpp/accessing-cells-of-a-worksheet/)
- [Metin Sayı Değerini Sayıya Dönüştürme](/cells/tr/javascript-cpp/convert-text-numeric-data-to-number/)
- [Alt Toplamlar Oluşturma](/cells/tr/javascript-cpp/creating-subtotals/)
- [Veri Filtreleme](/cells/tr/javascript-cpp/data-filtering/)
- [Veri Sıralama](/cells/tr/javascript-cpp/sort-data-of-excel/)
- [Veri Doğrulama](/cells/tr/javascript-cpp/data-validation/)
- [Veri Bulma veya Arama](/cells/tr/javascript-cpp/find-or-search-data/)
- [Biçimlendirmeyle ve biçimlendirme olmadan Hücre Dize Değerini Alın](/cells/tr/javascript-cpp/get-cell-string-value-with-and-without-formatting/)
- [Hücre İçinde HTML Zengin Metin Ekleme](/cells/tr/javascript-cpp/adding-html-rich-text-inside-the-cell/)
- [Excel veya OpenOffice'de Hyperlinkler Eklemek](/cells/tr/javascript-cpp/insert-hyperlinks-to-excel/)
- [Numaralandırıcıları Nerede ve Nasıl Kullanılır](/cells/tr/javascript-cpp/how-and-where-to-use-enumerators/)
- [Hücre Değeri Genişliğini ve Yüksekliğini Piksel Birimiyle Ölçme](/cells/tr/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Birden Fazla İş Parçacığında Aynı Anda Hücre Değerleri Okuma](/cells/tr/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Hücre adı ve satır/sütun indeksi arasında dönüşüm](/cells/tr/javascript-cpp/names-and-indices/)
- [Veri İlk Olarak Satır, Sonra Sütun Olarak Doldurma](/cells/tr/javascript-cpp/populate-data-first-by-row-then-by-column/)
- [Hücre Değerinin veya Aralığın Ön Eklemesini Koruma](/cells/tr/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Zengin Metnin Kısımlarına Erişme ve Güncelleme](/cells/tr/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
