---
title: 创建表格报表
type: docs
weight: 70
url: /zh/reportingservices/creating-tabular-report/
---

{{% alert color="primary" %}} 

Aspose.Cells报表模板中的表格由标题、表数据行、行组和页脚组成。下面显示了一个示例表格。

**示例表格** 

![todo:image_alt_text](creating-tabular-report_1.png)
#### **表头**
表头通常包含每个表格列的标题和其他文本项（如静态文本、报表参数、全局报表变量等）。表头是可选的。如果使用表头，应将表头标记放在表数据的第一列左侧，以指示该行是表头。
#### **表数据行**
表数据行是包含智能标记的单元格行。表格只能包含单个数据行。
#### **行组**
行组紧随表数据行，并包括两部分：组标记和组数据行。 

组标记应放在第一个表数据列的左侧，以指示该行是行组的数据行。组标记的格式为##group{GroupColumn}，例如##group{SalesOrderNumber}，其中SalesOrderNumber是数据集的列名之一。表格只能包含一个行组，但是行组可以包含多个组数据行。组标记只能放在第一数据行中，如上面的示例中所示。

组标记在呈现时从输出的Microsoft Excel文件中删除。行组是可选的。
#### **页脚**
页脚紧随行组，在包括三个部分：页脚标记、页脚数据行和页脚文本区域。 

页脚标记应放在表数据列的第一列左侧，表示该行是表页脚。表格可以包含多个页脚数据行，每个页脚行都必须用页脚标记标记。 

页脚文本区域可以包含静态文本、报表参数和全局报表变量，如上面的示例中所示。

页脚标记在呈现时从输出的Microsoft Excel文件中删除。页脚是可选的。

示例模板的输出如下所示。

**示例模板** 

![todo:image_alt_text](creating-tabular-report_2.png)

{{% /alert %}} 
###### **本部分包括以下主题:** 
- [准备创建表格报表](/cells/zh/reportingservices/preparing-for-creating-table-report/)
- [为表格添加基本信息](/cells/zh/reportingservices/adding-base-information-for-table/)
- [添加报表服务公式](/cells/zh/reportingservices/adding-reporting-services-formulas/)
- [添加表组](/cells/zh/reportingservices/adding-table-group/)
- [添加表页脚](/cells/zh/reportingservices/adding-table-footers/)
- [向报表中添加报表参数](/cells/zh/reportingservices/adding-report-parameters-to-report/)
- [向报表中添加报表服务全局变量](/cells/zh/reportingservices/adding-reporting-services-global-variables-to-report/)
- [设置报表属性](/cells/zh/reportingservices/setting-report-attributes/)
- [修改报表属性](/cells/zh/reportingservices/modifying-report-attributes/)
