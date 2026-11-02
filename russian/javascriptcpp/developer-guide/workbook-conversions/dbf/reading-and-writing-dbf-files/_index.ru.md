---
title: Чтение и запись файлов DBF
linktitle: Чтение и запись файлов DBF
description: Aspose.Cells — библиотека для JavaScript на базе C++ для работы с файлами электронных таблиц, которая поддерживает чтение и запись файлов dBASE III и IV (DBF). В этой статье объясняется, как импортировать данные из файлов DBF и экспортировать их в файлы DBF с помощью Aspose.Cells, включая сведения о формате файла, поддерживаемые функции и пошаговые примеры.
keywords: Aspose.Cells, библиотека для JavaScript на базе C++, DBF, dBASE, чтение DBF, запись DBF, импорт DBF, экспорт DBF, формат файла, .dbf
type: docs
weight: 200
url: /ru/javascript-cpp/reading-and-writing-dbf-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells обеспечивает полную поддержку чтения и записи файлов DBF (dBASE). Существующие файлы dBASE III и dBASE IV можно загрузить в объект `Workbook`, обработать данные с помощью широких возможностей API Aspose.Cells, а затем сохранить рабочую книгу обратно в формат DBF для использования в устаревших приложениях для работы с базами данных.
{{% /alert %}}

## **Введение**
DBF (файл базы данных) — устаревший формат баз данных, впервые представленный dBASE в начале 1980-х годов. Несмотря на возраст формата, файлы DBF по-прежнему широко используются во многих отраслях для хранения структурированных данных, особенно в бухгалтерском учете, GIS и других специализированных приложениях. Aspose.Cells позволяет без проблем интегрировать эти устаревшие файлы в современные процессы работы с электронными таблицами.
Библиотека поддерживает как чтение, так и запись файлов DBF, предоставляя следующие возможности:
- Импортировать данные из существующих файлов DBF в объекты `Workbook` библиотеки Aspose.Cells для дальнейшей обработки или преобразования в другие форматы.
- Создавать новые файлы DBF с нуля или на основе данных из других форматов электронных таблиц.
- Сохранять определения полей, типы данных и структуры записей при импорте данных из формата DBF и экспорте в него.
Файлы DBF также можно открывать непосредственно в Microsoft Excel и других приложениях для работы с электронными таблицами, что делает их удобным связующим звеном между устаревшими системами и современными инструментами обработки электронных таблиц.

## **Поддерживаемые версии DBF и функции**
Aspose.Cells поддерживает следующие версии формата DBF:
- **dBASE III** — первоначальный и наиболее широко поддерживаемый вариант формата DBF.
- **dBASE IV** — расширенная версия, поддерживающая дополнительные типы данных и большие размеры полей.

### Поддерживаемые функции
Библиотека обеспечивает всеобъемлющую поддержку следующих операций:
- Чтение данных DBF в объект `Workbook` с сохранением всех записей и определений полей.
- Запись данных рабочей книги обратно в формат DBF для экспорта в приложения, совместимые с dBASE.
- Обработка распространенных типов данных, используемых в файлах DBF, включая символьные, числовые, датовые и логические поля.
- Сохранение определений полей, включая имя, тип и длину поля, при операциях чтения и записи.

### Ограничения и особенности работы
При работе с файлами DBF учитывайте следующие ограничения:
- Максимальное количество полей в файле — **128**.
- Максимальный размер записи — **4000 байт**.
- Имена полей ограничены **10 символами**, должны записываться в верхнем регистре и не могут содержать пробелы.
- Значения дат в файлах DBF хранятся в формате `YYYYMMDD`.
- Кодировка символов может различаться в зависимости от приложения, в котором был создан файл (чаще всего используются Windows-1252 или OEM-кодовые страницы).

## **Чтение файла DBF**
Aspose.Cells обеспечивает простую загрузку данных из файла DBF в объект `Workbook`. Библиотека использует класс `LoadOptions` для указания исходного формата, обеспечивая корректную интерпретацию данных в процессе загрузки.

### Чтение файла DBF с помощью Aspose.Cells
Чтобы прочитать файл DBF, необходимо создать экземпляр `LoadOptions`, установить его свойство `loadFormat` в `LoadFormat.Dbf` и передать его в конструктор `Workbook` вместе с путем к файлу. После загрузки данные становятся доступны через коллекцию `Worksheets`, где можно перебирать ячейки, извлекать значения или изменять данные по мере необходимости.
В следующем примере показано, как с помощью Aspose.Cells загрузить существующий файл DBF, получить доступ к первому рабочему листу и прочитать значения ячеек.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".dbf" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select a DBF file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const fileData = new Uint8Array(await file.arrayBuffer());
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Dbf);
                const workbook = new Workbook(fileData, loadOptions);
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const maxRow = cells.maxDataRow;
                const maxCol = cells.maxDataColumn;
                const lines = [];
                for (let i = 0; i <= maxRow; i++) {
                    let line = "";
                    for (let j = 0; j <= maxCol; j++) {
                        const cell = cells.get(i, j);
                        const value = cell.stringValue;
                        line += "|" + value;
                    }
                    line += "|";
                    lines.push(line);
                }
                const output = document.createElement('pre');
                output.textContent = lines.join("\n");
                result.replaceChildren(output);
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                const message = document.createElement('p');
                message.style.color = "green";
                message.textContent = "DBF file loaded successfully. Converted XLSX saved as output.xlsx.";
                result.appendChild(message);
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Файлы DBF можно открывать непосредственно в Microsoft Excel, выбрав файл в диалоговом окне «Открыть». Excel откроет файл DBF как электронную таблицу и отобразит записи в табличной форме. Это позволяет быстро проверить данные после чтения или записи с помощью Aspose.Cells.
{{% /alert %}}

## **Запись файла DBF**
Запись данных в файл DBF выполняется так же, как сохранение данных в любом другом формате электронных таблиц с помощью Aspose.Cells. Создайте или загрузите объект `Workbook`, заполните рабочий лист данными, а затем вызовите метод `save`, указав `SaveFormat.Dbf` в качестве целевого формата.

### Запись файла DBF с помощью Aspose.Cells
Для создания файла DBF выполните следующие шаги:
1. Создайте новый экземпляр `Workbook`.
2. Получите первый рабочий лист из коллекции `Worksheets`.
3. Заполните рабочий лист данными, включая заголовки в первой строке и записи в последующих строках.
4. Вызовите метод `Workbook.save`, передав путь к файлу и `SaveFormat.Dbf` в качестве параметров.
В следующем примере показано, как создать новый файл DBF с нуля. Рабочий лист заполняется тестовыми данными с различными типами данных (строками, числами и датами), чтобы продемонстрировать обработку типов полей при экспорте в формат DBF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Заголовки столбцов
            cells.get(0, 0).value = "ID";
            cells.get(0, 1).value = "Name";
            cells.get(0, 2).value = "Department";
            cells.get(0, 3).value = "Salary";
            cells.get(0, 4).value = "HireDate";
            // Строка данных 1
            cells.get(1, 0).value = 101;
            cells.get(1, 1).value = "John Smith";
            cells.get(1, 2).value = "Engineering";
            cells.get(1, 3).value = 75000.50;
            cells.get(1, 4).value = new Date(2020, 2, 15);
            // Строка данных 2
            cells.get(2, 0).value = 102;
            cells.get(2, 1).value = "Jane Doe";
            cells.get(2, 2).value = "Marketing";
            cells.get(2, 3).value = 68000.75;
            cells.get(2, 4).value = new Date(2019, 6, 22);
            // Строка данных 3
            cells.get(3, 0).value = 103;
            cells.get(3, 1).value = "Bob Johnson";
            cells.get(3, 2).value = "Finance";
            cells.get(3, 3).value = 82000.00;
            cells.get(3, 4).value = new Date(2021, 0, 10);
            // Строка данных 4
            cells.get(4, 0).value = 104;
            cells.get(4, 1).value = "Alice Brown";
            cells.get(4, 2).value = "Human Resources";
            cells.get(4, 3).value = 71000.25;
            cells.get(4, 4).value = new Date(2018, 10, 5);
            // Строка данных 5
            cells.get(5, 0).value = 105;
            cells.get(5, 1).value = "Charlie Wilson";
            cells.get(5, 2).value = "Operations";
            cells.get(5, 3).value = 79500.80;
            cells.get(5, 4).value = new Date(2022, 4, 30);
            // Установка ширины столбцов для лучшей читаемости
            cells.setColumnWidth(0, 8);
            cells.setColumnWidth(1, 20);
            cells.setColumnWidth(2, 20);
            cells.setColumnWidth(3, 12);
            cells.setColumnWidth(4, 14);
            const outputData = workbook.save(AsposeCells.SaveFormat.Dbf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.dbf";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
При записи данных в файл DBF убедитесь, что они соответствуют ограничениям формата. Длина имен полей не должна превышать 10 символов; имена также не должны содержать пробелы. Записи размером более 4000 байт не будут сохранены корректно. Значения дат должны быть корректными и представимыми в формате YYYYMMDD.
{{% /alert %}}

## **Типы данных и форматирование**
При передаче данных между Aspose.Cells и форматом DBF важно понимать, как типы данных соотносятся в обеих системах, чтобы обеспечить целостность данных.

### Типы ячеек и типы полей DBF
Значения ячеек Aspose.Cells автоматически преобразуются в соответствующие типы полей DBF при сохранении:
- **Строковые значения** сопоставляются с символьными полями (C).
- **Числовые значения** (целые и десятичные числа) сопоставляются с числовыми полями (N).
- **Значения даты** сопоставляются с полями типа «Дата» (D) в формате `YYYYMMDD`.
- **Логические значения** сопоставляются с логическими полями (L).

### Кодировка
Файлы DBF могут использовать различные кодировки символов в зависимости от приложения, в котором они были созданы. В большинстве случаев Aspose.Cells автоматически обрабатывает кодировку, однако при возникновении проблем с отображением символов может потребоваться проверить кодировку исходного файла.

### Правила именования полей
Имена полей DBF должны соответствовать следующим правилам:
- Длина поля не должна превышать 10 символов.
- Имя поля должно начинаться с буквы.
- Имя поля не может содержать пробелы или специальные символы.
- Имя поля сохраняется в верхнем регистре независимо от регистра во входных данных.

### Проверка результата
После записи файла DBF результат можно проверить, открыв его в Microsoft Excel или любом приложении, совместимом с dBASE. Данные должны отображаться в табличной форме: имена полей должны использоваться в качестве заголовков столбцов, а записи — соответствовать переданным данным.

## **Преобразование между DBF и другими форматами**
Одним из наиболее практичных применений Aspose.Cells для чтения и записи файлов DBF является преобразование данных между форматом DBF и современными форматами электронных таблиц, такими как XLSX, XLS или CSV. Поскольку Aspose.Cells поддерживает широкий спектр форматов, можно легко загрузить файл DBF, сохранить его в любом другом поддерживаемом формате или выполнить обратное преобразование.

{{< app/cells/assistant language="javascript-cpp" >}}