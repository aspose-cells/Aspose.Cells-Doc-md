---
title: 参数化报表
type: docs
weight: 60
url: /zh/reportingservices/parameterized-report/
---

{{% alert color="primary" %}} 

*参数化报表*是指接受输入值并在处理报表时使用这些值的报表。 

通过参数化报表，您可以根据运行时设置的值来变化报表的输出。 Reporting Services支持两种参数：查询参数和报表参数。 

- **查询参数**用于在数据处理过程中选择或过滤数据。 如果指定了查询参数，则必须通过用户提供值或默认属性，完成检索报表数据的SELECT语句或存储过程。
- **报表参数**用于在报表处理过程中展示数据的不同方面。 报表参数通常用于过滤大量记录，但根据报表中的查询和表达式，还可以有其他用途。

报表参数与查询参数的区别在于报表参数在报表中定义并由报表服务器处理，而查询参数作为数据集查询的一部分定义并在数据库服务器上处理。 在Aspose.Cells.Report.Designer中，查询参数在创建查询时在Microsoft Query中指定。 

您可以在Aspose.Cells.Report.Designer中创建报表参数，并将查询参数映射到相应的报表参数。 这样，可以选择报表参数的值并将其传递给查询以限制从数据源检索的数据。

{{% /alert %}} 
###### **本节包括以下主题:** 
- [创建报表参数](/cells/zh/reportingservices/creating-report-parameters/)
- [修改报表参数](/cells/zh/reportingservices/modifying-report-parameters/)
- [将查询参数映射到报表参数](/cells/zh/reportingservices/mapping-query-parameters-to-report-parameters/)
