---
title: Copier les plages d'Excel
linktitle: Copier les plages
type: docs
weight: 30
url: /fr/java/copy-ranges-of-Excel/
---
## **Introduction**

Dans Excel, vous pouvez sélectionner une plage, copier la plage, puis la coller avec des options spécifiques dans la même feuille de calcul, d'autres feuilles de calcul ou d'autres fichiers.

## **Copier les plages à l'aide de Aspose.Cells**

 Aspose.Cells fournit une certaine surcharge[Range.Copy](https://reference.aspose.com/cells/java/com.aspose.cells/range) méthodes pour copier la plage.
## **Plage de copie**

Création de deux plages : la plage source, la plage cible, puis copie de la plage source dans la plage cible avec la méthode Range.Copy.

Voir le code suivant :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range.java" >}}

## **Coller la plage avec des options**

Aspose.Cells prend en charge le collage de la plage avec un type spécifique.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Paste-Range.java" >}}

## **Copiez uniquement les données de la plage.**
Vous pouvez également copier les données avec la méthode Range.CopyData avec les codes suivants :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range-Data.java" >}}


