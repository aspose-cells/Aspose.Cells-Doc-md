---
title: Table de requête de lecture et d'écriture de la feuille de travail
type: docs
weight: 560
url: /fr/java/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}} 

 Aspose.Cells fournit[Feuille de calcul.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) collection qui retourne le[QueryTableCollectionQueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection) . Pour obtenir un[Table de requête](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) , Utilisez le[QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\) ) et transmettez l'index de QueryTable. La[Table de requête](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) La classe a les deux propriétés suivantes pour ajuster le QueryTable.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Ce sont deux valeurs booléennes. Vous pouvez les visualiser dans Microsoft Excel via Données > Connexions > Propriétés.

{{% /alert %}} 
## **Table de requête de lecture et d'écriture de la feuille de travail**
 L'exemple de code suivant lit le premier[Table de requête](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)de la première feuille de calcul, puis imprime les deux[Table de requête](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) Propriétés. Ensuite, il définit le[QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) à**vrai**.

La capture d'écran suivante montre le[fichier excel source](5472578.xlsx) utilisé dans le code et ses propriétés montrant à la fois les[Table de requête](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)valeurs.

![tâche : image_autre_texte](reading-and-writing-query-table-of-worksheet_1.png)

La capture d'écran suivante montre le[fichier excel de sortie](5472574.xlsx) généré par le code et ses propriétés montrant à la fois les[Table de requête](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)valeurs. Comme vous pouvez le voir, la case à cocher Mise en forme conservée est cochée maintenant.

![tâche : image_autre_texte](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Sortie console**
Voici la sortie console de l'exemple de code ci-dessus

{{< highlight "java" >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}
## **Récupérer la plage de résultats de la table de requête**
Aspose.Cells offre la possibilité de lire l'adresse, c'est-à-dire la plage de résultats de cellules pour une table de requête. Le code suivant illustre cette fonctionnalité en lisant l'adresse de la plage de résultats pour une table de requête. Le fichier exemple peut être téléchargé[ici](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
