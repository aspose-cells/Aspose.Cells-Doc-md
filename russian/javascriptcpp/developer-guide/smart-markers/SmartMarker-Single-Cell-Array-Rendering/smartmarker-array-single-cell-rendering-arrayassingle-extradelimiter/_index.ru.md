---
title: Рендеринг массива в одной ячейке с помощью смарт-маркера | Aspose.Cells for JavaScript via C++
linktitle: Рендеринг массива в одной ячейке с помощью смарт-маркера | Aspose.Cells for JavaScript via C++
description: Узнайте, как с помощью атрибутов ArrayAsSingle и ExtraDelimiter в смарт-маркерах отображать данные массива в одной ячейке средствами Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, библиотека Aspose.Cells for JavaScript via C++, электронные таблицы, смарт-маркеры, ArrayAsSingle, ExtraDelimiter, массив в одной ячейке, рендеринг массивов, шаблон
type: docs
weight: 195
url: /ru/javascript-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает рендеринг данных массива в одной ячейке с помощью смарт-маркеров. Используя атрибут `ArrayAsSingle` вместе с атрибутом `ExtraDelimiter`, разработчики могут управлять разделением элементов массива в пределах одной ячейки, обеспечивая гибкое форматирование отчетов и шаблонов.
{{% /alert %}}

## **Введение**
Смарт-маркеры в Aspose.Cells — мощный механизм на основе шаблонов, который позволяет динамически заполнять электронные таблицы данными с помощью выражений вида `&=DataSource.Field`. Маркер размещается в рабочей книге-конструкторе, а после обработки шаблона с помощью `WorkbookDesigner` маркеры заменяются значениями из переданного источника данных.
По умолчанию, когда смарт-маркер ссылается на свойство, возвращающее массив, например `&=DataSource.Numbers`, движок распределяет элементы массива по отдельным соседним ячейкам — по горизонтали вдоль строки или по вертикали вдоль столбца. Хотя такое поведение удобно во многих сценариях, в некоторых случаях предпочтительнее отобразить весь массив в одной ячейке, объединив элементы и разделив их выбранным разделителем.
Атрибуты `ArrayAsSingle` и `ExtraDelimiter`, используемые совместно в теге смарт-маркера, решают эту задачу. Они позволяют сохранять компактные и предсказуемые макеты отчетов и при этом полноценно работать с источниками данных в виде массивов.

## **Зачем нужна эта функция**

### **Стандартное распределение элементов массива**
Если смарт-маркер ссылается на свойство, возвращающее массив, Aspose.Cells по умолчанию распределяет элементы массива по нескольким ячейкам. Например, маркер вида `&=Product.Tags` для массива из четырех строковых значений поместит каждое значение в отдельную ячейку, смещая остальное содержимое шаблона и потенциально нарушая тщательно разработанные макеты отчетов.

### **Ограничения использования**
Стандартное распределение элементов массива не всегда подходит для практических сценариев:
- **Отчеты с краткими итогами**, которым необходим компактный макет с одной строкой на каждую запись.
- **Списки тегов, меток или ключевых слов**, которые необходимо отображать в одной ячейке в виде значений, разделенных запятой или вертикальной чертой.
- **Фильтры-метки и индикаторы состояния**, объединяющие несколько значений в одном месте для удобства чтения.
- **Последующие конвейеры обработки** (экспорт в CSV, рендеринг PDF, слияние почты), ожидающие по одному объединенному значению в каждой ячейке вместо развернутого диапазона.
- **Совместимость между платформами**, при которой некоторые получатели не могут работать с массивами, выходящими за пределы одной ячейки.

### **Какую проблему устраняет эта функция**
Без встроенного механизма разработчикам пришлось бы предварительно обрабатывать данные в JavaScript — объединять элементы массивов в строки с разделителями перед привязкой данных к конструктору рабочих книг. Это приводит к дублированию логики, усложняет модели данных и повышает вероятность ошибок. Атрибуты `ArrayAsSingle` и `ExtraDelimiter` устраняют необходимость в таком обходном решении, поскольку форматирование задается декларативно непосредственно в теге смарт-маркера.

## **Преимущества функции**
Использование атрибутов `ArrayAsSingle` и `ExtraDelimiter` в смарт-маркерах обеспечивает несколько преимуществ:
- **Размещение в одной ячейке**: все элементы массива отображаются ровно в одной ячейке, поэтому макеты остаются компактными и предсказуемыми.
- **Настройка разделителя**: можно указать любую строку-разделитель — запятую, точку с запятой, дефис, вертикальную черту, новую строку или произвольный текст.
- **Форматирование на основе шаблона**: дополнительный код для предварительной обработки данных не требуется; правила форматирования задаются внутри тега смарт-маркера.
- **Более аккуратные отчеты**: элементы массива больше не сдвигают соседнее содержимое шаблона в другие строки или столбцы.
- **Поддержка различных типов данных**: функция работает со строками, числами, датами и любыми другими типами данных, которые можно объединить с помощью разделителя.
- **Обратная совместимость**: если атрибуты не указаны, сохраняется исходное поведение распределения элементов массива, поэтому существующие шаблоны продолжают работать без изменений.

## **Как использовать эту функцию**

### **Синтаксис смарт-маркера**
Атрибуты `ArrayAsSingle` и `ExtraDelimiter` передаются как пары «ключ-значение» внутри круглых скобок стандартного смарт-маркера. Общий синтаксис:

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
        const { Workbook, WorkbookDesigner } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const product = {
                Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
            };
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Tags";
            cells.get("A2").value = '&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")';
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Product", product);
            designer.process();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_arraySingle.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

Маркер состоит из следующих частей:
- `&=DataSource.ArrayProperty` — стандартный смарт-маркер, ссылающийся на свойство, возвращающее массив, в привязанном источнике данных.
- `arrayasSingle=true` — указывает движку отобразить весь массив в одной ячейке. Только значение `true` включает этот режим.
- `extraDelimiter=", "` — задает разделитель между элементами массива. Значение представляет собой строковый литерал: это может быть пустая строка, один символ или несколько символов.

{{% alert color="primary" %}}
Атрибут `extraDelimiter` принимает любой строковый литерал, включая многосимвольные разделители, пользовательский текст или управляющие последовательности, например `\n` для вывода значений с разделителем в виде новой строки. Если массив пуст, итоговая ячейка остается пустой.
{{% /alert %}}

### **Пошаговый рабочий процесс**
Ниже приведен порядок действий для рендеринга массива в одной ячейке с помощью смарт-маркеров.
1. **Подготовьте источник данных**: создайте объект или структуру данных со свойством, возвращающим массив. Это свойство может возвращать массив строк, чисел или любых других поддерживаемых типов значений.
2. **Создайте рабочую книгу-конструктор**: создайте новый `Workbook`, добавьте строку заголовка и поместите в ячейку смарт-маркер, ссылающийся на свойство, возвращающее массив, с атрибутами `arrayasSingle` и `extraDelimiter`.
3. **Создайте экземпляр `WorkbookDesigner`**: создайте объект `WorkbookDesigner`, передайте ему рабочую книгу-конструктор и привяжите источник данных с помощью метода `setDataSource`.
4. **Обработайте маркеры**: вызовите метод `workbookDesigner.process()`, чтобы раскрыть смарт-маркеры и заполнить рабочую книгу фактическими данными.
5. **Сохраните результат**: сохраните полученную рабочую книгу на диск в формате XLSX или любом другом поддерживаемом формате файла.

### **Пример кода 1 — Базовый рендеринг массива строк**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        class Student {
            constructor(scores) {
                this.Scores = scores;
            }
        }
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            document.getElementById("runExample").disabled = false;
            console.log("Aspose.Cells initialized");
        });
        document.getElementById("runExample").addEventListener("click", async () => {
            const student = new Student([95, 88, 76, 100, 67]);
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Scores";
            cells.get("A2").value = student.Scores.join(" - ");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById("downloadLink");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_numericArray.xlsx";
            downloadLink.style.display = "block";
            document.getElementById("result").innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Пример кода 2 — Числовой массив с пользовательским разделителем**

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
        const { Workbook, WorkbookDesigner, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const order = {
                Items: ["Apple", "Banana", "Cherry", "Date"]
            };
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Раздел 1: Смарт-маркер по умолчанию — значения распределяются горизонтально по ячейкам
            cells.get("A1").value = "Default Spreading Behavior:";
            cells.get("A2").value = "&=Order.Items";
            // Раздел 2: Новый способ отображения в одной ячейке с использованием arrayasSingle и extraDelimiter
            cells.get("A4").value = "Single Cell Rendering (arrayasSingle=true):";
            cells.get("A5").value = '&=Order.Items(arrayasSingle=true, extraDelimiter="; ")';
            // Связать источник данных и обработать смарт-маркеры
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Order", order);
            designer.process();
            // Сохранить полученную книгу
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_comparison.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Пример кода 3 — Сравнение стандартного поведения и поведения ArrayAsSingle**

### **Примечания и рекомендации**
При работе с атрибутами `ArrayAsSingle` и `ExtraDelimiter` учитывайте следующее:
- Значение `extraDelimiter` обрабатывается как строковый литерал; экранируйте специальные символы, которые могут быть интерпретированы обработчиком шаблонов.
- Атрибут `arrayasSingle` принимает логическое значение (`true` / `false`). Только `true` включает режим размещения в одной ячейке; любое другое значение приводит к восстановлению стандартного поведения распределения элементов массива.
- Если массив пуст или имеет значение `null`, ячейка остается пустой или содержит пустую строку в зависимости от типа данных.
- Функция работает как с объектными, так и с табличными источниками данных, в которых значения столбца можно разделить на массивы.
- Для вывода значений с разделителем в виде новой строки используйте `\n` в качестве значения разделителя.

## Связанные статьи
- [Добавить поля фильтра в сводную таблицу в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/add-page-field-in-pivot-table/)
- [Применить стили к сводным таблицам в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/apply-style-to-pivot-table/)
- [Изменить макет поля страницы в сводной таблице](/cells/ru/javascript-cpp/change-page-field-layout/)
- [Преобразовать спарклайн в изображение и HTML в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Преобразование Excel в формат OFD](/cells/ru/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}