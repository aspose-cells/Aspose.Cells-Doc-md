---
title: Изменения в общедоступном API в Aspose.Cells 8.3.1
type: docs
weight: 120
url: /ru/java/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells от версии 8.3.0 до 8.3.1, которые могут быть интересны разработчикам модулей/приложений.

{{% /alert %}} 
## **Добавленные API**
### **Добавлено свойство DataLabels.ShowCellRange**
Getter/setter для свойства ShowCellRange были добавлены в класс DataLabels для имитации функциональности Excel по форматированию меток данных диаграмм во время выполнения. Обратите внимание, что Excel предоставляет эту функцию через следующие шаги. 

1. Выберите метки данных серии и щелкните правой кнопкой мыши, чтобы открыть всплывающее меню.
1. Нажмите **Формат меток данных...** и отобразится **Параметры метки**.
1. Установите или снимите флажок **Метка содержит - значение из ячеек**.

Приведенный ниже образец кода получает метки данных серии диаграммы, а затем устанавливает метод DataLabels.setShowCellRange() в true, чтобы имитировать функцию Excel **Метка содержит - значение из ячеек**.

**Java**

{{< highlight csharp >}}

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

Пожалуйста, ознакомьтесь со статьей [Отображение диапазона ячеек в качестве меток данных](/cells/ru/java/showing-cell-range-as-the-data-labels/) для получения дополнительной информации.

{{% /alert %}} 

### **Добавлены методы Cell.getTable и ListObject.putCellValue**
Методы Cell.getTable и ListObject.putCellValue были добавлены с Aspose.Cells for Java 8.3.1 для облегчения доступа пользователей к ListObject из ячейки и добавления значений внутри него с использованием смещений строки и столбца. В приведенном ниже образце кода загружается исходная электронная таблица и добавляются значения внутри таблицы.

**Java**

{{< highlight csharp >}}

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

Пожалуйста, ознакомьтесь со статьей [Доступ к таблице из ячейки и добавление значений в ней с использованием смещений строк и столбцов](/cells/ru/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) для получения дополнительной информации.

{{% /alert %}} 

### **Добавлены методы OdsSaveOptions.isStrictSchema11 и OdsSaveOptions.setStrictSchema11**
Методы isStrictSchema11 и setStrictSchema11 были добавлены в класс OdsSaveOptions, чтобы позволить разработчикам сохранять электронную таблицу в формате, соответствующем спецификации ODF v1.2. Значение по умолчанию свойства setStrictSchema11 - false, это означает, что с версии 8.3.1 API Aspose.Cells ODS-файлы по умолчанию будут сохраняться в формате ODF версии 1.2.

Приведенный ниже отрывок кода сохраняет файл ODS в формате ODF 1.2.

**Java**

{{< highlight csharp >}}

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

Пожалуйста, ознакомьтесь со статьей [Сохранение файла ODS в спецификациях ODF 1.1 и 1.2](/cells/ru/ java/save-ods-file-in-odf-1-1-and-1-2-specifications/) для получения дополнительной информации.

{{% /alert %}} 

### **Добавлен метод SparklineCollection.add**
API Aspose.Cells добавило метод SparklineCollection.add(String dataRange, int row, int column) для указания диапазона данных и местоположения группы микрографик. Обратите внимание, что Excel предоставляет ту же функцию через следующие шаги. 

1. Выберите ячейку, содержащую ваш микрографик.
1. Выберите **Изменить данные** в разделе **Дизайн**.
1. Выберите **Изменить местоположение и данные группы**.
1. Укажите **Диапазон данных** и **Местоположение**.

Приведенный ниже образец кода загружает исходную электронную таблицу, получает первую группу микрографиков и добавляет новые диапазоны данных и местоположения для группы микрографиков. 

**Java**

{{< highlight csharp >}}

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

Пожалуйста, ознакомьтесь со статьей [Копирование микрографика с указанием диапазона данных и местоположения группы микрографиков](/cells/ru/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/) для получения дополнительной информации.

{{% /alert %}}
