---
title: 使用错误检查选项
type: docs
weight: 60
url: /zh/java/use-error-checking-options/
---

{{% alert color="primary" %}} 

Microsoft Excel允许用户定义错误检查选项和规则。用户在创建公式时经常会看到错误检查，单元格右上角的小三角形会在单元格出现问题时进行高亮显示。Excel提供的信息可帮助用户纠正常见问题。

{{% /alert %}} 
## **错误类型**
这些错误意味着公式无法返回结果，比如将数字除以零，需要立即处理，同时单元格中会显示一个错误值。点击绿色三角形会显示一个感叹号，点击后会打开选项列表。 

可以通过选项解决错误，也可以选择忽略错误。忽略错误意味着该错误在后续错误检查中不再显示。

Aspose.Cells提供了错误检查选项功能。ErrorCheckOptions类管理不同类型的错误检查，例如作为文本存储的数字、公式计算错误和验证错误。使用ErrorCheckType枚举设置所需的错误检查。
## **作为文本存储的数字**
有时，数字可能被格式化并作为文本存储在单元格中。这可能会导致计算出现问题或产生令人困惑的排序顺序。格式为文本的数字在单元格中是左对齐而不是右对齐的。如果应执行单元格上的公式未返回值，则检查公式引用的单元格中的对齐方式 - 可能是其中一些或全部的单元格被格式为文本。

可以使用错误检查选项快速将作为文本存储的数字转换为实际数字。在Microsoft Excel 2003中：

1. 在“工具”菜单上，单击“选项”。
1. 选择“错误检查”选项卡。
   **将作为文本存储的数字** 选项默认为选中状态。 
1. 取消其选中状态。
   查看下面的图片，显示MS Excel中数据的绿色三角形。

![todo:image_alt_text](use-error-checking-options_1.png)

以下示例代码显示如何使用Aspose.Cells APIs在模板XLS文件中禁用工作表中的文本存储的数字错误检查选项。 

**Java**

{{< highlight csharp >}}

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
