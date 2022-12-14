---
title: 使用错误检查选项
type: docs
weight: 60
url: /zh/java/use-error-checking-options/
---
{{% alert color="primary" %}} 

Microsoft Excel 允许用户定义错误检查选项和规则。用户在创建公式时经常会看到错误检查，当单元格出现问题时，单元格右上角的小三角形会突出显示。 Excel 提供的信息可帮助用户更正常见问题。

{{% /alert %}} 
## **错误类型**
意味着公式无法返回结果的错误（例如将数字除以零）需要立即引起注意，并且错误值会显示在单元格中。单击绿色三角形会显示一个感叹号，单击它会打开选项列表。

可以使用选项解决该错误，也可以忽略该错误。忽略错误意味着该错误不会出现在进一步的错误检查中。

Aspose.Cells 提供错误检查选项功能。 ErrorCheckOptions 类管理不同类型的错误检查，例如存储为文本的数字、公式计算错误和验证错误。使用 ErrorCheckType 枚举来设置所需的错误检查。
## **数字存储为文本**
有时，数字可能会被格式化并作为文本存储在单元格中。这可能会导致计算问题或产生混乱的排序顺序。格式化为文本的数字在单元格中左对齐而不是右对齐。如果应该对单元格执行数学运算的公式没有返回值，请检查公式引用的单元格中的对齐方式——部分或所有这些单元格可能是格式化为文本的数字。

您可以使用错误检查选项将以文本形式存储的数字快速转换为实数。在 Microsoft Excel 2003 中：

1. 在**工具**菜单，点击**选项**.
1. 选择错误检查选项卡。
   **数字存储为文本**默认情况下选中选项。
1. 禁用它。
请参阅下图，了解如何在 MS Excel 中显示数据的绿色三角形。

![待办事项：图片_替代_文本](use-error-checking-options_1.png)

以下示例代码显示如何使用 Aspose.Cells API 禁用模板 XLS 文件中作为工作表文本错误检查选项存储的数字。

**Java**

{{< highlight "csharp" >}}

 //Create a workbook and opening a template spreadsheet

Workbook workbook = new Workbook("d:\\files\\Book1.xls");

//Get the first worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Instantiate the error checking options

ErrorCheckOptionCollection opts = sheet.getErrorCheckOptions();

int index = opts.add();

ErrorCheckOption opt = opts.get(index);

//Disable the numbers stored as text option

opt.setErrorCheck(ErrorCheckType.TEXT_NUMBER, false);

//Set the range

opt.addRange(CellArea.createCellArea(0, 0, 65535, 255));

//Save the Excel file

workbook.save("d:\\files\\out_test.xls");



{{< /highlight >}}
