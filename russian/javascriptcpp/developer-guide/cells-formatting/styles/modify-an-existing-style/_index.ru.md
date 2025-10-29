---
title: Изменить существующий стиль.
linktitle: Изменить существующий стиль.
description: Aspose.Cells — это библиотека JavaScript через C++, для работы с файлами электронных таблиц, которая позволяет пользователям изменять существующие стили ячеек. В этой статье рассказывается, как модифицировать уже существующий стиль ячейки с помощью библиотеки Aspose.Cells, чтобы изменять внешний вид ячеек по мере необходимости.
keywords: Изменение существующих стилей, настройка внешнего вида вашего приложения, руководства, учебные пособия, справочная документация, документация по разработке, ссылки на API, образцы кода, загрузки, поддержка.
type: docs
weight: 90
url: /ru/javascript-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Для применения одинаковых параметров форматирования к ячейкам создайте новый объект стиля форматирования. Объект стиля форматирования представляет собой комбинацию параметров форматирования, таких как шрифт, размер шрифта, отступ, номер, граница, узоры и т. д., названных и сохраненных в виде набора. При применении все форматирование в этом стиле применяется.

Вы также можете использовать существующий стиль, сохранить его с книгой и использовать для форматирования информации с теми же атрибутами.

Когда ячейки не явно форматируются, применяется стиль **Обычный** (стандартный стиль книги). В Microsoft Excel предопределено несколько стилей, кроме стиля Нормальный, включая запятую, валюту и процент.

Aspose.Cells позволяет изменять любой из этих стилей или любой другой стиль, который вы определяете с желаемыми атрибутами.

{{% /alert %}}

## **Использование Microsoft Excel**

Для обновления стиля в Microsoft Excel 97-2003:

1. В меню **Формат**, выберите **Стиль**.
1. Выберите стиль, который вы хотите изменить в списке **Имя стиля**.
1. Нажмите **Изменить**.
1. Выберите параметры стиля, которые вы хотите с помощью вкладок в диалоговом окне Формат ячеек.
1. Нажмите **ОК**.
1. В разделе **Стиль включает**, укажите нужные особенности стиля.
1. Нажмите **OK**, чтобы сохранить стиль и применить его к выбранному диапазону.

## **Использование Aspose.Cells for JavaScript через C++**

Следующие примеры демонстрируют, как использовать метод [**Style.update()**](https://reference.aspose.com/cells/javascript-cpp/style/#update--).

### **Создание и изменение стиля**

Этот пример создает объект [**Style**](https://reference.aspose.com/cells/javascript-cpp/style), применяет его к диапазону ячеек и изменяет объект [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Изменения автоматически применяются к ячейке и диапазону, к которому был применен стиль.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Style Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a new style object.
            const style = workbook.createStyle();

            // Set the number format.
            style.number = 14;

            // Set the font color to red color.
            style.font.color = AsposeCells.Color.Red;

            // Name the style.
            style.name = "Date1";

            // Get the first worksheet cells.
            const cells = workbook.worksheets.get(0).cells;

            // Specify the style (described above) to A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.style = style;

            // Create a range (B1:D1).
            const range = cells.createRange("B1", "D1");

            // Initialize styleflag object.
            const flag = new AsposeCells.StyleFlag();

            // Set all formatting attributes on.
            flag.all = true;

            // Apply the style (described above) to the range.
            range.applyStyle(style, flag);

            // Modify the style (described above) and change the font color from red to black.
            style.font.color = AsposeCells.Color.Black;

            // Done! Since the named style (described above) has been set to a cell and range, 
            // The change would be reflected(new modification is implemented) to cell(A1) and 
            // Range (B1:D1).
            style.update();

            // Save the excel file. 
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book_styles.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **Изменение существующего стиля**

В этом примере используется простой шаблонный файл Excel, к которому уже был применен стиль Percent к диапазону. Пример:

1. получает стиль,
1. создает объект стиля и
1. изменяет форматирование стиля.

Изменения автоматически применяются к диапазону, к которому был применен стиль.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Named Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, Utils } = AsposeCells;

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

            // Create a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the named style "Percent" via the styles collection
            const style = workbook.styles.get("Percent");

            // Change the number format to "0.00%".
            style.number = 11;

            // Set the font color.
            style.font.color = Color.Red;

            // Update the style so ranges using this named style are updated.
            style.update();

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book2.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Style updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
