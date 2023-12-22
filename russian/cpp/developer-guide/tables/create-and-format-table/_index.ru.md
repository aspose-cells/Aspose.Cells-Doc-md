---
title: Создать и отформатировать таблицу
type: docs
weight: 10
url: /ru/cpp/create-and-format-table/
---
##  **Создать таблицу**
Одним из преимуществ электронных таблиц является то, что они позволяют создавать списки разных типов, например, списки телефонов, списки задач, списки транзакций, активов или обязательств. Несколько пользователей могут совместно использовать, создавать и поддерживать различные списки.

Aspose.Cells поддерживает создание списков и управление ими.
###  **Преимущества объекта списка**
Преобразование списка данных в реальный объект списка дает немало преимуществ.

- Новые строки и столбцы добавляются автоматически.
- Внизу списка можно легко добавить строку итогов для отображения СУММЫ, СРЗНАЧЕНИЯ, СЧЕТА и т. д.
- Столбцы, добавленные справа, автоматически включаются в объект «Список».
- Диаграммы, основанные на строках и столбцах, будут расширяться автоматически.
- Именованные диапазоны, назначенные строкам и столбцам, будут расширены автоматически.
- Список защищен от случайного удаления строк и столбцов.
###  **Создание объекта списка с помощью Microsoft Excel**

|**Выбор диапазона данных для создания объекта List**|
| :- |
|![задача: image_alt_text](jHcNq4o.png)|
Откроется диалоговое окно «Создать список».

|**Диалоговое окно «Создать список»**|
| :- |
|![задача: image_alt_text](kJmukRF.png)|
Реализация объекта List для данных и указание итоговой строки (выберите *Data**, затем *List**, а затем *Total Row**).

|**Создание объекта списка**|
| :- |
|![задача: image_alt_text](ECSGVdR.png)|
###  **Используя Aspose.Cells API**
 Aspose.Cells предоставляет класс[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) который представляет файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)коллекция, которая обеспечивает доступ к каждому листу в файле Excel.

Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Класс предоставляет широкий спектр методов для управления листом. Чтобы создать[СписокОбъект](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) на листе используйте[GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) метод сбора[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт. Каждый `[ListObject]` фактически является объектом[СписокОбъектКоллекция](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/) класс, который дополнительно обеспечивает[Добавлять](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)метод добавления объекта `[ListObject]` и указания диапазона ячеек для списка.

 В соответствии с указанным диапазоном ячеек объект `[ListObject]` создается Aspose.Cells. Используйте атрибуты (например[SetShowTotals](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/) и[GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)и т. д.) класса `[ListObject]` для управления списком.

В приведенном ниже примере мы создали тот же номер `[ListObject]`, используя Aspose.Cells API, который мы создали с помощью Microsoft Excel в приведенном выше разделе.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
##  **Форматировать таблицу**
Чтобы управлять и анализировать группу связанных данных, можно превратить диапазон ячеек в объект списка (также известный как таблица Excel). Таблица представляет собой серию строк и столбцов, содержащих связанные данные, управляемые независимо от данных в других строках и столбцах. По умолчанию для каждого столбца таблицы включена фильтрация в строке заголовка, что позволяет быстро фильтровать или сортировать данные объекта списка. Вы можете добавить итоговую строку (специальную строку в списке, которая предоставляет набор агрегатных функций, полезных для работы с числовыми данными) в объект списка, который предоставляет раскрывающийся список агрегатных функций для каждой ячейки строки итогов. Aspose.Cells предоставляет возможности для создания списков (или таблиц) и управления ими.
###  **Форматирование объекта списка**
 Aspose.Cells предоставляет класс[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) который представляет файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)коллекция, которая обеспечивает доступ к каждому листу в файле Excel.

Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Класс предоставляет широкий спектр методов для управления рабочими листами. Чтобы создать*СписокОбъект*на листе используйте `ListObjectCollection`. Каждый `[ListObject]` фактически является объектом класса `ListObjectCollection`, который дополнительно предоставляет[Добавлять](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)метод для добавления объекта `[ListObject]` и укажите диапазон ячеек, который он должен охватывать. В соответствии с указанным диапазоном ячеек,*СписокОбъект* создается на листе с номером Aspose.Cells. Используйте атрибуты (например,[Сеттаблестилетипе](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)) класса `[ListObject]`, чтобы отформатировать таблицу в соответствии с вашими требованиями.

В приведенном ниже примере на лист добавляется образец данных, добавляется номер `[ListObject]` и применяются к нему стили по умолчанию. Стили `[ListObject]` поддерживаются Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
