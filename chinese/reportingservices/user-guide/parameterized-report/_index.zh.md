---
title: 参数化报表
type: docs
weight: 60
url: /zh/reportingservices/parameterized-report/
---

{{% alert color="primary" %}} 

参数化报表是指在处理报表时接受输入值的报表。 

使用参数化报表，您可以根据运行时设置的值来改变报表的输出。Reporting Services支持两种参数：查询参数和报表参数。 

- **查询参数** 用于在数据处理期间选择或过滤数据。如果指定了查询参数，则必须由用户或默认属性提供值以完成检索报表数据的SELECT语句或存储过程。
- **报表参数** 在报表处理期间用于展示数据的不同方面。报表参数通常用于过滤大量记录，但根据报表中的查询和表达式，它也可能具有其他用途。

报表参数不同于查询参数的地方在于它们是在报表中定义并由报表服务器处理，而查询参数是作为数据集查询的一部分进行定义并在数据库服务器上处理。在Aspose.Cells.Report.Designer中，查询参数是在Microsoft Query中的查询创建期间指定的。 

您可以在Aspose.Cells.Report.Designer中创建报表参数，并将查询参数映射到相应的报表参数。通过这种方式，可以选择报表参数的值并将其传递到查询以限制从数据源检索的数据。

{{% /alert %}} 
###### **本部分包括以下主题:** 
- [创建报表参数](/cells/zh/reportingservices/creating-report-parameters/)
- [修改报表参数](/cells/zh/reportingservices/modifying-report-parameters/)
- [映射查询参数到报表参数](/cells/zh/reportingservices/mapping-query-parameters-to-report-parameters/)
