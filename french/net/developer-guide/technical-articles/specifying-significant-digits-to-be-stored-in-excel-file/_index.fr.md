---
title: Spécification des chiffres significatifs à stocker dans le fichier Excel
type: docs
weight: 30
url: /fr/net/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **Scénarios d'utilisation possibles**

Par défaut, Aspose.Cells stocke 17 chiffres significatifs de valeurs doubles dans le fichier Excel, contrairement à MS-Excel qui ne stocke que 15 chiffres significatifs. Vous pouvez modifier le comportement par défaut de Aspose.Cells de 17 chiffres significatifs à 15 chiffres significatifs à l'aide de la[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)la propriété.

## **Spécification des chiffres significatifs à stocker dans le fichier Excel**

 L'exemple de code suivant force Aspose.Cells à utiliser 15 chiffres significatifs tout en stockant des valeurs doubles dans le fichier Excel. S'il vous plaît, vérifiez le[fichier excel de sortie](22774105.xlsx) . Changez son extension en .zip et décompressez-le et vous verrez, seuls 15 chiffres significatifs sont stockés dans le fichier Excel. La capture d'écran suivante explique l'effet de[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)propriété sur le fichier Excel de sortie.

![tâche : image_autre_texte](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
