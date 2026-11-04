---
title: Aspose.Cells for JavaScript via C++ ile Özet Tablosu Değer Alanlarını Yönetme
linktitle: Aspose.Cells for JavaScript via C++ ile Özet Tablosu Değer Alanlarını Yönetme
description: Aspose.Cells for JavaScript via C++ ile bir özet tablonun veri bölgesine temel alanların nasıl ekleneceğini, özet fonksiyonunun PivotField.Function ile nasıl değiştirileceğini ve değer alanının Satır veya Sütun eksenine nasıl yerleştirileceğini öğrenin.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, özet tablo, değer alanı, PivotField, PivotField.Function, veri alanı, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /tr/javascript-cpp/manage-value-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Veri Bölgesine Alan Ekleme
Bir temel alanı veri (değer) bölgesine eklemek, bir özet tablonun kaynak verilerini nasıl toplulaştıracağını belirlemenin ilk adımıdır. Aspose.Cells for JavaScript via C++, `PivotFieldType.Data` sabitini ve kaynak sütun adını kabul eden `pivotTable.addFieldToArea(PivotFieldType.Data, "ColumnName")` aşırı yüklemesini sunar. Bir alan veri bölgesine eklendiğinde, API onu alanların eklendiği sıraya göre `pivotTable.getDataFields()` koleksiyonu üzerinden sunar. Varsayılan olarak, sayısal bir kaynak sütun `ConsolidationFunction.Sum` ile, sayısal olmayan bir kaynak sütun ise `Count` ile özetlenir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const headers = ["Category", "Item", "Year", "Amount"];
            for (let j = 0; j < headers.length; j++) {
                worksheet.cells.get(0, j).value = headers[j];
            }
            const data = [
                ["Fruit", "Apple", 2020, 100],
                ["Fruit", "Apple", 2021, 150],
                ["Fruit", "Banana", 2020, 80],
                ["Fruit", "Banana", 2021, 90],
                ["Vegetable", "Carrot", 2020, 50],
                ["Vegetable", "Carrot", 2021, 60],
                ["Vegetable", "Daikon", 2020, 40],
                ["Vegetable", "Daikon", 2021, 45]
            ];
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    worksheet.cells.get(i + 1, j).value = data[i][j];
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_drag.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Özet Fonksiyonunu Değiştirme
Bir alan veri bölgesine eklendiğinde, Aspose.Cells onu `pivotTable.getDataFields()` tarafından döndürülen `PivotField` nesnesi üzerinden sunar. Her `PivotField`, `ConsolidationFunction` türünde yazılabilir bir `function` özelliğine sahiptir ve bu özellik, ilgili alanın dayandığı değerlere uygulanan toplulaştırmayı denetler. `ConsolidationFunction`, `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` ve `Varp` üyelerinden oluşan bir numaralandırma türüdür — ilk altısı gerçek dünyadaki kullanım senaryolarının büyük çoğunluğunu karşılar, son dördü ise varyans analizi için yararlı istatistiksel toplulaştırmalardır.

{{% alert color="primary" %}}
`function` değerini değiştirmek yalnızca toplulaştırmayı etkiler; kaynak sütun ve özet tablonun satır/sütun yapısı değiştirilmez. Mevcut bir veri alanının toplulaştırma işlevini değiştirmek için `pivotTable.getDataFields()[i].setFunction(ConsolidationFunction.X)` çağrısını yapın, ardından özet tabloyu yeniden hesaplamak ve işlemek için `pivotTable.calculateData()` çağrısını yapın.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const headers = ["Category", "Item", "Year", "Amount"];
            for (let j = 0; j < headers.length; j++) {
                worksheet.cells.get(0, j).value = headers[j];
            }
            const data = [
                ["Fruit", "Apple", 2020, 100],
                ["Fruit", "Apple", 2021, 150],
                ["Fruit", "Banana", 2020, 80],
                ["Fruit", "Banana", 2021, 90],
                ["Vegetable", "Carrot", 2020, 50],
                ["Vegetable", "Carrot", 2021, 60],
                ["Vegetable", "Daikon", 2020, 40],
                ["Vegetable", "Daikon", 2021, 45]
            ];
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    worksheet.cells.get(i + 1, j).value = data[i][j];
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const countField = pivotTable.dataFields.get(1);
            countField.function = AsposeCells.ConsolidationFunction.Count;
            pivotTable.calculateData();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_function.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme
Bir özet tablo iki veya daha fazla veri alanı içerdiğinde, Aspose.Cells `pivotTable.getValuesField()` adlı ek bir sanal alan sunar. Bu sanal alan, veri bölgesinde bulunan tüm veri alanlarının toplulaştırmasını temsil eder. Bunu temel bir özet tablo alanı olarak Satır veya Sütun bölgesine sürükleyebilirsiniz; bu, birden fazla ölçütü yan yana yerleştirmek için yararlıdır.

{{% alert color="primary" %}}
`pivotTable.getValuesField()` tarafından döndürülen sanal değerler alanı, hiç değer alanı bulunmadığında veya yalnızca bir değer alanı bulunduğunda çalışmaz.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            const headers = ["Category", "Item", "Year", "Amount"];
            for (let j = 0; j < headers.length; j++) {
                cells.get(0, j).value = headers[j];
            }
            const data = [
                ["Fruit", "Apple", 2020, 100],
                ["Fruit", "Apple", 2021, 150],
                ["Fruit", "Banana", 2020, 80],
                ["Fruit", "Banana", 2021, 90],
                ["Vegetable", "Carrot", 2020, 50],
                ["Vegetable", "Carrot", 2021, 60],
                ["Vegetable", "Daikon", 2020, 40],
                ["Vegetable", "Daikon", 2021, 45]
            ];
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    cells.get(i + 1, j).value = data[i][j];
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.dataFields.get(1).function = AsposeCells.ConsolidationFunction.Count;
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, pivotTable.valuesField.name);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_plot.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

{{< app/cells/assistant language="javascript-cpp" >}}