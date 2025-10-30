---
title: Pivot Öğesinin Mutlak Konumunu Belirtme
type: docs
weight: 50
url: /tr/javascript-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Bazen, kullanıcı pivot öğelerinin mutlak konumunu belirtmek ister; Aspose.Cells for JavaC++ API, kullanıcı gereksinimlerini karşılamak için birkaç yeni özellik ve bir metod sağlar.

- Tüm ebeveyn düğümün bağımsızında PivotItems içindeki pozisyon indeksini belirlemek için kullanılabilecek [**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-) özelliği eklendi. - Aynı ebeveyn düğümdeki PivotItems içindeki pozisyon indeksini belirlemek için kullanılabilecek [**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-) özelliği eklendi.
- PivotItem'ı yukarı veya aşağı hareket ettirmek için [**PivotItem.move**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-) metodu eklendi, burada sayım değeri tarafından yapılacak PivotItem'ın yukarı veya aşağı hareket etme sayısını belirtir; Eğer sayım değeri sıfırdan küçükse, öğe yukarı hareket ettirilecek, eğer sayım değeri sıfırdan büyükse, PivotItem aşağı hareket eder, Boolean türünde olan isSameParent parametresi, hareket işleminin aynı ebeveyn düğümünde gerçekleştirilip gerçekleştirilmeyeceğini belirtir.
- *PivotItem.move(int count)* metodunun kullanımı kullanımdan kaldırıldı, bunun yerine yeni eklenen [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-) metodunun kullanılması önerilir.

{{% /alert %}}

Aşağıdaki örnek kod, bir Pivot Tablo oluşturur ve ardından aynı ebeveyn düğümdeki Pivot Öğelerinin konumlarını belirtir. Referansınız için [kaynak Excel](5112632.xlsx) ve [çıktı Excel](5112619.xlsx) dosyalarını indirebilirsiniz. Çıktı Excel dosyasını açarsanız, Pivot Öğesi "4H12"'nin "K11" üst ebeveynindeki 0. pozisyonda olduğunu ve "DIF400"'in 3. pozisyonda olduğunu göreceksiniz. Benzer şekilde, CA32 1. pozisyonda ve AAA3 2. pozisyonda.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Example</title>
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
        const { Workbook, SaveFormat, PivotFieldType, PivotFieldSubtotalType } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Add pivot worksheet and get data worksheet
            const wsPivot = workbook.worksheets.add("pvtNew Hardware");
            const wsData = workbook.worksheets.get("New Hardware - Yearly");

            // Get the pivottables collection for the pivot sheet
            const pivotTables = wsPivot.pivotTables;

            // Add PivotTable to the worksheet
            const index = pivotTables.add("='New Hardware - Yearly'!A1:D621", "A3", "HWCounts_PivotTable");

            // Get the PivotTable object
            const pvtTable = pivotTables.get(index);

            // Add vendor row field
            pvtTable.addFieldToArea(PivotFieldType.Row, "Vendor");

            // Add item row field
            pvtTable.addFieldToArea(PivotFieldType.Row, "Item");

            // Add data field
            pvtTable.addFieldToArea(PivotFieldType.Data, "2014");

            // Turn off the subtotals for the vendor row field
            const pivotField = pvtTable.rowFields.get("Vendor");
            pivotField.subtotals = PivotFieldSubtotalType.None;

            // Turn off grand total
            pvtTable.columnGrand = false;

            /*
             * Please call the PivotTable.refreshData() and PivotTable.calculateData()
             * before using PivotItem.setPosition,
             * PivotItem.setPositionInSameParentNode and PivotItem.move methods.
            */
            pvtTable.refreshData();
            pvtTable.calculateData();

            pvtTable.rowFields.get("Item").pivotItems.get("4H12").positionInSameParentNode = 0;
            pvtTable.rowFields.get("Item").pivotItems.get("DIF400").positionInSameParentNode = 3;

            /* 
             * As a result of using PivotItem.setPositionInSameParentNode,
             * it will change the original sort sequence.
             * So when you use PivotItem.setPositionInSameParentNode in another parent node.
             * You need call the method named "calculateData" again. 
            */
            pvtTable.calculateData();

            pvtTable.rowFields.get("Item").pivotItems.get("CA32").positionInSameParentNode = 1;
            pvtTable.rowFields.get("Item").pivotItems.get("AAA3").positionInSameParentNode = 2;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Lütfen dikkat, [**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-), [**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-) özellikleri ve [**PivotItem.move**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-) metodu kullanmadan önce PivotTable.RefreshData ve PivotTable.CalculateData yöntemlerini çağırmak gereklidir.

{{% /alert %}}
