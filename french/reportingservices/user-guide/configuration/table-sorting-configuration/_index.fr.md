---
title: Configuration de tri de tableau
type: docs
weight: 90
url: /fr/reportingservices/table-sorting-configuration/
---

La configuration inclut 5 types de propriétés. Il s'agit du nom du rapport, du nom du tableau, de la valeur de décalage de ligne, de l'indice de colonne et du type d'ordre.

- **nom** représente le nom du rapport et le nom du tableau. Le nom représente l'ensemble du rapport lorsque le nom est vide.
- **valeur** représente le décalage de ligne.
- **Index** représente la position de la colonne dans le tableau.
- **Ordre** représente le type d'ordre de tri.

Exemple de configuration de tri de tableau:

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
