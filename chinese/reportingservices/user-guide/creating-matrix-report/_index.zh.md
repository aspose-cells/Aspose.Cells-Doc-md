---
title: 创建矩阵报告
type: docs
weight: 10
url: /zh/reportingservices/creating-matrix-report/
---
{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services 可让您在 Microsoft Excel 中设计矩阵。

{{% /alert %}} 
### **矩阵模板**
在 Aspose.Cells 报告模板中，矩阵由角、行组、列组和数据部分组成。示例矩阵如下所示。

**样本矩阵** 

![待办事项：图像_替代_文本](creating-matrix-report_1.png)

- **矩阵角**：位于左上角，或右上角（对于从右到左 (RTL) 布局）。当您将行组和列组添加到矩阵数据区域时，会自动创建此区域。在此区域中，您可以合并嵌入文本框报表项的单元格。
- **矩阵列组区域**：位于右上角（RTL布局为左上角）。添加列组时会自动创建此区域。此区域中的单元格表示列组层次结构的成员，并显示列组实例值。图中显示OrderYear的单元格是嵌套的列组，显示OrderQtr的单元格是相邻的列组。
- **矩阵行组区域**：位于左下角（右下角为 RTL 布局）。添加行组时会自动创建此区域。此区域中的单元格表示行组层次结构的成员，并显示行组实例值。在图中，这些单元格是嵌套的行组。
- **矩阵数据区**：位于右下角（RTL 布局为左下角）。矩阵数据显示详细信息和分组数据。在此示例中，仅使用聚合数据。默认情况下，包含不包含聚合函数的简单表达式的组行或列中的单元格计算为组中的第一个值。在图中，单元格显示所有销售订单的行总计的总计。
#### **创建矩阵模板**
在创建矩阵报表之前，创建数据源、数据集和报表参数（可选）。 （按照说明[数据源和查询](/cells/zh/reportingservices/data-sources-and-queries/)如果您需要帮助。）在示例中，我们使用 SQL Server Reporting Services 2008 附带的 AdventureWorks 示例数据库。

要创建一个新矩阵：

1. 打开 Microsoft Excel。
1. 点击**打开报告**打开包含预先创建的数据源、数据集和报告参数的 RDL 报告文件。
一旦文件被成功打开，它的所有信息都可以使用，例如，它的数据集列在**数据集**列表。
1. 打开 Microsoft Excel 工作表并选择一个数据集。

![待办事项：图像_替代_文本](creating-matrix-report_2.png)




1. 通过设置行组和列组**集组**. 

![待办事项：图像_替代_文本](creating-matrix-report_3.png)




1. 合并单元格以设置矩阵角。

![待办事项：图像_替代_文本](creating-matrix-report_4.png)




1. 通过插入公式设置矩阵角点。

![待办事项：图像_替代_文本](creating-matrix-report_5.png)




![待办事项：图像_替代_文本](creating-matrix-report_6.png)




1. 点击**设置属性**设置矩阵属性。

![待办事项：图像_替代_文本](creating-matrix-report_7.png)



它由名称、范围、组和顺序组成。

1. 单击修改属性检查并修改当前工作表的所有矩阵属性。

![待办事项：图像_替代_文本](creating-matrix-report_8.png)




1. 保存、发布和审查报告。
