---
title: Aspose.Cells中设置工作簿的公式计算方式
type: docs
weight: 100
url: /zh/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel允许设置公式计算方式，即公式的计算方式。存在三个可能的值：

- 自动 - 每当发生更改时重新计算，以及每次打开工作簿时重新计算。
- 自动，数据表除外 - 每当发生更改时重新计算，但不包括数据表。
- 手动 - 仅当用户通过按 F9 或 CTRL+ALT+F9 明确请求时或保存工作簿时才重新计算。

{{% /alert %}} 

在Microsoft Excel中设置公式计算模式：

1. 选择**公式**接着**计算选项**.
1. 选择其中一个选项。

 Aspose.Cells 还允许您设置**公式计算模式**使用 FormulaSettings.CalculationMode 模式属性。您可以为其分配具有以下值之一的 CalcModeType 枚举：

- CalcModeType.自动
- CalcModeType.AutomaticExceptTable
- CalcModeType.手册

下面的示例代码首先创建一个工作簿，然后将公式计算模式设置为**手动的**并将工作簿作为输出 Excel 文件保存在磁盘上。

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **下载运行示例**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
