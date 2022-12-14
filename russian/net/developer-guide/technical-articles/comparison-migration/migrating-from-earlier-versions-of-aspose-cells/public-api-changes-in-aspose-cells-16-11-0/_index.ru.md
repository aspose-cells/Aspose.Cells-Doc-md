---
title: Общедоступный API Изменения в Aspose.Cells 16.11.0
type: docs
weight: 350
url: /ru/net/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 16.10.0 до 16.11.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка настроек глобализации**
Aspose.Cells 16.11.0 предоставил класс GlobalizationSettings вместе со свойством WorkbookSettings.GlobalizationSettings, чтобы заставить API Aspose.Cells использовать настраиваемые метки для промежуточных итогов. Класс GlobalizationSettings имеет следующие методы, которые можно переопределить в пользовательской реализации, чтобы дать нужные имена меткам.**Общий** & **Общий итог**.

- GlobalizationSettings.GetTotalName: получает общее имя функции.
- GlobalizationSettings.GetGrandTotalName: получает общее имя функции.

Вот простой пользовательский класс, который расширяет класс GlobalizationSettings и переопределяет его вышеупомянутые методы, чтобы возвращать пользовательские метки для функции консолидации Average.

**C#**

{{< highlight "csharp" >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "AVG";

            default:

                return base.GetTotalName(functionType);

        }

    }

    public override string GetGrandTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "GRD AVG";

            default:

                return base.GetGrandTotalName(functionType);

        }

    }

}

{{< /highlight >}}



Следующий фрагмент загружает существующую электронную таблицу и добавляет промежуточный итог типа «Среднее» к данным, уже доступным на листе. Класс CustomSettings и его методы GetTotalName и GetGrandTotalName будут вызываться во время добавления промежуточного итога на рабочий лист.

**C#**

{{< highlight "csharp" >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[]{ 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



Класс GlobalizationSettings также предлагает метод GetOtherName, который полезен для получения имени метки «Другое» для круговых диаграмм. Вот простой сценарий использования метода GlobalizationSettings.GetOtherName.

**C#**

{{< highlight "csharp" >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetOtherName()

    {

        int lcid = System.Globalization.CultureInfo.CurrentCulture.LCID;

        switch (lcid)

        {

            case 1033:

                return "Other";

            case 1036:

                return "Autre";

            case 1031:

                return "Andere";

            //Do other case

            default:

                return base.GetOtherName();

        }

    }

}

{{< /highlight >}}



Следующий фрагмент загружает существующую электронную таблицу, содержащую круговую диаграмму, и отображает диаграмму в изображение с использованием созданного выше класса CustomSettings.

**C#**

{{< highlight "csharp" >}}

 // Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.Worksheets[0];

// Accesses the 1st chart from the collection

Chart chart = sheet.Charts[0];

// Refreshes the chart

chart.Calculate();

// Renders the chart to image

chart.ToImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}


### **Добавлен класс CellsFactory**
Aspose.Cells 16.11.0 предоставил класс CellsFactory, который в настоящее время имеет один метод, то есть; Создать стиль. Метод CellsFactory.CreateStyle можно использовать для создания экземпляра класса Style без добавления его в пул стилей рабочей книги.

Вот простой сценарий использования метода CellsFactory.CreateStyle.

**C#**

{{< highlight "csharp" >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Добавлено свойство Workbook.AbsolutePath**
Aspose.Cells 16.11.0 предоставило свойство Workbook.AbsolutePath, позволяющее получить или установить абсолютный путь к книге, хранящийся в файле workbook.xml. Это свойство полезно только при обновлении внешних ссылок.
### **Добавлен метод GridHyperlinkCollection.GetHyperlink.**
Aspose.Cells.GridWeb 16.11.0 предоставляет метод GetHyperlink классу GridHyperlinkCollection, который позволяет получить экземпляр GridHyperlink путем передачи экземпляра GridCell или пары целых чисел, соответствующих индексам столбца строки.

{{% alert color="primary" %}} 

Если в указанной ячейке гиперссылка не найдена, метод GetHyperlink вернет значение null.

{{% /alert %}} 

Вот простой сценарий использования метода GetHyperlink.

**C#**

{{< highlight "csharp" >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **Устаревшие API**
### **Устаревший конструктор стилей**
В качестве альтернативы используйте метод cellFactory.CreateStyle.
## **Удаленные API**
### **Удален метод Cell.GetConditionalStyle.**
Вместо этого используйте метод Cell.GetConditionalFormattingResult.
### **Удален метод Cells.MaxDataRowInColumn(int column)**
В качестве альтернативы используйте метод Cells.GetLastDataRow(int).
### **Удаленное свойство PageSetup.Draft**
Вместо этого рекомендуется использовать свойство PageSetup.PrintDraft.
### **Удаленное свойство AutoFilter.FilterColumnCollection**
Пожалуйста, рассмотрите возможность использования свойства AutoFilter.FilterColumns для достижения той же цели.
### **Удалено свойство TickLabels.Rotation**
Вместо этого используйте свойство TickLabels.RotationAngle.
