---
title: Konfiguration der Tabellensortierung
type: docs
weight: 90
url: /de/reportingservices/table-sorting-configuration/
---
Die Konfiguration umfasst 5 Arten von Eigenschaften. Dazu gehören Berichtsname, Tabellenname, Zeilenoffsetwert, Spaltenindex und Auftragstyp.

- **Name** stellt Berichtsname und Tabellenname dar. name steht für den gesamten Bericht, wenn name leer ist.
- **Wert** stellt den Zeilenoffset dar.
- **Index** stellt die Spaltenposition in der Tabelle dar.
- **Befehl** stellt den Sortierreihenfolgetyp dar.

TableSorted-Konfigurationsbeispiel:

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
