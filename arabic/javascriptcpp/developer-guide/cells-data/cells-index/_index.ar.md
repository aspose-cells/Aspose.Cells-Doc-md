---
title: الحصول على فهرس الخلايا
type: docs
weight: 600
url: /ar/javascript-cpp/get-cells-index/
description: تعلم كيف تحصل على الصف أو العمود باستخدام اسم الصف، العمود، أو الخلايا. حول اسم الخلية إلى فهرس الصف والعمود التوقيتي الصفري باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: الحصول على فهرس الصف والعمود بواسطة اسم الخلية، الحصول على فهرس العمود بواسطة اسم العمود، الحصول على فهرس الصف بواسطة اسم الصف، الحصول على الفهرس بواسطة اسم الخلية. 
---

{{% alert color="primary" %}}
العرض الافتراضي لإكسل هو إعادة النظر في نمط A1 المرجعي، حيث يتم تعريف كل عمود بأحرف A وB وC...، وتسمى الخلايا A1 وB2 وC3... وهكذا.
قد ترغب في معرفة الصف والعمود الذي يحتوي هذه الخلية فيه.

{{% /alert %}}


## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج إلى تعديل بيانات معينة على ورقة العمل بواسطة مؤشر الصف والعمود فقط، تحتاج إلى معرفة مؤشر الصف والعمود لتلك الخلية المحددة. 
Aspose.Cells for Javaسكريبت عبر C++ يعرض هذه الميزة للحصول على فهرس الصف والعمود بواسطة اسم الصف والعمود والخلية. 
Aspose.Cells for Javaسكريبت عبر C++ يوفر الخصائص والطرق التالية لمساعدتك على تحقيق أهدافك.
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#rowNameToIndex-string-)

ملاحظة: الفهرسة تعتمد على الصفر في Aspose.Cells for Javaسكريبت عبر C++، لكن معرف الصف يبدأ من واحد في MS Excel.

## **الحصول على مؤشرات الخلايا باستخدام Aspose.Cells for Javaسكريبت عبر C++**
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل وإضافة بعض البيانات.
1. العثور على الخلية المحددة في الورقة العمل الأولى.
1. الحصول على مؤشر الصف والعمود بواسطة اسم الخلية.
1. الحصول على مؤشر العمود بواسطة اسم العمود.
1. الحصول على مؤشر الصف بواسطة اسم الصف.

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
