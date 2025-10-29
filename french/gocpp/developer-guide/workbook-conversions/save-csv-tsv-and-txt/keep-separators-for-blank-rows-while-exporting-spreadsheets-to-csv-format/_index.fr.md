---
title: Conserver les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul en format CSV avec Golang via C++
linktitle: Conserver les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul au format CSV
type: docs
weight: 160
url: /fr/go-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Découvrez comment conserver les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul en format CSV en utilisant Aspose.Cells avec Golang via C++.
---

## **Conserver les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV**

Aspose.Cells offre la capacité de conserver les séparateurs de ligne lors de la conversion de feuilles de calcul en format CSV. Pour cela, vous pouvez utiliser la propriété [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) de la classe [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/). [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) est une propriété booléenne. Pour conserver les séparateurs pour les lignes vides lors de la conversion du fichier Excel en CSV, définissez la propriété [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) sur **true**.

Le code d'exemple suivant charge le [fichier Excel source](84378743.xlsx). Il définit la propriété [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) à **true** et le sauvegarde en tant que [output.csv](84378744.csv). La capture d'écran montre la comparaison entre le fichier Excel source, la sortie par défaut générée lors de la conversion en CSV, et la sortie générée en définissant [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) à **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-KeepSeparatorsForBlankRowsWhileExportingSpreadsheetsToCsvFormat.go" >}}
