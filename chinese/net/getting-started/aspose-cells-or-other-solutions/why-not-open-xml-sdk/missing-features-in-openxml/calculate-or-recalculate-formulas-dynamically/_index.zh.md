---
title: 动态计算或重新计算公式
type: docs
weight: 10
url: /zh/net/calculate-or-recalculate-formulas-dynamically/
---

**公式计算**引擎嵌入在**Aspose.Cells**中。它不仅可以重新计算从设计文件导入的公式，还可以支持计算运行时添加的公式的结果。
## **添加公式及计算结果**
Aspose.Cells支持大部分作为Microsoft Excel一部分的公式或函数。开发者可以使用API或设计师电子表格来使用这些公式。Aspose.Excel支持大量的数学、字符串、布尔、日期/时间、统计、数据库、查找和引用公式。

使用Cell类的Formula属性向单元格添加公式。在向单元格应用公式时，始终以等号(=)开头，就像在Microsoft Excel中创建公式时那样。使用逗号(,)来分隔函数参数。

要计算公式的结果，请调用Excel类的CalculateFormula方法，该方法处理嵌入在Excel文件中的所有公式。阅读[url: CalculateFormula方法支持的函数列表](/cells/zh/net/supported-formula-functions/)

{{< highlight csharp >}}

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
## **仅计算一次公式**
用户调用Workbook.CalculateFormula()来计算工作簿模板内公式的值时，Aspose.Cells会创建一个计算链。计算链在第二次或第三次等计算公式时可以提高性能。
然而，如果用户模板包含大量不同的公式，那么第一次计算公式可能会消耗大量CPU处理时间和内存。

Aspose.Cells允许您关闭创建计算链，这在希望仅计算文件的公式一次时非常有用。

如果您希望通过Aspose.Cells改善公式计算的性能，并且不希望创建公式计算链，则请将**FormulaSettings.EnableCalculationChain**设置为**false**。默认情况下，它设置为**true**。

{{< highlight csharp >}}

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
## **直接计算公式**
公式计算引擎嵌入在Aspose.Cells中。除重新计算从设计文件中导入的公式外，Aspose.Cells还支持直接计算公式的结果。
有时，您需要直接计算公式的结果，而无需实际将它们添加到工作表中。工作表中已经存在公式中使用的单元格的值，您需要做的就是基于某个Ms-Excel公式找出这些值的结果而不将公式添加到工作表中。

您可以使用Aspose.Cells公式计算引擎API，即**worksheet.Calculate(string formula)**来计算此类公式的结果，而无需实际将它们添加到工作表中。

{{< highlight csharp >}}

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
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
