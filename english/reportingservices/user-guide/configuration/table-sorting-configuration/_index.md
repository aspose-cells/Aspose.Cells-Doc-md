---
title: Table Sorting Configuration
type: docs
weight: 90
url: /reportingservices/table-sorting-configuration/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

The configuration includes five kinds of properties. These include report name, table name, row offset value, column index, and order type.

- **Name** represents the report name and table name. **Name** represents the whole report when it is blank.  
- **Value** represents the row offset.  
- **Index** represents the column position in the table.  
- **Order** represents the sort order type.  

TableSorted Configuration Example:

*<TableSorted>
<Report name="report name">
    <Table name="table name">
        <RowOffset value="1"/>
        <Column Index="1" Order="Descending"/>
        <Column Index="2" Order="Ascending"/>
        ……
    </Table>
    <Table name="table name">
        <RowOffset value="1"/>
        <Column Index="1" Order="Descending"/>
        <Column Index="2" Order="Ascending"/>
        ……
    </Table>
</Report>
</TableSorted>*
