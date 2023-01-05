---
title: Общедоступный API Изменения в Aspose.Cells 8.3.1
type: docs
weight: 120
url: /ru/java/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.3.0 до 8.3.1, которые могут представлять интерес для разработчиков модулей/приложений.

{{% /alert %}} 
## **Добавлены API**
### **Добавлено свойство DataLabels.ShowCellRange.**
Метод получения/установки для свойства ShowCellRange был добавлен в класс DataLabels, чтобы имитировать функциональные возможности Excel по форматированию меток данных диаграммы во время выполнения. Обратите внимание, что Excel предоставляет эту функцию с помощью следующих шагов.

1. Выберите Метки данных серии и щелкните правой кнопкой мыши, чтобы открыть всплывающее меню.
1.  Нажмите на**Форматировать метки данных...** и это покажет**Параметры метки**.
1.  Установите или снимите флажок**Этикетка содержит — значение от Cells**.

 Приведенный ниже пример кода обращается к меткам данных серии диаграмм, а затем устанавливает для метода DataLabels.setShowCellRange() значение true, чтобы имитировать функцию Excel**Этикетка содержит — значение от Cells**.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from the source spreadsheet containing an existing chart

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.getNSeries().get(0).getDataLabels();

dataLabels.setShowCellRange(true);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Пожалуйста, проверьте статью[Отображение диапазона Cell в виде меток данных](/cells/ru/java/showing-cell-range-as-the-data-labels/) для дополнительной информации.

{{% /alert %}} 

### **Добавлены методы Cell.getTable и ListObject.putCellValue.**
Методы Cell.getTable и ListObject.putCellValue были добавлены с Aspose.Cells for Java 8.3.1, чтобы облегчить пользователям доступ к ListObject из ячейки и добавление значений внутри него, используя смещения строк и столбцов. Следующий пример кода загружает исходную электронную таблицу и добавляет значения в таблицу.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell D5 which lies inside the table

Cell cell = worksheet.getCells().get("D5");

//Put value inside the cell D5

cell.putValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.getTable();

//Add some value using Row and Column Offset

table.putCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Пожалуйста, проверьте статью[Доступ к таблице из Cell и добавление значений внутри нее с использованием смещений строк и столбцов](/cells/ru/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) для дополнительной информации.

{{% /alert %}} 

### **Добавлены методы OdsSaveOptions.isStrictSchema11 и OdsSaveOptions.setStrictSchema11.**
Методы isStrictSchema11 и setStrictSchema11 были добавлены в класс OdsSaveOptions, чтобы позволить разработчикам сохранять электронную таблицу в формате, соответствующем спецификации ODF v1.2. Значение свойства setStrictSchema11 по умолчанию равно false, что означает, что начиная с версии 8.3.1 API Aspose.Cells файлы ODS будут по умолчанию сохраняться в формате ODF версии 1.2.

Приведенный ниже фрагмент кода сохраняет файл ODS в формате ODF 1.2.

**Java**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some value in cell A1

Cell cell = worksheet.getCells().get("A1");

cell.putValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.setStrictSchema11(true);

workbook.save("ODF1.1.ods", options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Пожалуйста, проверьте статью[Сохраните файл ODS в спецификациях ODF 1.1 и 1.2.](/cells/ru/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) для дополнительной информации.

{{% /alert %}} 

### **Добавлен метод SparklineCollection.add**
 Aspose.Cells API-интерфейсы предоставили метод SparklineCollection.add(String dataRange, int row, int column) для указания диапазона данных и расположения группы Sparkline. Обратите внимание, что Excel предоставляет ту же функцию, выполнив следующие шаги.

1. Выберите ячейку, содержащую вашу спарклайн.
1.  Выбирать**Редактировать данные из спарклайна** раздел внутри**Дизайн** вкладка
1.  выберите**Изменить местоположение и данные группы**.
1.  Указать**Диапазон данных** & **Место расположения**.

 Следующий пример кода загружает исходную электронную таблицу, обращается к первой группе спарклайнов и добавляет новые диапазоны данных и местоположения для группы спарклайнов.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first sparkline group

SparklineGroup group = worksheet.getSparklineGroupCollection().get(0);

//Add Data Ranges and Locations inside this sparkline group

group.getSparklineCollection().add("D5:O5", 4, 15);

group.getSparklineCollection().add("D6:O6", 5, 15);

group.getSparklineCollection().add("D7:O7", 6, 15);

group.getSparklineCollection().add("D8:O8", 7, 15);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Пожалуйста, проверьте статью[Скопируйте спарклайн, указав диапазон данных и расположение группы спарклайнов](/cells/ru/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/) для дополнительной информации.

{{% /alert %}}
