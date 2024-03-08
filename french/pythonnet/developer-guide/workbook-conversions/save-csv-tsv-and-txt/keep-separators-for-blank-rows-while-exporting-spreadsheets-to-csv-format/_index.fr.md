---
title: Conservez les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV
type: docs
weight: 160
url: /fr/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Conservez les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV en utilisant Aspose.Cells for Python via .NET API.
keywords: Python Keep Separators for Blank Rows while exporting spreadsheets to CSV format, Keep Separators for Blank Rows while saving excel to CSV format in Python via NET, Python Keep Separators for Blank Rows when exporting excel to CSV format.
---
##  **Conservez les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV**

Aspose.Cells for Python via .NET offre la possibilité de conserver les séparateurs de lignes lors de la conversion des feuilles de calcul au format CSV. Pour cela, vous pouvez utiliser le**[keep_separators_for_blank_row](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)**propriété de**[TxtSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/)**classe.**[keep_separators_for_blank_row](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)**est une propriété booléenne. Pour conserver les séparateurs des lignes vides lors de la conversion du fichier Excel en CSV, définissez le**[keep_separators_for_blank_row](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)**propriété à *true**.

L'exemple de code suivant charge le[fichier Excel source](84378743.xlsx). Il fixe**[keep_separators_for_blank_row](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)**propriété à**vrai** et l'enregistre sous[sortie.csv](84378744.csv) . La capture d'écran montre la comparaison entre le fichier Excel source, la sortie par défaut générée lors de la conversion de la feuille de calcul en CSV et la sortie générée par le paramètre**[keep_separators_for_blank_row](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)**à *vrai**.

![tâche : image_alt_text](result.jpg)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-KeepSeparatorsForBlankRow-1.py" >}}
