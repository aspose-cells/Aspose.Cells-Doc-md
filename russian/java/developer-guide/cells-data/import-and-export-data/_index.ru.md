---
title: Импорт и экспорт данных
type: docs
weight: 130
url: /ru/java/import-and-export-data/
---
{{% alert color="primary" %}}

В этой статье обсуждаются некоторые методы импорта и экспорта данных, к которым у разработчиков есть доступ по номеру Aspose.Cells.

{{% /alert %}}

## Импорт данных в рабочий лист

Данные представляют мир таким, какой он есть. Чтобы разобраться в данных, мы анализируем их и понимаем мир. Данные превращаются в информацию.

Существует много способов выполнения анализа: размещение данных в электронных таблицах и различные манипуляции с ними — один из распространенных методов. С помощью Aspose.Cells легко создавать электронные таблицы, которые берут данные из ряда внешних источников и подготавливают их для анализа.

В этой статье обсуждаются некоторые методы импорта данных, к которым у разработчиков есть доступ по номеру Aspose.Cells.

### Импорт данных с помощью Aspose.Cells

Когда вы открываете файл Excel с номером Aspose.Cells, все данные в файле импортируются автоматически. Aspose.Cells также может импортировать данные из других источников данных:

- [Множество](/cells/ru/java/import-and-export-data/).
- [Список массивов](/cells/ru/java/import-and-export-data/).
- [Набор результатов](/cells/ru/java/import-and-export-data/).
- [JSON](/cells/ru/java/import-and-export-data/)

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит коллекцию[**Рабочий листКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) коллекция.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)collection предоставляет очень полезные методы для импорта данных из других источников данных. В этой статье объясняется, как можно использовать эти методы.

#### Импорт из массива

 Чтобы импортировать данные в электронную таблицу из массива, вызовите метод importArray класса[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)коллекция. Существует много перегруженных версий метода importArray, но типичная перегрузка принимает следующие параметры:

- **Множество**, объект массива, из которого вы импортируете контент.
- **Номер строки**номер строки первой ячейки, в которую будут импортированы данные.
- **Номер столбца**, номер столбца первой ячейки, в которую будут импортированы данные.
- **Вертикальный**, логическое значение, указывающее, следует ли импортировать данные вертикально или горизонтально.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Импорт из многомерных массивов

 Чтобы импортировать данные в электронную таблицу из многомерных массивов, вызовите соответствующую перегрузку importArray класса[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)коллекция:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### Импорт из ArrayList

 Чтобы импортировать данные из*ArrayList* к рабочим листам, вызовите[**Импортмассивлист**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean) ) метод[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) коллекция.[**Импортмассивлист**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) принимает следующие параметры:

- **ArrayList** ,*ArrayList*объект, содержимое которого будет импортировано.
- **Номер строки**, номер строки первой ячейки диапазона ячеек, содержимое которого будет импортировано.
- **Номер столбца**, номер столбца первой ячейки, из которой будут импортированы данные.
- **Вертикальный**— это логическое значение, указывающее, следует ли импортировать данные вертикально или горизонтально.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Импорт из пользовательских объектов в объединенную область

Чтобы импортировать данные из коллекции объектов на рабочий лист, содержащий объединенные ячейки, используйте[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)имущество. Если в шаблоне Excel есть объединенные ячейки, установите значение[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)свойство истинно. Пройти[**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)объект вместе со списком столбцов/свойств в метод для отображения желаемого списка объектов. В следующем примере кода показано использование[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)свойство для импорта данных из настраиваемых объектов в объединенные ячейки. Пожалуйста, смотрите прикрепленный[исходный файл Excel](90112035.xlsx)файл и[вывод Excel](90112036.xlsx)файл для справки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Импорт данных из JSON

 Aspose.Cells предоставляет[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) класс обработки JSON.[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) класс имеет[**Импорт данных**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) метод импорта данных JSON. Aspose.Cells также предоставляет[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)класс, представляющий параметры макета JSON.[**Импорт данных**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) метод принимает[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) как параметр.[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) класс предоставляет следующие свойства.

- [**Массив как таблица**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Указывает на то, что массив должен обрабатываться как таблица или нет.
- [**КонвертироватьЧисловойОрДате**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): Получает или задает значение, указывающее, следует ли преобразовать строку в JSON в число или дату.
- [**Формат даты**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Получает и задает формат значения даты.
- [**Игнораррайтитле**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): указывает, следует ли игнорировать заголовок, если свойство объекта является массивом
- [**ИгнорироватьНулл**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Указывает, следует ли игнорировать нулевое значение.
- [**Игнореобжекттитле**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Указывает, следует ли игнорировать заголовок, если свойство объекта является объектом.
- [**Формат номера**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Получает и задает формат числового значения.
- [**НазваниеСтиль**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Получает и задает стиль заголовка.

 Пример кода, приведенный ниже, демонстрирует использование[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) и[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) классы для импорта данных JSON.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Экспорт данных из рабочего листа

Aspose.Cells не только позволяет своим пользователям импортировать данные в рабочие листы из внешних источников данных, но также позволяет им экспортировать данные рабочего листа в массив.

### Экспорт данных с использованием Aspose.Cells - Экспорт данных в массив

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[**Рабочий листКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) коллекция.

 Данные можно легко экспортировать в объект Array с помощью[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) учебный класс'[**экспортмассив**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) метод.

#### Столбцы, содержащие строго типизированные данные

 Электронные таблицы хранят данные в виде последовательности строк и столбцов. Использовать[**экспортмассив**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) для экспорта данных из рабочего листа в массив.[**экспортмассив**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) принимает следующие параметры для экспорта данных рабочего листа в виде*Множество* объект:

- Номер строки, номер строки первой ячейки, из которой будут экспортированы данные.
- Номер столбца, номер столбца первой ячейки, откуда будут экспортированы данные
- Количество строк, количество строк для экспорта.
- Количество столбцов, количество столбцов для экспорта.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **Предварительные темы**
- [Импорт данных из объекта ResultSet базы данных Microsoft на рабочий лист](/cells/ru/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Укажите поля формулы при импорте данных на лист](/cells/ru/java/specify-formula-fields-while-importing-data-to-worksheet/)
