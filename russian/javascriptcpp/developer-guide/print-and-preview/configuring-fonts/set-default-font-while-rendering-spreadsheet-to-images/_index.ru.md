---
title: Установка шрифта по умолчанию при рендеринге таблиц в изображение с помощью JavaScript через C++
linktitle: Установить шрифт по умолчанию при преобразовании электронной таблицы в изображения
type: docs
weight: 360
url: /ru/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Узнайте, как установить шрифт по умолчанию при рендеринге таблиц в изображения с использованием Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}

Используйте свойство [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--), чтобы установить шрифт по умолчанию при рендеринге электронных таблиц в изображения. Это свойство будет действительным только в том случае, если шрифт по умолчанию книги не может отобразить ваши символы. Шрифт по умолчанию, указанный с помощью свойства [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--), используется для всех тех ячеек, которые имеют недопустимые или отсутствующие шрифты.

{{% /alert %}}

## Установка шрифта по умолчанию при рендеринге электронных таблиц в изображения

Следующий пример кода создает рабочую книгу, добавляет текст в ячейку A4 первого листа и устанавливает шрифт на недопустимый или несуществующий. Затем он создает два изображения этого листа. Первое изображение сделано, установив свойство [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) в *Courier New*, второе — установив свойство [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) в *Times New Roman*.

Это изображение после установки свойства [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) в *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Это изображение после установки свойства [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) в *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Образец кода

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Render Worksheet to Images with Default Fonts</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Courier New Image</a>
            <a id="downloadLink2" style="display: none;">Download Times New Roman Image</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, SheetRender } = AsposeCells;

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
            const result = document.getElementById('result');
            const downloadLink1 = document.getElementById('downloadLink1');
            const downloadLink2 = document.getElementById('downloadLink2');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read the selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Set default font of the workbook to none
            let s = wb.defaultStyle;
            s.font.name = "";
            wb.defaultStyle = s;

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Access cell A4 and add some text inside it.
            const cell = ws.cells.get("A4");
            cell.value = "This text has some unknown or invalid font which does not exist.";

            // Set the font of cell A4 which is unknown.
            let st = cell.style;
            st.font.name = "UnknownNotExist";
            st.font.size = 20;
            st.isTextWrapped = true;
            cell.style = st;

            // Set first column width and fourth row height
            ws.cells.setColumnWidth(0, 80);
            ws.cells.setRowHeight(3, 60);

            // Create image or print options.
            const opts = new ImageOrPrintOptions();
            opts.onePagePerSheet = true;
            opts.imageType = ImageType.Png;

            // Render worksheet image with Courier New as default font.
            opts.defaultFont = "Courier New";
            let sr = new SheetRender(ws, opts);
            const imgData1 = sr.toImage(0);
            const blob1 = new Blob([imgData1], { type: 'image/png' });
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'out_courier_new_out.png';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Courier New Image';

            // Render worksheet image again with Times New Roman as default font.
            opts.defaultFont = "Times New Roman";
            sr = new SheetRender(ws, opts);
            const imgData2 = sr.toImage(0);
            const blob2 = new Blob([imgData2], { type: 'image/png' });
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'times_new_roman_out.png';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Times New Roman Image';

            result.innerHTML = '<p style="color: green;">Images rendered successfully! Use the download links to save the PNG files.</p>';
        });
    </script>
</html>
```
