---
title: Supprimer les lignes et colonnes vides initiales lors de l exportation de feuilles de calcul au format CSV
type: docs
weight: 100
url: /fr/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Éliminer les lignes et colonnes vides en tête lors de l exportation de feuilles de calcul au format CSV en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Python Éliminer les lignes et colonnes vides en tête lors de l exportation de feuilles de calcul au format CSV, Éliminer les lignes et colonnes vides en tête lors de l enregistrement du classeur au format CSV en Python via NET, Python Éliminer les lignes et colonnes vides lors de l exportation du classeur au format CSV.
---

## **Scénarios d'utilisation possibles**

Parfois, votre fichier Excel ou CSV contient des colonnes ou des lignes vides initiales. Par exemple, considérez cette ligne

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Ici, les trois premières cellules ou colonnes sont vides. Lorsque vous ouvrez un tel fichier CSV dans Microsoft Excel, Microsoft Excel ignore ces lignes et colonnes vides initiales.

Par défaut, Aspose.Cells pour Python via .NET ne supprime pas les premières colonnes et lignes vides lors de l'enregistrement, mais si vous souhaitez les supprimer comme le fait Microsoft Excel, alors Aspose.Cells pour Python via .NET fournit la propriété [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/). Veuillez la définir sur **true** et alors toutes les premières lignes et colonnes vides seront supprimées lors de l'enregistrement.

{{% alert color="primary" %}}

Avant la version 20.4 d'Aspose.Cells pour Python via .NET, la valeur par défaut de [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) était **false**. Depuis la version 20.4, la valeur par défaut de [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) est **true**.

{{% /alert %}}

## **Supprimer les lignes et colonnes vides en tête lors de l'exportation de feuilles de calcul au format CSV**

Le code d'exemple suivant charge le [fichier Excel source](sampleTrimBlankColumns.xlsx) qui contient deux premières colonnes vides. Il enregistre d'abord le fichier Excel au format CSV sans aucun changement, puis définit la propriété [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) sur **true** et l'enregistre à nouveau. La capture d'écran montre le [fichier Excel source](sampleTrimBlankColumns.xlsx), le [fichier CSV en sortie sans suppression](outputWithoutTrimBlankColumns.csv) et le [fichier CSV en sortie avec suppression](outputTrimBlankColumns.csv).

![todo:image_alt_text](result.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}
