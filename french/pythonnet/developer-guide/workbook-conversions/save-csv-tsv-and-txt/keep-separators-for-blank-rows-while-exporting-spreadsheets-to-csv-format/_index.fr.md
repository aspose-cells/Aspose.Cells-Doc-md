---
title: Conserver les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul au format CSV
type: docs
weight: 160
url: /fr/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Conservez les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul au format CSV en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Python Conservez les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul au format CSV, Conservez les séparateurs pour les lignes vides lors de l enregistrement du classeur au format CSV en Python via NET, Python Conservez les séparateurs pour les lignes vides lors de l exportation du classeur au format CSV.
---

## **Conserver les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV**

Aspose.Cells pour Python via .NET offre la possibilité de conserver les séparateurs de ligne lors de la conversion des feuilles de calcul au format CSV. Pour cela, vous pouvez utiliser la propriété [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) de la classe [**TxtSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/). [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) est une propriété booléenne. Pour conserver les séparateurs pour les lignes vides lors de la conversion du fichier Excel en CSV, définissez la propriété [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) sur **true**.

Le code d'exemple suivant charge le [fichier Excel source](84378743.xlsx). Il définit la propriété [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) sur **true** et l'enregistre sous le nom [output.csv](84378744.csv). La capture d'écran montre la comparaison entre le fichier Excel source, la sortie par défaut générée lors de la conversion de la feuille de calcul en CSV et la sortie générée en définissant [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) sur **true**.

![todo:image_alt_text](result.jpg)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-KeepSeparatorsForBlankRow-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
