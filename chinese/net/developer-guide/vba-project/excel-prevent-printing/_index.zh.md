---
title: 如何防止用户打印 Excel 文件
type: docs
weight: 600
url: /zh/net/how-to-prevent-printing-excel/
description: 通过 Aspose.Cells for .NET API 学习如何防止用户通过打印 Excel 文件。
keywords: excel 打印，防止打印 excel，如何防止用户打印 excel，excel 防止打印，防止打印工作簿，使用 VBA 防止用户打印整个工作簿。 
---

## **可能的使用场景**
在我们的日常工作中，Excel 文件中可能包含一些重要信息，为了防止内部数据泄露，公司不允许我们打印它们。本文将告诉您如何防止他人打印 Excel 文件。

## **如何防止 MS-Excel 中的用户打印文件**
您可以应用以下 VBA 代码来保护特定文件不被打印。
1. 打开您不允许其他人打印的工作簿。
1. 在 Excel 标签中选择“开发人员”选项卡，然后单击“控件”部分的“查看代码”按钮。 或者，您可以按住 ALT + F11 键打开 Microsoft Visual Basic for Applications 窗口。
<br>
<img src="1.png" width=70% />
1. 然后在左侧的“项目资源管理器”中，双击 ThisWorkbook 以打开模块，并添加一些 VBA 代码。
<br>
<img src="2.png" width=70% />
1. 然后保存并关闭此代码，返回工作簿，现在当您打印示例文件时，它们将不被允许打印，并且您将看到以下警告框：
<br>
<img src="3.png" width=70% />

## **通过 Aspose.Cells for .NET 防止用户打印 Excel 文件**

下面的示例代码说明了如何防止用户打印 Excel 文件：

1. 加载[示例文件](sample.xlsx)。
1. 从 Workbook 的 VbaProject 属性获取 VbaModuleCollection 对象。
1. 通过“ ThisWorkbook”名称获取 VbaModule 对象。
1. 设置 VbaModule 的代码属性。
1. 将示例文件保存为[xlsm 格式](out.xlsm)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}
