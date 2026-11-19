---
title: Рендеринг массива в одной ячейке с помощью SmartMarker | Aspose.Cells for Node.js via Java
description: Узнайте, как отображать данные массива в одной ячейке с помощью атрибутов Smart Marker arrayassingle и arraydelimiter в Aspose.Cells for Node.js via Java.
linktitle: Рендеринг массива в одной ячейке с помощью SmartMarker | Aspose.Cells for Node.js via Java
url: /ru/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, библиотека Node.js via Java, электронная таблица, Smart Markers, arrayassingle, arraydelimiter, массив в одной ячейке, рендеринг массива, шаблон
type: docs
weight: 195
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells позволяет с помощью Smart Markers отображать источник данных, являющийся массивом, в одной ячейке. Атрибут `arrayassingle` отключает стандартное распределение элементов по отдельным ячейкам, а атрибут `arraydelimiter` задает разделитель между объединенными элементами — по умолчанию запятую либо любой указанный вами одиночный символ или заключенную в кавычки многосимвольную строку.
{{% /alert %}}

## **Введение**

Smart Markers в Aspose.Cells — функция на основе шаблонов, которая динамически заполняет данные электронной таблицы с помощью выражений маркеров, таких как `&=DataSource.Field`. Маркер размещается в рабочей книге-шаблоне, а при обработке шаблона с помощью `WorkbookDesigner` маркеры заменяются значениями из предоставленного источника данных.
По умолчанию, если Smart Marker ссылается на поле массива (например, `&=Product.Tags`, связанное с массивом из четырех значений), движок разворачивает массив и помещает каждый элемент в отдельную ячейку, распределяя значения вертикально вниз по столбцу под маркером. Хотя это поведение удобно во многих сценариях, иногда предпочтительнее отобразить весь массив в одной ячейке, объединив элементы и разделив их выбранным разделителем.
Атрибуты `arrayassingle` и `arraydelimiter`, записываемые внутри круглых скобок Smart Marker в формате `name:value`, именно удовлетворяют этому требованию. Они позволяют сохранять макеты отчетов компактными и предсказуемыми, продолжая нативно работать с источниками данных-массивами.

## **Зачем нужна эта функция**

### **Стандартное распределение элементов массива**

Если Smart Marker ссылается на поле массива, Aspose.Cells по умолчанию разворачивает массив по нескольким ячейкам. Например, маркер `&=Product.Tags` для массива из четырех значений помещает каждое значение в отдельную ячейку под маркером, сдвигая остальное содержимое шаблона и потенциально нарушая тщательно продуманные макеты отчетов.

### **Ограничения вариантов применения**

Стандартное распределение элементов не подходит во многих практических сценариях:
- **Отчеты с краткой сводкой**, требующие компактного макета с одной строкой для каждой записи.
- **Списки тегов, меток или ключевых слов**, которые необходимо отображать в одной ячейке в виде значений, разделенных запятыми или вертикальными чертами.
- **Элементы фильтрации или индикаторы состояния**, объединяющие несколько значений в одном месте для удобства чтения.
- **Последующие конвейеры обработки** (экспорт CSV, рендеринг PDF, слияние почты), ожидающие одно объединенное значение в каждой ячейке вместо развернутого диапазона.
- **Совместимость между платформами**, где некоторые получатели данных не допускают распределения массивов по нескольким ячейкам.

### **Разрыв, который устраняет эта функция**

Без встроенного механизма разработчикам пришлось бы предварительно обрабатывать данные в JavaScript — объединять массивы в строки с разделителями до их привязки к `WorkbookDesigner`. Это дублирует логику, усложняет модели данных и повышает вероятность ошибок. Атрибуты `arrayassingle` и `arraydelimiter` устраняют необходимость в таком обходном решении, выполняя форматирование декларативно непосредственно в Smart Marker.

## **Преимущества функции**

Использование атрибутов `arrayassingle` и `arraydelimiter` в Smart Markers обеспечивает несколько преимуществ:
- **Размещение в одной ячейке**: все элементы массива отображаются ровно в одной ячейке, поэтому макеты остаются компактными и предсказуемыми.
- **Управление пользовательским разделителем**: укажите нужный разделитель — запятую по умолчанию, точку с запятой, дефис, вертикальную черту или заключенную в кавычки многосимвольную строку, например `" | "`.
- **Форматирование на основе шаблона**: дополнительный код для предварительной обработки данных не требуется; правила форматирования заданы непосредственно в теге Smart Marker.
- **Более чистые отчеты**: данные массива больше не сдвигают соседнее содержимое шаблона в другие строки или столбцы.
- **Универсальные типы данных**: функция работает с массивами строк, переданными в виде строк JSON, включая числовые значения, представленные в виде строк.
- **Обратная совместимость**: если атрибуты не указаны, сохраняется исходное поведение распределения элементов, поэтому существующие шаблоны продолжают работать без изменений.

## **Как использовать эту функцию**

### **Синтаксис Smart Marker**

Атрибуты `arrayassingle` и `arraydelimiter` используют синтаксис атрибутов Aspose.Cells в формате `name:value` внутри круглых скобок стандартного Smart Marker. Общий синтаксис:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

Маркер состоит из следующих частей:
- `&=DataSource.ArrayField` — стандартный Smart Marker, ссылающийся на поле массива в привязанном источнике данных.
- `arrayassingle:true` — указывает движку отображать весь массив в одной ячейке вместо распределения элементов.
- `arraydelimiter:;` — необязательный атрибут, задающий разделитель между элементами массива. Если он не указан, используется запятая.

{{% alert color="warning" %}}
Записывайте атрибуты в формате `name:value` (двоеточие, а не знак равенства) и разделяйте несколько атрибутов запятой **без пробелов**. Пробел после запятой сдвигает разобранное значение на один символ — в `(arrayassingle:true, arraydelimiter:;)` элементы будут объединены с ошибочным разделителем `:;` вместо `;`.
{{% /alert %}}

### **Формы разделителей**

- Одиночный символ записывается сразу после двоеточия: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Многосимвольный разделитель заключается в двойные кавычки: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Пошаговый порядок действий**

Следующий порядок действий описывает, как отобразить массив в одной ячейке с помощью Smart Markers.
1. **Подготовьте источник данных**: подготовьте каждую запись в виде объекта JSON, поле которого содержит массив, например `{"Tags": ["C#", "Aspose"]}`. Простые объекты и массивы JavaScript, переданные в `setDataSource`, на этой платформе не привязываются — поддерживается табличное представление в виде строк JSON.
2. **Создайте книгу-шаблон**: создайте новый `Workbook`, добавьте строку заголовков и поместите в ячейку Smart Marker, ссылающийся на поле массива и содержащий атрибут `arrayassingle` (а также `arraydelimiter`, если нужен пользовательский разделитель).
3. **Создайте экземпляр WorkbookDesigner**: создайте `WorkbookDesigner` для этой книги и присоедините строки JSON с помощью `setJsonDataSource`.
4. **Обработайте маркеры**: вызовите метод `workbookDesigner.process()`, чтобы развернуть Smart Markers и заполнить книгу реальными данными.
5. **Сохраните результат**: сохраните полученную книгу на диск в формате XLSX или любом другом поддерживаемом формате файлов.

### **Пример кода 1 — отображение строкового массива**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Tags");
// No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-single.xlsx");
```

В примере выводится объединенное значение всего массива. Четыре тега помещаются в одну ячейку и разделяются запятой по умолчанию:

```
C#,Aspose,SmartMarker,Excel
```

### **Пример кода 2 — числовые значения с пользовательским разделителем**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Scores");
// arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-numeric.xlsx");
```

Если оценки переданы в виде строк JSON, объединенный результат сохраняет обычные числа:

```
95-88-76-100-67
```

{{% alert color="note" %}}
Числа в JSON, проходящие через движок Java, поступают как числа типа `double`, поэтому `[95, 88]` объединятся как `95.0-88.0`. Заключайте числа в кавычки в строках JSON, если в объединенной ячейке требуется точный текст целого числа.
{{% /alert %}}

### **Пример кода 3 — сравнение стандартного и одиночного отображения**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();
// Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default");
cells.get("B2").putValue("&=Order.Items");
// Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell");
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]');
designer.process();
for (let row = 1; row <= 5; row++) {
    const b = cells.get(row, 1).getStringValue() || "";
    const c = cells.get(row, 2).getStringValue() || "";
    if (b || c) console.log(`B${row + 1}=[${b}]  C${row + 1}=[${c}]`);
}
workbook.save("output-array-comparison.xlsx");
```

Маркер по умолчанию заполняет одну ячейку для каждого элемента в столбце B, тогда как маркер с `arrayassingle` объединяет тот же массив в одну ячейку в столбце C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Примечания и рекомендации**

При работе с атрибутами `arrayassingle` и `arraydelimiter` учитывайте следующее:
- Значения атрибутов записываются в формате `name:value`. Формат со знаком равенства, например `arrayassingle=true`, не распознается, и система без предупреждения возвращается к стандартному распределению элементов.
- Разделяйте атрибуты запятой без пробелов; пробел после запятой сдвигает значение разделителя на один символ (см. предупреждение выше).
- Значение `arraydelimiter` может быть одиночным символом, записанным непосредственно после двоеточия, или многосимвольной строкой в двойных кавычках.
- Если `arraydelimiter` не указан, элементы объединяются с помощью запятой.
- Передавайте поля массива через объекты строк в `setJsonDataSource`; простые объекты и массивы JavaScript, переданные в `setDataSource`, на этой платформе не привязываются.
- Числа JSON поступают через движок Java как числа типа `double` (`95` объединяется как `95.0`); заключайте числовые значения в кавычки в строках JSON, если важен точный текст целого числа.
- Размещайте Smart Marker в ячейке достаточной ширины для отображения полученной объединенной строки; в противном случае содержимое может визуально переходить в соседние ячейки в зависимости от формата.

## Связанные статьи
- [Добавить поля фильтров в сводную таблицу в Aspose.Cells for Node.js via Java](/cells/ru/nodejs-java/add-page-field-in-pivot-table/)
- [Применение стилей к сводным таблицам в Aspose.Cells for Node.js via Java](/cells/ru/nodejs-java/apply-style-to-pivot-table/)
- [Изменение макета поля страницы в сводной таблице](/cells/ru/nodejs-java/change-page-field-layout/)
- [Преобразование спарклайнов в изображения и HTML в Aspose.Cells for Node.js via Java](/cells/ru/nodejs-java/convert-sparkline-to-image-and-html/)
- [Конвертация Excel в формат OFD](/cells/ru/nodejs-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="nodejs-java" >}}