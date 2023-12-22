---
title: Импортировать данные в рабочий лист
type: docs
weight: 170
url: /ru/net/import-data-into-worksheet/
description: Узнайте, как импортировать данные в рабочий лист с помощью Aspose.Cells for .NET API.
keywords: C# Import Data into Worksheet, Import data into Excel with ICellsDataTable interface, Import data from Array, Import Data from ArrayList, Import Data from Custom Objects, Import Data from Custom Objects to merged area, Import Data from DataTable, Import Data from dynamic object as data source, Import Data from DataColumn, Import Data from DataView, Import Data from DataGrid, Import Data from GridView, Import HTML formatted data, Import Data Data from JSON
---
{{% alert color="primary" %}}

В этой статье обсуждаются некоторые методы импорта данных, к которым разработчики имеют доступ по номеру Aspose.Cells.

{{% /alert %}}

##  **Как импортировать данные в рабочий лист**

Когда вы открываете файл Excel с номером Aspose.Cells, все данные в файле автоматически импортируются. Aspose.Cells также может импортировать данные из других источников данных.

Aspose.Cells предоставляет[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс, представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)коллекция.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Collection предоставляет полезные методы для импорта данных из разных источников данных. В этой статье объясняется, как можно использовать эти методы.

##  **Как импортировать данные в Excel с помощью интерфейса ICellsDataTable**
 Осуществлять[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) чтобы обернуть различные источники данных, затем используйте[Cells.ИмпортДанных()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) импортировать данные в лист Excel.
###  **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

Реализация*CustomerDataSource*, *Customer* и *CustomerList* классы приведены ниже

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


##  **Как импортировать данные в Excel из массива**

 Чтобы импортировать данные в электронную таблицу из массива, вызовите метод[**Импортировать массив**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)коллекция. Существует множество перегруженных версий[**Импортировать массив**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)метод, но типичная перегрузка принимает следующие параметры:

- *Array** — объект массива, из которого вы импортируете контент.
- *Номер строки** — номер строки первой ячейки, в которую будут импортированы данные.
- *Номер столбца** – номер столбца первой ячейки, в которую будут импортированы данные.
- *Вертикально** — логическое значение, указывающее, следует ли импортировать данные вертикально или горизонтально.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

##  **Как импортировать данные в Excel из ArrayList**

 Чтобы импортировать данные из*ArrayList* к рабочим листам, позвоните в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**ИмпортArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)метод. Метод ImportArray принимает следующие параметры:

-  *Список массивов** представляет собой*ArrayList*объект, который вы импортируете.
- *Номер строки** представляет собой номер строки первой ячейки, в которую будут импортированы данные.
- *Номер столбца** — номер столбца первой ячейки, в которую будут импортированы данные.
- *Вертикально** — логическое значение, указывающее, следует ли импортировать данные вертикально или горизонтально.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

##  **Как импортировать данные в Excel из пользовательских объектов**

 Чтобы импортировать данные из коллекции объектов на лист, используйте[**Импорт пользовательских объектов**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Предоставьте список столбцов/свойств методу для отображения желаемого списка объектов.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

##  **Как импортировать данные в Excel из пользовательских объектов в объединенную область**

Чтобы импортировать данные из коллекции объектов на лист, содержащий объединенные ячейки, используйте[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) свойство. Если в шаблоне Excel ячейки объединены, установите значение[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)свойство истинно. Пройти[**Импорттаблеопции**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) объект вместе со списком столбцов/свойств в метод для отображения желаемого списка объектов. В следующем примере кода показано использование[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) свойство для импорта данных из пользовательских объектов в объединенные ячейки. Пожалуйста, смотрите прикрепленный файл[исходный Excel](90112033.xlsx) файл и[вывод Excel](90112034.xlsx) файл для справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

##  **Как импортировать данные в Excel из DataTable**

Чтобы импортировать данные из *DataTable*, вызовите метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**Импортдататабле**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) метод. Существует множество перегруженных версий[**Импортдататабле**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)метод, но типичная перегрузка принимает следующие параметры:

-  *Таблица данных**,*Таблица данных* объект, из которого вы импортируете контент.
-  *Отображается ли имя поля**, указывает, будут ли имена полей*Таблица данных*столбцы должны быть импортированы на лист как первая строка или нет.
- *Начальная ячейка** представляет имя начальной ячейки (например, «A1»), из которой импортируется содержимое *DataTable*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

##  **Как импортировать данные в Excel из динамического объекта в качестве источника данных**

Aspose.Cells предоставляет функции для работы с динамическими объектами в качестве источника данных. Это помогает использовать источник данных, где свойства динамически добавляются к объектам. После добавления свойств к объекту Aspose.Cells считает первую запись шаблоном и соответствующим образом обрабатывает остальные. Это означает, что если какое-то динамическое свойство добавляется только к первому элементу, а не к другим объектам, Aspose.Cells считает, что все элементы в коллекции должны быть одинаковыми.

В этом примере используется шаблонная модель, которая изначально содержит только две переменные. Этот список преобразуется в список динамических объектов. Затем в него добавляется какое-то дополнительное поле и, наконец, загружается в книгу. Книга выбирает только те значения, которые находятся в файле шаблона XLSX. В этом шаблоне книги используются смарт-маркеры, которые также содержат параметры. Параметры позволяют вам изменить способ размещения информации. Подробную информацию об интеллектуальных маркерах можно получить из следующей статьи:

[Использование интеллектуальных маркеров](/cells/ru/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

##  **Как импортировать данные в Excel из DataColumn (.NET)**

A *Таблица данных*или*Просмотр данных*объект состоит из одного или нескольких столбцов. Разработчики также могут импортировать данные из любого столбца/столбцов*Таблица данных*или*Просмотр данных*позвонив в[**Импортдата**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)коллекция.[**Импортдата**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)метод принимает параметр типа[**Импорттаблеопции**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions).[**Импорттаблеопции**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) класс обеспечивает[**Индексы столбцов**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)свойство, которое принимает массив индексов столбцов.

Пример кода, приведенный ниже, демонстрирует использование[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)для импорта выборочных столбцов.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

##  **Как импортировать данные в Excel из DataView (.NET)**

 Чтобы импортировать данные из *DataView*, вызовите метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**Импортдата**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) метод. Существует множество перегруженных версий[**Импортдата**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)метод, но метод для DataView принимает следующие параметры:

- **Просмотр данных:***Просмотр данных*объект, из которого вы собираетесь импортировать контент.
- **Первая строка:**номер строки первой ячейки, в которую будут импортированы данные.
- **Первый столбец:**номер столбца первой ячейки, в которую будут импортированы данные.
- **Импорттаблеопции:**Варианты импорта.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

##  **Как импортировать данные в Excel из DataGrid (.NET)**

 Есть возможность импортировать данные из*DataGrid* позвонив в[**Импортдатагрид**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)коллекция. Существует множество перегруженных версий[**Импортдатагрид**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)метод, но типичная перегрузка принимает следующие параметры:

-  *Сетка данных**,*DataGrid*объект, из которого вы импортируете контент.
- *Номер строки** — номер строки первой ячейки, в которую будут импортированы данные.
- *Номер столбца**: номер столбца первой ячейки, в которую будут импортированы данные.
- *Вставить строки** — логическое свойство, которое указывает, следует ли добавлять на лист дополнительные строки, чтобы они соответствовали данным, или нет.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

##  **Как импортировать данные в Excel из GridView**

 Чтобы импортировать данные из*Вид сетки* контроль, позвоните в[**Импортгридвиев**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)коллекция.

Aspose.Cells позволяет нам учитывать значения в формате HTML при импорте данных в электронную таблицу. Если при импорте данных включен анализ HTML, Aspose.Cells преобразует HTML в соответствующий формат ячейки.

##  **Как импортировать данные в формате HTML в Excel**

 Aspose.Cells предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)класс, предоставляющий очень полезные методы для импорта данных из внешних источников данных. В этой статье показано, как анализировать форматированный текст HTML при импорте данных и преобразовывать HTML в форматированные значения ячеек.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

##  **Как импортировать данные в Excel с телефона JSON**

Aspose.Cells предоставляет[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) класс обработки JSON.[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) в классе есть[**Импортдата**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) метод импорта данных JSON. Aspose.Cells также предоставляет[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) класс, который представляет параметры макета JSON.[**Импортдата**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)метод принимает[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)в качестве параметра.[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)класс предоставляет следующие свойства.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): указывает, должен ли массив обрабатываться как таблица или нет.
- [**КонвертироватьНумерикОрДата**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Получает или задает значение, указывающее, должна ли строка в JSON быть преобразована в числовую форму или в дату.
- [**Формат даты**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Получает и задает формат значения даты.
- [**ИгнорироватьArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Указывает, игнорировать ли заголовок, если свойство объекта является массивом.
- [**ИгнорироватьNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Указывает, следует ли игнорировать нулевое значение или нет.
- [**Игнорировать заголовок объекта**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Указывает, игнорировать ли заголовок, если свойство объекта является объектом.
- [**Числовой формат**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Получает и устанавливает формат числового значения.
- [**НазваниеСтиль**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Получает и устанавливает стиль заголовка.

Пример кода, приведенный ниже, демонстрирует использование[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) и[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)классы для импорта данных JSON.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

##  **Предварительные темы**
- [Укажите поля формулы при импорте данных на лист](/cells/ru/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Сдвиньте первую строку вниз при вставке Cells строк таблицы данных.](/cells/ru/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
