---
title: 创建矩阵报表
type: docs
weight: 10
url: /zh/reportingservices/creating-matrix-report/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services 允许您在 Microsoft Excel 中设计矩阵。 

{{% /alert %}} 
### **矩阵模板**
在 Aspose.Cells 报表模板中，矩阵包括角、行组、列组和数据部分。以下是一个示例矩阵。

**一个示例矩阵** 

![todo:image_alt_text](creating-matrix-report_1.png)

- **矩阵角**：位于左上角，或右到左（RTL）布局的右上角。当您向矩阵数据区域添加行组和列组时，此区域会自动创建。在此区域中，您可以合并单元格嵌入的文本框报表项。
- **矩阵列组区域**：位于右上角（RTL 布局的左上角）。当您添加列组时，此区域会自动创建。该区域中的单元格代表列组层次结构的成员，并显示列组实例值。图中显示 OrderYear 的单元格是一个嵌套的列组，显示 OrderQtr 的单元格是相邻的列组。
- **矩阵行组区域**：位于左下角（RTL 布局的右下角）。当您添加行组时，此区域会自动创建。该区域中的单元格代表行组层次结构的成员，并显示行组实例值。在图中，这些单元格是嵌套的行组。
- **矩阵数据区域**：位于右下角（RTL 布局的左下角）。矩阵数据显示详细和分组数据。在此示例中，仅使用聚合数据。默认情况下，包含简单表达式但不包括聚合函数的组行或列中的单元格将求值为该组中的第一个值。在图中，单元格显示了所有销售订单行总计的聚合总计。
#### **创建矩阵模板**
在创建矩阵报表之前，创建数据源、数据集和报表参数（可选）。（如果需要帮助，请参考[数据源和查询](/cells/zh/reportingservices/data-sources-and-queries/)中的说明。）在示例中，我们使用了随 SQL Server Reporting Services 2008 附带的 AdventureWorks 示例数据库。

要创建新的矩阵：

1. 打开 Microsoft Excel。
1. 单击**打开报表**以打开预先创建的包含数据源、数据集和报表参数的RDL报表文件。
   成功打开文件后，其中的所有信息都可以用于操作，例如其数据集会显示在**数据集**列表中。
1. 打开 Microsoft Excel 工作表并选择一个数据集。 

![todo:image_alt_text](creating-matrix-report_2.png)




1. 通过**设置分组**设置行分组和列分组。 

![todo:image_alt_text](creating-matrix-report_3.png)




1. 合并单元格以设置矩阵角。

![todo:image_alt_text](creating-matrix-report_4.png)




1. 通过插入公式设置矩阵角。 

![todo:image_alt_text](creating-matrix-report_5.png)




![todo:image_alt_text](creating-matrix-report_6.png)




1. 单击**设置属性**以设置矩阵属性。 

![todo:image_alt_text](creating-matrix-report_7.png)



它包括名称、范围、分组和排序。

1. 单击修改属性会检查并修改当前工作表的所有矩阵属性。

![todo:image_alt_text](creating-matrix-report_8.png)




1. 保存、发布并查看报表。
