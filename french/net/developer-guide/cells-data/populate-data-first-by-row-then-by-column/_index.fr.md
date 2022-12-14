---
title: Remplir les données d'abord par ligne puis par colonne
type: docs
weight: 1000
url: /fr/net/populate-data-first-by-row-then-by-column/
---
{{% alert color="primary" %}} 

Remplir une feuille de calcul avec des données d'abord par ligne, puis par colonne améliore les performances globales.

{{% /alert %}} 

Mettre les données dans la séquence A1, B1, A2, B2 est plus rapide que A1, A2, B1, B2. S'il y a beaucoup de cellules dans une feuille de calcul et que vous suivez la deuxième séquence, c'est-à-dire que vous remplissez les données ligne par ligne, cette astuce peut rendre le programme beaucoup plus rapide.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-PopulateDataEfficiently-PopulateDataFirstByRowThenColumns.cs" >}}
