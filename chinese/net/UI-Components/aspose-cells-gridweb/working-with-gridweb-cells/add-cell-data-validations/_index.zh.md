---
title: 添加单元格数据验证
type: docs
weight: 90
url: /zh/net/aspose-cells-gridweb/add-cell-data-validations/
keywords: GridWeb,验证,数据验证,GridValidation
description: 本文介绍了如何在GridWeb中添加数据验证(GridValidation)。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb允许您使用GridWorksheet.Validations.Add()方法添加**数据验证**。使用此方法，您必须指定**单元格范围**。但如果要在单个GridCell中创建数据验证，可以直接使用GridCell.CreateValidation()方法。同样，您可以使用GridCell.RemoveValidation()方法从GridCell中移除**数据验证**。

{{% /alert %}} 
## **在 GridWeb 的 GridCell 中创建数据验证**
下面的示例代码在 B3 单元格中创建了**数据验证**。如果输入任何不在 20 到 40 之间的值，B3 单元格将以**红色 XXXX**的形式显示**验证错误**，如屏幕截图所示。

![todo:image_alt_text](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
