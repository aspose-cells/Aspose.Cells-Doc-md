---
title: Темы и цвета Excel
linktitle: Темы и цвета Excel  
type: docs  
weight: 100  
url: /ru/javascript-cpp/excel-themes-and-colors/  
description: Узнайте, как использовать пользовательские схемы цветов с Aspose.Cells for JavaScript через C++.  
keywords: JavaScript Создание и применение схем цветов, JavaScript программное создание пользовательской схемы цвета, как программно применить пользовательскую схему цвета в JavaScript, как использовать цветовую схему в Excel  
---

## **Как применить и создать цветовую схему в Excel**  
Темы документов позволяют легко координировать цвета, шрифты и графические эффекты форматирования документов Excel и быстро обновлять их.  
Темы обеспечивают единый внешний вид с именованными стилями, графическими эффектами и другими объектами, используемыми в книге. Например, стиль Accent1 выглядит по-разному в темах Office и Apex. Часто вы применяете тему документа, а затем дополнительно изменяете её по вашему желанию.  

### **Как применить цветовую схему в Excel**  
1. Откройте Excel и перейдите на вкладку "Разметка страницы" на ленте Excel.  
1. Нажмите кнопку "Цвета" в разделе "Темы".  
<br>  
<img src="color.png" width=70% />  
1. Выберите цветовую палитру, которая соответствует вашим требованиям, или наведите курсор на схему, чтобы увидеть предварительный просмотр.  

### **Как создать пользовательскую цветовую схему в Excel**  
Вы можете создать собственный набор цветов, чтобы придать вашему документу свежий, уникальный вид или соответствовать корпоративному стилю вашей организации.  

1. Откройте Excel и перейдите на вкладку "Разметка страницы" на ленте Excel.  
1. Нажмите кнопку "Цвета" в разделе "Темы".  
1. Нажмите кнопку "Настроить цвета...".  
<br>  
<img src="color2.png" width=70% />  

1. В диалоговом окне "Создание новых тем цветов" вы можете выбрать цвета для каждого элемента, нажав на выпадающие списки цветов рядом с ними. Вы можете выбрать цвета из палитры или определить пользовательские цвета, используя опцию "Другие цвета".  
<br>  
<img src="color3.png" width=70% />  
1. После выбора всех желаемых цветов укажите имя для вашей пользовательской цветовой схемы в поле "Имя".  

1. Нажмите кнопку "Сохранить", чтобы сохранить вашу пользовательскую цветовую схему. Ваша пользовательская цветовая схема теперь будет доступна в раскрывающемся меню "Цвета" для последующего использования.  

## **Как создать и применить цветовую схему в Aspose.Cells**  
Aspose.Cells предоставляет возможности настройки тем и цветов.  

### **Как создать пользовательскую цветовую тему в Aspose.Cells**  
Если в файле используются цвета темы, нам не нужно изменять каждую ячейку вручную; достаточно изменить цвета в теме.  

Приведенный ниже пример показывает, как применить пользовательские темы с желаемыми цветами. Мы используем образец файла шаблона, созданный вручную в Microsoft Excel 2007.  

Следующий пример загружает шаблон XLSX, задаёт цвета для различных типов цветов темы, применяет пользовательские цвета и сохраняет файл Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Custom Theme Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Define Color array (of 12 colors) for Theme.
            const carr = [
                new Color("AntiqueWhite"), // Background1
                new Color("Brown"), // Text1
                new Color("AliceBlue"), // Background2
                new Color("Yellow"), // Text2
                new Color("YellowGreen"), // Accent1
                new Color("Red"), // Accent2
                new Color("Pink"), // Accent3
                new Color("Purple"), // Accent4
                new Color("PaleGreen"), // Accent5
                new Color("Orange"), // Accent6
                new Color("Green"), // Hyperlink
                new Color("Gray") // Followed Hyperlink
            ];

            // Set the custom theme with specified colors.
            workbook.customTheme("CustomeTheme1", carr);

            // Save as the excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom theme applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



### **Как применить цвета темы в Aspose.Cells**  
Следующий пример применяет цвет переднего плана и фондовый цвет ячейки на основе стандартных типов цветов темы (рабочей книги). Также он сохраняет файл Excel на диск.  


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
            // Instantiate a Workbook.
            const workbook = new Workbook();

            // Get cells collection in the first (default) worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Get the D3 cell.
            const c = cells.get("D3");

            // Get the style of the cell.
            const s = c.style;

            // Set foreground color for the cell from the default theme Accent2 color.
            s.foregroundThemeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent2, 0.5);

            // Set the pattern type.
            s.pattern = AsposeCells.BackgroundType.Solid;

            // Get the font for the style.
            const f = s.font;

            // Set the theme color.
            f.themeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent4, 0.1);

            // Apply style.
            c.style = s;

            // Put a value.
            c.value = "Testing1";

            // Save the excel file and provide download link.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


### **Как получить и установить цвета темы в Aspose.Cells**  
Ниже приведены несколько методов и свойств, реализующих цвета темы.  

- [**Style.foregroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundThemeColor-themecolor-): Используется для установки цвета переднего плана.  
- [**Style.backgroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundThemeColor-themecolor-): Используется для установки цвета фона.  
- [**Font.themeColor**](https://reference.aspose.com/cells/javascript-cpp/font/#themeColor-themecolor-): Используется для установки цвета шрифта.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-): Используется для получения цвета темы.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-color-): Используется для установки цвета темы.  

В следующем примере показано, как получить и установить цвета темы.  

Следующий пример использует шаблон XLSX, получает цвета для различных типов цветов темы, изменяет их и сохраняет файл Microsoft Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Theme Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, ThemeColorType } = AsposeCells;

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

            // Instantiating a Workbook object and opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Background1 theme color.
            let c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1: ", c);

            // Get the Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2: ", c);

            // Change the Background1 theme color.
            workbook.themeColor(ThemeColorType.Background1, Color.Red);

            // Get the updated Background1 theme color.
            c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1 changed to: ", c);

            // Change the Accent2 theme color.
            workbook.themeColor(ThemeColorType.Accent2, Color.Blue);

            // Get the updated Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2 changed to: ", c);

            // Saving the updated file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Updated Excel File';

            // Display results
            let resultHtml = '';
            resultHtml += `<p>theme color Background1: ${JSON.stringify(workbook.themeColor(ThemeColorType.Background1))}</p>`;
            resultHtml += `<p>theme color Accent2: ${JSON.stringify(workbook.themeColor(ThemeColorType.Accent2))}</p>`;
            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! See console for detailed logs.</p>' + resultHtml;
        });
    </script>
</html>
```


## **Продвинутые темы**  
- [Извлечение данных о теме из файла Excel](/cells/ru/javascript-cpp/extract-theme-data-from-excel-file/)
