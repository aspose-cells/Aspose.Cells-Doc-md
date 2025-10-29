---
title: Установка заголовков и нижних колонтитулов с помощью JavaScript через C++
linktitle: Установка заголовков и нижних колонтитулов
type: docs
weight: 30
url: /ru/javascript-cpp/setting-headers-and-footers/
description: В этой статье объясняется, как программно вставлять изображение в заголовки и нижние колонтитулы листов Excel с помощью Aspose.Cells for JavaScript через C++. 
keywords: вставка изображения в заголовок и нижний колонтитул Excel JavaScript через C++, установка команд сценария заголовка и нижнего колонтитула Excel JavaScript через C++
---

{{% alert color="primary" %}}

Заголовки и нижние колонтитулы - это строки текста, отображаемые ниже верхнего поля или выше нижнего поля соответственно. Также возможно добавить заголовки и нижние колонтитулы к листам. Заголовки и нижние колонтитулы могут использоваться для отображения полезной информации, такой как номер страницы, имя автора, название темы или дата и время. Заголовки и нижние колонтитулы управляются с использованием настроек разметки страницы.

{{% /alert %}}

## **Настройка колонтитулов и подвалов**

Aspose.Cells for JavaScript через C++ позволяет добавлять заголовки и нижние колонтитулы к листам во время выполнения, но мы рекомендуем вручную установить заголовки и нижние колонтитулы в предварительно подготовленном файле для печати. Вы можете использовать Microsoft Excel в качестве графического интерфейса для установки заголовков и нижних колонтитулов, чтобы сэкономить время и усилия при разработке. Aspose.Cells может импортировать файл и сохранять настройки.

Чтобы добавить верхние и нижние колонтитулы во время выполнения, Aspose.Cells предоставляет специальные вызовы API и команды сценариев для форматирования верхних и нижних колонтитулов.

### **Скриптовые команды**

Команды сценариев - это специальные команды, которые позволяют задавать форматирование верхних и нижних колонтитулов.

|**Сценарные команды**|**Описание**|
| :- | :- |
|&P|Текущий номер страницы|
|&G|Картинка|
|&N|Общее количество страниц|
|&D|Текущая дата|
|&T|Текущее время|
|&A|Имя листа|
|&F|Имя файла без пути|
|&&Text|Показывает &Text. Например: &&WO будет отображаться как &WO|
|&"\<FontName>"|Представляет имя шрифта. Например: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Представляет имя шрифта со стилем. Например: &"Arial,Bold"|
|&\<FontSize>|Представляет размер шрифта. Например: “&14abc”. Однако, если за этой командой следует обычное число для печати в заголовке, его следует отделить пробелом от размера шрифта. Например: “&14 123”.

### **Установить заголовки и нижние колонтитулы**

Класс [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) предоставляет два метода, [**header(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-string-) и [**footer(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-string-), используемые для добавления заголовка и нижнего колонтитула к листу. Эти методы принимают только два параметра:

- **Раздел** - раздел, куда следует поместить заголовок или колонтитул. Существуют три раздела: слева, по центру и справа, представленные соответственно 0, 1 и 2.
- **Сценарий** - сценарий, используемый для заголовка или колонтитула. В этом сценарии содержатся команды сценариев для форматирования заголовков или колонтитулов.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Set Headers and Footers Example</h1>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            // Setting worksheet name at the left section of the header
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[0] = "&A";

            // Setting current date and current time at the central section of the header
            // and changing the font of the header
            pageSetup.header[1] = "&\"Times New Roman,Bold\"&D-&T";

            // Setting current file name at the right section of the header and changing the
            // font of the header
            pageSetup.header[2] = "&\"Times New Roman,Bold\"&12&F";

            // Setting a string at the left section of the footer and changing the font
            // of a part of this string ("123")
            pageSetup.footer = pageSetup.footer || [];
            pageSetup.footer[0] = "Hello World! &\"Courier New\"&14 123";

            // Setting the current page number at the central section of the footer
            pageSetup.footer[1] = "&P";

            // Setting page count at the right section of footer
            pageSetup.footer[2] = "&N";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetHeadersAndFooters_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers and footers set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Вставка изображения в заголовок или колонтитул**

Класс [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) имеет два дополнительных метода, [**headerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerPicture-number-numberarray-) и [**footerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerPicture-number-numberarray-), используемых для вставки изображений в заголовок и нижний колонтитул. Эти методы принимают параметры:

- **Секция** - раздел заголовка или колонтитула, в который будет помещено изображение. Существуют три секции: слева, по центру и справа, представленные значениями 0, 1 и 2 соответственно.
- **Массив байтов** - графические данные (двоичные данные должны быть записаны в буфер массива байтов).

После выполнения нижеприведенного кода и открытия файла проверьте заголовок листа:

1. На меню **Файл** выберите **Настройка страницы**. Будет отображено диалоговое окно.
1. Выберите вкладку **Шапка/Нижний колонтитул**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Image in Header/Footer Example</title>
    </head>
    <body>
        <h1>Insert Image in Header/Footer Example</h1>
        <p>Select an existing Excel file to modify (optional). If none is selected, a new workbook will be used.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select an image to insert into the header:</p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Insert Image into Header</button>
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the header.</p>';
                return;
            }

            // Read image bytes
            const imageFile = imageInput.files[0];
            const imageBuffer = await imageFile.arrayBuffer();
            const binaryData = new Uint8Array(imageBuffer);

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const excelBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(excelBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet's page setup
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Set the header picture and header scripts (converted from setters to properties)
            pageSetup.headerPicture = binaryData;
            pageSetup.header = "&G";
            pageSetup.header = "&A";

            // Save the workbook as Excel97-2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertImageInHeaderFooter_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Image inserted into header successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
