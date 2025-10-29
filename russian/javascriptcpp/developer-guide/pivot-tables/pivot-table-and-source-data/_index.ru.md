---
title: Сводная таблица и исходные данные
type: docs
weight: 30
url: /ru/javascript-cpp/pivot-table-and-source-data/
---

## **Исходные данные сводной таблицы**

Иногда возникают ситуации, когда вы хотите создать отчеты Microsoft Excel с сводными таблицами, использующими данные из разных источников данных (например, базы данных), которые неизвестны на этапе проектирования. В этой статье представлен подход к динамическому изменению источника данных сводной таблицы.

### **Изменение исходного источника данных сводной таблицы**

1. Создание нового файла шаблона дизайнера.
   1. Создайте новый файл шаблона дизайнера, как показано на скриншоте ниже.
   1. Затем определите именованный диапазон **DataSource**, который ссылается на этот диапазон ячеек.

      **Создание файла шаблона дизайнера и определение именованного диапазона DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Создание сводной таблицы на основе этого именованного диапазона.
   1. В Microsoft Excel выберите **Данные**, затем **Сводная таблица** и **Отчет сводной таблицы и диаграмма**.
   1. Создайте сводную таблицу на основе созданного в первом шаге именованного диапазона.

      **Создание сводной таблицы на основе именованного диапазона DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Перетащите соответствующее поле на строку и столбец сводной таблицы, затем создайте результирующую сводную таблицу, как показано на скриншоте ниже.

   **Создание сводной таблицы на основе соответствующего поля** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Щелкните правой кнопкой мыши на сводной таблице и выберите **Параметры таблицы**.
   1. Установите **Обновлять при открытии** в настройках **Параметры данных**.

      **Настройка параметров сводной таблицы** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Теперь вы можете сохранить этот файл как файл вашего дизайнерского шаблона.

1. Пополнение новыми данными и изменение исходных данных сводной таблицы.
   1. После создания дизайнерского шаблона используйте следующий код для изменения исходных данных сводной таблицы.

Исполнение приведенного ниже примера кода изменяет исходные данные сводной таблицы.

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Populating new data to the worksheet cells
            worksheet.cells.get("A9").value = "Golf";
            worksheet.cells.get("B9").value = "Qtr4";
            worksheet.cells.get("C9").value = 7000;

            // Changing named range "DataSource"
            const range = worksheet.cells.createRange(0, 0, 9, 3);
            range.name = "DataSource";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
