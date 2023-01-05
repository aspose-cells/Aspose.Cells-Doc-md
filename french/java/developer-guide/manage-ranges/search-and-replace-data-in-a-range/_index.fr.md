---
title: Rechercher et remplacer des données dans une plage
type: docs
weight: 60
url: /fr/java/search-and-replace-data-in-a-range/
description: Cet article explique comment rechercher et remplacer des données dans une plage dans Excel à l'aide du code Java.
keywords: java search and replace data in excel, java search data in excel, java search and replace data in a range, java search data in a range, java searching data in a range, java searching data in range, java searching data in excel, java search data in range, search and replace data in excel with java, search and replace data in a range with java, search and replace data in range with java
---
{{% alert color="primary" %}}

Parfois, vous devez rechercher et remplacer des données spécifiques dans une plage, en ignorant les valeurs de cellule en dehors de la plage souhaitée. Aspose.Cells vous permet de limiter une recherche à une plage spécifique. Cet article explique comment.

{{% /alert %}}

Aspose.Cells fournit le[**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) méthode pour spécifier une plage lors de la recherche de données.

 Supposons que vous souhaitiez rechercher la chaîne**"rechercher"** et le remplacer par**"remplacer"** dans le périmètre**E3:H6**. Dans la capture d'écran ci-dessous, la chaîne "recherche" peut être vue dans plusieurs cellules mais nous voulons la remplacer uniquement dans une plage donnée, ici surlignée en jaune.

**Fichier d'entrée**

![tâche : image_autre_texte](search-and-replace-data-in-a-range_1.png)

Après l'exécution du code, le fichier de sortie ressemble à ce qui suit. Toutes les chaînes de "recherche" dans la plage ont été remplacées par "remplacer".

**Fichier de sortie**

![tâche : image_autre_texte](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## Articles Liés

- [Rechercher ou rechercher des données](/cells/fr/java/find-or-search-data/)
