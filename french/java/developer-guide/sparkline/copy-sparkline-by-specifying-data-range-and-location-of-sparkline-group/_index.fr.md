---
title: Copier le mini graphique en spécifiant la plage de données et l emplacement du groupe de mini graphiques
type: docs
weight: 120
url: /fr/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

Copier le mini-graphique en spécifiant la plage de données et l'emplacement du groupe de mini-graphiques dans MS Excel

Microsoft Excel vous permet de copier une Sparkline en spécifiant la plage de données et l'emplacement du groupe de Sparkline. Suivez ces étapes pour copier votre Sparkline dans d'autres cellules.

- Sélectionnez la cellule contenant votre Sparkline.
- Sélectionnez **Modifier les données** dans la section **Sparkline** à l'intérieur de l'onglet **Création**.
- Choisissez **Modifier l'emplacement et les données du groupe...**
- Spécifiez la plage de données et l'emplacement et cliquez sur OK.

## Exemple

Aspose.Cells fournit la méthode [**SparklineCollection.add(dataRange, row, column)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) pour spécifier la plage de données et l'emplacement du groupe de Sparkline.

### Captures d'écran des fichiers source et de sortie

La capture d'écran suivante montre le fichier Excel source utilisé dans le code. La zone surlignée en rouge montre l'option "**Modifier l'emplacement et les données du groupe...**" pour spécifier la plage de données et l'emplacement du groupe de sparkline. La cellule P4 montre la sparkline qui sera copiée dans les quatre autres cellules remplies de couleur jaune à l'aide de Aspose.Cells.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

La capture d'écran suivante montre le fichier Excel de sortie généré par le code d'exemple. Comme vous pouvez le voir, la sparkline dans la cellule P4 a été copiée dans les quatre cellules suivantes de la colonne P, chacune avec une plage de données différente.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Code Java pour copier une sparkline en spécifiant la plage de données et l'emplacement du groupe de sparkline

Le code d'exemple suivant charge le fichier Excel source comme indiqué dans la capture d'écran ci-dessus, puis accède au premier groupe de sparkline et ajoute des plages de données et des emplacements à l'intérieur du groupe de sparkline. Enfin, il écrit le fichier Excel de sortie sur le disque, comme le montre également la capture d'écran ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
