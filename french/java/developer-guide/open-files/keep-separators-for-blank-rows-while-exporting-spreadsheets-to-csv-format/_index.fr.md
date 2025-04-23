---
title: Conserver les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul au format CSV
type: docs
weight: 110
url: /fr/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Conserver les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV**

Aspose.Cells offre la possibilité de conserver les séparateurs de lignes lors de la conversion de feuilles de calcul au format CSV. Pour cela, vous pouvez utiliser la propriété [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) de la classe [**TxtSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions). [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) est une propriété booléenne. Pour conserver les séparateurs pour les lignes vides lors de la conversion du fichier Excel en CSV, définissez la propriété [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) sur **true**.

Le code d'exemple suivant charge le [fichier Excel source](KeepSeparatorsForBlankRow.xlsx). Il définit la propriété [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) sur **true** et l'enregistre sous [KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv). La capture d'écran montre la comparaison entre le fichier Excel source, la sortie par défaut générée lors de la conversion de la feuille de calcul en CSV et la sortie générée en définissant [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) sur **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
{{< app/cells/assistant language="java" >}}
