---
title: Tabellsorteringskonfiguration
type: docs
weight: 90
url: /sv/reportingservices/table-sorting-configuration/
---
Konfigurationen inkluderar 5 typer av egenskaper. Dessa inkluderar rapportnamn, tabellnamn, radförskjutningsvärde, kolumnindex och ordertyp.

- **namn** representerar rapportnamn och tabellnamn. namn representerar hela rapporten när namnet är tomt.
- **värde** representerar radförskjutning.
- **Index** representerar kolumnpositionen i tabellen.
- **Ordning** representerar sorteringsordningstyp.

TabellSorterad konfigurationsexempel:

*<TabellSorterad>
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
