---
title: Установка границы диапазона с помощью JavaScript через C++
linktitle: Установить границу диапазона
type: docs
weight: 600
url: /ru/javascript-cpp/set-range-border/
---

## **Возможные сценарии использования**  
Когда нужно установить границу для диапазона, не обязательно делать это для каждой ячейки отдельно. Можно установить границу для всего диапазона. Script через C++ предлагает эту возможность.  
Этот пример кода показывает, как с помощью Script через C++ установить границу диапазона.  

## **Установить границу диапазона в Excel**  
Чтобы установить границу диапазона в Excel, выполните следующие шаги:  
1. Выберите диапазон ячеек, к которым вы хотите применить границу.  
2. На вкладке "Домой" ленты найдите группу "Шрифт".  
3. Внутри группы "Шрифт" нажмите на кнопку "Границы".  
<br>  
<img src="border.png" />  
4. Выберите тип границы, который вы хотите применить из вариантов в выпадающем меню. Вы можете выбрать из предустановленных стилей границы или настроить свою собственную границу.  
5. Как только вы выбрали желаемый стиль границы, она будет применена к выбранному диапазону ячеек.  

## **Установка границы диапазона с помощью Script через C++**  
Этот пример показывает, как:  

1. Создать книгу.  
2. Добавьте данные в ячейки на первом листе.  
3. Создайте [**Range**](https://reference.aspose.com/cells/javascript-cpp/range).  
4. Установите внутреннюю границу диапазона.  
5. Установите внешнюю границу диапазона.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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
            // Instantiate a new workbook
            const workbook = new Workbook();
            // Obtaining the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
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

            // Create a range (A1:C5).
            const range = cells.createRange("A1", "C5");

            // set inner border of range
            const innerColor = workbook.createCellsColor();
            innerColor.color = AsposeCells.Color.Red;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Vertical,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };
            innerColor.color = AsposeCells.Color.Green;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Horizontal,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };

            // set outer border of range
            const outerColor = workbook.createCellsColor();
            outerColor.color = AsposeCells.Color.Blue;
            range.outlineBorders = {
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: outerColor
            };

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
