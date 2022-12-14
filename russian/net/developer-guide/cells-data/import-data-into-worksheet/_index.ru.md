---
title: Импорт данных в рабочий лист
type: docs
weight: 170
url: /ru/net/import-data-into-worksheet/
---
{{% alert color="primary" %}}

В этой статье обсуждаются некоторые методы импорта данных, к которым у разработчиков есть доступ по номеру Aspose.Cells.

{{% /alert %}}

## **Импорт данных в рабочий лист**

Когда вы открываете файл Excel с номером Aspose.Cells, все данные в файле импортируются автоматически. Aspose.Cells также может импортировать данные из других источников данных.

Aspose.Cells предоставляет[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс, представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)коллекция.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection предоставляет полезные методы для импорта данных из разных источников данных. В этой статье объясняется, как можно использовать эти методы.

## **Импорт данных в Excel с интерфейсом ICellsDataTable**
 Осуществлять[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) чтобы обернуть ваши различные источники данных, затем используйте[Cells.ИмпортДанные()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) для импорта данных на лист Excel.
### **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

Реализация*источник данных клиента*, *Покупатель*, а также*список клиентов* классы приведены ниже

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **Импорт из массива**

 Чтобы импортировать данные в электронную таблицу из массива, вызовите метод[**ИмпортМассив**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Существует множество перегруженных версий[**ИмпортМассив**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)метод, но типичная перегрузка принимает следующие параметры:

- **Множество**, объект массива, из которого вы импортируете контент.
- **Номер строки**номер строки первой ячейки, в которую будут импортированы данные.
- **Номер столбца**, номер столбца первой ячейки, в которую будут импортированы данные.
- **Вертикальный**, логическое значение, указывающее, следует ли импортировать данные вертикально или горизонтально.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **Импорт из ArrayList**

 Чтобы импортировать данные из*ArrayList* к рабочим листам, вызовите[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**Импортмассивлист**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)метод. Метод ImportArray принимает следующие параметры:

- **Список массивов** , представляет*ArrayList*объект, который вы импортируете.
- **Номер строки**, представляет номер строки первой ячейки, в которую будут импортированы данные.
- **Номер столбца**, представляет номер столбца первой ячейки, в которую будут импортированы данные.
- **Вертикальный**, логическое значение, указывающее, следует ли импортировать данные вертикально или горизонтально.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **Импорт из пользовательских объектов**

 Чтобы импортировать данные из коллекции объектов на рабочий лист, используйте[**Импорт пользовательских объектов**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Предоставьте методу список столбцов/свойств для отображения желаемого списка объектов.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **Импорт из пользовательских объектов в объединенную область**

Чтобы импортировать данные из коллекции объектов на рабочий лист, содержащий объединенные ячейки, используйте[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) имущество. Если в шаблоне Excel есть объединенные ячейки, установите значение[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)свойство истинно. Пройти[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) объект вместе со списком столбцов/свойств в метод для отображения желаемого списка объектов. В следующем примере кода показано использование[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) свойство для импорта данных из настраиваемых объектов в объединенные ячейки. Пожалуйста, смотрите прикрепленный[исходный файл Excel](90112033.xlsx) файл и[вывод Excel](90112034.xlsx) файл для справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **Импорт из DataTable**

 Чтобы импортировать данные из*Таблица данных* , позвоните в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**Таблица ИмпортДанных**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) метод. Существует множество перегруженных версий[**Таблица ИмпортДанных**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)метод, но типичная перегрузка принимает следующие параметры:

- **Таблица данных** ,*Таблица данных* объект, из которого вы импортируете контент.
- **Показано ли имя поля** , указывает, будут ли имена*Таблица данных*столбцы должны быть импортированы на лист как первая строка или нет.
- **Начальная ячейка** представляет имя начальной ячейки (например, «A1»), откуда импортируется содержимое*Таблица данных*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Импорт из динамического объекта в качестве источника данных**

Aspose.Cells предоставляет функции для работы с динамическими объектами в качестве источника данных. Это помогает в использовании источника данных, где свойства динамически добавляются к объектам. После добавления свойств к объекту Aspose.Cells считает первую запись шаблоном и соответствующим образом обрабатывает остальные. Это означает, что если какое-либо динамическое свойство добавляется только к первому элементу, а не к другим объектам, Aspose.Cells считает, что все элементы в коллекции должны быть одинаковыми.

В этом примере используется шаблонная модель, изначально содержащая только две переменные. Этот список преобразуется в список динамических объектов. Затем в него добавляется какое-то дополнительное поле и, наконец, загружается в книгу. Рабочая книга выбирает только те значения, которые находятся в файле шаблона XLSX. В этом шаблоне рабочей книги используются интеллектуальные маркеры, которые также содержат параметры. Параметры позволяют изменить способ размещения информации. Подробную информацию об умных маркерах можно получить из следующей статьи:

[Использование смарт-маркеров](/cells/ru/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **Импорт из DataColumn (.NET)**

А*Таблица данных*или же*Просмотр данных*объект состоит из одного или нескольких столбцов. Разработчики также могут импортировать данные из любого столбца/столбцов*Таблица данных*или же*Просмотр данных*позвонив в[**Импорт данных**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)коллекция.[**Импорт данных**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)метод принимает параметр типа[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions).[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) класс предоставляет[**Индексы столбцов**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)свойство, которое принимает массив индексов столбцов.

Пример кода, приведенный ниже, демонстрирует использование[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) для импорта выбранных столбцов.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **Импорт из DataView (.NET)**

 Чтобы импортировать данные из*Просмотр данных* , позвоните в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**Импорт данных**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) метод. Существует множество перегруженных версий[**Импорт данных**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)метод, но метод для DataView принимает следующие параметры:

- **Просмотр данных:***Просмотр данных*объект, из которого вы собираетесь импортировать содержимое.
- **Первый ряд:**номер строки первой ячейки, в которую будут импортированы данные.
- **Первая колонка:**номер столбца первой ячейки, в которую будут импортированы данные.
- **Параметры таблицы импорта:**Варианты импорта.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **Импорт из DataGrid (.NET)**

 Можно импортировать данные из*DataGrid* позвонив в[**ИмпортДатаГрид**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Существует множество перегруженных версий[**ИмпортДатаГрид**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)метод, но типичная перегрузка принимает следующие параметры:

- **Сетка данных** ,*DataGrid*объект, из которого вы импортируете содержимое.
- **Номер строки**номер строки первой ячейки, в которую будут импортированы данные.
- **Номер столбца**, номер столбца первой ячейки, в которую будут импортированы данные.
- **Вставить строки**, логическое свойство, указывающее, следует ли добавлять на лист дополнительные строки для соответствия данным или нет.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **Импорт из GridView**

 Чтобы импортировать данные из*Вид сетки* контроль, звоните[**Импортгридвиев**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)коллекция.

Aspose.Cells позволяет нам учитывать значения в формате HTML при импорте данных в электронную таблицу. Когда синтаксический анализ HTML включен при импорте данных, Aspose.Cells преобразует HTML в соответствующий формат ячейки.

## **Импорт данных в формате HTML**

 Aspose.Cells предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)класс, предоставляющий очень полезные методы для импорта данных из внешних источников данных. В этой статье показано, как анализировать текст в формате HTML при импорте данных и преобразовывать HTML в форматированные значения ячеек.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **Импорт данных из JSON**

Aspose.Cells предоставляет[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) класс для обработки JSON.[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) класс имеет[**Импорт данных**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) метод импорта данных JSON. Aspose.Cells также предоставляет[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) класс, который представляет параметры макета JSON.[**Импорт данных**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)метод принимает[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)как параметр.[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)класс предоставляет следующие свойства.

- [**Массив как таблица**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Указывает на то, что массив должен обрабатываться как таблица или нет.
- [**КонвертироватьЧисловойОрДате**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Получает или задает значение, указывающее, следует ли преобразовать строку в формате JSON в числовую или дату.
- [**Формат даты**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Получает и задает формат значения даты.
- [**Игнораррайтитле**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): указывает, следует ли игнорировать заголовок, если свойство объекта является массивом
- [**ИгнорироватьНулл**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Указывает, следует ли игнорировать нулевое значение.
- [**Игнореобжекттитле**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Указывает, следует ли игнорировать заголовок, если свойство объекта является объектом.
- [**Формат номера**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Получает и задает формат числового значения.
- [**НазваниеСтиль**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Получает и задает стиль заголовка.

Пример кода, приведенный ниже, демонстрирует использование[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) а также[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) классы для импорта данных JSON.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **Предварительные темы**
- [Укажите поля формулы при импорте данных на лист](/cells/ru/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Сдвинуть первую строку вниз при вставке Cells строк таблицы данных](/cells/ru/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
