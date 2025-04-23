---
title: Добавление и извлечение данных
type: docs
weight: 20
url: /ru/java/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

В [Доступ к ячейкам листа](/cells/ru/java/accessing-cells-of-a-worksheet/) мы обсудили основные подходы для доступа к ячейкам на листе. В этой статье используется один из этих подходов для добавления различных типов данных в ячейки.

{{% /alert %}} 
## **Добавление данных в ячейки**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) содержит коллекцию [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Каждый элемент в коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) представляет объект класса [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell).

Aspose.Cells позволяет разработчикам добавлять данные в ячейки листов, вызывая свойство [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) класса [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell). Используя свойство [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value), можно добавить значение логического, строкового, вещественного, целочисленного или дата/время и т. д. в ячейку.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Повышение эффективности**
{{% alert color="primary" %}} 

Если вы используете свойство [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) для добавления большого количества данных на лист, вам следует добавлять значения в ячейки сначала по строкам, а затем по столбцам. Этот подход значительно повышает эффективность ваших приложений.

{{% /alert %}} 

При работе с листами пользователи могут добавлять различные типы данных в ячейки. Эти данные могут включать логические, целочисленные, с плавающей запятой, текстовые или дата/время значения. Вы можете получить соответствующие значения из ячеек в соответствии с их типами данных, используя Aspose.Cells.
## **Извлечение данных из ячеек**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), который представляет файл Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) содержит коллекцию [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Каждый элемент в коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) представляет объект класса [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell).

Класс [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) предоставляет несколько свойств, которые позволяют разработчикам извлекать значения из ячеек в соответствии с их типами данных. Эти свойства включают в себя:

- [StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#StringValue), значение ячейки в виде строки.
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), возвращает двойное значение ячейки.
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), логическое значение ячейки.
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), дата/время значение ячейки.
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), значение с плавающей запятой ячейки.
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), целочисленное значение ячейки.

Кроме того, тип данных, содержащихся в ячейке, можно проверить с использованием свойства [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell) класса [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell). Фактически, свойство [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell) класса [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) основано на перечислении [CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType), значения которого перечислены ниже:

|**Типы Значений Ячеек**|**Описание**|
| :- | :- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-BOOL)|Указывает, что значение ячейки является булевым.|
|[IS_DATE_TIME](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-DATE-TIME)|Указывает, что значение ячейки является датой/временем.|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-ERROR)|Представляет, что ячейка содержит ошибку|
|[IS_NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-NULL)|Представляет пустую ячейку.|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-NUMERIC)|Указывает, что значение ячейки числовое.|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-STRING)|Указывает, что значение ячейки является строкой.|
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-UNKNOWN)|Указывает, что значение ячейки неизвестно.|
Вы также можете использовать вышеуказанные предопределенные типы значений ячеек для сравнения с типом данных, содержащимся в каждой ячейке.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
{{< app/cells/assistant language="java" >}}
