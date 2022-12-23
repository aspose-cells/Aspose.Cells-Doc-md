---
title: Фильтровать объекты при загрузке книги или листа
type: docs
weight: 1060
url: /ru/java/filter-objects-while-loading-workbook-or-worksheet/
---
## **Возможные сценарии использования**
 Пожалуйста, используйте[LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) свойство при фильтрации данных из книги. Но если вы хотите фильтровать данные с отдельных рабочих листов, вам придется переопределить[LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\) ) метод. Укажите соответствующее значение из[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) перечисление при создании или работе с[Загрузить фильтр](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)перечисление имеет следующие значения.

- [НИКТО](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [ВСЕ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELL_BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELL_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELL_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [CELL_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELL_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [CELL_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [ФОРМУЛА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [CELL_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [ДИАГРАММА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [ФОРМА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [MERGED_AREA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [УСЛОВНО_ФОРМАТИРОВАНИЕ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [ВАЛИДАЦИЯ ДАННЫХ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [PIVOT_TABLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [ТАБЛИЦА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [ГИПЕРССЫЛКИ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [ЛИСТ_НАСТРОЙКИ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [SHEET_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [BOOK_SETTINGS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [НАСТРОЙКИ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_MAP](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [СТРУКТУРА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [СВОЙСТВА ДОКУМЕНТА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [DEFINED_NAMES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [СТИЛЬ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Фильтровать объекты при загрузке книги**
 В следующем примере кода показано, как фильтровать диаграммы из книги. Пожалуйста, проверьте[образец эксель файла](5472489.xlsx) используется в этом коде и[вывод PDF](5472488.pdf)порожденный им. Как вы можете видеть в выводе PDF, все диаграммы были отфильтрованы из рабочей книги.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Фильтровать объекты при загрузке листа**
 Следующий пример кода загружает[исходный файл excel](5472492.xlsx) и фильтрует следующие данные из своих рабочих листов, используя настраиваемый фильтр.

- Он фильтрует диаграммы из рабочего листа с именем NoCharts.
- Он фильтрует фигуры из рабочего листа с именем NoShapes.
- Он фильтрует условное форматирование из листа с именем NoConditionalFormatting.

 Один раз он загружает[исходный файл excel](5472492.xlsx) с пользовательским фильтром он берет изображения всех рабочих листов одно за другим. Вот выходные изображения для справки. Как видите, на первом изображении нет диаграмм, на втором изображении нет фигур, а на третьем изображении нет условного форматирования.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
