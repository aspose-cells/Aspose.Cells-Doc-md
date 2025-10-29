---
title: Получение заголовков или колонтитулов с помощью JavaScript через C++
linktitle: Получение заголовков или нижних колонтитулов
type: docs
weight: 30
url: /ru/javascript-cpp/get-headers-or-footers/
description: Эта статья объясняет, как программно получать заголовки и колонтитулы из файлов Excel или OpenOffice с помощью API JavaScript через C++.
---

{{% alert color="primary" %}}

Заголовки и нижние колонтитулы отображаются только в представлении макета страницы, предварительном просмотре и на распечатанных страницах. 

Также вы можете использовать диалоговое окно настройки страницы, если хотите просмотреть заголовки или нижние колонтитулы для более чем одного листа одновременно. 

Для других типов листов, таких как листы диаграмм или диаграммы, вы можете вставлять заголовки и нижние колонтитулы только с помощью диалогового окна настройки страницы.

{{% /alert %}}

## **Получение заголовков и нижних колонтитулов в MS Excel**
1. Нажмите на лист, где вы хотите просмотреть или изменить заголовки или нижние колонтитулы.
2. На вкладке Вид в группе Просмотры рабочей книги щёлкните «Разметка страницы».
   Excel отображает лист в режиме макета страницы.
3. Чтобы просмотреть или отредактировать заголовок или нижний колонтитул, щелкните на текстовом поле заголовка или колонтитула слева, по центру или справа вверху или внизу страницы листа (под заголовком или над колонтитулом).


## **Получение заголовков и колонтитулов с помощью Script Aspose.Cells for Java через C++**
С помощью методов [**PageSetup.header(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-) и [**PageSetup.footer(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-) разработчики JavaScript могут просто получать заголовки или колонтитулы из файла.

1. Создайте рабочую книгу для открытия файла.
2. Получите лист, из которого необходимо получить заголовки или нижний колонтитул.
3. Получите заголовок или нижний колонтитул с конкретным ID раздела.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Header/Footer Reader Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

        function escapeHtml(str) {
            if (str === null || str === undefined) return '';
            return String(str)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerLeft = sheet.pageSetup.header(0);
            // Gets center section of header
            const headerCenter = sheet.pageSetup.header(1);
            // Gets right section of header
            const headerRight = sheet.pageSetup.header(2);
            // Gets center section of footer
            const footerCenter = sheet.pageSetup.footer(1);

            const resultHtml = [
                `<p><strong>Left Header:</strong> ${escapeHtml(headerLeft)}</p>`,
                `<p><strong>Center Header:</strong> ${escapeHtml(headerCenter)}</p>`,
                `<p><strong>Right Header:</strong> ${escapeHtml(headerRight)}</p>`,
                `<p><strong>Center Footer:</strong> ${escapeHtml(footerCenter)}</p>`
            ].join('');

            document.getElementById('result').innerHTML = resultHtml;
        });
    </script>
</html>
```

## **Разбор заголовков и колонтитулов в список команд**
Текст заголовка или нижнего колонтитула может содержать специальные команды, например, заполнители для номера страницы, текущей даты или атрибутов форматирования текста.

Специальные команды представлены одним символом с ведущим амперсандом ("&").

Строки заголовка и нижнего колонтитула создаются с использованием грамматики ABNF. Без просмотрщика их понять сложно.

Script Aspose.Cells for Java через C++ предоставляет метод [**PageSetup.commands(string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#commands-string-) для парсинга заголовков и колонтитулов в виде списка команд.

Следующий код показывает, как парсить заголовок или нижний колонтитул как список команд и обрабатывать команды:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Header/Footer Commands Example</title>
    </head>
    <body>
        <h1>Header/Footer Commands Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerSection = sheet.pageSetup.header(0);
            const commands = sheet.pageSetup.commands(headerSection) || [];

            const items = [];
            commands.forEach(c => {
                const type = c.type;
                switch (type) {
                    case AsposeCells.HeaderFooterCommandType.SheetName:
                        // embedded the name of the sheet to header or footer
                        items.push('<li>SheetName command found (embeds sheet name)</li>');
                        break;
                    default:
                        items.push(`<li>Command type: ${type}</li>`);
                        break;
                }
            });

            if (!items.length) {
                items.push('<li>No header/footer commands found.</li>');
            }

            resultDiv.innerHTML = `<ul>${items.join('')}</ul>`;

            // Save the (possibly unchanged) workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HeaderFooter_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Workbook';
        });
    </script>
</html>
```
