---
title: Использование встроенных стилей
linktitle: Использование встроенных стилей
type: docs
weight: 80
url: /ru/javascript-cpp/using-built-in-styles/
description: Код JavaScript для использования встроенных стилей Excel с помощью Aspose.Cells for JavaScript через C++.
keywords: JavaScript использует встроенные стили Excel, программное применение стилей в рабочей книге, программное применение стилей в рабочей книге, JavaScript применяет встроенные стили в Excel, JavaScript применяет встроенные стили в рабочей книге, JavaScript код применяет встроенные стили в рабочей книге, JavaScript код применяет встроенные стили в Excel рабочей книге
---

{{% alert color="primary" %}}  
Aspose.Cells предоставляет огромную коллекцию повторно используемых стилей для форматирования ячейки в документе электронной таблицы. Мы можем использовать встроенные стили в нашей книге и также создавать пользовательские стили.  
{{% /alert %}}  

## **Как использовать встроенные стили**  

Метод [**Workbook.createBuiltinStyle(BuiltinStyleType)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createBuiltinStyle-builtinstyletype-) и перечисление [**BuiltinStyleType**](https://reference.aspose.com/cells/javascript-cpp/builtinstyletype) делают использование встроенных стилей удобным. Вот список всех возможных встроенных стилей:  

- TwentyPercentAccent1
- TwentyPercentAccent2
- TwentyPercentAccent3
- TwentyPercentAccent4
- TwentyPercentAccent5
- TwentyPercentAccent6
- FortyPercentAccent1
- FortyPercentAccent2
- FortyPercentAccent3
- FortyPercentAccent4
- FortyPercentAccent5
- FortyPercentAccent6
- SixtyPercentAccent1
- SixtyPercentAccent2
- SixtyPercentAccent3
- SixtyPercentAccent4
- Акцент 60% 5
- Акцент 60% 6
- Акцент 1
- Акцент 2
- Акцент 3
- Акцент 4
- Акцент 5
- Акцент 6
- Плохо
- Расчет
- ПроверкаЯчейки
- Запятая
- Запятая1
- Валюта
- Валюта1
- ОбъяснительныйТекст
- Хорошо
- Заголовок1
- Заголовок2
- Заголовок3
- Заголовок4
- Гиперссылка
- ГиперссылкаПодписанная
- Ввод
- СвязаннаяЯчейка
- Нейтральный
- Нормальный
- Заметка
- Вывод
- Процент
- Заголовок
- Итого
- Текст предостережения
- Уровень строки
- Уровень столбца


## Код JavaScript для использования встроенных стилей  
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
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Output.xlsx</a>
        <a id="downloadLink2" style="display: none;">Download Output.out.ods</a>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Creating a new Workbook
            const workbook = new Workbook();

            // Creating a built-in style (Title)
            const style = workbook.createBuiltinStyle(AsposeCells.BuiltinStyleType.Title);

            // Accessing first worksheet, its cells, and cell A1
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Setting cell value and style (converted setter)
            cell.putValue("Aspose");
            cell.style = style;

            // Auto-fit column and row
            worksheet.autoFitColumn(0);
            worksheet.autoFitRow(0);

            // Save as XLSX
            const outputData1 = workbook.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Output.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Output.xlsx';

            // Save as ODS
            const outputData2 = workbook.save(SaveFormat.Ods);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'Output.out.ods';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Output.out.ods';

            document.getElementById('result').innerHTML = '<p style="color: green;">Files generated. Click the download links to save them.</p>';
        });
    </script>
</html>
```
