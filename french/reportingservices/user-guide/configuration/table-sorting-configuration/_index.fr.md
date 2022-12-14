---
title: Configuration du tri des tables
type: docs
weight: 90
url: /fr/reportingservices/table-sorting-configuration/
---
La configuration comprend 5 types de propriétés. Ceux-ci incluent le nom du rapport, le nom de la table, la valeur de décalage de ligne, l'index de colonne et le type de commande.

- **Nom** représente le nom du rapport et le nom de la table. nom représente l'ensemble du rapport lorsque nom est vide.
- **évaluer** représente le décalage de ligne.
- **Indice** représente la position de la colonne dans le tableau.
- **Ordre** représente le type d'ordre de tri.

Exemple de configuration TableSorted :

*<TableTrié>
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
