---
title: Создание и управление таблицами файлов Microsoft Excel.
linktitle: Таблицы
type: docs
weight: 150
url: /ru/python-net/create-and-format-table/
description: Вставка, изменение размера, редактирование, удаление, форматирование таблиц Excel с использованием библиотеки Aspose.Cells.
---

## **Создать таблицу**

Одним из преимуществ электронных таблиц является возможность создания различных типов списков, например, списков телефонов, списков задач, списков транзакций, активов или обязательств. Несколько пользователей могут вместе работать с созданием и поддержкой различных списков.

Aspose.Cells для Python via .NET поддерживает создание и управление списками.

### **Преимущества объекта списка**

Существует несколько преимуществ при преобразовании списка данных в фактический объект списка

- Новые строки и столбцы автоматически включаются.
- Итоговая строка внизу списка легко добавляется для отображения SUM, AVERAGE, COUNT и т. д.
- Добавленные столбцы справа автоматически включаются в объект списка.
- Графики, основанные на строках и столбцах, будут автоматически расширены.
- Именованные диапазоны, присвоенные строкам и столбцам, будут автоматически расширены.
- Список защищен от случайного удаления строк и столбцов.

### **Создание объекта списка с использованием Microsoft Excel**

- Выбор диапазона данных для создания объекта Список
- Это отображает диалоговое окно Создания списка.
- Реализация объекта Список для данных и указание итоговой строки (Выберите **Данные**, затем **Список**, затем **Итоговая строка**).

### **Использование API Aspose.Cells для Python via .NET**

Aspose.Cells для Python via .NET предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию, которая позволяет получать доступ к каждому листу в файле Excel.

Лист представляет собой класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листом. Для создания [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) на листе используйте свойство коллекции [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Каждый [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) на самом деле является объектом класса [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool), который далее предоставляет метод [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) для добавления объекта Список и указания диапазона ячеек для списка.

В соответствии с указанным диапазоном ячеек объект List создается с помощью Aspose.Cells для Python via .NET. Используйте атрибуты (например, [**show_totals**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/show_totals), [**ListColumns**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/list_columns) и т.д.) класса [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) для управления списком.

В приведенном ниже примере мы создали тот же [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) с помощью API Aspose.Cells для Python via .NET, как мы создали, используя Microsoft Excel в предыдущем разделе.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-CreatingListObject-1.py" >}}

## **Форматирование таблицы**

Чтобы управлять и анализировать группу связанных данных, можно преобразовать диапазон ячеек в объект списка (также известный как таблица Excel). Таблица — это серия строк и столбцов, содержащих связанные данные, управляемые независимо от данных в других строках и столбцах. По умолчанию в каждой колонке таблицы включена фильтрация в строке заголовка, чтобы вы могли быстро фильтровать или сортировать данные своего объекта. Вы можете добавить строку итогов (специальную строку в списке, которая предоставляет набор агрегатных функций, полезных для работы с числовыми данными) в объект списка, которая предоставляет выпадающий список агрегатных функций для каждой ячейки строки итогов. Aspose.Cells для Python via .NET предоставляет возможности для создания и управления списками (или таблицами).

### **Форматирование объекта списка**

Aspose.Cells для Python via .NET предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая позволяет обращаться к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листами. Для создания [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) на листе используйте свойство коллекции [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Каждый [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) на самом деле является объектом класса [**ListObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection), который далее предоставляет метод [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) для добавления объекта Список и указания диапазона ячеек, которые он должен включать. Согласно указанному диапазону ячеек, на листе создается [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) с помощью Aspose.Cells. Используйте атрибуты (например, [**table_style_type**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/table_style_type)) класса [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) для форматирования таблицы по вашему требованию.

В следующем примере добавляются образцовые данные на лист, добавляется [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) и к нему применяются стандартные стили. Стили [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) поддерживаются в Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FormataListObject-1.py" >}}

## **Продвинутые темы**
- [Преобразовать таблицу в ODS](/cells/ru/python-net/convert-table-to-ods/)
- [Поиск таблиц запросов и объектов списка, связанных с внешними подключениями к данным](/cells/ru/python-net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Чтение и запись таблицы с источником данных из запроса к таблице](/cells/ru/python-net/read-and-write-table-with-query-table-data-source/)
- [Установите комментарий таблицы или объекта списка внутри листа.](/cells/ru/python-net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Таблицы и диапазоны](/cells/ru/python-net/tables-and-ranges/)


{{< app/cells/assistant language="python-net" >}}
