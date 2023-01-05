---
title: Créer un tableau en utilisant des lignes de bordure pour une plage
type: docs
weight: 50
url: /fr/java/create-table-by-using-border-lines-for-a-range/
description: Comment créer un tableau avec plage en utilisant des lignes de bordure. Aspose.Cells for Java fournit un API simple à utiliser qui peut être utilisé pour ajouter des bordures à une plage.
keywords: create table, range to table, range to table excel, excel range to table, range to table with borders, how to create table from range, convert range to table, excel convert range to table, excel create table, range to table java 
---
{{% alert color="primary" %}}

 Parfois, vous souhaitez créer un tableau en ajoutant des lignes de bordure pour un**Intervalle**/**ZoneCellule** en fonction de l'adresse des cellules que vous avez. Vous pouvez utiliser[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean) ) méthode pour créer une plage de cellules. Le[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean) ) La méthode renvoie un[**Intervalle**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) objet. Vous pouvez créer un[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objet et spécifiez les options de bordures (haut, gauche, bas, droite) en conséquence. Plus tard, vous pouvez obtenir les cellules de la[**Intervalle**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)et appliquez la mise en forme souhaitée aux cellules.

{{% /alert %}}

 L'exemple suivant montre comment créer un[**Intervalle**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)et spécifiez les limites des cellules de la plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

Après avoir exécuté le code ci-dessus, nous pouvons avoir le fichier Excel généré contenant le tableau formaté ; voici la capture d'écran du fichier.

![tâche : image_autre_texte](create-table-by-using-border-lines-for-a-range_1.png)
