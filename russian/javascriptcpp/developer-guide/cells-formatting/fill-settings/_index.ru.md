---
title: Настройки заливки
linktitle: Настройки заливки
description: Узнайте, как настроить параметры заливки, фон и стиль ячеек с помощью библиотеки Aspose.Cells для JavaScript через C++.
keywords: Aspose.Cells, Ячейки, Параметры заливки, Фон, Стиль, JavaScript через C++
type: docs
weight: 50
url: /ru/javascript-cpp/cells-fill-settings/
---

## **Цвета и фоновые узоры**

Microsoft Excel может устанавливать передний (контур) и задний (заливка) цвета ячеек и фоновые узоры.

Aspose.Cells также поддерживает эти функции гибким образом. В этой теме мы узнаем, как использовать эти функции с использованием Aspose.Cells.

### **Настройка цветов и фоновых узоров**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), которая позволяет получить доступ к каждому листу в Excel-файле. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Каждый элемент в коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

У [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) есть свойство [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--), которое используется для получения и установки форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) предоставляет свойства для установки переднего и заднего цвета ячеек. Aspose.Cells предоставляет перечисление [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype), содержащее набор предопределённых типов фона и узоров, описанных ниже.

|**Фоновые узоры**|**Описание**|
| :- | :- |
|DiagonalCrosshatch|Представляет диагональный рисунок косой крест|
|DiagonalStripe|Представляет диагональную полосу|
|Gray6|Представляет 6,25% серый узор|
|Gray12|Представляет 12,5% серый узор|
|Gray25|Представляет 25% серый узор|
|Gray50|Представляет 50% серый узор|
|Gray75|Представляет 75% серый узор|
|HorizontalStripe|Представляет горизонтальный узор полосы|
|None|Представляет отсутствие фона|
|ReverseDiagonalStripe|Представляет обратный диагональный узор полосы|
|Solid|Представляет сплошной узор|
|ThickDiagonalCrosshatch|Представляет толстый диагональный крестовый узор|
|ThinDiagonalCrosshatch|Представляет тонкий диагональный крестовый узор|
|ThinDiagonalStripe|Представляет тонкий диагональный узор полосы|
|ThinHorizontalCrosshatch|Представляет тонкий горизонтальный крестовый узор|
|ThinHorizontalStripe|Представляет тонкий горизонтальный узор полосы|
|ThinReverseDiagonalStripe|Представляет тонкий обратный диагональный узор полосы|
|ThinVerticalStripe|Представляет тонкий вертикальный узор полосы|
|VerticalStripe|Представляет вертикальный узор полосы|

В приведенном ниже примере цвет переднего плана ячейки A1 установлен, но ячейка A2 настроена иметь как передний, так и фоновый цвета с фоновым узором вертикальных полос.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Define a Style and get the A1 cell style
            let style = worksheet.cells.get("A1").style;

            // Setting the foreground color to yellow
            style.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A1 cell
            worksheet.cells.get("A1").style = style;

            // Get the A2 cell style
            style = worksheet.cells.get("A2").style;

            // Setting the foreground color to blue
            style.foregroundColor = AsposeCells.Color.Blue;

            // Setting the background color to yellow
            style.backgroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A2 cell
            worksheet.cells.get("A2").style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```


### **Важно знать**

{{% alert color="primary" %}}

- Чтобы установить цвет переднего плана или фона ячейки, используйте свойства [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) или [**backgroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundColor-color-) объекта [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Оба вступят в силу только если свойство [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) объекта [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) настроено.
- Свойство [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) устанавливает цвет оттенка ячейки. Свойство [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) указывает тип используемого фона или узора для цвета переднего плана или фона. Aspose.Cells предоставляет перечисление [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype), которое содержит набор предопределенных типов узоров фона.
- Если выбрать значение *BackgroundType.None* из перечисления [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype), фон переднего плана не применяется. Аналогично, цвет фона не применяется, если выбрать значения *BackgroundType.None* или *BackgroundType.Solid*.
- При извлечении цвета тени ячейки, если [**style.pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) равно *BackgroundType.None*, [**style.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor--) вернет *Color.Empty*.

{{% /alert %}}

### **Применение эффектов градиентного заливки**

Чтобы применить желаемые градиентные эффекты заполнения к ячейке, используйте свойство [**twoColorGradient**](https://reference.aspose.com/cells/javascript-cpp/style/#twoColorGradient-color-color-gradientstyletype-number-) объекта [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) соответствующим образом.

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
        const { Workbook, SaveFormat, Color, GradientStyleType, TextAlignmentType } = AsposeCells;

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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.get(2, 1).putValue("test");

            const style = worksheet.cells.get("B3").style;

            style.isGradient = true;
            style.twoColorGradient = [ new Color(255, 255, 255), new Color(79, 129, 189), GradientStyleType.Horizontal, 1 ];
            style.font.color = Color.Red;
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            worksheet.cells.get("B3").style = style;

            worksheet.cells.rowHeightPixel = [2, 53];

            worksheet.cells.merge(2, 1, 1, 2);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Цвета и палитра**

Палитра - это количество цветов, доступных для использования при создании изображения. Использование стандартной палитры в презентации позволяет пользователю создавать однородный вид. Каждый файл Microsoft Excel (97-2003) имеет палитру из 56 цветов, которые могут быть применены к ячейкам, шрифтам, сеткам, графическим объектам, заливкам и линиям в диаграмме.

С помощью Aspose.Cells можно использовать не только существующие цвета палитры, но и пользовательские цвета. Прежде чем использовать пользовательский цвет, сначала добавьте его в палитру.

Эта тема обсуждает, как добавить пользовательские цвета в палитру.

### **Добавление пользовательских цветов в палитру**

Aspose.Cells поддерживает 56-цветную палитру Microsoft Excel. Для использования пользовательского цвета, который не определен в палитре, добавьте цвет в палитру.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит метод [**changePalette**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-), принимающий следующие параметры для добавления пользовательского цвета и изменения палитры:

- Пользовательский цвет, пользовательский цвет, который будет добавлен.
- Индекс, индекс цвета в палитре, который будет заменен пользовательским цветом. Должен быть от 0 до 55.

Приведенный ниже пример добавляет пользовательский цвет (Орхидея) в палитру перед его применением к шрифту.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(AsposeCells.Color.Orchid, 55);

            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining new Style object
            const styleObject = workbook.createStyle();
            // Setting the Orchid (custom) color to the font
            styleObject.font.color = workbook.colors[55];

            // Applying the style to the cell
            cell.style = styleObject;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Палитра может содержать только 56 цветов. Когда вы добавляете пользовательский цвет в палитру, палитра изменяется, и любой элемент в файле, отформатированный предыдущим цветом, изменяется. Поэтому при изменении палитры, пожалуйста, будьте очень осторожны. Более того, это ограничение только для формата файла XLS (Excel 97-2003), так как нет такого ограничения для форматов файлов XLSX или других более продвинутых форматов файлов MS Excel (2007/2010 или 2013).

{{% /alert %}}
