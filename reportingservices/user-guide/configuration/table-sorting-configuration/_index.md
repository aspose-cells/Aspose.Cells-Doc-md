---
title: Table Sorting Configuration
type: docs
weight: 90
url: /reportingservices/table-sorting-configuration/
---

The configuration includes 5 kinds of properties. These include report name, table name, row offset value, column index and order type.

- **name** represents report name and table name. name represents the whole report when name is blank.
- **value** represents row offset.
- **Index** represents column position in table.
- **Order** represents sort order type.

TableSorted Configuration Example:

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
