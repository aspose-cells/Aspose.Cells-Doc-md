---
title: Изменения общедоступного API в Aspose.Cells 8.4.2
type: docs
weight: 160
url: /ru/java/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в Aspose.Cells API с версии 8.4.1 до 8.4.2, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные общедоступные методы, [добавленные классы и т. д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-4-2/), но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Улучшен механизм создания диаграмм**
Класс com.aspose.cells.charts.Chart предоставил метод setChartDataRange для упрощения задачи создания диаграмм. Метод setChartDataRange принимает два параметра, где первый параметр имеет тип string и указывает область ячеек, из которой нужно строить ряды данных. Второй параметр имеет тип Boolean и указывает ориентацию построения, то есть, строить ли ряды данных диаграммы из диапазона значений ячеек по строкам или по столбцам.

Следующий фрагмент кода показывает, как создать столбчатую диаграмму с помощью нескольких строк кода, предполагая, что данные рядов диаграммы находятся на том же листе, с ячейки A1 по D4.

**Java**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **Добавлен метод VbaModuleCollection.add**
Aspose.Cells for Java 8.4.2 предоставил метод VbaModuleCollection.add для добавления нового VBA-модуля в экземпляр Workbook. Метод VbaModuleCollection.add принимает параметр типа Worksheet для добавления модуля, специфичного для листа.

Следующий фрагмент кода показывает, как использовать метод add из коллекции VbaModuleCollection.

**Java**

{{< highlight csharp >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add VBA module

int idx = workbook.getVbaProject().getModules().add(worksheet);

//Access the VBA Module, set its name and code

VbaModule module = workbook.getVbaProject().getModules().get(idx);

module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub");

//Save the workbook

workbook.save(output, SaveFormat.XLSM);

{{< /highlight >}}

### **Перегруженный метод Cells.copyColumns добавлен**
Aspose.Cells for Java 8.4.2 добавил перегруженную версию метода Cells.copyColumns для повторения исходных столбцов в пункт назначения. Новый метод принимает общим образом 5 параметров, где первые 4 параметра такие же, как у обычного метода Cells.copyColumns. Однако последний параметр типа int указывает количество столбцов пункта назначения, на которые должны повторяться исходные столбцы.

Следующий фрагмент кода показывает, как использовать вновь добавленный метод Cells.copyColumns.

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.copyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Добавлены перечисления Fields PasteType.DEFAULT и PasteType.ALL_EXCEPT_BORDERS**
С выходом v8.4.2 API Aspose.Cells добавил 2 новых перечисления для PasteType, подробности ниже.

- PasteType.DEFAULT: Работает аналогично функции Excel "Все" для вставки диапазона ячеек.
- PasteType.ALL_EXCEPT_BORDERS: Работает аналогично функции Excel "Все кроме границ" для вставки диапазона ячеек.

Следующий образец кода демонстрирует использование поля PasteType.DEFAULT.

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Create source & destination ranges

Range source = cells.createRange("A1:B6");

Range destination = cells.createRange("D1:E6");

//Create an instance of PasteOptions and set its PasteType property

PasteOptions options = new PasteOptions();

options.setPasteType(PasteType.DEFAULT);

//Copy the source range onto the destination range with everything except column widths

destination.copy(source, options);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

Начиная с выпуска Aspose.Cells for Java 8.4.2, перечисление PasteType.ALL ведет себя по-другому по сравнению с функцией Excel "Все" для вставки диапазона ячеек. Теперь PasteType.ALL также копирует ширину столбцов в пункт назначения, в отличие от функции Excel "Все". Чтобы имитировать поведение Excel "Все", используйте PasteType.DEFAULT.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
