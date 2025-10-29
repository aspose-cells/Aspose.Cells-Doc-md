---
title: Настройки чисел
linktitle: Настройки чисел
description: Aspose.Cells — это библиотека JavaScript для работы с файлами таблиц, которая поддерживает множество настроек номеров ячеек. В этой статье рассматривается, как использовать библиотеку Aspose.Cells для управления настройками номеров ячеек для настройки форматов чисел в таблицах.
keywords: Aspose.Cells, библиотека JavaScript, электронная таблица, настройки номеров ячеек, форматирование, управление, Форматы чисел и дат
type: docs
weight: 10
url: /ru/javascript-cpp/cells-number-settings/
---

## **Как установить отображаемые форматы чисел и дат**  

Одной из сильных сторон Microsoft Excel является возможность задавать форматы отображения числовых значений и дат. Мы знаем, что числовые данные могут использоваться для представления различных значений, включая десятичные, валютные, процентные, дробные или бухгалтерские значения и т. д. Все эти числовые значения отображаются в различных форматах в зависимости от типа информации, которую они представляют. Аналогично, существует множество форматов отображения даты или времени.  
Aspose.Cells поддерживает эту функциональность и позволяет разработчикам устанавливать отображаемый формат для числа или даты.  

### **Как установить отображаемые форматы в Microsoft Excel**  

Чтобы установить отображаемые форматы в Microsoft Excel:  

1. Щелкните правой кнопкой мыши любую ячейку.  
2. Выберите **Формат ячеек**. Появится диалоговое окно, в котором можно установить форматы отображения для любого значения.  

Слева в диалоговом окне есть множество категорий значений, таких как **Общий**, **Число**, **Валюта**, **Бухгалтерия**, **Дата**, **Время**, **Процент** и др. Aspose.Cells поддерживает все эти форматы отображения.  

Aspose.Cells предоставляет модуль, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Excel. Модуль [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен модулем [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Модуль [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) представляет объект модуля [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).  

Aspose.Cells предоставляет свойство [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) для модуля [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). Это свойство используется для получения и установки формата ячейки. Модуль [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) предоставляет некоторые полезные свойства для работы с форматами отображения чисел и дат.  

### **Как использовать встроенные форматы чисел**  

Aspose.Cells предлагает встроенные форматы чисел для настройки отображения чисел и дат. Эти встроенные форматы можно применить с помощью свойства [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) объекта [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Все встроенные форматы чисел имеют уникальные числовые значения. Разработчики могут присвоить любое желаемое числовое значение свойству [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) объекта [**Style**](https://reference.aspose.com/cells/javascript-cpp/style), чтобы применить формат отображения. Такой подход быстр. Ниже приведены списки встроенных форматов чисел, поддерживаемых Aspose.Cells.  

|**Значение**|**Тип**|**Строка формата**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|т:мм:сс|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = new Date();

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 20;

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 2546;

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  


### **Как использовать пользовательские форматы чисел**  

Чтобы определить свой собственный настраиваемый формат строки для установки формата отображения, используйте свойство [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) объекта [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Этот подход не так быстр, как использование предустановленных форматов, но более гибкий.  

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

            // Instantiate or open workbook depending on whether a file is provided
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.putValue(new Date());

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.putValue(20);

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.putValue(2546);

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


{{% alert color="primary" %}}  

Если вы используете свойство [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) для установки формата числа, любой предыдущий формат, установленный с помощью свойства [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-), будет перезаписан, и наоборот.  

{{% /alert %}}  

## **Продвинутые темы**  
- [Проверьте Пользовательский числовой формат при установке Свойства Custom.](/cells/ru/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Список поддерживаемых форматов чисел](/cells/ru/javascript-cpp/list-of-supported-number-formats/)  
- [Отображение пользовательского формата даты Шаблон g и ge mm dd](/cells/ru/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Укажите пользовательские разделители десятичных и групповых чисел для рабочей книги](/cells/ru/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Указание форматирования собственного шаблона DBNum](/cells/ru/javascript-cpp/specifying-dbnum-custom-pattern-formatting/)
