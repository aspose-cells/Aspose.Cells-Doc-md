---
title: Отрисовка массива в одной ячейке с помощью SmartMarker | Aspose.Cells for Java
description: Узнайте, как с помощью атрибутов смарт-маркера arrayassingle и arraydelimiter в Aspose.Cells for Java отрисовать данные массива в одной ячейке.
linktitle: Отрисовка массива в одной ячейке | Aspose.Cells
url: /ru/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, библиотека Java, электронная таблица, смарт-маркеры, arrayassingle, arraydelimiter, массив в одной ячейке, отрисовка массива, шаблон
type: docs
weight: 195
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells позволяет с помощью смарт-маркеров отрисовать источник данных массива в одну ячейку. Атрибут `arrayassingle` отключает стандартное поэлементное распределение, а атрибут `arraydelimiter` задаёт разделитель между объединёнными элементами — по умолчанию запятую либо любой указанный вами одиночный символ или многосимвольную строку в кавычках.
{{% /alert %}}

## **Введение**

Смарт-маркеры в Aspose.Cells — это функция на основе шаблонов, которая динамически заполняет данные электронной таблицы с помощью выражений маркеров, таких как `&=DataSource.Field`. Маркер размещается в книге-конструкторе, а после обработки шаблона с помощью `WorkbookDesigner` маркеры заменяются значениями из предоставленного источника данных.
По умолчанию, когда смарт-маркер ссылается на свойство массива (например, `&=Product.Tags`, связанный с `String[]` из четырёх значений), механизм разворачивает массив и помещает каждый элемент в отдельную ячейку, распределяя значения вертикально вниз по столбцу под маркером. Хотя такое поведение удобно во многих сценариях, иногда предпочтительно отрисовать весь массив в одной ячейке, объединив его элементы и разделив их выбранным разделителем.
Атрибуты `arrayassingle` и `arraydelimiter`, записываемые в круглых скобках смарт-маркера в формате `name:value`, в полной мере отвечают этому требованию. Они позволяют сохранять компактные и предсказуемые макеты отчётов, сохраняя при этом нативную работу с источниками данных массивов.

## **Почему необходима эта функция**

### **Стандартное распределение массива**

Когда смарт-маркер ссылается на свойство массива, Aspose.Cells по умолчанию разворачивает массив по нескольким ячейкам. Например, маркер `&=Product.Tags`, связанный с `String[]` из четырёх значений, помещает каждое значение в отдельную ячейку под маркером, сдвигая остальное содержимое шаблона и потенциально нарушая тщательно продуманные макеты отчётов.

### **Ограничения вариантов использования**

Стандартное распределение не подходит во многих практических сценариях:
- **Отчёты в стиле сводок**, которым необходим компактный макет с одной строкой для каждой записи.
- **Списки тегов, меток или ключевых слов**, которые необходимо отображать в одной ячейке в виде значений, разделённых запятыми или вертикальными чертами.
- **Фильтры-метки или индикаторы состояния**, объединяющие несколько значений в одном месте для удобства чтения.
- **Последующие конвейеры обработки** (экспорт в CSV, отрисовка PDF, слияние почты), ожидающие одно объединённое значение в каждой ячейке вместо развёрнутого диапазона.
- **Кроссплатформенная совместимость**, поскольку некоторые получатели не допускают массивов, выходящих за пределы одной ячейки.

### **Какую проблему это решает**

Без встроенного механизма разработчикам пришлось бы предварительно обрабатывать данные в Java — объединять массивы в строки с разделителями перед их привязкой к книге-конструктору. Это дублирует логику, усложняет модели данных и повышает вероятность ошибок. Атрибуты `arrayassingle` и `arraydelimiter` устраняют необходимость в таком обходном решении, декларативно выполняя форматирование непосредственно в смарт-маркере.

## **Преимущества функции**

Использование атрибутов `arrayassingle` и `arraydelimiter` в смарт-маркерах даёт несколько преимуществ:
- **Содержание в одной ячейке**: Все элементы массива отрисовываются ровно в одной ячейке, сохраняя компактность и предсказуемость макетов.
- **Управление разделителем**: Укажите нужный разделитель — запятую по умолчанию, точку с запятой, дефис, вертикальную черту или многосимвольную строку в кавычках, например `" | "`.
- **Форматирование на основе шаблона**: Для предварительной обработки данных не требуется дополнительный код; правила форматирования задаются внутри тега смарт-маркера.
- **Более чистые отчёты**: Данные массива больше не сдвигают соседнее содержимое шаблона в другие строки или столбцы.
- **Разнообразие типов данных**: Работает с массивами строк и числовыми значениями, представленными в виде строк, из источников данных на основе компонентов JavaBean.
- **Обратная совместимость**: Если атрибуты не указаны, сохраняется исходное поведение распределения, поэтому существующие шаблоны продолжают работать без изменений.

## **Как использовать эту функцию**

### **Синтаксис смарт-маркера**

Атрибуты `arrayassingle` и `arraydelimiter` используют синтаксис атрибутов Aspose.Cells в формате `name:value` внутри круглых скобок стандартного смарт-маркера. Общий синтаксис:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

Маркер состоит из следующих частей:
- `&=DataSource.ArrayProperty` — стандартный смарт-маркер, ссылающийся на свойство массива в связанном источнике данных.
- `arrayassingle:true` — предписывает механизму отрисовать весь массив в одной ячейке вместо распределения его элементов.
- `arraydelimiter:;` — необязательный атрибут; задаёт разделитель между элементами массива. Если он не указан, используется запятая.

{{% alert color="warning" %}}
Записывайте атрибуты в формате `name:value` (двоеточие, а не знак равенства) и разделяйте несколько атрибутов запятой **без пробелов**. Пробел после запятой сдвигает разбираемое значение на один символ: `(arrayassingle:true, arraydelimiter:;)` приведёт к объединению с ошибочным разделителем `:;` вместо `;`.
{{% /alert %}}

### **Формы разделителя**

- Одиночный символ записывается непосредственно после двоеточия: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Многосимвольный разделитель записывается в двойных кавычках: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Пошаговый рабочий процесс**

Следующий порядок действий описывает, как отрисовать массив в одной ячейке с помощью смарт-маркеров.
1. **Подготовьте источник данных**: Создайте `public` класс компонента с геттером, возвращающим массив, например `String[] getTags()`, и свяжите `java.util.List` таких компонентов, чтобы механизм считывал по одной записи на строку. Одних публичных полей самих по себе недостаточно для привязки — механизм читает геттеры JavaBean.
2. **Создайте книгу-конструктор**: Создайте новый `Workbook`, добавьте строку заголовков и поместите ячейку со смарт-маркером, ссылающимся на свойство массива, с атрибутом `arrayassingle` (а также `arraydelimiter`, если нужен пользовательский разделитель).
3. **Создайте экземпляр WorkbookDesigner**: Создайте `WorkbookDesigner` для этой книги и свяжите свой список с помощью `setDataSource`.
4. **Обработайте маркеры**: Вызовите метод `WorkbookDesigner.process()`, чтобы развернуть смарт-маркеры и заполнить книгу фактическими данными.
5. **Сохраните результат**: Сохраните полученную книгу на диск в формате XLSX или любом другом поддерживаемом формате файлов.

### **Пример кода 1 — базовая отрисовка массива строк**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    // The bean must be public and expose a getter; public fields bind nothing
    public static class Product {
        private String[] tags;
        public String[] getTags() { return tags; }
        public void setTags(String[] tags) { this.tags = tags; }
    }

    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.setTags(new String[] { "C#", "Aspose", "SmartMarker", "Excel" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Product", Arrays.asList(product));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-single.xlsx");
    }
}
```

В примере выводится объединённое значение всего массива. Четыре тега попадают в одну ячейку и разделяются запятой по умолчанию:

```
C#,Aspose,SmartMarker,Excel
```

### **Пример кода 2 — числовые значения с пользовательским разделителем**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Student {
        private String[] scores;
        public String[] getScores() { return scores; }
        public void setScores(String[] scores) { this.scores = scores; }
    }

    public static void main(String[] args) throws Exception {
        Student student = new Student();
        student.setScores(new String[] { "95", "88", "76", "100", "67" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Scores");
        // arraydelimiter:- joins the values with a hyphen
        worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Student", Arrays.asList(student));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-numeric.xlsx");
    }
}
```

Числовые значения объединяются так же, как строки, если свойство массива возвращает `String[]`:

```
95-88-76-100-67
```

{{% alert color="note" %}}
Сохраняйте тип свойства массива как `String[]` в Java. Примитивное свойство `int[]`, объединённое в одну ячейку, отображает текст toString объекта массива (например, `[I@1a2b3c4d`), а не числа, поскольку объединение работает со строковым представлением каждого элемента, а примитивный массив является одним непрозрачным элементом.
{{% /alert %}}

### **Пример кода 3 — сравнение стандартного режима и отрисовки в одной ячейке**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Order {
        private String[] items;
        public String[] getItems() { return items; }
        public void setItems(String[] items) { this.items = items; }
    }

    public static void main(String[] args) throws Exception {
        Order order = new Order();
        order.setItems(new String[] { "Apple", "Banana", "Cherry", "Date" });
        Workbook workbook = new Workbook();
        Cells cells = workbook.getWorksheets().get(0).getCells();
        // Column B: default marker — values spread vertically down the column
        cells.get("B1").putValue("Default");
        cells.get("B2").putValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells.get("C1").putValue("Single cell");
        cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Order", Arrays.asList(order));
        designer.process();
        for (int row = 1; row <= 5; row++) {
            String b = cells.get(row, 1).getStringValue();
            String c = cells.get(row, 2).getStringValue();
            if (b != null && !b.isEmpty() || c != null && !c.isEmpty())
                System.out.println("B" + (row + 1) + "=[" + b + "]  C" + (row + 1) + "=[" + c + "]");
        }
        workbook.save("output-array-comparison.xlsx");
    }
}
```

Стандартный маркер заполняет одну ячейку для каждого элемента вниз по столбцу B, тогда как маркер `arrayassingle` объединяет тот же массив в одной ячейке столбца C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Примечания и рекомендации**

При работе с атрибутами `arrayassingle` и `arraydelimiter` учитывайте следующее:
- Значения атрибутов используют формат `name:value`. Форма со знаком равенства, например `arrayassingle=true`, не распознаётся, и механизм молча возвращается к стандартному поведению распределения.
- Разделяйте атрибуты запятой без пробелов; пробел после запятой сдвигает значение разделителя на один символ (см. предупреждение выше).
- Значение `arraydelimiter` может быть одиночным символом, записанным непосредственно после двоеточия, или многосимвольной строкой в двойных кавычках.
- Если `arraydelimiter` не указан, элементы объединяются запятой.
- Связывайте `java.util.List` публичных компонентов JavaBean с геттерами массивов. Один объект компонента или одни только публичные поля оставляют маркеры неразрешёнными.
- Сохраняйте свойства массивов в типе `String[]`; примитивный `int[]` при объединении отображает текст метода toString (см. примечание выше).
- Помещайте смарт-маркер в ячейку достаточной ширины для отображения полученной объединённой строки; в противном случае содержимое может визуально перетекать в соседние ячейки в зависимости от формата.

## Связанные статьи
- [Добавление полей фильтрации в сводную таблицу с помощью Aspose.Cells for Java](/cells/ru/java/add-page-field-in-pivot-table/)
- [Применение стилей к сводным таблицам в Aspose.Cells for Java](/cells/ru/java/apply-style-to-pivot-table/)
- [Изменение макета поля страницы в сводной таблице](/cells/ru/java/change-page-field-layout/)
- [Преобразование спарклайнов в изображения и HTML в Aspose.Cells for Java](/cells/ru/java/convert-sparkline-to-image-and-html/)
- [Конвертация Excel в формат OFD](/cells/ru/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}