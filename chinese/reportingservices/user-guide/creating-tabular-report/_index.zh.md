---
title: 创建表格报告
type: docs
weight: 70
url: /zh/reportingservices/creating-tabular-report/
---
{{% alert color="primary" %}} 

Aspose.Cells 报告模板中的表格由标题、表格数据行、行组和页脚组成。示例表如下所示。

**示例表** 

![待办事项：图像_替代_文本](creating-tabular-report_1.png)
#### **表头**
表头通常包含每个表列的标题和其他文本项，如静态文本、报表参数、全局报表变量等。表头是可选的。如果使用表头，则表头标签应放置在表格数据第一列的左侧，以指示该行是表头。
#### **表数据行**
表格数据行是包含智能标记的一行单元格。一个表只能包含一个数据行。
#### **行组**
行组紧跟在表格数据行之后，由两部分组成：组标签和组数据行。

组标签应该放在第一个表数据列的左边，表示该行是行组的数据行。组标记的格式为##group{GroupColumn}，例如##group{SalesOrderNumber}，其中SalesOrderNumber 是数据集的列名之一。一张表只能包含一个行组，但一个行组可以包含多个组数据行。组标记只能放在第一个数据行中，如上面的示例所示。

组标记在渲染时从输出 Microsoft Excel 文件中删除。行组是可选的。
#### **页脚**
页脚位于行组之后，包括三部分：页脚标签、页脚数据行和页脚文本区。

页脚标记应放置在表格数据列第一列的左侧，表示该行是表格页脚。一张表可以包含多个页脚数据行，每个页脚行都必须用页脚标签标记。

页脚文本区域可以包含静态文本、报表参数和全局报表变量，如上例所示。

页脚标记在呈现时从输出 Microsoft Excel 文件中删除。页脚是可选的。

示例模板的输出如下所示。

**样本模板** 

![待办事项：图像_替代_文本](creating-tabular-report_2.png)

{{% /alert %}} 
###### **本节包括以下主题：**
- [准备创建表格报告](/cells/zh/reportingservices/preparing-for-creating-table-report/)
- [为表添加基础信息](/cells/zh/reportingservices/adding-base-information-for-table/)
- [添加 Reporting Services 公式](/cells/zh/reportingservices/adding-reporting-services-formulas/)
- [添加表组](/cells/zh/reportingservices/adding-table-group/)
- [添加表格页脚](/cells/zh/reportingservices/adding-table-footers/)
- [将报表参数添加到报表](/cells/zh/reportingservices/adding-report-parameters-to-report/)
- [将 Reporting Services 全局变量添加到报表](/cells/zh/reportingservices/adding-reporting-services-global-variables-to-report/)
- [设置报告属性](/cells/zh/reportingservices/setting-report-attributes/)
- [修改报表属性](/cells/zh/reportingservices/modifying-report-attributes/)
