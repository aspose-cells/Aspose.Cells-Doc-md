---
title: Remplir d abord les données par ligne puis par colonne
type: docs
weight: 10
url: /fr/java/populate-data-first-by-row-then-by-column/
---

{{% alert color="primary" %}}

Remplir une feuille de calcul avec des données d'abord par ligne puis par colonne améliore les performances globales.

{{% /alert %}}

## Remplir d'abord les données par ligne, puis par colonne

Placer les données dans la séquence A1, B1, A2, B2 est plus rapide que A1, A2, B1, B2. S'il y a de nombreuses cellules dans une feuille de calcul et que vous suivez la deuxième séquence, c'est-à-dire que vous remplissez les données ligne par ligne, ce conseil peut rendre le programme beaucoup plus rapide.

## Code Java pour remplir d'abord les données par ligne, puis par colonne

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PopulateDatabyRowthenColumn-PopulateDatabyRowthenColumn.java" >}}
{{< app/cells/assistant language="java" >}}
