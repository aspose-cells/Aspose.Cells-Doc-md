---
title: Spécification des chiffres significatifs à stocker dans le fichier Excel
type: docs
weight: 20
url: /fr/java/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Scénarios d'utilisation possibles**

Par défaut, Aspose.Cells stocke 17 chiffres significatifs de valeurs double dans les feuilles de calcul, contrairement à l'application Excel qui ne stocke que 15 chiffres significatifs. Vous pouvez changer le comportement par défaut d'Aspose.Cells pour ce cas, c'est-à-dire; vous pouvez changer le nombre de chiffres significatifs de 17 à 15 tout en utilisant la propriété [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits).

## **Spécification des chiffres significatifs à stocker dans le fichier Excel**

Le code d'exemple suivant oblige Aspose.Cells à utiliser 15 chiffres significatifs lors du stockage de valeurs double dans le fichier Excel. Veuillez consulter le [fichier Excel de sortie](23166982.xlsx). Changez son extension en .zip, décompressez-le et vous verrez que seuls 15 chiffres significatifs sont stockés dans le fichier Excel. La capture d'écran suivante explique l'effet de la propriété [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits) sur le fichier Excel de sortie.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
{{< app/cells/assistant language="java" >}}
