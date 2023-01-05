---
title: Добавить и получить данные
type: docs
weight: 20
url: /ru/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 В[Доступ к Cells рабочего листа](/cells/ru/cpp/accessing-cells-of-a-worksheet/), мы обсудили основные подходы к доступу к ячейкам на листе. В этой статье используется один из этих подходов для добавления различных типов данных в ячейки.

{{% /alert %}} 
## **Добавление данных в Cells**
 Aspose.Cells предоставляет класс[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет собой файл Excel Microsoft.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) класс содержит[IWorksheets](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) класс предоставляет[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция. Каждый элемент в[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция представляет собой объект[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)учебный класс.

Aspose.Cells позволяет разработчикам добавлять данные в ячейки на листах, вызывая[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) учебный класс[путвалуе](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) метод. Aspose.Cells предоставляет перегруженные версии[путвалуе](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) метод, который позволяет разработчикам добавлять в ячейки различные типы данных. Используя эти перегруженные версии[путвалуе](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)метод, в ячейку можно добавить логические, строковые, двойные, целочисленные значения, дату/время и т. д.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells.cpp" >}}
### **Повышение эффективности**
 Если вы используете[путвалуе](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)Чтобы поместить большой объем данных на лист, вы должны добавить значения в ячейки, сначала по строкам, а затем по столбцам. Такой подход значительно повышает эффективность ваших приложений.
## **Получение данных с Cells**
 Aspose.Cells предоставляет класс[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет собой файл Excel Microsoft.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) класс содержит[IWorksheets](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) коллекция, которая позволяет получить доступ к рабочим листам в файле. Рабочий лист представлен[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) класс предоставляет[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция. Каждый элемент в[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция представляет собой объект[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)учебный класс.

[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Класс предоставляет несколько методов, которые позволяют разработчикам извлекать значения из ячеек в соответствии с их типами данных. Эти методы включают в себя:

- [GetStringValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac048c664985e2cadc2404840599d7ac3), возвращает строковое значение ячейки.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a), возвращает двойное значение ячейки.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac61870c4b1d6a68077092fb043bf8741), возвращает логическое значение ячейки.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7932b40c41141f716b096cc521113a61), возвращает значение даты/времени ячейки.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44), возвращает значение с плавающей запятой ячейки.
- [GetIntValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7acc93c97c062cbd60a7f1ab00a022d8), возвращает целочисленное значение ячейки.

 Когда поле не заполнено, ячейки с[GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a) или же[GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44)выдает исключение.

 Тип данных, содержащихся в ячейке, также можно проверить с помощью[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) учебный класс[GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) метод. Фактически,[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) учебный класс[GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) метод основан на[CellValueType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a745bf00b4815ec8dcf1bd11922fa4b62)перечисление, предопределенные значения которого перечислены ниже:

|**Cell Типы значений**|**Описание**|
|:- |:- |
|CellValueType_IsBool|Указывает, что значение ячейки является логическим.|
|CellValueType_IsDateTime|Указывает, что значением ячейки является дата/время.|
|CellValueType_IsNull|Представляет собой пустую ячейку.|
|CellValueType_IsNumeric|Указывает, что значение ячейки является числовым.|
|CellValueType_IsString|Указывает, что значение ячейки является строкой.|
|CellValueType_IsUnknown|Указывает, что значение ячейки неизвестно.|
Вы также можете использовать указанные выше предварительно определенные типы значений ячеек для сравнения с типом данных, представленных в каждой ячейке.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells.cpp" >}}
