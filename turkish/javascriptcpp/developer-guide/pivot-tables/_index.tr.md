---
title: Pivot Tablo Ekle
linktitle: Pivot Tabloları
type: docs
weight: 160
url: /tr/javascript-cpp/create-pivot-table/
description: Excel elek tablo dosyalarının pivot tablolarını oluşturun ve biçimlendirin.
---

## **Pivot Tablosu Oluştur**

C++ aracılığıyla Aspose.Cells for JavaScript kullanarak elektronik tablolarınıza pivot tablolarını programlı olarak eklemek mümkündür.

### **Pivot Tablosu Nesne Modeli**

C++ aracılığıyla Aspose.Cells for JavaScript, pivot tablolarını oluşturmak ve kontrol etmek için özel bir sınıf seti sağlar. Bu sınıflar, [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) nesnelerini oluşturmak ve ayarlamak için kullanılır, bunlar pivot tablosunun yapıtaşlarıdır. Nesneler şunlardır:

- [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield), bir [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) içindeki bir alanı temsil eder.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection), [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) içindeki tüm [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) nesnelerinin bir koleksiyonunu temsil eder.
- [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable), bir çalışma sayfasındaki bir PivotTable'ı temsil eder.
- [**PivotTableCollection**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection), bir çalışma sayfasındaki tüm [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) nesnelerinin bir koleksiyonunu temsil eder.

### **Aspose.Cells Kullanarak Basit Bir Pivot Tablosu Oluşturma**

1. [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) nesnesinin [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) metodu kullanılarak bir çalışma sayfasına veri ekleyin.
   Bu veri, pivot tablosunun veri kaynağı olarak kullanılacaktır.
2. Çağrılan [**add**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#add-string-string-string-) metoduna (Worksheet nesnesinde kapsüllenmiş olan) [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) koleksiyonuna bir pivot tablosu ekleyin.
3. PivotTable endeksini geçerek [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) koleksiyonundan yeni [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) nesnesine erişin.
4. Pivot tablosunu yönetmek için yukarıda açıklanan [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) nesnelerinden herhangi birini kullanın.

Örnek kodu çalıştırdıktan sonra bir pivot tablosu çalışma sayfasına eklenir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Pivot Table Example</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                // Instantiate a new Workbook object
                const workbook = new Workbook();

                // Obtaining the reference of the newly added worksheet
                const sheetIndex = workbook.worksheets.add();
                const sheet = workbook.worksheets.get(sheetIndex);
                const cells = sheet.cells;

                // Setting the value to the cells
                let cell = cells.get("A1");
                cell.value = "Sport";
                cell = cells.get("B1");
                cell.value = "Quarter";
                cell = cells.get("C1");
                cell.value = "Sales";

                cell = cells.get("A2");
                cell.value = "Golf";
                cell = cells.get("A3");
                cell.value = "Golf";
                cell = cells.get("A4");
                cell.value = "Tennis";
                cell = cells.get("A5");
                cell.value = "Tennis";
                cell = cells.get("A6");
                cell.value = "Tennis";
                cell = cells.get("A7");
                cell.value = "Tennis";
                cell = cells.get("A8");
                cell.value = "Golf";

                cell = cells.get("B2");
                cell.value = "Qtr3";
                cell = cells.get("B3");
                cell.value = "Qtr4";
                cell = cells.get("B4");
                cell.value = "Qtr3";
                cell = cells.get("B5");
                cell.value = "Qtr4";
                cell = cells.get("B6");
                cell.value = "Qtr3";
                cell = cells.get("B7");
                cell.value = "Qtr4";
                cell = cells.get("B8");
                cell.value = "Qtr3";

                cell = cells.get("C2");
                cell.value = 1500;
                cell = cells.get("C3");
                cell.value = 2000;
                cell = cells.get("C4");
                cell.value = 600;
                cell = cells.get("C5");
                cell.value = 1500;
                cell = cells.get("C6");
                cell.value = 4070;
                cell = cells.get("C7");
                cell.value = 5000;
                cell = cells.get("C8");
                cell.value = 6430;

                const pivotTables = sheet.pivotTables;

                // Adding a PivotTable to the worksheet
                const index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

                // Accessing the instance of the newly added PivotTable
                const pivotTable = pivotTables.get(index);

                // Unshowing grand totals for rows.
                pivotTable.rowGrand = false;

                // Dragging the first field to the row area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);

                // Dragging the second field to the column area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 1);

                // Dragging the third field to the data area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);

                // Saving the Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'CreatePivotTable_out.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created successfully! Click the download link to get the file.</p>';
            });
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Veri kaynağı olarak bir hücre aralığı atadığınızda, aralığın sol üstten sağ alta gitmesi gerekir. Örneğin, "A1:C3" geçerlidir ancak "C3:A1" geçerli değildir.

{{% /alert %}}
