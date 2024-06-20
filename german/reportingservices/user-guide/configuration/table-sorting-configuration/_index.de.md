---
title: Tabellensortierung Konfiguration
type: docs
weight: 90
url: /de/reportingservices/table-sorting-configuration/
---

Die Konfiguration umfasst 5 Arten von Eigenschaften. Diese umfassen Berichtsnamen, Tabellennamen, Zeilenversatzwert, Spaltenindex und Sortiertyp.

- **name** repräsentiert Berichtsnamen und Tabellennamen. name repräsentiert den gesamten Bericht, wenn name leer ist.
- **value** repräsentiert Zeilenversatz.
- **Index** repräsentiert die Spaltenposition in der Tabelle.
- **Order** repräsentiert den Sortiertyp.

Tabellensortierung Konfigurationsbeispiel:

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
