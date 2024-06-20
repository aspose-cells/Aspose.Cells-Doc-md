---
title: Conserver les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul au format CSV
type: docs
weight: 160
url: /fr/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Conserver les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV**

Aspose.Cells offre la possibilité de conserver les séparateurs de lignes lors de la conversion de feuilles de calcul au format CSV. Pour cela, vous pouvez utiliser la propriété [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) de la classe [**TxtSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions). [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) est une propriété booléenne. Pour conserver les séparateurs pour les lignes vides lors de la conversion du fichier Excel en CSV, définissez la propriété [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) sur **true**.

Le code d'exemple suivant charge le [fichier Excel source](84378743.xlsx). Il définit la propriété [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) sur **true** et l'enregistre sous le nom [output.csv](84378744.csv). La capture d'écran montre la comparaison entre le fichier Excel source, la sortie par défaut générée lors de la conversion de la feuille de calcul en CSV et la sortie générée en définissant [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) sur **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}
