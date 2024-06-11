---
title: 如何防止用户打印Excel文件
type: docs
weight: 600
url: /zh/net/how-to-prevent-printing-excel/
description: 学习如何使用 Aspose.Cells for .NET API 防止用户打印 Excel。
keywords: excel打印、防止excel打印、如何防止用户打印excel、excel防止打印、防止打印工作簿、使用VBA阻止用户打印整个工作簿 
---

## **可能的使用场景**
在我们日常工作中，Excel文件中可能会包含一些重要信息，为了防止内部数据泄漏，公司不允许我们打印这些文件。本文档将告诉您如何防止他人打印Excel文件。

## **如何防止用户在MS-Excel中打印文件**
您可以应用以下VBA代码来保护您的特定文件不被打印。
1. 打开您不允许他人打印的工作簿。
1. 在ExcelRibbon中选择“开发人员”选项卡，并单击“控件”部分的“查看代码”按钮。或者，您可以按住ALT + F11键以打开Microsoft Visual Basic for Applications窗口。
<br>
<img src="1.png" width=70% />
1. 然后在左边的“项目资源管理器”中，双击ThisWorkbook打开模块，并添加一些VBA代码。
<br>
<img src="2.png" width=70% />
1. 然后保存并关闭此代码，返回工作簿，现在当您打印示例文件时，它们将不允许被打印，并且会收到以下警告框：
<br>
<img src="3.png" width=70% />

## **如何使用 Aspose.Cells for .NET 防止用户打印 Excel 文件**

以下示例代码演示了如何防止用户打印Excel文件：

1. 加载[示例文件](sample.xlsx)。
1. 从工作簿的VbaProject属性获取VbaModuleCollection对象。
1. 通过“ThisWorkbook”名称获取VbaModule对象。
1. 设置VbaModule的代码属性。
1. 将示例文件保存为[xlsm格式](out.xlsm)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}
