---
title: Создать и отформатировать таблицу
type: docs
weight: 10
url: /ru/cpp/create-and-format-table/
---
## **Создать таблицу**
Одним из преимуществ электронных таблиц является то, что они позволяют создавать различные типы списков, например, списки телефонов, списки задач, списки транзакций, активов или пассивов. Несколько пользователей могут работать вместе, чтобы использовать, создавать и поддерживать различные списки.

Aspose.Cells поддерживает создание списков и управление ими.
### **Преимущества объекта списка**
Преобразование списка данных в фактический объект списка дает довольно много преимуществ.

- Новые строки и столбцы включаются автоматически.
- Итоговую строку в нижней части списка можно легко добавить для отображения СУММЫ, СРЕДНЕГО, СЧЕТА и т. д.
- Столбцы, добавленные справа, автоматически включаются в объект List.
- Диаграммы на основе строк и столбцов будут расширены автоматически.
- Именованные диапазоны, назначенные строкам и столбцам, будут расширены автоматически.
- Список защищен от случайного удаления строк и столбцов.
### **Создание объекта списка с использованием Microsoft Excel**

|**Выбор диапазона данных для создания объекта List**|
|:- |
|![дело:изображение_альтернативный_текст](jHcNq4o.png)|
Отобразится диалоговое окно «Создать список».

|**Диалоговое окно «Создать список»**|
|:- |
|![дело:изображение_альтернативный_текст](kJmukRF.png)|
 Реализация объекта List для данных и указание итоговой строки (Select**Данные** , тогда**Список** , с последующим**Итоговая строка**).

|**Создание объекта списка**|
|:- |
|![дело:изображение_альтернативный_текст](ECSGVdR.png)|
### **Используя Aspose.Cells API**
 Aspose.Cells предоставляет класс[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет собой файл Excel Microsoft.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) класс содержит[IWorksheets](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Класс предоставляет широкий спектр методов для управления рабочим листом. Чтобы создать[IListObject](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object) на листе используйте[GetIListObjects](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4356bc4b8cffee624891f10ea49a4705) метод сбора[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс. Каждый `[IListObject]` на самом деле является объектом[IListObjectCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection) класс, который дополнительно обеспечивает[Добавлять](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)способ добавления объекта `[IListObject]` и указания диапазона ячеек для списка.

 В соответствии с указанным диапазоном ячеек объект `[IListObject]` создается Aspose.Cells. Используйте атрибуты (например,[ПоказатьИтоги](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a9026460927f035f374f5e1ea74e639f2) а также[СписокКолонки](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#afeeb7bfabd0971e9fe34a09f0b83ae73)д.) класса `[IListObject]` для управления списком.

В приведенном ниже примере мы создали тот же `[IListObject]`, используя Aspose.Cells API, что и мы, используя Microsoft Excel в предыдущем разделе.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects.cpp" >}}
## **Форматировать таблицу**
Для управления и анализа группы связанных данных можно превратить диапазон ячеек в объект списка (также известный как таблица Excel). Таблица — это последовательность строк и столбцов, которые содержат связанные данные, управляемые независимо от данных в других строках и столбцах. По умолчанию для каждого столбца в таблице включена фильтрация в строке заголовка, что позволяет быстро фильтровать или сортировать данные объекта списка. Вы можете добавить итоговую строку (специальную строку в списке, которая предоставляет набор агрегатных функций, полезных для работы с числовыми данными) в объект списка, который предоставляет раскрывающийся список агрегатных функций для каждой ячейки строки итогов. Aspose.Cells предоставляет параметры для создания списков (или таблиц) и управления ими.
### **Форматирование объекта списка**
 Aspose.Cells предоставляет класс[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет собой файл Excel Microsoft.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) класс содержит[IWorksheets](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Класс предоставляет широкий спектр методов для управления рабочими листами. Чтобы создать*СписокОбъект*на листе используйте `IListObjectCollection`. Каждый `[IListObject]` фактически является объектом класса `IListObjectCollection`, который дополнительно обеспечивает[Добавлять](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)метод добавления объекта `[IListObject]` и указать диапазон ячеек, который он должен охватывать. Согласно указанному диапазону ячеек,*СписокОбъект* создан на листе пользователем Aspose.Cells. Используйте атрибуты (например,[TableStyleType](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a5de8b5321b0ccb30dfb09cefe6536462)) класса `[IListObject]`, чтобы отформатировать таблицу в соответствии с вашими требованиями.

В приведенном ниже примере на лист добавляются образцы данных, добавляется `[IListObject]` и к нему применяются стили по умолчанию. `[IListObject]` стили поддерживаются Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable.cpp" >}}
