---
title: Trimer les lignes et colonnes vides en début lors de l exportation de feuilles de calcul en format CSV avec Golang via C++
linktitle: Apprenez comment supprimer les lignes et colonnes vides en tête lors de l exportation de feuilles de calcul en format CSV en utilisant Aspose.Cells avec C++.
type: docs
weight: 100
url: /fr/go-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Découvrez comment couper les lignes et colonnes vides en tête lors de l exportation de feuilles de calcul au format CSV en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Parfois, votre fichier Excel ou CSV comporte des colonnes ou lignes vides en tête. Par exemple, considérez cette ligne :

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Ici, les trois premières cellules ou colonnes sont vides. Lorsque vous ouvrez un tel fichier CSV dans Microsoft Excel, Microsoft Excel ignore ces lignes et colonnes vides initiales.

Par défaut, Aspose.Cells ne supprime pas les colonnes et lignes vides de tête lors de l'enregistrement, mais si vous souhaitez les supprimer comme le fait Microsoft Excel, alors Aspose.Cells fournit la propriété [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/). Veuillez la définir sur **true** et ensuite toutes les colonnes et lignes vides de tête seront supprimées lors de l'enregistrement.

{{% alert color="primary" %}}

Avant la sortie de Aspose.Cells for C++ 20.4, la valeur par défaut de [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) était **false**. Depuis la version 20.4, la valeur par défaut de [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) est **true.**

{{% /alert %}}

## **Supprimer les lignes et colonnes vides en tête lors de l'exportation de feuilles de calcul au format CSV**

Le code d'exemple suivant charge le [fichier Excel source](sampleTrimBlankColumns.xlsx) qui contient deux premières colonnes vides. Il enregistre d'abord le fichier Excel au format CSV sans aucun changement, puis définit la propriété [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) sur **true** et l'enregistre à nouveau. La capture d'écran montre le [fichier Excel source](sampleTrimBlankColumns.xlsx), le [fichier CSV en sortie sans suppression](outputWithoutTrimBlankColumns.csv) et le [fichier CSV en sortie avec suppression](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCsvFormat.go" >}}
