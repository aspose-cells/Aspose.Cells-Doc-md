---
title: Hücrelerin Endeksini Alın
type: docs
weight: 600
url: /tr/javascript-cpp/get-cells-index/
description: Satır veya sütunları isimleriyle nasıl alacağınızı öğrenin, ayrıca satır, sütun veya hücre isimlerini adresleye çevirmeyi öğrenin. Hücrenin adını, 0 tabanlı satır ve sütun indeksine dönüştürmek için C++ ile Script kullanın.
keywords: Hücrenin adı ile satır ve sütun endeksini alın, sütunun adı ile sütun endeksini alın, satırın adı ile satır endeksini alın, hücrenin adı ile endeksini alın. 
---

{{% alert color="primary" %}}
Excel'in varsayılan görünümü A1 stili referanstır, her sütun A, B, C..... şeklinde adlandırılır ve hücreler A1, B2, C3... ve benzeri şekilde adlandırılır.
Bu hücrenin hangi satır ve sütun olduğunu bilmek isteyebilirsiniz.

{{% /alert %}}


## **Olası Kullanım Senaryoları**
Yalnızca belirli bir veriyi çalışsayısında satır ve sütun endeksi tarafından yönlendirmeniz gerektiğinde, o belirli hücrenin sütun ve satır endekslerini bilmeniz gerekir. 
Aspose.Cells for JavaScript C++ aracılığıyla satır ve sütun adlarına göre satır ve sütun dizinleri alma özelliği sunar. 
Aspose.Cells for JavaScript C++ aşağıdaki özellikleri ve yöntemleri sağlayarak hedeflerinize ulaşmanıza yardımcı olur.
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#rowNameToIndex-string-)

Not: Aspose.Cells for JavaScript C++'te indeksleme sıfır tabanlıdır, ancak MS Excel'de Satırın kimliği bir tabanlıdır.

## **Aspose.Cells for JavaScript C++ kullanarak Hücreler Dizini Alın.**
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturun ve bazı verileri ekleyin.
1. İlk çalışsayfadaki belirli hücreyi bulun.
1. Hücrenin adına göre Satır dizinini ve Sütun dizinini alın.
1. Sütunun adına göre Sütun dizinini alın.
1. Satırın adına göre Satır dizinini alın.

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
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();

            // Access cells of the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            let cell = cells.get("A1");
            cell.putValue("Fruit");
            cell = cells.get("B1");
            cell.putValue("Count");
            cell = cells.get("C1");
            cell.putValue("Price");

            cell = cells.get("A2");
            cell.putValue("Apple");
            cell = cells.get("A3");
            cell.putValue("Mango");
            cell = cells.get("A4");
            cell.putValue("Blackberry");
            cell = cells.get("A5");
            cell.putValue("Cherry");

            cell = cells.get("B2");
            cell.putValue(5);
            cell = cells.get("B3");
            cell.putValue(3);
            cell = cells.get("B4");
            cell.putValue(6);
            cell = cells.get("B5");
            cell.putValue(4);

            cell = cells.get("C2");
            cell.putValue(5);
            cell = cells.get("C3");
            cell.putValue(20);
            cell = cells.get("C4");
            cell.putValue(30);
            cell = cells.get("C5");
            cell.putValue(60);

            // Find the cell containing "Blackberry"
            const curr = cells.find("Blackberry", null);

            // Current cell name
            const currentCellName = curr.name;

            // get row and column index of current cell
            const rowCol = CellsHelper.cellNameToIndex(curr.name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];

            // get column name by column index
            const columnName = CellsHelper.columnIndexToName(currCol);

            // get row name by row index
            const rowName = CellsHelper.rowIndexToName(currRow);

            // get column index by column name
            const columnIndex = CellsHelper.columnNameToIndex(columnName);

            // get row index by row name
            const rowIndex = CellsHelper.rowNameToIndex(rowName);

            const outputs = [];
            outputs.push("Current Cell Name: " + currentCellName);
            outputs.push("Row Index: " + currRow + "  Column Index: " + currCol);
            outputs.push("Column Name: " + columnName + " Row Name: " + rowName);
            outputs.push("Column Index: " + columnIndex + " Row Index: " + rowIndex);
            outputs.push("columnIndex == currCol: " + (columnIndex == currCol));
            outputs.push("rowIndex == currRow: " + (rowIndex == currRow));

            document.getElementById('result').innerHTML = '<pre>' + outputs.join('\n') + '</pre>';

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```
