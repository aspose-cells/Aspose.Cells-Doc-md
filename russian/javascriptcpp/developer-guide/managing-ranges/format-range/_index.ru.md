---
title: Форматирование диапазонов с помощью JavaScript через C++
linktitle: Форматирование диапазонов
type: docs
weight: 105
url: /ru/javascript-cpp/how-to-format-a-range/
description: Узнайте, как форматировать диапазон ячеек в Excel с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**  
Когда вам необходимо применить стиль к диапазону, вы можете использовать форматирование диапазона.  

## **Как форматировать диапазон в Excel**  

Для форматирования диапазона ячеек в Excel вы можете использовать встроенные варианты форматирования, предоставленные Excel. Вот как можно форматировать диапазон ячеек непосредственно в Excel:  

1. Откройте Excel и книгу, которая содержит диапазон, который вы хотите отформатировать.  

2. Выберите диапазон ячеек, который вы хотите отформатировать. Вы можете щелкнуть и перетащить, чтобы выбрать диапазон, или вы можете использовать комбинации клавиш, такие как Shift + стрелки, чтобы расширить выбор.  

3. После выбора диапазона щелкните правой кнопкой мыши по выбранному диапазону и выберите "Формат ячеек" в контекстном меню. В качестве альтернативы, вы можете перейти на вкладку "Домой" на ленте Excel, щелкнуть на выпадающем списке "Формат" в группе "Ячейки" и выбрать "Формат ячеек".  

4. Появится диалоговое окно "Формат ячеек". Здесь вы можете выбрать различные варианты форматирования для применения к выбранному диапазону. Например, вы можете изменить стиль шрифта, размер шрифта, цвет шрифта, формат чисел, границы, цвет фона и т. д. Исследуйте различные вкладки в диалоговом окне, чтобы получить доступ к различным вариантам форматирования.  

5. После внесения желаемых изменений форматирования нажмите кнопку "OK", чтобы применить форматирование к выбранному диапазону.  

## **Как отформатировать диапазон с использованием JavaScript**  

Для форматирования диапазона с помощью Aspose.Cells for JavaScript через C++, вы можете использовать следующие методы:  
1. [Range.applyStyle(style, flag)](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.style](https://reference.aspose.com/cells/javascript-cpp/range/#style-style-)  
3. [Range.style](https://reference.aspose.com/cells/javascript-cpp/range/#style-style-)  

## **Образец кода**  
В этом примере мы создаем книгу Excel, добавляем некоторые образцовые данные, получаем доступ к первому рабочему листу и определяем два диапазона ("A1:C3" и "A4:C5"). Затем создаем новые стили, устанавливаем различные параметры форматирования (например, цвет шрифта, жирный) и применяем стиль к диапазону. Наконец, сохраняем книгу в новый файл.  
<br>  
![todo:image_alt_text](format-range.png)  

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
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

            // Access the worksheet (already have ws, but keep variable for clarity)
            const worksheet = workbook.worksheets.get(0);

            // Define the range
            const range = worksheet.cells.createRange("A1:C3");

            // Apply formatting to the range
            const style = workbook.createStyle();
            style.font.color = AsposeCells.Color.Red;
            style.font.isBold = true;

            const flag = new AsposeCells.StyleFlag();
            flag.font = true;
            range.applyStyle(style, flag);

            // Define the range
            const range2 = worksheet.cells.createRange("A4:C5");

            // Apply formatting to the range
            const style2 = workbook.createStyle();
            style2.font.color = AsposeCells.Color.Blue;
            style2.font.isItalic = true;
            range2.setStyle(style2);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
