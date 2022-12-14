---
title: Добавить и получить данные
type: docs
weight: 20
url: /ru/java/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 В[Доступ к Cells рабочего листа](/cells/ru/java/accessing-cells-of-a-worksheet/)мы обсудили основные подходы к доступу к ячейкам на листе. В этой статье используется один из этих подходов для добавления различных типов данных в ячейки.

{{% /alert %}} 
## **Добавление данных в Cells**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс предоставляет[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция. Каждый элемент в[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция представляет собой объект[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)учебный класс.

 Aspose.Cells позволяет разработчикам добавлять данные в ячейки на листах, вызывая[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) учебный класс'[установить значение](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)имущество. С помощью[установить значение](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)свойство, в ячейку можно добавить логические, строковые, двойные, целые числа или значения даты/времени и т. д.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Повышение эффективности**
{{% alert color="primary" %}} 

 Если вы используете[установить значение](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)Чтобы добавить большой объем данных на лист, вы должны добавить значения в ячейки, сначала по строкам, а затем по столбцам. Такой подход значительно повышает эффективность ваших приложений.

{{% /alert %}} 

При работе с рабочими листами пользователи могут добавлять в ячейки различные типы данных. Эти элементы данных могут включать логические значения, целые числа, числа с плавающей запятой, текст или значения даты/времени. Вы можете получить соответствующие значения из ячеек в соответствии с их типами данных, используя Aspose.Cells.
## **Получение данных с Cells**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) который представляет файл Excel.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс предоставляет[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция. Каждый элемент в[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)коллекция представляет собой объект[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)учебный класс.

[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)Класс предоставляет несколько свойств, которые позволяют разработчикам извлекать значения из ячеек в соответствии с их типами данных. Эти свойства включают в себя:

- [Строковое значение](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), строковое значение ячейки.
- [Двойное значение](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), возвращает двойное значение ячейки.
- [логическое значение](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), логическое значение ячейки.
- [ДатаВремяЗначение](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), значение даты/времени ячейки.
- [Плавающее значение](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), плавающее значение ячейки.
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), целочисленное значение ячейки.

 Кроме того, тип данных, содержащихся в ячейке, также можно проверить с помощью[Тип](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) собственность[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) учебный класс. Фактически,[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) учебный класс'[Тип](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) имущество основано на[CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType)перечисление, предопределенные значения которого перечислены ниже:

|**Cell Типы значений**|**Описание**|
|:- |:- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|Указывает, что значение ячейки является логическим.|
|[ЯВЛЯЕТСЯ_СВИДАНИЕ_ВРЕМЯ](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|Указывает, что значением ячейки является дата/время.|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|Представляет, что ячейка содержит значение ошибки|
|[НУЛЕВОЙ](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|Представляет собой пустую ячейку.|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|Указывает, что значение ячейки является числовым.|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|Указывает, что значение ячейки является строкой.|
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|Указывает, что значение ячейки неизвестно.|
Вы также можете использовать указанные выше предопределенные типы значений ячеек для сравнения с типом данных, присутствующих в каждой ячейке.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
