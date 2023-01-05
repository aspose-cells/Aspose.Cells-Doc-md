---
title: Фильтрация данных
type: docs
weight: 60
url: /ru/java/data-filtering/
---
{{% alert color="primary" %}}

Microsoft Excel предоставляет несколько полезных функций для автоматической фильтрации данных рабочего листа. Aspose.Cells полностью поддерживает функции автофильтра Microsoft Excel. В этой статье объясняется, как использовать функции в Microsoft Excel и как кодировать их с помощью Aspose.Cells.

{{% /alert %}}

## **Данные автофильтра**

Автофильтрация — это самый быстрый способ выбрать на листе только те элементы, которые вы хотите отобразить в списке. Функция автофильтра позволяет пользователям фильтровать элементы в списке в соответствии с заданными критериями. Фильтровать по тексту, числам или датам.

### **Автофильтр в Microsoft Excel**

Чтобы активировать функцию автофильтра в Microsoft Excel:

1. Щелкните строку заголовка на листе.
1. От**Данные**меню, выберите**Фильтр**а потом**Автофильтр**.

Когда вы применяете автофильтр к рабочему листу, переключатели фильтров (черные стрелки) появляются справа от заголовков столбцов.

1. Щелкните стрелку фильтра, чтобы просмотреть список параметров фильтра.

Некоторые параметры автофильтра:

|**Параметры**|**Описание**|
|:- |:- |
|Все|Показать все элементы в списке один раз.|
|Обычай|Настройте критерии фильтра, такие как содержит/не содержит|
|Фильтр по цвету|Фильтры на основе заполненного цвета|
|Фильтры даты|Фильтрует строки по разным критериям по дате|
|Числовые фильтры|Различные типы фильтров по числам, такие как сравнение, средние значения, 10 лучших и т. д.|
|Текстовые фильтры|Различные фильтры, такие как начинается с, заканчивается, содержит и т. д.|
|Пустые/не пустые|Эти фильтры могут быть реализованы с помощью пустого текстового фильтра.|
Пользователи вручную фильтруют данные своих рабочих листов в Microsoft Excel, используя эти параметры.

### **Автофильтр с Aspose.Cells**

Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)класс содержит[**Рабочий листКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)который позволяет получить доступ к каждому рабочему листу в файле Excel.

Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)Класс предоставляет широкий спектр свойств и методов для управления рабочими листами. Для создания автофильтра используйте[**Автофильтр**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)собственность[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)учебный класс.[**Автофильтр**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)имущество – это объект[**Автофильтр**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)класс, который обеспечивает[**Спектр**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)свойство для указания диапазона ячеек, составляющих строку заголовка. Автофильтр применяется к диапазону ячеек, который является строкой заголовка.

На каждом листе можно указать только один диапазон фильтров. Это ограничено Microsoft Excel. Для пользовательской фильтрации данных используйте[**АвтоФильтр.Пользовательский**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) метод.

В приведенном ниже примере мы создали тот же автофильтр, используя Aspose.Cells, что и мы, используя Microsoft Excel в предыдущем разделе.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Различные типы фильтров**

Aspose.Cells предоставляет несколько вариантов для применения различных типов фильтров, таких как цветной фильтр, фильтр даты, числовой фильтр, текстовый фильтр, пустые фильтры и пустые фильтры.

##### **Цвет заливки**

Aspose.Cells предоставляет функцию[**добавитьFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)для фильтрации данных на основе свойства цвета заливки ячеек. В приведенном ниже примере файл шаблона с разными цветами заливки в первом столбце листа используется для проверки функции фильтрации цветов. Для проверки работоспособности можно загрузить следующие файлы.

1. [ColoredCells.xlsx](72417315.xlsx)
1. [FilteredColoredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Датировать**

Различные типы фильтров дат могут быть реализованы, например, фильтрация всех строк, имеющих даты в январе 2018 года. Следующий пример кода демонстрирует этот фильтр с использованием[**добавитьдатефильтр**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)) функция. Следующие файлы можно использовать для тестирования этой функциональности.

1. [Дата.xlsx](72417317.xlsx)
1. [Фильтредате.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Динамическая дата**

Иногда требуются динамические фильтры на основе даты, например, все ячейки, имеющие даты в январе, независимо от года. В таком случае,[**Динамический фильтр**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int)) используется, как показано в следующем примере кода. Следующие файлы могут быть использованы для тестирования.

1. [Дата.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Число**

Пользовательские фильтры можно применять с помощью Aspose.Cells, например, выбирать ячейки с номером в заданном диапазоне. Следующий пример демонстрирует использование[**обычай()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) для фильтрации чисел. Образцы файлов можно скачать по следующим ссылкам.

1. [Номер.xlsx](72417320.xlsx)
1. [Фильтредномер.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Текст**

Если столбец содержит текст, и необходимо выбрать ячейки, содержащие определенный текст,[**фильтр()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String)) можно использовать. В следующем примере файл шаблона содержит список стран, и необходимо выбрать строку, содержащую название конкретной страны. В следующем коде демонстрируется фильтрация текста с использованием приведенных ниже примеров файлов.

1. [Текст.xlsx](72417322.xlsx)
1. [Фильтрованный текст.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Бланки**

Если столбец содержит текст, так что несколько ячеек пусты, и фильтр требуется для выбора только тех строк, в которых присутствуют пустые ячейки,[**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int)) можно использовать, как показано ниже. Образцы файлов можно скачать по следующим ссылкам.

1. [Пустой.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Не пустые**

Когда ячейки с любым текстом должны быть отфильтрованы, используйте[**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int)) функция фильтра, как показано ниже. Образцы файлов можно скачать по следующим ссылкам.

1. [Пустой.xlsx](72417324.xlsx)
1. [Фильтреднонбланк.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Пользовательский фильтр с содержит**

Excel предоставляет настраиваемые фильтры, такие как строки фильтра, которые содержат определенную строку. Эта функция доступна в версии Aspose.Cells и демонстрируется ниже путем фильтрации имен в образце файла. Образцы файлов можно скачать по следующим ссылкам.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [аутсаурсесамплекатринамес.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Пользовательский фильтр с NotContains**

Excel предоставляет настраиваемые фильтры, такие как строки фильтра, которые не содержат какой-либо конкретной строки. Эта функция доступна в Aspose.Cells и демонстрируется ниже путем фильтрации имен в образце файла, приведенном ниже.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Пользовательский фильтр с BeginsWith**

Excel предоставляет настраиваемые фильтры, такие как строки фильтра, которые начинаются с определенной строки. Эта функция доступна в Aspose.Cells и демонстрируется ниже путем фильтрации имен в образце файла, приведенном ниже.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Пользовательский фильтр с EndsWith**

Excel предоставляет настраиваемые фильтры, такие как строки фильтра, которые заканчиваются определенной строкой. Эта функция доступна в Aspose.Cells и демонстрируется ниже путем фильтрации имен в образце файла, приведенном ниже.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Предварительные темы**
- [Применить расширенный фильтр Microsoft Excel для отображения записей, отвечающих сложным критериям](/cells/ru/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Получить все индексы скрытых строк после обновления автофильтра](/cells/ru/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

