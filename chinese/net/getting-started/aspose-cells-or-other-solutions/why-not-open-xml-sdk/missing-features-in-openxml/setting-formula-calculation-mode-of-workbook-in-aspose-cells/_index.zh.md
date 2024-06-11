---
title: 在Aspose.Cells中设置工作簿的公式计算模式
type: docs
weight: 100
url: /zh/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel允许您设置公式计算模式，即公式计算的方式。有三种可能的值：

- 自动 - 每当有变更时重新计算，并且每次打开工作簿时。
- 自动除数据表外 - 每当有变更时重新计算，但是不包括数据表。
- 手动 - 仅当用户通过按F9或CTRL+ALT+F9明确请求时，或者保存工作簿时重新计算。

{{% /alert %}} 

在Microsoft Excel中设置公式计算模式：

1. 选择**公式**然后**计算选项**。
1. 选择其中一个选项。

Aspose.Cells还允许您使用FormulaSettings.CalculationMode属性设置**公式计算模式**。您可以将CalcModeType枚举赋值给它，该枚举具有以下值:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

以下示例代码首先创建一个工作簿，然后将公式计算模式设置为**手动**，并将工作簿保存为磁盘上的输出Excel文件。

**C#**

{{< highlight csharp >}}

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
