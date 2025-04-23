---
title: Импорт данных в лист
type: docs
weight: 170
url: /ru/net/import-data-into-worksheet/
description: Узнайте, как импортировать данные в лист через API Aspose.Cells for .NET.
keywords: C# Импорт данных в лист, Импорт данных в Excel с помощью интерфейса ICellsDataTable, Импорт данных из массива, Импорт данных из ArrayList, Импорт данных из пользовательских объектов, Импорт данных из пользовательских объектов в объединенную область, Импорт данных из DataTable, Импорт данных из динамического объекта в качестве источника данных, Импорт данных из DataColumn, Импорт данных из DataView, Импорт данных из DataGrid, Импорт данных из GridView, Импорт данных в формате HTML, Импорт данных из JSON
---

{{% alert color="primary" %}}

В этой статье обсуждаются некоторые техники импорта данных, к которым разработчики имеют доступ через Aspose.Cells.

{{% /alert %}}

## **Как импортировать данные в лист**

При открытии файла Excel с помощью Aspose.Cells весь контент файла автоматически импортируется. Aspose.Cells также может импортировать данные из других источников данных.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) для доступа к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Коллекция [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) предоставляет полезные методы для импорта данных из разных источников данных. В данной статье объясняется, как можно использовать эти методы.

## **Как импортировать данные в Excel с помощью интерфейса ICellsDataTable**
Реализуйте [ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable)для упаковки различных источников данных, затем используйте [Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) для импорта данных в лист Excel.
### **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

Реализация классов *CustomerDataSource*, *Customer* и *CustomerList* представлена ниже

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **Как импортировать данные в Excel из массива**

Чтобы импортировать данные в электронную таблицу из массива, вызовите метод [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Существует множество перегруженных версий метода [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index), но типичная перегрузка принимает следующие параметры:

- **Массив**, объект массива, из которого вы импортируете содержимое.
- **Номер строки**, номер строки первой ячейки, в которую будет импортировано содержимое.
- **Номер столбца**, номер столбца первой ячейки, в которую будет импортировано содержимое.
- **Вертикальный**, логическое значение, указывающее, следует ли импортировать данные вертикально или горизонтально.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **Как импортировать данные в Excel из ArrayList**

Чтобы импортировать данные из *ArrayList* в листы, вызовите метод [**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Метод ImporArray принимает следующие параметры:

- **Список массивов**, представляет объект *ArrayList*, который вы импортируете.
- **Номер строки**, представляет номер строки первой ячейки, в которую будет импортированы данные.
- **Номер столбца**, представляет номер столбца первой ячейки, в которую будет импортированы данные.
- **Вертикальный**, логическое значение, указывающее, следует ли импортировать данные вертикально или горизонтально.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **Как импортировать данные в Excel из пользовательских объектов**

Чтобы импортировать данные из коллекции объектов в лист Excel, используйте [**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Предоставьте список столбцов/свойств методу, чтобы отобразить требуемый список объектов.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **Как импортировать данные в Excel из пользовательских объектов и проверить объединенную область**

Чтобы импортировать данные из коллекции объектов в лист Excel с объединенными ячейками, используйте свойство [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells). Если в шаблоне Excel есть объединенные ячейки, установите значение свойства [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) в true. Передайте объект [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) вместе со списком столбцов/свойств методу, чтобы отобразить требуемый список объектов. В следующем примере кода показано использование свойства [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) для импорта данных из пользовательских объектов в объединенные ячейки. Пожалуйста, обратитесь к приложенному файлу [исходного файла Excel](90112033.xlsx) и [файлу Excel с результатом](90112034.xlsx) для справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **Как импортировать данные в Excel из DataTable**

Чтобы импортировать данные из *DataTable*, вызовите метод [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекции [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index). Есть множество перегруженных версий метода [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index), но типичная перегрузка принимает следующие параметры:

- **Таблица данных**, объект *DataTable*, из которого вы импортируете содержимое.
- **Показать имя поля**, указывает, должны ли имена столбцов *DataTable* быть импортированы в лист Excel в качестве первой строки или нет.
- **Начальная ячейка**, представляет имя начальной ячейки (например, "A1"), из которой импортируется содержимое *DataTable*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Как импортировать данные в Excel из динамического объекта в качестве источника данных**

Aspose.Cells предоставляет возможности работы с динамическими объектами в качестве источника данных. Это помогает использовать источник данных, где свойства добавляются динамически к объектам. После добавления свойств к объекту Aspose.Cells рассматривает первую запись как шаблон и обрабатывает остальные соответственно. Это означает, что если к первому объекту добавлено динамическое свойство, а к другим объектам - нет, то Aspose.Cells считает, что все объекты в коллекции должны быть одинаковыми.

В этом примере используется шаблонная модель, которая изначально содержит только две переменные. Этот список преобразуется в список динамических объектов. Затем в него добавляется дополнительное поле и, наконец, загружается в рабочую книгу. Рабочая книга выбирает только те значения, которые содержатся в файле шаблона XLSX. Эта шаблонная рабочая книга использует умные маркеры, которые также содержат параметры. Параметры позволяют вам изменять способ представления информации. Подробные сведения о умных маркерах можно получить из следующей статьи:

[Использование умных маркеров](/cells/ru/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **Как импортировать DataColumn в Excel**

Объект *DataTable* или *DataView* состоит из одного или нескольких столбцов. Разработчики также могут импортировать данные из любого столбца/столбцов *DataTable* или *DataView*, вызвав метод [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Метод [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) принимает параметр типа [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). Класс [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) предоставляет свойство [**ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes), которое принимает массив индексов столбцов.

Приведенный ниже пример кода демонстрирует использование [**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) для импорта выборочных столбцов.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **Как импортировать DataView в Excel**

Чтобы импортировать данные из *DataView*, вызовите метод [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Есть множество перегруженных версий метода [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index), но одна для DataView принимает следующие параметры:

- **DataView:** Объект *DataView*, из которого вы собираетесь импортировать содержимое.
- **Первая строка:** номер строки первой ячейки, в которую будут импортированы данные.
- **Первый столбец:** номер столбца первой ячейки, в которую будут импортированы данные.
- **ImportTableOptions:** Параметры импорта.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **Как импортировать DataGrid в Excel**

Импорт данных из *DataGrid* возможен с вызовом метода [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекции [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index). Есть множество перегруженных версий метода [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index), но типичная перегрузка принимает следующие параметры:

- **Data grid**, объект *DataGrid*, из которого вы импортируете содержимое.
- **Номер строки**, номер строки первой ячейки, в которую будут импортированы данные.
- **Номер столбца**, номер столбца первой ячейки, в которую будут импортированы данные.
- **Вставить строки**, логическое свойство, указывающее, следует ли добавлять дополнительные строки на лист, чтобы вместить данные.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **Как импортировать GridView в Excel**

Для импорта данных из элемента управления *GridView* вызовите метод [**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells).

Aspose.Cells позволяет учитывать HTML-форматированные значения при импорте данных в электронную таблицу. Когда парсинг HTML разрешен при импорте данных, Aspose.Cells преобразует HTML в соответствующее форматирование ячейки.

## **Как импортировать данные в формате HTML в Excel**

Aspose.Cells предоставляет класс [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), который содержит очень полезные методы для импорта данных из внешних источников. В данной статье показано, как выполняется разбор HTML-отформатированного текста при импорте данных и преобразование HTML в отформатированные значения ячеек.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **Как импортировать данные в Excel из JSON**

Aspose.Cells предоставляет класс [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) для обработки JSON. Класс [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) содержит метод [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) для импорта данных JSON. Aspose.Cells также предоставляет класс [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions), который представляет параметры макета JSON. Метод [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) принимает [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) в качестве параметра. Класс [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) предоставляет следующие свойства:

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Указывает, должен ли массив обрабатываться как таблица или нет.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Получает или устанавливает значение, указывающее, должна ли строка в JSON быть преобразована в числовую или дату.
- [**DateFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Получает и задает формат значения даты.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Указывает, следует ли игнорировать заголовок, если свойство объекта является массивом
- [**IgnoreNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Указывает, следует ли игнорировать значение null или нет.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Указывает, следует ли игнорировать заголовок, если свойство объекта является объектом.
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Получает и задает формат числового значения.
- [**TitleStyle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Получает и задает стиль заголовка.

Приведенный ниже образец кода демонстрирует использование классов [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) и [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) для импорта данных JSON.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **Продвинутые темы**
- [Указание формульных полей при импорте данных в рабочий лист](/cells/ru/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Сдвинуть первую строку вниз при вставке строк таблицы данных ячеек](/cells/ru/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
{{< app/cells/assistant language="csharp" >}}
