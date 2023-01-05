---
title: 动态计算或重新计算公式
type: docs
weight: 10
url: /zh/net/calculate-or-recalculate-formulas-dynamically/
---
**公式计算**引擎嵌入**Aspose.Cells**.它不仅可以重新计算从设计器文件中导入的公式，还支持计算运行时添加的公式的结果。
## **添加公式和计算结果**
Aspose.Cells 支持 Microsoft Excel 中的大部分公式或函数。开发人员可以通过 API 或 Designer Spreadsheets 使用这些公式。 Aspose.Excel 支持大量的数学、字符串、布尔、日期/时间、统计、数据库、查找和参考公式。

使用 Cell 类的 Formula 属性将公式添加到单元格。将公式应用于单元格时，始终以等号 (=) 开头字符串，就像在 Microsoft Excel 中创建公式时所做的那样。使用逗号 (,) 分隔函数参数。

要计算公式的结果，请调用 Excel 类的 CalculateFormula 方法，该方法处理嵌入在 Excel 文件中的所有公式。阅读[url: CalculateFormula 方法支持的函数列表](/cells/zh/net/supported-formula-functions/).

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a value to "A1" cell

worksheet.Cells["A1"].PutValue(1);

//Adding a value to "A2" cell

worksheet.Cells["A2"].PutValue(2);

//Adding a value to "A3" cell

worksheet.Cells["A3"].PutValue(3);

//Adding a SUM formula to "A4" cell

worksheet.Cells["A4"].Formula = "=SUM(A1:A3)";

//Calculating the results of formulas

workbook.CalculateFormula();

//Get the calculated value of the cell

string value = worksheet.Cells["A4"].Value.ToString();

//Saving the Excel file

workbook.Save("Adding Formula.xls");

{{< /highlight >}}
## **只计算一次公式**
当用户调用 Workbook.CalculateFormula() 计算工作簿模板中公式的值时，Aspose.Cells 创建一个计算链。当第二次或第三次计算公式等时，它会提高性能。
但是，如果用户模板包含大量不同的公式，那么第一次公式计算会消耗大量的 CPU 处理时间和内存。

Aspose.Cells 允许您关闭创建计算链，这在您只想计算一次文件公式的情况下很有用。

如果您希望通过Aspose.Cells提高公式计算的性能并且您不想创建公式计算链，那么请设置**公式设置.启用计算链**作为**错误的**.默认情况下，它被设置为**真的**.

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Adding Formula.xlsx";

//Load the template workbook

Workbook workbook = new Workbook(FileName);

//Print the time before formula calculation

Console.WriteLine(DateTime.Now);

//Set the CreateCalcChain as false

workbook.Settings.FormulaSettings.EnableCalculationChain = false;

//Calculate the workbook formulas

workbook.CalculateFormula();

//Print the time after formula calculation

Console.WriteLine(DateTime.Now);

workbook.Save(FileName);

{{< /highlight >}}
## **公式直接计算**
Aspose.Cells内嵌公式计算引擎，除了对从设计器文件导入的公式重新计算，Aspose.Cells还支持直接计算公式结果。
有时，您需要直接计算公式的结果，而无需将它们实际添加到工作表中。公式中使用的单元格值已经存在于工作表中，您只需根据某些 Ms-Excel 公式查找这些值的结果，而无需在工作表中添加公式。

可以使用Aspose.Cells公式计算引擎API即**worksheet.Calculate(字符串公式)**计算这些公式的结果而不实际将它们添加到工作表中。

{{< highlight "csharp" >}}

 //Create a workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put 20 in cell A1

Cell cellA1 = worksheet.Cells["A1"];

cellA1.PutValue(20);

//Put 30 in cell A2

Cell cellA2 = worksheet.Cells["A2"];

cellA2.PutValue(30);

//Calculate the Sum of A1 and A2

var results = worksheet.CalculateFormula("=Sum(A1:A2)");

Cell cellA3 = worksheet.Cells["A3"];

cellA3.PutValue(results);

//Print the output

Debug.WriteLine("Value of A1: " + cellA1.StringValue);

Debug.WriteLine("Value of A2: " + cellA2.StringValue);

Debug.WriteLine("Result of Sum(A1:A2): " + results.ToString());

workbook.Save("Calulate Any Formulae.xls");

{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
