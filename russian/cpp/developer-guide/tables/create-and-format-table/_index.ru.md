---
title: Создание и форматирование таблицы
type: docs
weight: 10
url: /ru/cpp/create-and-format-table/
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

|**Выбор диапазона данных для создания объекта списка**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
Это отображает диалоговое окно Создать список.

|**Диалоговое окно Создать список**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
Реализация объекта списка для данных и указание общего количества строк (выберите **Данные**, затем **Список**, а затем **Общая строка**).

|**Создание объекта списка**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|
### **Использование API Aspose.Cells**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), представляющий файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), позволяющую получать доступ к каждому листу в файле Excel.

Лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет широкий спектр методов для управления листом. Для создания объекта [ListObject](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) на листе используйте метод [GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) класса [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Каждый `[ListObject]` на самом деле является объектом класса [ListObjectCollection](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/), который дополнительно предоставляет метод [Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/) для добавления объекта `[ListObject]` и указания диапазона ячеек для списка.

Согласно указанному диапазону ячеек, объект `[ListObject]` создается с использованием Aspose.Cells. Используйте атрибуты (например [SetShowTotals](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/) и [GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/) и т. д.) класса `[ListObject]` для управления списком.

В приведенном ниже примере мы создали тот же `[ListObject]` с использованием API Aspose.Cells, что и сделали с помощью Microsoft Excel в предыдущем разделе.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
## **Форматирование таблицы**
Для управления и анализа группы связанных данных можно преобразовать диапазон ячеек в объект списка (также известный как таблица Excel). Таблица представляет собой серию строк и столбцов, содержащих связанные данные, управляемые независимо от данных в других строках и столбцах. По умолчанию каждый столбец в таблице имеет включенную фильтрацию в строке заголовка, так что вы можете быстро фильтровать или сортировать ваши данные объекта списка. Вы можете добавить общую строку (специальная строка в списке, предоставляющая выбор агрегатных функций, полезных для работы с числовыми данными) в объект списка, предоставляющий выпадающий список агрегатных функций для каждой ячейки итоговой строки. Aspose.Cells предоставляет варианты для создания и управления списками (или таблицами).
### **Форматирование объекта списка**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), представляющий файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), позволяющую получать доступ к каждому листу в файле Excel.

Лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет широкий спектр методов для управления листами. Чтобы создать *ListObject* на листе, используйте `ListObjectCollection`. Каждый `[ListObject]` на самом деле является объектом класса `ListObjectCollection`, который дополнительно предоставляет метод [Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/) для добавления объекта `[ListObject]` и указания диапазона ячеек. Согласно указанному диапазону ячеек, *ListObject* создается в листе с использованием Aspose.Cells. Используйте атрибуты (например, [SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)) класса `[ListObject]` для форматирования таблицы в соответствии с вашими требованиями.

В приведенном ниже примере добавляются образцовые данные на лист, добавляется `[ListObject]` и к нему применяются стили по умолчанию. Стили `[ListObject]` поддерживаются Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
