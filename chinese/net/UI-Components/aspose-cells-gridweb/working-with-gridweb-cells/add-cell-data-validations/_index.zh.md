---
title: 添加单元格数据有效性
type: docs
weight: 90
url: /zh/net/aspose-cells-gridweb/add-cell-data-validations/
keywords: GridWeb,validation,data validation,GridValidation
description: 本文介绍了如何在GridWeb中添加数据验证(GridValidation)。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb使您能够使用GridWorksheet.Validations.Add()方法添加**数据验证**。 使用此方法，您必须指定**单元格范围**。 但是，如果要在单个GridCell中创建数据验证，可以直接使用GridCell.CreateValidation()方法。 同样，您可以使用GridCell.RemoveValidation()方法从GridCell中删除**数据验证**。

{{% /alert %}} 
## **在GridWeb的GridCell中创建数据验证**
以下示例代码在单元格B3中创建了一个**数据验证**。 如果您输入任何不在20和40之间的值，单元格B3将以**红色XXXX**形式显示**验证错误**，如此截屏所示。

![todo:image_alt_text](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
