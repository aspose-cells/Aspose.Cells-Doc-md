---
title: Создание и управление таблицами Microsoft файлов Excel.
linktitle: Столы
type: docs
weight: 150
url: /ru/net/create-and-format-table/
description: Вставка, изменение размера, редактирование, удаление, форматирование таблицы файлов Excel с использованием библиотеки Aspose.Cells.
---
## **Создать таблицу**

Одним из преимуществ электронных таблиц является то, что они позволяют создавать различные типы списков, например, списки телефонов, списки задач, списки транзакций, активов или пассивов. Несколько пользователей могут работать вместе, чтобы использовать, создавать и поддерживать различные списки.

Aspose.Cells поддерживает создание списков и управление ими.

### **Преимущества объекта списка**

Преобразование списка данных в фактический объект списка дает довольно много преимуществ.

- Новые строки и столбцы включаются автоматически.
- Итоговую строку в нижней части списка можно легко добавить для отображения СУММЫ, СРЕДНЕГО, СЧЕТА и т. д.
- Столбцы, добавленные справа, автоматически включаются в объект списка.
- Диаграммы на основе строк и столбцов будут расширены автоматически.
- Именованные диапазоны, назначенные строкам и столбцам, будут расширены автоматически.
- Список защищен от случайного удаления строк и столбцов.

### **Создание объекта списка с использованием Microsoft Excel**

- Выбор диапазона данных для создания объекта List
- Отобразится диалоговое окно «Создать список».
-  Реализуйте объект списка для данных и укажите итоговую строку (выберите**Данные** , тогда**Список** , с последующим**Итоговая строка**).

### **Используя Aspose.Cells API**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочим листом. Чтобы создать[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) на листе используйте[**СписокОбъектов**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) коллекционное имущество г.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс. Каждый[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) фактически является объектом[**КоллекцияОбъектовСписка**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) класс, который дополнительно обеспечивает[**Добавлять**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)метод для добавления объекта List и указания диапазона ячеек для списка.

По указанному диапазону ячеек создается объект Список по Aspose.Cells. Используйте атрибуты (например,[**ПоказатьИтоги**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**СписокКолонки**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns) и др.)[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)класс для управления списком.

 В приведенном ниже примере мы создали тот же[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)используя Aspose.Cells API, как мы создали с помощью Microsoft Excel в предыдущем разделе.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **Форматировать таблицу**

Для управления и анализа группы связанных данных можно превратить диапазон ячеек в объект списка (также известный как таблица Excel). Таблица — это последовательность строк и столбцов, которые содержат связанные данные, управляемые независимо от данных в других строках и столбцах. По умолчанию для каждого столбца в таблице включена фильтрация в строке заголовка, что позволяет быстро фильтровать или сортировать данные объекта списка. Вы можете добавить итоговую строку (специальную строку в списке, которая предоставляет выбор агрегатных функций, полезных для работы с числовыми данными) в объект списка, который предоставляет раскрывающийся список агрегатных функций для каждой ячейки итоговой строки. Aspose.Cells предоставляет параметры для создания списков (или таблиц) и управления ими.

### **Форматирование объекта списка**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочими листами. Чтобы создать[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) на листе используйте[**СписокОбъектов**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) коллекционное имущество г.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс. Каждый[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) фактически является объектом[**КоллекцияОбъектовСписка**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) класс, который дополнительно обеспечивает[**Добавлять**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) чтобы добавить объект List и указать диапазон ячеек, который он должен охватывать. Согласно указанному диапазону ячеек,[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)создан на листе пользователем Aspose.Cells. Используйте атрибуты (например,[**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype) ) принадлежащий[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)класс для форматирования таблицы в соответствии с вашими требованиями.

 В приведенном ниже примере на рабочий лист добавляются образцы данных, добавляется[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) и применить к нему стили по умолчанию.[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)стили поддерживаются Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **Предварительные темы**
- [Преобразование таблицы в ODS](/cells/ru/net/convert-table-to-ods/)
- [Поиск таблиц запросов и список объектов, связанных с подключениями к внешним данным](/cells/ru/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Чтение и запись таблицы с источником данных таблицы запросов](/cells/ru/net/read-and-write-table-with-query-table-data-source/)
- [Установите комментарий к таблице или объекту списка внутри рабочего листа](/cells/ru/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Таблицы и диапазоны](/cells/ru/net/tables-and-ranges/)

