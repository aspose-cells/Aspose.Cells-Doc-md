---
title: Spécification des chiffres significatifs à stocker dans le fichier Excel avec Golang via C++
linktitle: Spécification des chiffres significatifs
type: docs
weight: 30
url: /fr/go-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Apprenez comment spécifier le nombre de chiffres significatifs à stocker dans les fichiers Excel en utilisant Aspose.Cells avec Golang via C++.
---

## **Scénarios d'utilisation possibles**

Par défaut, Aspose.Cells stocke 17 chiffres significatifs des valeurs doubles à l'intérieur du fichier Excel, contrairement à MS-Excel qui ne stocke que 15 chiffres significatifs. Vous pouvez modifier le comportement par défaut d'Apose.Cells de 17 chiffres significatifs à 15 chiffres significatifs en utilisant la propriété [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/).

## **Spécification des chiffres significatifs à stocker dans le fichier Excel**

Le code d'exemple suivant force Aspose.Cells à utiliser 15 chiffres significatifs lors du stockage des valeurs doubles dans le fichier Excel. Veuillez vérifier le [fichier Excel en sortie](22774105.xlsx). Changez son extension en .zip et dézippez-le, et vous verrez que seuls 15 chiffres significatifs sont stockés dans le fichier Excel. La capture d'écran suivante explique l'effet de la propriété [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) sur le fichier Excel en sortie.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSignificantDigitsToBeStoredInExcelFile.go" >}}
