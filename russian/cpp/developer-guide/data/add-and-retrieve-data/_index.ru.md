---
title: Добавление и извлечение данных
type: docs
weight: 20
url: /ru/cpp/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

В статье [Доступ к ячейкам рабочего листа](/cells/ru/cpp/accessing-cells-of-a-worksheet/) мы обсудили основные методы доступа к ячейкам в рабочем листе. В этой статье используется один из этих методов для добавления различных типов данных в ячейки.

{{% /alert %}} 
## **Добавление данных в ячейки**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), представляющий файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), позволяющую получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Каждый элемент в коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) представляет объект класса [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells позволяет разработчикам добавлять данные в ячейки рабочих листов, вызывая метод класса [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/). Aspose.Cells предоставляет перегруженные версии метода [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/), которые позволяют добавлять различные типы данных в ячейки. Используя эти перегруженные версии метода [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/), можно добавить значения логического, строкового, вещественного, целочисленного или даты/времени и т. д. в ячейку.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
### **Повышение эффективности**
Если вы используете метод [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) для вставки большого количества данных в рабочий лист, вы должны добавлять значения в ячейки сначала по строкам, а затем по столбцам. Этот подход значительно повышает эффективность ваших приложений.
## **Извлечение данных из ячеек**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), представляющий файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), позволяющую доступ к рабочим листам в файле. Рабочий лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Каждый элемент коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) представляет объект класса [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Класс [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) предоставляет несколько методов, которые позволяют разработчикам извлекать значения из ячеек в соответствии с их типами данных. К ним относятся:

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), возвращает строковое значение ячейки.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), возвращает вещественное значение ячейки.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/), возвращает логическое значение ячейки.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), возвращает дату/время значения ячейки.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), возвращает значение с плавающей точкой ячейки.
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/), возвращает целочисленное значение ячейки.

Когда поле не заполнено, ячейки с [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) или [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) вызывают исключение.

Тип данных, содержащихся в ячейке, также можно проверить с помощью метода [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) класса [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Фактически, метод [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) класса [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) основан на перечислении [CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/), чьи предопределенные значения перечислены ниже:

|**Типы Значений Ячеек**|**Описание**|
| :- | :- |
|CellValueType_IsBool|Указывает, что значение ячейки является логическим.
|CellValueType_IsDateTime|Указывает, что значение ячейки является датой/временем.
|CellValueType_IsNull|Представляет пустую ячейку.
|CellValueType_IsNumeric|Указывает, что значение ячейки является числовым.
|CellValueType_IsString|Указывает, что значение ячейки является строкой.
|CellValueType_IsUnknown|Указывает, что значение ячейки неизвестно.
Вы также можете использовать вышеупомянутые предопределенные типы значений ячеек для сравнения с типом данных, присутствующим в каждой ячейке.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
