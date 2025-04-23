---
title: Фильтрация данных
type: docs
weight: 60
url: /ru/java/data-filtering/
---

{{% alert color="primary" %}}

Microsoft Excel предоставляет некоторые хорошие функции для автофильтрации данных на листе. Aspose.Cells полностью поддерживает автофильтрацию Microsoft Excel. В этой статье объясняется, как использовать функции в Microsoft Excel и как написать код для их использования с помощью Aspose.Cells.

{{% /alert %}}

## **Автофильтрация данных**

Автофильтрация - самый быстрый способ выбрать только те элементы с листа, которые вы хотите отображать в списке. Функция автофильтрации позволяет фильтровать элементы в списке в соответствии с набором критериев. Отфильтруйте на основе текста, чисел или дат.

### **Автофильтр в Microsoft Excel**

Чтобы активировать функцию автофильтра в Microsoft Excel:

1. Щелкните строку заголовка на листе.
1. На вкладке **Данные** выберите **Фильтр** и затем **Автофильтр**.

При применении автофильтра к листу появляются переключатели фильтра (черные стрелки) справа от заголовков столбцов.

1. Щелкните стрелку фильтра, чтобы увидеть список вариантов фильтра.

Некоторые из вариантов автофильтра:

|**Опции**|**Описание**|
| :- | :- |
|All|Показать все элементы в списке один раз.|
|Custom|Настроить критерии фильтрации, такие как содержит/не содержит.|
|Filter by Color|Фильтрация на основе заполненного цвета.|
|Date Filters|Фильтрация строк на основе различных критериев по дате.|
|Number Filters|Различные типы фильтров для чисел, такие как сравнение, среднее и Топ-10 и т. д.|
|Text Filters|Различные фильтры, такие как начинается с, заканчивается на, содержит и т. д.|
|Blanks/Non Blanks|Эти фильтры могут быть применены с помощью пустого текстового фильтра.|
Пользователи вручную фильтруют данные своего листа в Microsoft Excel, используя эти опции.

### **Автофильтр с Aspose.Cells**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), который позволяет получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листами. Чтобы создать автофильтр, используйте свойство [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Свойство [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) является объектом класса [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter), который предоставляет свойство [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range) для указания диапазона ячеек, составляющих строку заголовка. Автофильтр применяется к диапазону ячеек, который является строкой заголовка.

В каждом листе вы можете указать только один диапазон фильтра. Это ограничено Microsoft Excel. Для настраиваемой фильтрации данных используйте метод [**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-).

В приведенном ниже примере мы создали тот же AutoFilter, используя Aspose.Cells, что и создали с помощью Microsoft Excel в предыдущем разделе.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Различные типы фильтров**

Aspose.Cells предоставляет несколько вариантов применения различных типов фильтров, таких как Фильтр по цвету, Фильтр по дате, Фильтр по числам, Фильтр по тексту, Фильтры для заполненных ячеек и незаполненных ячеек.

##### **Цвет заливки**

Aspose.Cells предоставляет функцию [**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter-int-int-com.aspose.cells.CellsColor-com.aspose.cells.CellsColor-) для фильтрации данных на основе свойства цвета заливки ячеек. В приведенном ниже примере используется файл шаблона с различными цветами заливки в первом столбце листа для тестирования функции фильтрации по цвету. Для проверки функциональности могут быть загружены следующие файлы.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Дата**

Можно реализовать различные типы фильтров по дате, например, фильтрация всех строк с датами в январе 2018 года. Приведенный ниже образец кода демонстрирует этот фильтр с использованием функции [**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter-int-int-int-int-int-int-int-int-). Для тестирования этой функциональности можно использовать следующие файлы.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Динамическая дата**

Иногда требуются динамические фильтры на основе даты, например, все ячейки с датами в январе независимо от года. В этом случае используется функция [**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter-int-int-), как показано в следующем примере кода. Для тестирования этой функциональности можно использовать следующие файлы.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Число**

Aspose.Cells позволяет применять настраиваемые фильтры, такие как выбор ячеек с числами в заданном диапазоне. Пример ниже демонстрирует использование функции [**custom()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-) для фильтрации чисел. Примеры файлов можно загрузить по следующим ссылкам.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Текст**

Если столбец содержит текст, и требуется выбрать ячейки, содержащие определенный текст, можно использовать функцию [**filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter-int-java.lang.String-). В приведенном ниже примере файл-шаблон содержит список стран, и строка должна быть выбрана в соответствии с определенным именем страны. Приведенный ниже код демонстрирует фильтрацию текста с использованием приведенных ниже образцов файлов.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Пустые**

Если столбец содержит текст так, что некоторые ячейки пусты, и требуется выбрать только те строки, где есть пустые ячейки, можно использовать функцию [**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks-int-), как показано ниже. Примеры файлов можно загрузить по следующим ссылкам.

1. [Пустой.xlsx](72417324.xlsx)
1. [ОтфильтрованныйПустой.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Не пустые**

Когда требуется отфильтровать ячейки, содержащие любой текст, используйте функцию фильтра [**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks-int-), как показано ниже. Примеры файлов можно загрузить по следующим ссылкам.

1. [Пустой.xlsx](72417324.xlsx)
1. [ОтфильтрованныеНеПустой.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Пользовательский фильтр с содержит**

Excel предоставляет пользовательские фильтры, такие как фильтрация строк, которые содержат определенную строку. Эта функция доступна в Aspose.Cells и демонстрируется ниже путем фильтрации имен в образцовом файле. Образцы файлов можно загрузить по следующим ссылкам.

1. [ИсходныйОбразецНазванийСтран.xlsx](sourseSampleCountryNames.xlsx)
1. [ИсходныйОбразецНазванийСтран.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Пользовательский фильтр с не содержит**

Excel предоставляет пользовательские фильтры, такие как фильтрация строк, которые не содержат определенную строку. Эта функция доступна в Aspose.Cells и демонстрируется ниже путем фильтрации имен в предоставленном образце файла.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Пользовательский фильтр с начинается с**

Excel предоставляет пользовательские фильтры, такие как фильтрация строк, которые начинаются с определенной строки. Эта функция доступна в Aspose.Cells и демонстрируется ниже путем фильтрации имен в предоставленном образце файла.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Пользовательский фильтр с EndsWith**

Excel предоставляет пользовательские фильтры, такие как фильтрация строк, которые заканчиваются определенной строкой. Эта функция доступна в Aspose.Cells и демонстрируется ниже по фильтру имен в предоставленном образце файла.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Продвинутые темы**
- [Применение расширенного фильтра Microsoft Excel для отображения записей, удовлетворяющих сложным критериям](/cells/ru/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Получить все скрытые индексы строк после обновления автофильтра](/cells/ru/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

{{< app/cells/assistant language="java" >}}
