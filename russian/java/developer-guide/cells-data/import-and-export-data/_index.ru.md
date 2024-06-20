---
title: Импорт и экспорт данных
type: docs
weight: 130
url: /ru/java/import-and-export-data/
---

{{% alert color="primary" %}}

В этой статье обсуждаются некоторые техники импорта и экспорта данных, к которым разработчики имеют доступ через Aspose.Cells.

{{% /alert %}}

## Импорт данных в лист

Данные представляют мир таким, каков он есть. Чтобы понять данные, мы анализируем их и приобретаем понимание мира. Данные превращаются в информацию.

Существует много способов анализа: одним из распространенных методов является ввод данных в электронные таблицы и их манипулирование различными способами. С Aspose.Cells легко создавать электронные таблицы, которые берут данные из ряда внешних источников и готовят их к анализу.

В этой статье обсуждаются некоторые техники импорта данных, к которым разработчики имеют доступ через Aspose.Cells.

### Импорт данных с использованием Aspose.Cells

При открытии файла Excel с помощью Aspose.Cells все данные в файле автоматически импортируются. Aspose.Cells также может импортировать данные из других источников данных:

- [Массив](/cells/ru/java/import-and-export-data/).
- [Список массивов](/cells/ru/java/import-and-export-data/).
- [Набор результатов](/cells/ru/java/import-and-export-data/).
- [JSON](/cells/ru/java/import-and-export-data/)

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит коллекцию [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets), которая позволяет получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). Коллекция [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) предоставляет очень полезные методы для импорта данных из других источников данных. В этой статье объясняется, как можно использовать эти методы.

#### Импорт из массива

Для импорта данных в таблицу из массива вызовите метод importArray коллекции [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). Существует много перегруженных версий метода importArray, но типичная перегрузка принимает следующие параметры:

- **Массив**, объект массива, из которого вы импортируете содержимое.
- **Номер строки**, номер строки первой ячейки, в которую будет импортировано содержимое.
- **Номер столбца**, номер столбца первой ячейки, в которую будет импортировано содержимое.
- **Вертикальный**, логическое значение, указывающее, следует ли импортировать данные вертикально или горизонтально.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Импорт из многомерных массивов

Чтобы импортировать данные в таблицу из многомерных массивов, вызовите соответствующую перегрузку метода importArray коллекции [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### Импорт из ArrayList

Чтобы импортировать данные из *ArrayList* в листы, вызовите метод [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) коллекции [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). Метод [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) принимает следующие параметры:

- **ArrayList**, объект *ArrayList*, содержимое которого будет импортировано.
- **Номер строки**, номер строки первой ячейки диапазона ячеек, из которого будет импортировано содержимое.
- **Номер столбца**, номер столбца первой ячейки, из которой будут импортированы данные.
- **Вертикальный**, логическое значение, указывающее, следует ли импортировать данные вертикально или горизонтально.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Импорт из пользовательских объектов в объединенную область

Чтобы импортировать данные из коллекции объектов в лист, содержащий объединенные ячейки, используйте свойство [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells). Если в шаблоне Excel есть объединенные ячейки, установите значение свойства [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) в true. Передайте объект [**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions) вместе со списком столбцов/свойств в метод для отображения выбранного списка объектов. В следующем примере кода демонстрируется использование свойства [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) для импорта данных из пользовательских объектов в объединенные ячейки. См. прикрепленные файлы [исходного Excel](90112035.xlsx) и [результирующего Excel](90112036.xlsx) для справки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Импорт данных из JSON

Aspose.Cells предоставляет класс [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) для обработки JSON. У класса [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) есть метод [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions)) для импорта данных JSON. Aspose.Cells также предоставляет класс [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions), представляющий опции макета JSON. Метод [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions)) принимает [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) в качестве параметра. Класс [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) предоставляет следующие свойства.

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Указывает, должен ли массив обрабатываться как таблица или нет.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): Получает или задает значение, указывающее, должна ли строка в JSON преобразовываться в числовую или дату.
- [**DateFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Получает и задает формат значения даты.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Указывает, следует ли игнорировать заголовок, если свойство объекта является массивом.
- [**IgnoreNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Указывает, следует ли игнорировать значение null или нет.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Указывает, следует ли игнорировать заголовок, если свойство объекта является объектом.
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Получает и задает формат числового значения.
- [**TitleStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Получает и задает стиль заголовка.

Приведенный ниже образец кода демонстрирует использование классов [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) и [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) для импорта данных из JSON.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Экспорт данных из листа

Aspose.Cells позволяет пользователям не только импортировать данные в листы из внешних источников данных, но также экспортировать данные листа в массив.

### Экспорт данных с использованием Aspose.Cells - Экспорт данных в массив

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets), позволяющий доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells).

Данные можно легко экспортировать в объект Array, используя метод [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) класса [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells).

#### Столбцы, содержащие жестко определенные данные

Таблицы сохраняют данные в виде последовательности строк и столбцов. Используйте метод [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) для экспорта данных из листа в массив. Для экспорта данных листа в объект *Array* используются следующие параметры: [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int))

- Номер строки, номер первой ячейки, из которой будет экспортированы данные.
- Номер столбца, номер первой ячейки, из которой будет экспортированы данные.
- Количество строк, количество строк для экспорта.
- Количество столбцов, количество столбцов для экспорта.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **Продвинутые темы**
- [Импорт данных из объекта результирующего набора базы данных Microsoft Access в лист](/cells/ru/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Указание формульных полей при импорте данных в рабочий лист](/cells/ru/java/specify-formula-fields-while-importing-data-to-worksheet/)
