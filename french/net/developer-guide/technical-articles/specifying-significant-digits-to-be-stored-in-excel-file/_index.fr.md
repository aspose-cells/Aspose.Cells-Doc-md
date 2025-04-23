---
title: Spécification des chiffres significatifs à stocker dans le fichier Excel
type: docs
weight: 30
url: /fr/net/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Scénarios d'utilisation possibles**

Par défaut, Aspose.Cells stocke 17 chiffres significatifs des valeurs double dans le fichier Excel, contrairement à MS-Excel qui stocke seulement 15 chiffres significatifs. Vous pouvez modifier le comportement par défaut de Aspose.Cells de 17 chiffres significatifs à 15 chiffres significatifs en utilisant la propriété [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits).

## **Spécification des chiffres significatifs à stocker dans le fichier Excel**

Le code d'exemple suivant force Aspose.Cells à utiliser 15 chiffres significatifs lors du stockage des valeurs doubles dans le fichier Excel. Veuillez vérifier le [fichier Excel de sortie](22774105.xlsx). Changez son extension en .zip, décompressez-le et vous verrez que seuls 15 chiffres significatifs sont stockés dans le fichier Excel de sortie. La capture d'écran suivante explique l'effet de la propriété [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits) sur le fichier Excel de sortie.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
{{< app/cells/assistant language="csharp" >}}
