---
title: Создание и управление таблицами файлов Microsoft Excel.
linktitle: Таблицы
type: docs
weight: 150
url: /ru/net/create-and-format-table/
description: Вставка, изменение размера, редактирование, удаление, форматирование таблиц Excel с использованием библиотеки Aspose.Cells.
---

## **Создать таблицу**

Одним из преимуществ электронных таблиц является возможность создания различных типов списков, например, списков телефонов, списков задач, списков транзакций, активов или обязательств. Несколько пользователей могут вместе работать с созданием и поддержкой различных списков.

Aspose.Cells поддерживает создание и управление списками.

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

### **Использование API Aspose.Cells**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), представляющий файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), позволяющую получить доступ к каждому рабочему листу в файле Excel.

Лист представляет собой класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листом. Для создания [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) на листе используйте свойство коллекции [**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Каждый [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) на самом деле является объектом класса [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection), который далее предоставляет метод [**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) для добавления объекта Список и указания диапазона ячеек для списка.

Согласно указанному диапазону ячеек, объект Список создается с помощью Aspose.Cells. Используйте атрибуты (например, [**ShowTotals**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**ListColumns**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns) и т. д.) класса [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject), чтобы контролировать список.

В приведенном ниже примере мы создали тот же [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) с использованием API Aspose.Cells, что и при создании в Microsoft Excel в предыдущем разделе.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **Форматирование таблицы**

Для управления и анализа группы связанных данных можно преобразить диапазон ячеек в объект списка (также известный как таблица Excel). Таблица представляет собой серию строк и столбцов, содержащих связанные данные, управляемые независимо от данных в других строках и столбцах. По умолчанию у каждого столбца в таблице включена фильтрация в строке заголовка, чтобы можно было быстро фильтровать или сортировать данные объекта списка. Можно добавить всю строку (специальная строка в списке, предоставляющая выбор агрегатных функций, полезных для работы с числовыми данными) к объекту списка, предоставляющую раскрывающийся список агрегатных функций для каждой ячейки всей строки. Aspose.Cells предоставляет возможности для создания и управления списками (или таблицами).

### **Форматирование объекта списка**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), представляющий файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), позволяющую получить доступ к каждому рабочему листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листами. Для создания [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) на листе используйте свойство коллекции [**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Каждый [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) на самом деле является объектом класса [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection), который далее предоставляет метод [**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) для добавления объекта Список и указания диапазона ячеек, которые он должен включать. Согласно указанному диапазону ячеек, на листе создается [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) с помощью Aspose.Cells. Используйте атрибуты (например, [**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype)) класса [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) для форматирования таблицы по вашему требованию.

В следующем примере добавляются образцовые данные на лист, добавляется [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) и к нему применяются стандартные стили. Стили [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) поддерживаются в Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **Продвинутые темы**
- [Преобразовать таблицу в ODS](/cells/ru/net/convert-table-to-ods/)
- [Поиск таблиц запросов и объектов списка, связанных с внешними подключениями к данным](/cells/ru/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Чтение и запись таблицы с источником данных из запроса к таблице](/cells/ru/net/read-and-write-table-with-query-table-data-source/)
- [Установите комментарий таблицы или объекта списка внутри листа.](/cells/ru/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Таблицы и диапазоны](/cells/ru/net/tables-and-ranges/)

{{< app/cells/assistant language="csharp" >}}
