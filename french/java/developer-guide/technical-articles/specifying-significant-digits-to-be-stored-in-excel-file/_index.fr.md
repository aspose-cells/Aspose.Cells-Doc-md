---
title: Spécification des chiffres significatifs à stocker dans le fichier Excel
type: docs
weight: 20
url: /fr/java/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **Scénarios d'utilisation possibles**

Par défaut, Aspose.Cells stocke 17 chiffres significatifs de valeurs doubles dans les feuilles de calcul contrairement à l'application Excel qui ne stocke que 15 chiffres significatifs. Vous pouvez modifier le comportement par défaut de Aspose.Cells pour ce cas, c'est-à-dire ; vous pouvez changer le nombre de chiffres significatifs de 17 à 15 tout en utilisant le[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)propriété.

## **Spécification des chiffres significatifs à stocker dans le fichier Excel**

 L'exemple de code suivant force Aspose.Cells à utiliser 15 chiffres significatifs tout en stockant des valeurs doubles dans le fichier Excel. S'il vous plaît, vérifiez le[fichier excel de sortie](23166982.xlsx) . Changez son extension en .zip et décompressez-le et vous verrez, seuls 15 chiffres significatifs sont stockés dans le fichier Excel. La capture d'écran suivante explique l'effet de[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)propriété sur le fichier Excel de sortie.

![tâche : image_autre_texte](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
