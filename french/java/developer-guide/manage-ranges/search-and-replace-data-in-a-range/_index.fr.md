---
title: Rechercher et remplacer des données dans une plage
type: docs
weight: 60
url: /fr/java/search-and-replace-data-in-a-range/
description: Cet article montre comment rechercher et remplacer des données dans une plage dans Excel en utilisant du code Java.
keywords: java rechercher et remplacer des données dans excel, java rechercher des données dans excel, java rechercher et remplacer des données dans une plage, java rechercher des données dans une plage, java recherche de données dans une plage, java recherche de données dans une plage, java recherche de données dans excel, java rechercher des données dans une plage, rechercher et remplacer des données dans excel avec java, rechercher et remplacer des données dans une plage avec java, rechercher et remplacer des données dans une plage avec java
---

{{% alert color="primary" %}}

Parfois, vous avez besoin de rechercher et remplacer des données spécifiques dans une plage, en ignorant les valeurs de cellule en dehors de la plage désirée. Aspose.Cells vous permet de limiter une recherche à une plage spécifique. Cet article explique comment.

{{% /alert %}}

Aspose.Cells fournit la méthode [**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) pour spécifier une plage lors de la recherche de données.

Supposons que vous voulez rechercher la chaîne **"recherche"** et la remplacer par **"remplacer"** dans la plage **E3:H6**. Dans la capture d'écran ci-dessous, la chaîne "rechercher" est visible dans plusieurs cellules, mais nous voulons la remplacer uniquement dans une plage donnée, ici surlignée en jaune.

**Fichier d'entrée**

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

Après l'exécution du code, le fichier de sortie ressemble à ce qui suit. Toutes les chaînes "rechercher" dans la plage ont été remplacées par "remplacer".

**Fichier de sortie**

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## Articles Connexes

- [Trouver ou rechercher des données](/cells/fr/java/find-or-search-data/)
