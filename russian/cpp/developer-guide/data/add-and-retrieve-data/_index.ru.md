---
title: Добавить и получить данные
type: docs
weight: 20
url: /ru/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 В[Доступ к Cells рабочего листа](/cells/ru/cpp/accessing-cells-of-a-worksheet/)мы обсудили основные подходы к доступу к ячейкам на листе. В этой статье используется один из таких подходов для добавления в ячейки различных типов данных.

{{% /alert %}} 
##  **Добавление данных в номер Cells**
 Aspose.Cells предоставляет класс[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) который представляет файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) класс обеспечивает[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция. Каждый предмет в[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция представляет собой объект[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)сорт.

 Aspose.Cells позволяет разработчикам добавлять данные в ячейки на листах, вызывая[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) сорт[Путвалуе](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) метод. Aspose.Cells предоставляет перегруженные версии[Путвалуе](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) метод, который позволяет разработчикам добавлять в ячейки различные типы данных. Используя эти перегруженные версии[Путвалуе](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)В ячейку можно добавить логические, строковые, двойные, целочисленные значения, значения даты/времени и т. д.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
###  **Повышение эффективности**
 Если вы используете[Путвалуе](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)Чтобы поместить большой объем данных на лист, вам следует добавлять значения в ячейки сначала по строкам, а затем по столбцам. Такой подход значительно повышает эффективность ваших приложений.
##  **Получение данных от Cells**
 Aspose.Cells предоставляет класс[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) который представляет файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) коллекция, которая обеспечивает доступ к листам в файле. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) класс обеспечивает[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция. Каждый предмет в[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция представляет собой объект[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)сорт.

[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)Класс предоставляет несколько методов, которые позволяют разработчикам извлекать значения из ячеек в соответствии с их типами данных. Эти методы включают в себя:

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), возвращает строковое значение ячейки.
- [Получить двойное значение](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), возвращает двойное значение ячейки.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/), возвращает логическое значение ячейки.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), возвращает значение даты/времени ячейки.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), возвращает значение ячейки с плавающей запятой.
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/)возвращает целочисленное значение ячейки.

 Если поле не заполнено, ячейки с[Получить двойное значение](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) или[GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)выдает исключение.

 Тип данных, содержащихся в ячейке, также можно проверить с помощью[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) сорт[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) метод. Фактически,[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) сорт[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) метод основан на[Тип ячейкиValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/)перечисление, предварительно определенные значения которого перечислены ниже:

|**Cell Типы значений**|**Описание**|
| :- | :- |
|CellValueType_IsBool|Указывает, что значение ячейки является логическим.|
|CellValueType_IsDateTime|Указывает, что значением ячейки является дата/время.|
|CellValueType_IsNull|Представляет пустую ячейку.|
|CellValueType_IsNumeric|Указывает, что значение ячейки является числовым.|
|CellValueType_IsString|Указывает, что значение ячейки является строкой.|
|CellValueType_IsUnknown|Указывает, что значение ячейки неизвестно.|
Вы также можете использовать предварительно определенные типы значений ячеек, указанные выше, для сравнения с типом данных, присутствующих в каждой ячейке.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
