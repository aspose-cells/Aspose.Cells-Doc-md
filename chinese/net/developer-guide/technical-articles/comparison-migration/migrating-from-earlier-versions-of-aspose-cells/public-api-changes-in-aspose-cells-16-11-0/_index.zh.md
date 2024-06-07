---
title: Aspose.Cells 16.11.0中的公共API更改
type: docs
weight: 350
url: /zh/net/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

本文描述了从版本16.10.0到16.11.0的Aspose.Cells API更改，可能对模块/应用程序开发人员感兴趣。其中包括新增和更新的公共方法，添加和删除的类等，还有对Aspose.Cells背后的行为变更的描述。

{{% /alert %}} 
## **已添加API**
### **支持全球化设置**
Aspose.Cells 16.11.0现在暴露了GlobalizationSettings类以及WorkbookSettings.GlobalizationSettings属性，以便强制Aspose.Cells API使用自定义标签来显示小计。GlobalizationSettings类有以下方法，可以在自定义实现中被重写，以给出所需名称的标签**Total**和**Grand Total**。

- GlobalizationSettings.GetTotalName: 获取函数的总名称。
- GlobalizationSettings.GetGrandTotalName: 获取函数的总总名称。

这里是一个简单的自定义类，扩展GlobalizationSettings类并重写其前述方法，以返回平均值合并函数的自定义标签。

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



以下片段加载现有电子表格并在工作表中已有数据的基础上添加平均值类型的小计。在添加小计到工作表时，将调用CustomSettings类及其GetTotalName和GetGrandTotalName方法。

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



GlobalizationSettings类还提供了GetOtherName方法，用于获取饼图的"其他"标签的名称。这里是GlobalizationSettings.GetOtherName方法的简单使用情景。

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



以下代码片段加载包含饼图的现有电子表格，并在利用上面创建的CustomSettings类的同时将图表渲染为图像。

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


### **添加了CellsFactory类**
Aspose.Cells 16.11.0已经公开了CellsFactory类，目前只有一个方法，即CreateStyle。CellsFactory.CreateStyle方法可用于创建Style类的实例，而不将其添加到工作簿样式池中。

以下是CellsFactory.CreateStyle方法的简单使用场景。

**C#**

{{< highlight csharp >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **添加了Workbook.AbsolutePath属性**
Aspose.Cells 16.11.0已公开了Workbook.AbsolutePath属性，允许获取或设置存储在workbook.xml文件中的绝对工作簿路径。此属性在仅更新外部链接时非常有用。
### **添加了GridHyperlinkCollection.GetHyperlink方法**
Aspose.Cells.GridWeb 16.11.0已经公开了GetHyperlink方法到GridHyperlinkCollection类，通过传递GridCell的实例或对应于行列索引的一对整数，可以获取GridHyperlink的实例。

{{% alert color="primary" %}} 

如果在指定单元格上未找到超链接，则GetHyperlink方法将返回null。

{{% /alert %}} 

以下是GetHyperlink方法的简单使用场景。

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
## **已废弃的API**
### **已弃用的Style构造函数**
请使用cellsFactory.CreateStyle方法作为替代。
## **已删除的API**
### **已删除的Cell.GetConditionalStyle方法**
请改用Cell.GetConditionalFormattingResult方法。
### **已删除的Cells.MaxDataRowInColumn(int column)方法**
请使用Cells.GetLastDataRow(int)方法作为替代。
### **已删除的PageSetup.Draft属性**
建议使用PageSetup.PrintDraft属性。
### **已删除的AutoFilter.FilterColumnCollection属性**
请考虑使用AutoFilter.FilterColumns属性来实现相同的目标。
### **已删除的TickLabels.Rotation属性**
请改用TickLabels.RotationAngle属性。
