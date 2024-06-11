---
title: 表格排序配置
type: docs
weight: 90
url: /zh/reportingservices/table-sorting-configuration/
---

该配置包括5种属性。这些属性包括报告名称、表名称、行偏移值、列索引和排序类型。

- **name** 代表报告名称和表名称。当名称为空时，name代表整个报告。
- **value** 代表行偏移。
- **Index** 代表表中的列位置。
- **Order** 代表排序类型。

表格排序配置示例：

*<TableSorted>
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
