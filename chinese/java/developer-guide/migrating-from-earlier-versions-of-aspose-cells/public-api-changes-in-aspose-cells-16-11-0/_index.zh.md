---
title: Aspose.Cells 16.11.0中的公共API更改
type: docs
weight: 360
url: /zh/java/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

本文描述了从版本16.10.0到16.11.0的Aspose.Cells API更改，可能对模块/应用程序开发人员感兴趣。其中包括新增和更新的公共方法，添加和删除的类等，还有对Aspose.Cells背后的行为变更的描述。

{{% /alert %}} 
## **已添加API**
### **支持全球化设置**
Aspose.Cells 16.11.0现在暴露了GlobalizationSettings类以及WorkbookSettings.GlobalizationSettings属性，以便强制Aspose.Cells API使用自定义标签来显示小计。GlobalizationSettings类有以下方法，可以在自定义实现中被重写，以给出所需名称的标签**Total**和**Grand Total**。

- GlobalizationSettings.getTotalName: 获取函数的总名称。
- GlobalizationSettings.getGrandTotalName: 获取函数的总总名称。

这里是一个简单的自定义类，扩展GlobalizationSettings类并重写其前述方法，以返回平均值合并函数的自定义标签。

**Java**

{{< highlight csharp >}}

 public class CustomSettings extends GlobalizationSettings

{    

    public String getTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "AVG";

             default:

                return super.getTotalName(functionType);

         }

    }

    public String getGrandTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "GRAND AVG";

             default:

            	 return super.getGrandTotalName(functionType);

         }



    }

}

{{< /highlight >}}

以下代码段加载现有电子表格，并在工作表中已有的数据上添加类型为平均值的分类小计。在添加小计时将调用CustomSettings类及其getTotalName和getGrandTotalName方法。

**Java**

{{< highlight csharp >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[] { 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

GlobalizationSettings类还提供了getOtherName方法，用于获取饼图的“其他”标签的名称。以下是GlobalizationSettings.getOtherName方法的简单使用场景。

**Java**

{{< highlight csharp >}}

 public class CustomSettings extends GlobalizationSettings

{ 

	public String getOtherName()

	{

		String language = Locale.getDefault().getLanguage();

		System.out.println(language);

		switch (language)

		{

			case "en":

				return "Other";

			case "fr":

				return "Autre";

			case "de":

				return "Andere";

			//Do other cases

			default:

				return super.getOtherName();

		}

	}

}

{{< /highlight >}}

以下代码片段加载包含饼图的现有电子表格，并在利用上面创建的CustomSettings类的同时将图表渲染为图像。

**Java**

{{< highlight csharp >}}

 //Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.getWorksheets().get(0);

//Accesses the 1st chart from the collection

Chart chart = sheet.getCharts().get(0);

//Refreshes the chart

chart.calculate();

//Renders the chart to image

chart.toImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}
### **添加了CellsFactory类**
Aspose.Cells 16.11.0现已公开了CellsFactory类，目前该类具有一个方法，即createStyle。CellsFactory.createStyle方法可用于创建样式类的实例，而不将其添加到工作簿样式池中。

以下是CellsFactory.createStyle方法的简单使用场景。

**Java**

{{< highlight csharp >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **添加了Workbook.AbsolutePath属性**
Aspose.Cells 16.11.0已公开了Workbook.AbsolutePath属性，允许获取或设置存储在workbook.xml文件中的绝对工作簿路径。此属性在仅更新外部链接时非常有用。
### **添加了GridHyperlinkCollection.getHyperlink方法**
Aspose.Cells.GridWeb 16.11.0已向GridHyperlinkCollection类公开了getHyperlink方法，允许通过传递GridCell实例或行列索引对获取GridHyperlink的实例。

{{% alert color="primary" %}} 

如果在指定单元格上未找到超链接，则getHyperlink方法将返回null。

{{% /alert %}} 

以下是getHyperlink方法的简单使用场景。

**Java**

{{< highlight csharp >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **已废弃的API**
### **已弃用的Style构造函数**
请使用cellsFactory.createStyle方法作为替代方法。
## **已删除的API**
### **删除了Cell.getConditionalStyle方法**
请改用Cell.getConditionalFormattingResult方法。
### **删除了Cells.getMaxDataRowInColumn(int column)方法**
请使用Cells.getLastDataRow(int)方法作为替代方法。
### **已删除的PageSetup.Draft属性**
建议使用PageSetup.PrintDraft属性。
### **已删除的AutoFilter.FilterColumnCollection属性**
请考虑使用AutoFilter.FilterColumns属性来实现相同的目标。
### **已删除的TickLabels.Rotation属性**
请改用TickLabels.RotationAngle属性。
