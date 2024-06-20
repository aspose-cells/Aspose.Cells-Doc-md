---
title: Фильтрование объектов при загрузке книги Excel или листа
type: docs
weight: 1060
url: /ru/java/filter-objects-while-loading-workbook-or-worksheet/
---

## **Возможные сценарии использования**
Пожалуйста, используйте свойство [LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) при фильтрации данных из рабочей книги. Но если вы хотите фильтровать данные из отдельных листов, то вам придется переопределить метод [LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\)). Пожалуйста, укажите соответствующее значение из перечисления [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) при создании или работе с [LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

Перечисление [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) содержит следующие значения.

- [НЕТ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [ВСЕ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [ПУСТАЯ_ЯЧЕЙКА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [СТРОКА_ЯЧЕЙКИ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [ЧИСЛОВАЯ_ЯЧЕЙКА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [ОШИБКА_ЯЧЕЙКИ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [ЛОГИЧЕСКАЯ_ЯЧЕЙКА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [ЗНАЧЕНИЕ_ЯЧЕЙКИ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [ФОРМУЛА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [ДАННЫЕ_ЯЧЕЙКИ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [ДИАГРАММА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [ФИГУРА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [ОБЪЕДИНЕННАЯ_ОБЛАСТЬ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [УСЛОВНОЕ_ФОРМАТИРОВАНИЕ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [ПРОВЕРКА_ДАННЫХ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [СВОДНАЯ_ТАБЛИЦА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [ТАБЛИЦА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [ГИПЕРССЫЛКИ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [НАСТРОЙКИ_ЛИСТА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [ДАННЫЕ_ЛИСТА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [НАСТРОЙКИ_КНИГИ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [НАСТРОЙКИ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_СВЯЗЬ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [СТРУКТУРА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [СВОЙСТВА_ДОКУМЕНТА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [ОПРЕДЕЛЕННЫЕ_ИМЕНА](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [СТИЛЬ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Объекты фильтрации при загрузке книги**
Приведенный ниже образец кода демонстрирует, как фильтровать диаграммы из книги. Пожалуйста, проверьте [образец электронной таблицы](5472489.xlsx), использованный в этом коде, и [выходной файл PDF](5472488.pdf), созданный им. Как видно из выходного файла PDF, все диаграммы были отфильтрованы из электронной таблицы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Объекты фильтрации при загрузке листа**
Приведенный ниже образец кода загружает [исходный файл Excel](5472492.xlsx) и фильтрует следующие данные из его листов с использованием настраиваемого фильтра.

- Он фильтрует Диаграммы из листа с именем NoCharts.
- Он фильтрует формы из листа с именем NoShapes.
- Он фильтрует Условное форматирование из листа с именем NoConditionalFormatting.

После загрузки [исходного файла Excel](5472492.xlsx) с пользовательским фильтром, он берет изображения всех листов по очереди. Вот изображения для вашего справочника. Как видно, на первом изображении нет диаграмм, на втором - нет форм, а на третьем нет управляемого форматирования.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
