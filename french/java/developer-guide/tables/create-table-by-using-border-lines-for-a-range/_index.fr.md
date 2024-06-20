---
title: Créer un tableau en utilisant des lignes de bordure pour une plage
type: docs
weight: 50
url: /fr/java/create-table-by-using-border-lines-for-a-range/
description: Comment créer une table avec une plage en utilisant des lignes de bordure. Aspose.Cells for Java fournit une API simple à utiliser qui peut être utilisée pour ajouter des bordures à une plage.
keywords: créer un tableau, plage en tableau, plage en tableau excel, plage en tableau avec bordures, comment créer un tableau à partir d une plage, convertir une plage en tableau, excel convertir une plage en tableau, excel créer un tableau, plage en tableau java 
---

{{% alert color="primary" %}}

Parfois, vous voulez créer un tableau en ajoutant des lignes de bordure pour une **Plage**/**Zone de cellules** en fonction de l'adresse des cellules que vous avez. Vous pouvez utiliser la méthode [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean)) pour créer une plage de cellules. La méthode [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean)) renvoie un objet [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range). Vous pouvez créer un objet [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) et spécifier les options de bordures (haut, gauche, bas, droite) en conséquence. Plus tard, vous pouvez obtenir les cellules de la [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) et appliquer la mise en forme souhaitée aux cellules.

{{% /alert %}}

L'exemple suivant montre comment créer un [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) et spécifier les limites pour les cellules de la plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

Après avoir exécuté le code ci-dessus, nous pouvons obtenir le fichier Excel généré contenant le tableau formaté; voici la capture d'écran du fichier.

![todo:image_alt_text](create-table-by-using-border-lines-for-a-range_1.png)
