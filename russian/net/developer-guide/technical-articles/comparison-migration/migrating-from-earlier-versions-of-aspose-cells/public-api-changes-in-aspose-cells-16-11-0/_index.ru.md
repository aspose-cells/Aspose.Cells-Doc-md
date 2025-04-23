---
title: Изменения в открытом API в Aspose.Cells 16.11.0
type: docs
weight: 350
url: /ru/net/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells от версии 16.10.0 до 16.11.0, которые могут быть интересны модульным/программным разработчикам. Он включает не только новые и обновленные публичные методы, добавленные и удаленные классы и т. д., но также описывает любые изменения в поведении за кадром в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка настроек глобализации**
Aspose.Cells 16.11.0 предоставляет класс GlobalizationSettings вместе со свойством WorkbookSettings.GlobalizationSettings для принудительного использования пользовательских меток для Промежуточных и Итоговых итогов в API Aspose.Cells. В классе GlobalizationSettings есть следующие методы, которые могут быть переопределены в пользовательской реализации, чтобы дать желаемые имена меткам **Промежуточный** и **Итоговый**.

- GlobalizationSettings.GetTotalName: Получает общее имя функции.
- GlobalizationSettings.GetGrandTotalName: Получает полное имя функции.

Вот простой пользовательский класс, который расширяет класс GlobalizationSettings и переопределяет упомянутые выше методы для возврата пользовательских меток для функции объединения Среднее.

**C#**

{{< highlight csharp >}}

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



Следующий фрагмент загружает существующую электронную таблицу и добавляет Итог типа Среднее для данных, уже имеющихся в листе. При добавлении Итога в лист будут вызваны класс CustomSettings и его методы GetTotalName и GetGrandTotalName.

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[] { 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



Класс GlobalizationSettings также предлагает метод GetOtherName, который полезен для получения имени меток "Другие" для круговых диаграмм. Вот простой сценарий использования метода GlobalizationSettings.GetOtherName.

**C#**

{{< highlight csharp >}}

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



Следующий фрагмент загружает существующую электронную таблицу с круговой диаграммой и рендерит диаграмму в изображение, используя созданный выше класс CustomSettings.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells 16.11.0 предоставил класс CellsFactory, который на данный момент имеет один метод: CreateStyle. Метод CellsFactory.CreateStyle может использоваться для создания экземпляра класса Style без добавления его в пул стилей книги.

Вот простой сценарий использования метода CellsFactory.CreateStyle.

**C#**

{{< highlight csharp >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Добавлено свойство AbsolutePath книги**
Aspose.Cells 16.11.0 предоставляет свойство AbsolutePath для книги, которое позволяет получить или установить абсолютный путь книги, сохраненный в файле workbook.xml. Это свойство полезно только при обновлении внешних ссылок.
### **Добавлен метод GridHyperlinkCollection.GetHyperlink**
Aspose.Cells.GridWeb 16.11.0 предоставил метод GetHyperlink классу GridHyperlinkCollection, который позволяет получить экземпляр GridHyperlink путем передачи экземпляра GridCell или пары целых чисел, соответствующих индексам строки и столбца.

{{% alert color="primary" %}} 

В случае, если на указанной ячейке не найдена гиперссылка, метод GetHyperlink вернет null.

{{% /alert %}} 

Вот простой сценарий использования метода GetHyperlink.

**C#**

{{< highlight csharp >}}

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
### **Устаревший конструктор Style**
Пожалуйста, используйте метод cellsFactory.CreateStyle в качестве альтернативы.
## **Удаленные API**
### **Метод Cell.GetConditionalStyle удален**
Пожалуйста, используйте метод Cell.GetConditionalFormattingResult вместо.
### **Метод Deleted Cells.MaxDataRowInColumn(int column)**
Пожалуйста, в качестве альтернативы используйте метод Cells.GetLastDataRow(int).
### **Удален свойство Draft класса PageSetup**
Рекомендуется использовать свойство PrintDraft класса PageSetup вместо.
### **Удалено свойство FilterColumnCollection класса AutoFilter**
Пожалуйста, рассмотрите возможность использования свойства AutoFilter.FilterColumns для достижения той же цели.
### **Свойство Deleted TickLabels.Rotation**
Пожалуйста, используйте свойство TickLabels.RotationAngle вместо.
{{< app/cells/assistant language="csharp" >}}
