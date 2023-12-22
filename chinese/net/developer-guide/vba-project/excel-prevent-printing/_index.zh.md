---
title: 如何阻止用户打印 Excel 文件
type: docs
weight: 600
url: /zh/net/how-to-prevent-printing-excel/
description: 通过Aspose.Cells for .NET API了解如何防止用户打印excel。
keywords: excel printing, prevent printing excel, how to prevent users from printing excel, excel prevent printing, prevent printing workbook, Prevent users from printing the whole workbook with VBA. 
---
##  **可能的使用场景**
在我们的日常工作中，excel文件中可能会有一些重要的信息，为了保护内部数据的扩散，公司不会允许我们打印它们。本文档将告诉您如何防止他人打印 Excel 文件。

##  **如何阻止用户在 MS-Excel 中打印文件**
您可以应用以下 VBA 代码来保护要打印的特定文件。
1. 打开您不允许其他人打印的工作簿。
1. 选择 Excel 功能区中的“开发人员”选项卡，然后单击“控件”部分中的“查看代码”按钮。或者，您可以按住 ALT + F11 键打开 Microsoft Visual Basic for Applications 窗口。
<br>
<img src="1.png" width=70% />
1. 然后在左侧的Project Explorer中，双击ThisWorkbook打开该模块，并添加一些vba代码。
<br>
<img src="2.png" width=70% />
1. 然后保存并关闭此代码，然后返回工作簿，现在当您打印示例文件时，它们将不允许打印，并且您将收到以下警告框：
<br>
<img src="3.png" width=70% />

##  **如何阻止用户使用Aspose.Cells for .NET打印Excel文件**

下面的示例代码说明了如何阻止用户打印excel文件：

1. 加载[样本文件](sample.xlsx).
1. 从 Workbook 的 VbaProject 属性获取 VbaModuleCollection 对象。
1. 通过“ThisWorkbook”名称获取VbaModule对象。
1. 设置VbaModule 的codes 属性。
1. 将示例文件保存到[xlsm格式](out.xlsm).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}