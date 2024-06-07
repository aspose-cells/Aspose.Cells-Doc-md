---
title: 使用错误检查选项。
type: docs
weight: 60
url: /zh/java/use-error-checking-options/
---

{{% alert color="primary" %}} 

Microsoft Excel允许用户定义错误检查选项和规则。在创建公式时，用户经常会看到错误检查，单元格右上角的小三角形突出显示单元格存在问题时。Excel提供信息帮助用户纠正常见问题。

{{% /alert %}} 
## **错误类型。**
这种表示公式无法返回结果的错误（例如将数字除以零）需要立即处理，单元格中会显示错误值。单击绿色三角形会显示感叹号，点击后会打开选项列表。 

可以使用选项解决错误，也可以忽略错误。忽略错误意味着该错误不会出现在后续的错误检查中。

Aspose.Cells提供错误检查选项功能。ErrorCheckOptions类管理不同类型的错误检查，例如以文本形式存储的数字、公式计算错误和验证错误。使用ErrorCheckType枚举来设置所需的错误检查。
## **以文本形式存储的数字。**
有时，数字可能会以文本形式格式化并存储在单元格中。这可能会导致计算错误或产生混乱的排序顺序。以文本形式格式化的数字以文本左对齐而不是右对齐显示在单元格中。如果公式应在单元格上执行数学运算而没有返回值，则检查公式引用的单元格中的对齐方式-这些单元格中的一些或全部可能是作为文本格式化的数字。

可以使用错误检查选项快速将存储为文本的数字转换为真实数字。在Microsoft Excel 2003中：

1. 在**工具**菜单上，单击**选项**。
1. 选择错误检查选项卡。
   默认情况下选中**作为文本存储的数字**选项。 
1. 禁用它。
   查看下面的图片，了解在MS Excel中为数据显示绿色三角形的情况。

![todo:image_alt_text](use-error-checking-options_1.png)

以下示例代码展示了如何使用Aspose.Cells API在模板XLS文件中为工作表禁用以文本形式存储的数字错误检查选项。 

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
