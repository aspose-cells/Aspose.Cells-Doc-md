---
title: Lecture et écriture de table de requêtes de feuille de calcul
type: docs
weight: 560
url: /fr/java/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}} 

Aspose.Cells fournit une collection [Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) qui renvoie la [QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection). Pour obtenir un [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) spécifique, utilisez la propriété [QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\)) et transmettez l'index du QueryTable. La classe [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) possède les deux propriétés suivantes pour ajuster la QueryTable.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Ce sont toutes deux des valeurs booléennes. Vous pouvez les consulter dans Microsoft Excel via Données > Connexions > Propriétés.

{{% /alert %}} 
## **Lecture et écriture d'un tableau de requête de feuille de calcul**
Le code d'exemple suivant lit le premier [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) de la première feuille de calcul et imprime ensuite les deux propriétés [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable). Ensuite, il définit le [QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) à **true**.

La capture d'écran suivante montre le [fichier Excel source](5472578.xlsx) utilisé dans le code et ses propriétés montrant les deux valeurs de [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable).

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_1.png)

La capture d'écran suivante montre le [fichier Excel de sortie](5472574.xlsx) généré par le code et ses propriétés montrant les deux valeurs de [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable). Comme vous pouvez le voir, la case à cocher de formatage préservé est maintenant cochée.

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Sortie console**
Voici la sortie de la console du code d'exemple ci-dessus

{{< highlight java >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}

## **Récupérer la plage de résultats de la table de requête**
Aspose.Cells offre la possibilité de lire l'adresse, c'est-à-dire la plage de résultats des cellules pour une table de requête. Le code suivant illustre cette fonctionnalité en lisant l'adresse de la plage de résultats pour une table de requête. Le fichier d'exemple peut être téléchargé [ici](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
