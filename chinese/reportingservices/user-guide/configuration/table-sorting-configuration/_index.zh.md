---
title: 表排序配置
type: docs
weight: 90
url: /zh/reportingservices/table-sorting-configuration/
---
配置包括5种属性。这些包括报表名称、表名称、行偏移值、列索引和订单类型。

- **姓名**代表报告名称和表名称。 name 为空时代表整个报表。
- **价值**表示行偏移量。
- **指数**表示表中的列位置。
- **命令**表示排序顺序类型。

TableSorted 配置示例：

*<表格排序>
<Report name=”report name” >
<Table name="table name">
<RowOffset value="1"/>
<Column Index="1" Order="Descending" />
<Column Index="2" Order="Ascending" />
……
</Table>
<Table name="table name">
<RowOffset value="1"/>
<Column Index="1" Order="Descending" />
<Column Index="2" Order="Ascending" />
……
</Table>
</Report>
</TableSorted>*
