---
title: 添加 Cell 数据验证
type: docs
weight: 90
url: /zh/net/add-cell-data-validations/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 允许您添加**数据验证**使用 GridWorksheet.Validations.Add() 方法。使用此方法，您必须指定**Cell 范围**.但是如果你想在单个 GridCell 中创建数据验证，那么你可以直接使用 GridCell.CreateValidation() 方法来完成。同样，您可以删除**数据验证**从 GridCell 使用 GridCell.RemoveValidation() 方法。

{{% /alert %}} 
## **在 GridWeb 的 GridCell 中创建数据验证**
下面的示例代码创建一个**数据验证**在单元格 B3 中。如果您输入任何不在 20 到 40 之间的值，单元格 B3 将显示**验证错误**形式为**红色 XXXX**如这个屏幕截图所示。

![待办事项：图像_替代_文本](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
