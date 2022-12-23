---
title: 参数化报告
type: docs
weight: 60
url: /zh/reportingservices/parameterized-report/
---
{{% alert color="primary" %}} 

一种*参数化报告*是接受处理报表时使用的输入值的报表。

使用参数化报告，您可以根据运行时设置的值改变报告的输出。 Reporting Services 支持两种参数：查询参数和报表参数。

- **查询参数**用于在数据处理过程中选择或过滤数据。如果指定了查询参数，则必须由用户或默认属性提供一个值，以完成为报表检索数据的 SELECT 语句或存储过程。
- **报表参数**在报表处理期间使用，以显示数据的不同方面。报表参数通常用于过滤大量记录，但根据报表中的查询和表达式，它也可以有其他用途。

报表参数与查询参数的不同之处在于，它们在报表中定义并由报表服务器处理，而查询参数定义为数据集查询的一部分并在数据库服务器上处理。在 Aspose.Cells.Report.Designer 中，查询参数在 Microsoft Query 中的查询创建时指定。

您可以在 Aspose.Cells.Report.Designer 中创建报表参数并将查询参数映射到相应的报表参数。这样，就可以为报表参数选择值并将它们传递到查询中以限制从数据源检索的数据。

{{% /alert %}} 
###### **本节包括以下主题：**
- [创建报告参数](/cells/zh/reportingservices/creating-report-parameters/)
- [修改报告参数](/cells/zh/reportingservices/modifying-report-parameters/)
- [将查询参数映射到报告参数](/cells/zh/reportingservices/mapping-query-parameters-to-report-parameters/)
