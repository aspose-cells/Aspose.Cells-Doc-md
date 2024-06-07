---
title: 创建矩阵报表
type: docs
weight: 10
url: /zh/reportingservices/creating-matrix-report/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services 允许您在 Microsoft Excel 中设计矩阵报表。 

{{% /alert %}} 
### **矩阵模板**
在 Aspose.Cells 报表模板中，矩阵包括角、行分组、列分组和数据部分。下图显示了一个样本矩阵。

**一个样本矩阵** 

![todo:image_alt_text](creating-matrix-report_1.png)

- **矩阵角**: 位于左上角，或对于从右到左 (RTL) 布局的情况，位于右上角。当您向矩阵数据区域添加行分组和列分组时，会自动创建此区域。在此区域中，您可以合并嵌入的文本框报表项的单元格。
- **矩阵列分组区域**: 位于右上角 (RTL 布局的左上角)。当您添加列分组时，会自动创建此区域。此区域中的单元格表示列分组层次的成员，并显示列分组实例值。在图中，显示 OrderYear 的单元格是一个嵌套的列分组，显示 OrderQtr 的单元格是相邻列分组。
- **矩阵行分组区域**: 位于左下角 (RTL 布局的右下角)。当您添加行分组时，会自动创建此区域。此区域中的单元格表示行分组层次的成员，并显示行分组实例值。在图中，这些单元格是嵌套行分组。
- **矩阵数据区域**: 位于右下角 (RTL 布局的左下角)。矩阵数据显示详细和分组数据。在这个示例中，只使用了聚合数据。默认情况下，组行或列中包含简单表达式的单元格会计算为组中的第一个值，不包括聚合函数。在图中，单元格显示了所有销售订单行总计的聚合总计。
#### **创建矩阵模板**
在创建矩阵报表之前，创建数据源、数据集和报表参数（可选）。（如果需要帮助，请参考 [数据源和查询](/cells/zh/reportingservices/data-sources-and-queries/) 中的说明。）在示例中，我们使用随 SQL Server Reporting Services 2008 附带的 AdventureWorks 示例数据库。

要创建新的矩阵:

1. 打开Microsoft Excel。
1. 单击 **打开报表** 打开一个包含提前创建的数据源、数据集和报表参数的 RDL 报表文件。
   一旦文件成功打开，它的所有信息可供使用，例如，其数据集在 **数据集** 列表中列出。
1. 打开 Microsoft Excel 工作表并选择一个数据集。 

![todo:image_alt_text](creating-matrix-report_2.png)




1. 通过 **设置分组** 设置行分组和列分组。 

![todo:image_alt_text](creating-matrix-report_3.png)




1. 合并单元格以设置矩阵角。

![todo:image_alt_text](creating-matrix-report_4.png)




1. 通过插入公式设置矩阵角。 

![todo:image_alt_text](creating-matrix-report_5.png)




![todo:image_alt_text](creating-matrix-report_6.png)




1. 单击 **设置属性** 设置矩阵属性。 

![todo:image_alt_text](creating-matrix-report_7.png)



它包括名称、范围、组和顺序。

1. 单击修改属性，检查和修改当前工作表的所有矩阵属性。

![todo:image_alt_text](creating-matrix-report_8.png)




1. 保存、发布和审阅报表。
