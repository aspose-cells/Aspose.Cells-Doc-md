---
title: 页面设置和打印选项
type: docs
weight: 60
url: /zh/python-net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

有时，开发者需要配置页面设置和打印参数以控制打印过程。页面设置和打印参数提供多种选项，并在 Aspose.Cells for Python via .NET 中得到全支持。

本文演示如何在 Visual Studio.Net 中创建控制台应用，使用 Aspose.Cells for Python via .NET API 以少量代码应用页面设置和打印选项。

{{% /alert %}}

## **处理页面和打印设置**

在本例中，我们创建了一个 Excel 工作簿，使用 Aspose.Cells for Python via .NET 设置页面布局和打印选项。

### **使用 Aspose.Cells 设置页面设置选项**

首先在Microsoft Excel中创建一个简单的工作表。然后将页面设置选项应用于它。执行代码将更改页面设置选项，如下面的屏幕截图所示。

|**输出文件。**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. 在Microsoft Excel中创建一个带有一些数据的工作表：
   1. 在Microsoft Excel中打开一个新的工作簿。
   1. 添加一些数据。
1. 设置页面设置选项：
   将页面设置选项应用于文件。以下是应用新选项之前的默认选项的屏幕截图。

|**默认页面设置选项。**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPageSetup-1.py" >}}

### **设置打印选项**

页面设置还提供了几个打印选项(也称为工作表选项)，允许用户控制工作表页面的打印方式。它们允许用户:

- 选择工作表的特定打印区域。
- 打印标题。
- 打印网格线。
- 打印行/列标题。
- 获得草稿质量。
- 打印注释。
- 打印单元格错误。
- 定义页面排序。

下面的示例将打印选项应用于上面示例中创建的文件(PageSetup.xls)。下面的屏幕截图显示了应用新选项之前的默认打印选项。

|**输入文档**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
执行代码会更改打印选项。

|**输出文件**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPrintingOptions-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
