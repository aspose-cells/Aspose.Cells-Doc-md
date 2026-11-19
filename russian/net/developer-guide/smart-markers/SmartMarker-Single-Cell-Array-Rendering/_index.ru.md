---
title: Рендеринг массива в одной ячейке SmartMarker | Aspose.Cells for .Net
description: Узнайте, как выполнить рендеринг данных массива в одной ячейке с помощью атрибутов Smart Marker `arrayassingle` и `arraydelimiter` в Aspose.Cells for .Net.
linktitle: Рендеринг массива в одной ячейке | Aspose.Cells
url: /ru/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, библиотека .NET, электронная таблица, Smart Markers, arrayassingle, arraydelimiter, массив в одной ячейке, рендеринг массива, шаблон
type: docs
weight: 195
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
В Aspose.Cells источник данных в виде массива можно преобразовать в содержимое одной ячейки с помощью Smart Markers. Атрибут `arrayassingle` отключает стандартное распределение элементов по отдельным ячейкам, а атрибут `arraydelimiter` задает разделитель между элементами после их объединения — по умолчанию запятую либо любой указанный вами одиночный символ или многосимвольную строку в кавычках.
{{% /alert %}}

## **Введение**

Smart Markers в Aspose.Cells — это функция на основе шаблонов, которая динамически заполняет данные электронной таблицы с помощью выражений маркеров, таких как `&=DataSource.Field`. Маркер размещается в рабочей книге, подготовленной в режиме конструктора, а после обработки шаблона с помощью `WorkbookDesigner` маркеры заменяются значениями из переданного источника данных.
По умолчанию, когда Smart Marker ссылается на свойство, представляющее массив (например, `&=Product.Tags`, привязанный к `string[]` с четырьмя значениями), движок разворачивает массив и помещает каждый элемент в отдельную ячейку, последовательно размещая значения вниз по столбцу под маркером. Хотя такое поведение удобно во многих сценариях, иногда весь массив требуется отобразить в одной ячейке, объединив его элементы и разделив их выбранным разделителем.
Атрибуты `arrayassingle` и `arraydelimiter`, записываемые в скобках Smart Marker в формате `name:value`, решают именно эту задачу. Они позволяют сохранять компактную и предсказуемую структуру отчетов, одновременно обеспечивая нативную работу с источниками данных, содержащими массивы.

## **Почему необходима эта функция**

### **Стандартное поведение разбиения массива**

Когда Smart Marker ссылается на свойство, представляющее массив, Aspose.Cells по умолчанию разворачивает массив по нескольким ячейкам. Например, маркер вида `&=Product.Tags` для `string[]` с четырьмя значениями помещает каждое значение в отдельную ячейку под маркером, сдвигая остальное содержимое шаблона и потенциально нарушая тщательно продуманную структуру отчетов.

### **Ограничения стандартного применения**

Существует много практических сценариев, в которых стандартное разбиение массива нежелательно:
- **Отчеты в стиле сводки**, требующие компактной компоновки, в которой каждой записи соответствует одна строка.
- **Списки тегов, меток или ключевых слов**, которые должны отображаться в одной ячейке в виде значений, разделенных запятыми или вертикальной чертой.
- **Чипы фильтров или индикаторы состояния**, объединяющие несколько значений в одном месте для удобства чтения.
- **Последующие конвейеры обработки** (экспорт в CSV, рендеринг PDF, слияние почты), ожидающие одно объединенное значение в каждой ячейке вместо развернутого диапазона.
- **Кроссплатформенная совместимость**, при которой некоторые системы не могут работать с массивами, распределенными по нескольким ячейкам.

### **Какую проблему решает эта функция**

Без встроенного механизма разработчикам пришлось бы предварительно обрабатывать данные на C# или VB.NET, объединяя массивы в строки с разделителями перед их привязкой к `WorkbookDesigner`. Это приводит к дублированию логики, усложняет модели данных и повышает вероятность ошибок. Атрибуты `arrayassingle` и `arraydelimiter` устраняют необходимость в таком обходном решении: форматирование задается декларативно внутри самого Smart Marker.

## **Преимущества функции**

Использование атрибутов `arrayassingle` и `arraydelimiter` в Smart Markers обеспечивает несколько преимуществ:
- **Размещение в одной ячейке**: все элементы массива отображаются ровно в одной ячейке, поэтому структура остается компактной и предсказуемой.
- **Управление разделителем**: можно указать разделитель по своему выбору — запятую по умолчанию, точку с запятой, дефис, вертикальную черту или многосимвольную строку в кавычках, например `" | "`.
- **Форматирование на основе шаблона**: предварительная обработка данных не требует дополнительного кода; правила форматирования заданы внутри самого Smart Marker.
- **Более аккуратные отчеты**: данные массива больше не сдвигают соседнее содержимое шаблона в другие строки или столбцы.
- **Разнообразные типы данных**: поддерживаются строковые и числовые массивы из объектных источников данных.
- **Обратная совместимость**: если атрибуты не указаны, сохраняется исходное поведение разбиения, поэтому существующие шаблоны продолжают работать без изменений.

## **Как использовать эту функцию**

### **Синтаксис Smart Marker**

Атрибуты `arrayassingle` и `arraydelimiter` используют синтаксис атрибутов Aspose.Cells в формате `name:value` внутри скобок стандартного Smart Marker. Общий синтаксис:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

Маркер состоит из следующих частей:
- `&=DataSource.ArrayProperty` — стандартный Smart Marker, ссылающийся на свойство-массив в привязанном источнике данных.
- `arrayassingle:true` — предписывает движку отобразить весь массив в одной ячейке вместо распределения элементов по отдельным ячейкам.
- `arraydelimiter:;` — необязательный атрибут; задает разделитель между элементами массива. Если он не указан, используется запятая.

{{% alert color="warning" %}}
Указывайте атрибуты в формате `name:value` (двоеточие, а не знак равенства) и разделяйте несколько атрибутов запятой **без пробелов**. Пробел после запятой сдвигает значение, считанное анализатором, на один символ — `(arrayassingle:true, arraydelimiter:;)` приведет к объединению с ошибочным разделителем `:;` вместо `;`.
{{% /alert %}}

### **Формы разделителей**

- Одиночный символ указывается непосредственно после двоеточия: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Многосимвольный разделитель заключается в двойные кавычки: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Пошаговый порядок действий**

В следующем порядке действий показано, как отобразить массив в одной ячейке с помощью Smart Markers.
1. **Подготовьте источник данных**: создайте класс со свойством, возвращающим массив, например `string[]` или `int[]`, и привяжите `List<T>` этого класса, чтобы движок считывал по одной записи на строку.
2. **Создайте рабочую книгу конструктора**: создайте новый `Workbook`, добавьте строку заголовков и поместите ячейку со Smart Marker, ссылающимся на свойство-массив, с атрибутом `arrayassingle` (а также `arraydelimiter`, если нужен пользовательский разделитель).
3. **Создайте экземпляр `WorkbookDesigner`**: создайте `WorkbookDesigner` для рабочей книги и привяжите источник данных с помощью `SetDataSource`.
4. **Обработайте маркеры**: вызовите метод `WorkbookDesigner.Process()`, чтобы развернуть Smart Markers и заполнить книгу реальными данными.
5. **Сохраните результат**: сохраните полученную книгу на диск в формате XLSX или любом другом поддерживаемом формате файла.

### **Пример кода 1 — Базовый рендеринг строкового массива**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Product
    {
        public string[] Tags { get; set; }
    }

    static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Product", new List<Product> { product });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-single.xlsx");
    }
}
```

В примере выводится объединенное значение всего массива. Четыре тега помещаются в одну ячейку и разделяются запятой по умолчанию:

```
C#,Aspose,SmartMarker,Excel
```

### **Пример кода 2 — Числовой массив с пользовательским разделителем**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Student
    {
        public int[] Scores { get; set; }
    }

    static void Main()
    {
        Student student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        // arraydelimiter:- joins the numbers with a hyphen
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Student", new List<Student> { student });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-numeric.xlsx");
    }
}
```

Числовые массивы объединяются точно так же, как строковые, — каждый элемент сохраняет обычное текстовое представление числа:

```
95-88-76-100-67
```

### **Пример кода 3 — Сравнение стандартного рендеринга и отображения в одной ячейке**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Order
    {
        public string[] Items { get; set; }
    }

    static void Main()
    {
        Order order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        Cells cells = sheet.Cells;
        // Column B: default marker — values spread vertically down the column
        cells["B1"].PutValue("Default");
        cells["B2"].PutValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells["C1"].PutValue("Single cell");
        cells["C2"].PutValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", new List<Order> { order });
        designer.Process();
        for (int row = 1; row <= 5; row++)
        {
            string b = cells[row, 1].StringValue;
            string c = cells[row, 2].StringValue;
            if (!string.IsNullOrEmpty(b) || !string.IsNullOrEmpty(c))
                Console.WriteLine($"B{row + 1}=[{b}]  C{row + 1}=[{c}]");
        }
        workbook.Save("output-array-comparison.xlsx");
    }
}
```

Стандартный маркер заполняет отдельную ячейку для каждого элемента в столбце B, тогда как маркер с `arrayassingle` сворачивает тот же массив в одну ячейку в столбце C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Примечания и рекомендации**

При работе с атрибутами `arrayassingle` и `arraydelimiter` учитывайте следующее:
- Значения атрибутов имеют формат `name:value`. Форма со знаком равенства, например `arrayassingle=true`, не распознается, и система без предупреждения возвращает стандартное поведение разбиения.
- Разделяйте атрибуты запятой без пробелов; пробел после запятой сдвигает значение разделителя на один символ (см. предупреждение выше).
- Значением `arraydelimiter` может быть одиночный символ, записанный непосредственно после двоеточия, или многосимвольная строка в двойных кавычках.
- Если `arraydelimiter` не указан, элементы объединяются запятой.
- Источник данных должен позволять движку перечислять записи: привяжите `List<T>` (или другую коллекцию), тип элементов которой предоставляет свойство-массив. Привязка одного объекта оставляет маркеры в теле шаблона необработанными.
- Одни и те же атрибуты работают со строковыми и числовыми массивами; каждый элемент отображается в виде обычного текста своего значения.

## Связанные статьи
- [Добавить поля фильтров в сводную таблицу в Aspose.Cells для .NET](/cells/ru/net/add-page-field-in-pivot-table/)
- [Применение стилей к сводным таблицам в Aspose.Cells for .NET](/cells/ru/net/apply-style-to-pivot-table/)
- [Изменение макета поля страницы в сводной таблице](/cells/ru/net/change-page-field-layout/)
- [Преобразование спарклайнов в изображение и HTML в Aspose.Cells for .NET](/cells/ru/net/convert-sparkline-to-image-and-html/)
- [Конвертация Excel в формат OFD](/cells/ru/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}