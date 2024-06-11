---
title: 创建表报
type: docs
weight: 70
url: /zh/reportingservices/creating-tabular-report/
---

{{% alert color="primary" %}} 

Aspose.Cells报表模板中的表格包括标题、表数据行、行分组和页脚。下面显示了一个示例表格。

**示例表格** 

![todo:image_alt_text](creating-tabular-report_1.png)
#### **表头**
表头通常包含每个表格列的标题以及其他文本项，如静态文本、报表参数、全局报表变量等。表头是可选的。如果使用表头，应将表头标记放置在表格数据第一列的左侧，以指示该行是表头。
#### **表数据行**
表数据行是包含智能标记的单元格行。一个表格只能包含一个数据行。
#### **行分组**
行分组紧随表数据行之后，由两部分组成：分组标记和分组数据行。 

分组标记应放置在第一列表数据左侧，以指示该行是行分组的数据行。分组标记的格式为##group{GroupColumn}，例如##group{SalesOrderNumber}，其中SalesOrderNumber是数据集的列名之一。一个表格只能包含一个行分组，但是行分组可以包含多个分组数据行。分组标记只能放置在第一数据行中，如上面的示例所示。

在渲染时，输出的 Microsoft Excel 文件中删除了组标记。行组是可选的。
#### **页脚**
页脚位于行组之后，包括三个部分：页脚标记、页脚数据行和页脚文本区。 

页脚标记应放置在表格数据列的第一列左侧，表示该行是表格页脚。一个表格可以包含多个页脚数据行，每个页脚行都必须由页脚标记标记。 

页脚文本区可以包含静态文本、报表参数和全局报表变量，如上面的示例所示。

在渲染时，页脚标记会从输出的 Microsoft Excel 文件中移除。页脚是可选的。

示例模板的输出如下。

**示例模板** 

![todo:image_alt_text](creating-tabular-report_2.png)

{{% /alert %}} 
###### **本节包括以下主题:** 
- [准备创建表格报告](/cells/zh/reportingservices/preparing-for-creating-table-report/)
- [为表格添加基本信息](/cells/zh/reportingservices/adding-base-information-for-table/)
- [添加报表服务公式](/cells/zh/reportingservices/adding-reporting-services-formulas/)
- [添加表格组](/cells/zh/reportingservices/adding-table-group/)
- [添加表格页脚](/cells/zh/reportingservices/adding-table-footers/)
- [向报表添加报表参数](/cells/zh/reportingservices/adding-report-parameters-to-report/)
- [向报表添加报表服务全局变量](/cells/zh/reportingservices/adding-reporting-services-global-variables-to-report/)
- [设置报表属性](/cells/zh/reportingservices/setting-report-attributes/)
- [修改报表属性](/cells/zh/reportingservices/modifying-report-attributes/)
