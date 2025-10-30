---
title: Pivot Tablosunda Hesaplanmış Alan Ekleme
type: docs
weight: 130
url: /tr/javascript-cpp/add-calculated-field-in-pivot-table/
description: Aspose.Cells for JavaScript ile C++ kullanarak pivot tabloya hesaplanmış alan nasıl eklenir.
keywords: Aspose.Cells for JavaScript ile C++ kullanarak Excel, Excel JavaScript kütüphanesi, pivot tabloya hesaplanmış alan ekleme
---

## **Olası Kullanım Senaryoları**
Bilgisine sahip olduğunuz verilere dayalı olarak bir pivot tablosu oluşturduğunuzda, içindeki verilerin istediğiniz gibi olmadığını fark edersiniz. İstediğiniz veri, bu orijinal verilerin bir kombinasyonudur. Örneğin, veriden önce verilerin çıkarılması, çarpılması ve bölünmesi gerekebilir. Bu durumda, bir hesaplanmış alan oluşturmanız ve hesaplama için ilgili formülü ayarlamanız gerekir. Daha sonra hesaplanmış alanda bazı istatistikler ve diğer işlemleri gerçekleştirin. 

## **Excel'de Pivot Tablosuna Hesaplanmış Alan Eklemek**
Excel'de bir PivotTable'a hesaplanmış bir alan eklemek için şu adımları izleyin:

1. Bir hesaplanmış alan eklemek istediğiniz PivotTable'ı seçin. 
2. Kuruluş sekmesine gidin ve üzerinde PivotTable Analizi olan sekmeyi seçin.
3. "Alanlar, Öğeler ve Kümeler" üzerine tıklayın ve ardından açılır menüden "Hesaplanmış Alan"ı seçin.
4. "Ad" alanına hesaplanmış alan için bir ad girin.
5. "Formül" alanına, kullanmak istediğiniz PivotTable alan adları ve matematiksel operatörleri kullanarak gerçekleştirmek istediğiniz hesaplama için formülü girin. 
<br>
<img src="1.png" width=80% />
6. Hesaplanmış alan oluşturmak için "tamam"a tıklayın.
7. Yeni hesaplanmış alan, Değerler bölümü altında PivotTable Alan Listesinde görünecektir.
8. Hesaplanmış alanı PivotTable'ın Değerler bölümüne sürükleyerek hesaplanmış değerleri görüntüleyin.
<br>
<img src="2.png" width=80% />

## ** Aspose.Cells for JavaScript ile C++ Kütüphanesi kullanarak Pivot Tabloya hesaplanmış alan nasıl eklenir**
Aspose.Cells for JavaScript kullanarak Excel dosyasına hesaplanmış alan ekleyin. Lütfen aşağıdaki örnek kodu inceleyin. Örnek kodu çalıştırdıktan sonra, hesaplanmış alan içeren bir pivot tablo çalışma sayfasına eklenir.
1. Orijinal verileri ayarlayın ve bir pivot tablosu oluşturun. 
2. Mevcut PivotField'a göre hesaplanmış alanı oluşturun.
3. Hesaplanmış alanı veri alanına ekleyin. 
4. Son olarak, çalışma kitabını [çıktı XLSX](out.xlsx) formatında kaydeder. 

## **Örnek Kod**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldType, Utils } = AsposeCells;

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

            // Obtain the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";
            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";
            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;
            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Adding a PivotTable to the worksheet (converted getPivotTables -> pivotTables)
            const i = ws.pivotTables.add("=A1:C5", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(PivotFieldType.Row, 0);
            // Adding a calculated field to PivotTable and drag it to data area.
            pivotTable.addCalculatedField("total", "=Count*Price", true);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
