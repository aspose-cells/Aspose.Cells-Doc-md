---
title: Фигуры в диаграммах с помощью JavaScript через C++
linktitle: Формы в диаграммах
description: Узнайте, как использовать Aspose.Cells for JavaScript через C++ для добавления элементов управления и настройки диаграмм в Microsoft Excel. В этом руководстве показано, как управлять элементами диаграммы, регулировать форматирование и улучшать общий внешний вид и удобство использования ваших диаграмм.
keywords: Aspose.Cells for JavaScript через C++, элементы диаграммы, настройка диаграмм, Microsoft Excel, элементы диаграммы, форматирование.
type: docs
weight: 70
url: /ru/javascript-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
Иногда вам может потребоваться вставить объекты рисования, такие как метки, текстовые поля, изображения и т. д., в график. Aspose.Cells может добавлять элементы управления в график во время выполнения.
{{% /alert %}}

## **Добавление элемента управления метки в график**

Метки предоставляют средство информирования пользователей о содержании электронной таблицы. Aspose.Cells позволяет добавлять и управлять метками даже в диаграммах.

Класс [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) содержит метод с именем [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLabelInChart-number-number-number-number-), используемый для добавления элемента управления меткой в график. Ниже приведен список параметров, используемых для этого метода:

- **top** – вертикальное смещение метки от верхнего левого угла в единицах 1/4000 от области графика.
- **left** – горизонтальное смещение метки от верхнего левого угла в единицах 1/4000 от области графика.
- **height** – высота метки в единицах 1/4000 от области графика.
- **width** – ширина метки в единицах 1/4000 от области графика.

Метод возвращает объект [**Label**](https://reference.aspose.com/cells/javascript-cpp/label/). Класс [**Label**](https://reference.aspose.com/cells/javascript-cpp/label/) представляет собой метку в графике. Он имеет несколько важных членов:

- [**text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--) (свойство) – указывает строку заголовка метки.
- [**fill**](https://reference.aspose.com/cells/javascript-cpp/shape/#fill--) (свойство) – указывает атрибуты цвета заливки.

В следующем примере показано, как добавить метку в график. В примере используется файл дизайнера (**exp_piechart.xls**), в котором есть график. Мы используем этот файл для вставки метки в график. Ниже приведен исходный код для добавления метки в график. При выполнении кода генерируется следующий вывод.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Label In Chart Example</title>
    </head>
    <body>
        <h1>Add Label In Chart Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Add a new label to the chart.
            const label = chart.shapes.addLabelInChart(100, 100, 350, 900);

            // Set the caption of the label.
            label.text = "A Label In Chart";

            // Set the Placement Type, the way the Label is attached to the cells.
            label.placement = AsposeCells.PlacementType.FreeFloating;

            // Save the excel file and provide a download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Label added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Добавление элемента управления текстовым полем в график**

Один из способов выделить важную информацию в отчете – использование текстового поля. Например, введите текст для выделения названия компании или для указания географического региона с наибольшими продажами. Класс [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) предоставляет метод с именем [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-), который используется для добавления элемента управления текстовым полем в график. Ниже приведен список параметров, используемых для метода:

- **top** – вертикальное смещение текстового поля от верхнего левого угла в единицах 1/4000 от области графика.
- **left** – горизонтальное смещение текстового поля от верхнего левого угла в единицах 1/4000 от области графика.
- **height** – высота текстового поля в единицах 1/4000 от области графика.
- **ширина** - ширина текстового блока в единицах 1/4000 от области диаграммы.

Метод возвращает объект [**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/). Класс [**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/) представляет собой текстовый блок на диаграмме.

В следующем примере показано, как добавить текстовое поле на диаграмму. В примере используется предыдущий файл дизайнера (**exp_piechart.xls**), в котором есть диаграмма. Мы используем этот файл, чтобы вставить текстовое поле на диаграмму для отображения заголовка диаграммы. Ниже приведен исходный код для добавления текстового поля на диаграмму.

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Add a new textbox to the chart.
            const textbox0 = chart.shapes.addTextBoxInChart(100, 1100, 350, 2550);

            // Fill the text.
            textbox0.text = "Sales By Region";

            // Get the textbox text frame.
            // const textframe0 = textbox0.textFrame;

            // Set the textbox to adjust it according to its contents.
            // textframe0.autoSize = true;

            // Set the font color.
            textbox0.font.color = AsposeCells.Color.Maroon;

            // Set the font to bold.
            textbox0.font.isBold = true;

            // Set the font size.
            textbox0.font.size = 14;

            // Set font attribute to italic.
            textbox0.font.isItalic = true;

            // Get the fill format of the textbox.
            const fillformat = textbox0.fill;

            // Get the line format type of the textbox.
            const lineformat = textbox0.line;

            // Set the line weight.
            lineformat.weight = 2;

            // Set the dash style to solid.
            lineformat.dashStyle = AsposeCells.MsoLineDashStyle.Solid;

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Добавление изображения на диаграмму**

Aspose.Cells позволяет вставлять изображения в диаграмму. Например, добавьте изображение, чтобы подчеркнуть или придать больший смысл диаграмме или ее содержимому, или вставьте файл изображения бренда.

Класс [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) предоставляет метод с именем [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-), который используется для добавления объекта изображения на диаграмму. Ниже приведен список параметров, используемых для метода:

- **верх** - вертикальное смещение изображения от верхнего левого угла в единицах 1/4000 от области диаграммы.
- **слева** - горизонтальное смещение изображения от верхнего левого угла в единицах 1/4000 от области диаграммы.
- **поток** - объект потока, содержащий данные изображения.
- **масштабШирины** - масштаб ширины изображения, значение в процентах.
- **масштабВысоты** - масштаб высоты изображения, значение в процентах.

Метод возвращает объект [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/). Класс [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/) представляет собой объект изображения на диаграмме.

В следующем примере показано, как добавить изображение на диаграмму. Пример использует предыдущий файл дизайнера (**exp_piechart.xls**), в котором есть диаграмма. Мы используем этот файл, чтобы вставить изображение на диаграмму. Ниже приведен исходный код для добавления изображения на диаграмму.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Picture to Chart</title>
    </head>
    <body>
        <h1>Add Picture to Chart Example</h1>
        <p>Select an Excel file and an image to add to the first chart in the first worksheet.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            if (!fileInput.files.length || !imageInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file and an image file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const imageFile = imageInput.files[0];

            const arrayBuffer = await file.arrayBuffer();
            const imageBuffer = await imageFile.arrayBuffer();

            // Instantiating a Workbook object from the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the first sheet.
            const sheet = workbook.worksheets.get(0);
            const chart = sheet.charts.get(0);

            // Add a new picture to the chart.
            const pic0 = chart.shapes.addPictureInChart(50, 50, new Uint8Array(imageBuffer), 40, 40);

            // Get the lineformat type of the picture.
            const lineformat = pic0.line;

            // Set the dash style.
            lineformat.dashStyle = AsposeCells.MsoLineDashStyle.Solid;

            // Set the line weight.
            lineformat.weight = 4;

            // Save the modified Excel file and provide a download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Picture added to chart successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Добавление флажка на диаграмму**

Aspose.Cells позволяет вставлять флажки на лист диаграммы, используя перечисление [**MsoDrawingType**](https://reference.aspose.com/cells/javascript-cpp/msodrawingtype/). В следующем примере показано добавление флажка на лист диаграммы.

На следующем изображении показан лист диаграммы с флажком в выходном файле.

![todo:image_alt_text](controls-in-charts_1.jpg)

Ссылка на [выходной файл](101089316.xlsx), сгенерированный следующим фрагментом кода, прикреплена для вашего ознакомления.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Checkbox in Chart Sheet Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLink { display: none; margin-top: 10px; display: inline-block; }
            #result p { margin: 8px 0; }
        </style>
    </head>
    <body>
        <h1>Insert Checkbox in Chart Sheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';
            // This example creates a new workbook and inserts a chart sheet with a checkbox in the chart.
            // The file input is optional for this example (a new workbook is created regardless).

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a chart sheet to the workbook
            const index = workbook.worksheets.add(AsposeCells.SheetType.Chart);

            // Access the newly added chart sheet
            const sheet = workbook.worksheets.get(index);

            // Add a floating column chart to the chart sheet
            sheet.charts.addFloatingChart(AsposeCells.ChartType.Column, 0, 0, 1024, 960);

            // Add nSeries to the chart (single series with values 1,2,3)
            sheet.charts.get(0).nSeries.add("{1,2,3}", false);

            // Add checkbox to the chart
            sheet.charts.get(0).shapes.addShapeInChart(AsposeCells.MsoDrawingType.CheckBox, AsposeCells.PlacementType.Move, 400, 400, 1000, 600);

            // Set text of the checkbox shape
            sheet.charts.get(0).shapes.get(0).text = "CheckBox 1";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertCheckboxInChartSheet_out.xlsx';
            downloadLink.style.display = 'inline-block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Chart sheet with checkbox created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Добавить водяной знак WordArt на диаграмму](/cells/ru/javascript-cpp/add-wordart-watermark-to-chart/)
