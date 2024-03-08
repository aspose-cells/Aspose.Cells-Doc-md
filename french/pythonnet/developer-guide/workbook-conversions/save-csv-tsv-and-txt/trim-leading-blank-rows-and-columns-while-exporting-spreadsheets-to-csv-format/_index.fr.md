---
title: Supprimez les premières lignes et colonnes vides lors de l'exportation de feuilles de calcul au format CSV.
type: docs
weight: 100
url: /fr/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Coupez les premières lignes et colonnes vides lors de l'exportation de feuilles de calcul au format CSV en utilisant Aspose.Cells for Python via .NET API.
keywords: Python Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format, Trim Leading Blank Rows and Columns while saving excel to CSV format in Python via NET, Python Trim Leading Blank Rows and Columns exporting excel to CSV format.
---
##  **Scénarios d'utilisation possibles**

Parfois, votre fichier Excel ou CSV comporte des colonnes ou des lignes vides au début. Par exemple, considérons cette ligne

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Ici, les trois premières cellules ou colonnes sont vides. Lorsque vous ouvrez un tel fichier CSV dans Microsoft Excel, Microsoft Excel supprime ces premières lignes et colonnes vides.

 Par défaut, Aspose.Cells for Python via .NET ne supprime pas les premières colonnes et lignes vides lors de l'enregistrement, mais si vous souhaitez les supprimer comme le fait Microsoft Excel, alors Aspose.Cells for Python via .NET fournit**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** propriété. Veuillez le régler sur**vrai**puis toutes les premières lignes et colonnes vides seront supprimées lors de l'enregistrement.

{{% alert color="primary" %}}

Avant la sortie de Aspose.Cells for Python via .NET 20.4, la valeur par défaut de**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** était**FAUX**. Depuis la version 20.4, la valeur par défaut de **[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** est**vrai.**

{{% /alert %}}

##  **Supprimez les premières lignes et colonnes vides lors de l'exportation de feuilles de calcul au format CSV.**

 L'exemple de code suivant charge le[fichier Excel source](sampleTrimBlankColumns.xlsx) qui comporte deux premières colonnes vides. Il enregistre d'abord le fichier Excel au format CSV sans aucune modification, puis il définit**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** propriété à**vrai** et l'enregistre à nouveau. La capture d'écran montre le[fichier Excel source](sampleTrimBlankColumns.xlsx), [sortie du fichier CSV sans découpage](outputWithoutTrimBlankColumns.csv), et le[sortie du fichier CSV avec découpage](outputTrimBlankColumns.csv).

![tâche : image_alt_text](result.png)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
