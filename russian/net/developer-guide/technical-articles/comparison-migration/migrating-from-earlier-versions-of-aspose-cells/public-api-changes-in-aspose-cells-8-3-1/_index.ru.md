---
title: Изменения в общедоступном API в Aspose.Cells 8.3.1
type: docs
weight: 110
url: /ru/net/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells от версии 8.3.0 до 8.3.1, которые могут быть интересны разработчикам модулей/приложений.

{{% /alert %}} 
## **Добавленные API**
### **Добавлено свойство DataLabels.ShowCellRange**
В класс DataLabels добавлено свойство ShowCellRange для имитации функционала Excel по форматированию подписей данных диаграмм во время выполнения. Обратите внимание, что в Excel эту функцию можно использовать следующим образом. 

1. Выберите метки данных серии и щелкните правой кнопкой мыши, чтобы открыть всплывающее меню.
1. Нажмите **Формат меток данных...** и отобразится **Параметры метки**.
1. Установите или снимите флажок **Метка содержит - значение из ячеек**.

Приведенный ниже образец кода получает доступ к подписям данных серии диаграммы, а затем устанавливает метод DataLabels.ShowCellRange в true для имитации функции Excel **Подпись содержит - Значение из ячеек**.

**C#**

{{< highlight csharp >}}

 //Create workbook from the source Excel file

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.NSeries[0].DataLabels;

dataLabels.ShowCellRange = true;

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}



'Create workbook from the source Excel file

Dim m_workbook As Workbook = New Workbook("sample.xlsx")

'Access the first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the chart inside the worksheet

Dim m_chart As Chart = m_worksheet.Charts(0)

'Check the "Label Contains - Value From Cells"

Dim m_dataLabels As DataLabels = m_chart.NSeries(0).DataLabels

m_dataLabels.ShowCellRange = True

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь со статьей [Отображение диапазона ячеек в качестве подписей данных](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels) для получения дополнительной информации.

{{% /alert %}} 

### **Добавлены методы Cell.GetTable и ListObject.PutCellValue**
Методы Cell.GetTable и ListObject.PutCellValue были добавлены с Aspose.Cells for .NET 8.3.1 для удобства пользователей в получении доступа к ListObject из ячейки и добавления значений внутри него с использованием смещений строки и столбца. Ниже приведен фрагмент кода, который загружает исходную электронную таблицу и добавляет значения внутри таблицы.

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell D5 which lies inside the table

Cell cell = worksheet.Cells["D5"];

//Put value inside the cell D5

cell.PutValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.GetTable();

//Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access cell D5 which lies inside the table

Dim m_cell As Cell = m_worksheet.Cells("D5")

'Put value inside the cell D5

m_cell.PutValue("D5 Data")

'Access the Table from this cell

Dim table As ListObject = m_cell.GetTable()

'Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]")

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь со статьей [Доступ к таблице из ячейки и добавление значений внутри с использованием смещений строки и столбца](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets) для получения дополнительной информации.

{{% /alert %}} 

### **Добавлено свойство OdsSaveOptions.IsStrictSchema11**
В класс OdsSaveOptions было добавлено свойство IsStrictSchema11, чтобы позволить разработчикам сохранять электронные таблицы в формате, соответствующем спецификации ODF v1.2. Значение по умолчанию свойства IsStrictSchema11 - false, что означает, что с версии 8.3.1 API Aspose.Cells файлы ODS будут сохраняться в формате ODF версии 1.2 по умолчанию.

Приведенный ниже отрывок кода сохраняет файл ODS в формате ODF 1.2.

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some value in cell A1

Cell cell = worksheet.Cells["A1"];

cell.PutValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.Save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.IsStrictSchema11 = true;

workbook.Save("ODF1.1.ods", options);


{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Create workbook 

Dim m_workbook As Workbook = New Workbook()

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Put some value in cell A1

Dim m_cell As Cell = m_worksheet.Cells("A1")

m_cell.PutValue("Welcome to Aspose!")

'Save ODS in ODF 1.2 version which is default

Dim options As OdsSaveOptions = New OdsSaveOptions()

m_workbook.Save("ODF1.2.ods", options)

'Save ODS in ODF 1.1 version

options.IsStrictSchema11 = True

m_workbook.Save("ODF1.1.ods", options)

{{< /highlight >}}

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь со статьей [Сохранение файла ODS в спецификациях ODF 1.1 и 1.2](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications) для получения дополнительной информации.

{{% /alert %}} 

### **Добавлен метод SparklineCollection.Add**
API Aspose.Cells раскрыли метод SparklineCollection.Add(string dataRange, int row, int column) для указания диапазона данных и расположения группы мини-графиков. Обратите внимание, что Excel предоставляет аналогичную функцию следующим образом. 

1. Выберите ячейку, содержащую ваш микрографик.
1. Выберите **Изменить данные** в разделе **Дизайн**.
1. Выберите **Изменить местоположение и данные группы**.
1. Укажите **Диапазон данных** и **Местоположение**.

Приведенный ниже образец кода загружает исходную электронную таблицу, получает первую группу микрографиков и добавляет новые диапазоны данных и местоположения для группы микрографиков. 

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first sparkline group

SparklineGroup group = worksheet.SparklineGroupCollection[0];

//Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15);

group.SparklineCollection.Add("D6:O6", 5, 15);

group.SparklineCollection.Add("D7:O7", 6, 15);

group.SparklineCollection.Add("D8:O8", 7, 15);

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the first sparkline group

Dim group As SparklineGroup = m_worksheet.SparklineGroupCollection(0)

'Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15)

group.SparklineCollection.Add("D6:O6", 5, 15)

group.SparklineCollection.Add("D7:O7", 6, 15)

group.SparklineCollection.Add("D8:O8", 7, 15)

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь с статьей [Копирование мерцания, указав диапазон данных и местоположение группы мерцания](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) для получения более подробной информации.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
