---
title: Copier Sparkline en spécifiant la plage de données et l'emplacement du groupe Sparkline
type: docs
weight: 120
url: /fr/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
Copier Sparkline en spécifiant la plage de données et l'emplacement du groupe Sparkline dans MS Excel

Microsoft Excel vous permet de copier un Sparkline en spécifiant la plage de données et l'emplacement du groupe Sparkline. Suivez ces étapes pour copier votre Sparkline dans d'autres cellules.

- Sélectionnez la cellule contenant votre Sparkline.
-  Sélectionner**Modifier les données** du**Sparkline** section à l'intérieur du**Concevoir** languette
-  Choisir**Modifier l'emplacement et les données du groupe...**
- Spécifiez la plage de données et l'emplacement, puis cliquez sur OK.

## Exemple

 Aspose.Cells fournit le[**SparklineCollection.add(dataRange, ligne, colonne)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) pour spécifier la plage de données et l'emplacement du groupe Sparkline.

### Captures d'écran des fichiers source et de sortie

La capture d'écran suivante montre le fichier Excel source utilisé dans le code. La zone en surbrillance rouge indique "**Modifier l'emplacement et les données du groupe...**" option pour spécifier la plage de données et l'emplacement du groupe sparkline. La cellule P4 affiche le sparkline qui sera copié dans les quatre autres cellules remplies de couleur jaune à l'aide de Aspose.Cells.

![tâche : image_autre_texte](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

La capture d'écran suivante montre le fichier Excel de sortie généré par l'exemple de code. Comme vous pouvez le voir, la ligne sparkline de la cellule P4 a été copiée dans les quatre cellules suivantes de la colonne P, chacune avec une plage de données différente.

![tâche : image_autre_texte](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Java code pour copier sparkline en spécifiant la plage de données et l'emplacement du groupe sparkline

L'exemple de code suivant charge le fichier Excel source comme indiqué dans la capture d'écran ci-dessus, puis accède au premier groupe de lignes sparkline et ajoute des plages de données et des emplacements à l'intérieur du groupe de lignes sparkline. Enfin, il écrit le fichier Excel de sortie sur le disque, qui est également illustré dans la capture d'écran ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
