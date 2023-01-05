---
title: Общедоступный API Изменения в Aspose.Cells 8.4.2
type: docs
weight: 160
url: /ru/java/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

 В этом документе описаны изменения в Aspose.Cells API с версии 8.4.1 до 8.4.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы,[добавлены классы и т.д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-4-2/), но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Улучшенный механизм создания диаграмм**
Класс com.aspose.cells.charts.Chart предоставляет метод setChartDataRange для упрощения задачи создания диаграммы. Метод setChartDataRange принимает два параметра, первый из которых имеет строковый тип, указывающий область ячейки, из которой строятся ряды данных. Второй параметр имеет тип Boolean, который определяет ориентацию графика, то есть; следует ли строить ряды данных диаграммы из диапазона значений ячеек по строкам или по столбцам.

В следующем фрагменте кода показано, как создать столбчатую диаграмму с помощью нескольких строк кода, предполагая, что данные серии графиков представлены на одном листе от ячеек A1 до D4.

**Java**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **Добавлен метод VbaModuleCollection.add**
Aspose.Cells for Java 8.4.2 предоставил метод VbaModuleCollection.add для добавления нового модуля VBA в экземпляр Workbook. Метод VbaModuleCollection.add принимает параметр типа Worksheet для добавления модуля, специфичного для рабочего листа.

В следующем фрагменте кода показано, как использовать метод VbaModuleCollection.add.

**Java**

{{< highlight "csharp" >}}

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

### **Добавлен перегруженный метод Cells.copyColumns**
Aspose.Cells for Java 8.4.2 предоставляет перегруженную версию метода Cells.copyColumns для повторения исходных столбцов в месте назначения. Новый открытый метод принимает в общей сложности 5 параметров, где первые 4 параметра такие же, как и в обычном методе Cells.copyColumns. Однако последний параметр типа int указывает количество столбцов назначения, в которых должны повторяться исходные столбцы.

В следующем фрагменте кода показано, как использовать недавно открытый метод Cells.copyColumns.

**Java**

{{< highlight "csharp" >}}

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

### **Добавлены поля перечисления PasteType.DEFAULT и PasteType.ALL_EXCEPT_BORDERS**
С выпуском v8.4.2 в Aspose.Cells API добавлено 2 новых поля перечисления для PasteType, как описано ниже.

- PasteType.DEFAULT: работает аналогично функции Excel «Все» для вставки диапазона ячеек.
- PasteType.ALL_КРОМЕ_ГРАНИЦЫ: работает аналогично функции Excel «Все, кроме границ» для вставки диапазона ячеек.

Следующий пример кода демонстрирует использование поля PasteType.DEFAULT.

**Java**

{{< highlight "csharp" >}}

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

Начиная с выпуска Aspose.Cells for Java 8.4.2, поле перечисления PasteType.ALL ведет себя иначе, чем функция Excel «Все» для вставки диапазона ячеек. Теперь PasteType.ALL также копирует ширину столбца в целевой диапазон, в отличие от функции Excel «Все». Чтобы имитировать поведение Excel «Все», используйте PasteType.DEFAULT.

{{% /alert %}}
