---
title: Изменения общедоступного API в Aspose.Cells 8.4.2
type: docs
weight: 150
url: /ru/net/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

В этом документе описаны изменения в API Aspose.Cells с версии 8.4.1 по 8.4.2, которые могут быть интересны для разработчиков модулей/приложений. Он включает не только новые и обновленные общедоступные методы, [добавленные классы и т. д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-4-2/), но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Улучшен механизм создания диаграмм**
Класс Aspose.Cells.Charts.Chart добавил метод SetChartDataRange для упрощения задачи создания диаграмм. Метод SetChartDataRange принимает два параметра, где первый параметр типа string указывает область ячеек, из которой надо построить ряды данных. Второй параметр типа Boolean указывает ориентацию построения диаграммы, то есть, следует ли строить ряды данных диаграммы из диапазона ячеек по строкам или по столбцам.

Следующий фрагмент кода показывает, как создать столбчатую диаграмму с помощью нескольких строк кода, предполагая, что данные рядов диаграммы находятся на том же листе, с ячейки A1 по D4.

**C#**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **Добавлен метод VbaModuleCollection.Add**
Aspose.Cells for .NET 8.4.2 добавил метод VbaModuleCollection.Add для добавления нового модуля VBA к экземпляру Workbook. Метод VbaModuleCollection.Add принимает параметр типа Worksheet для добавления модуля, связанного с рабочим листом.

В следующем фрагменте кода показано, как использовать метод VbaModuleCollection.Add.

**C#**

{{< highlight csharp >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add VBA module for first worksheet

int idx = workbook.VbaProject.Modules.Add(worksheet);

//Access the VBA Module, set its name and code

Aspose.Cells.Vba.VbaModule module = workbook.VbaProject.Modules[idx];

module.Name = "TestModule";

module.Codes = "Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub";

//Save the workbook

workbook.Save(output, SaveFormat.Xlsm);

{{< /highlight >}}


### **Добавлен перегруженный метод Cells.CopyColumns**
Aspose.Cells for .NET 8.4.2 добавил перегруженную версию метода Cells.CopyColumns для повторения исходных столбцов в назначение. Новый метод принимает в общей сложности 5 параметров, где первые 4 параметра такие же, как у обычного метода Cells.CopyColumns. Однако последний параметр типа int указывает количество целевых столбцов, на которые надо повторить исходные столбцы.

В следующем фрагменте кода показано, как использовать вновь добавленный метод Cells.CopyColumns.

**C#**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.CopyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **Добавлены перечисления полей PasteType.Default и PasteType.DefaultExceptBorders**
С выходом v8.4.2 API Aspose.Cells добавил 2 новых перечисления для PasteType, подробности ниже.

- PasteType.Default: Работает аналогично функциональности "Все" в Excel для вставки диапазона ячеек.
- PasteType.DefaultExceptBorders: Работает аналогично функциональности "Все, кроме границ" в Excel для вставки диапазона ячеек.

В следующем образце кода демонстрируется использование поля PasteType.Default.

**C#**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Create source & destination ranges

Range source = cells.CreateRange("A1:B6");

Range destination = cells.CreateRange("D1:E6");

//Copy the source range onto the destination range with everything except column widths

destination.Copy(source, new PasteOptions() { PasteType = PasteType.Default });

//Save the workbook

workbook.Save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

Начиная с выпуска Aspose.Cells for .NET 8.4.2, перечисление PasteType.All ведет себя по-другому по сравнению с функциональностью "Все" в Excel для вставки диапазона ячеек. Теперь PasteType.All также копирует ширину столбцов в целевой диапазон, в отличие от функциональности "Все" в Excel. Чтобы имитировать поведение "Все" в Excel, используйте PasteType.Default.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
