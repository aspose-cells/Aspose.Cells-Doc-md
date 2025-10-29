---
title: Convertir le texte en colonnes à l aide d Aspose.Cells
type: docs
weight: 30
url: /fr/python-net/convert-text-to-columns-using-aspose-cells/
description: Cet article montre comment convertir du texte en colonnes en utilisant l API Aspose.Cells for Python via .NET.
keywords: Bibliothèque Excel Python, Convertir du texte en colonnes en Python, Convertir du texte en colonnes en Python.
---

## **Scénarios d'utilisation possibles**

Vous pouvez convertir votre texte en colonnes à l'aide de Microsoft Excel. Cette fonctionnalité est disponible dans *Outils de données* sous l'onglet *Données*. Pour diviser le contenu d'une colonne en plusieurs colonnes, les données doivent contenir un délimiteur spécifique tel qu'une virgule (ou tout autre caractère) sur la base duquel Microsoft Excel divise le contenu d'une cellule en plusieurs cellules. Aspose.Cells for Python via .NET fournit également cette fonctionnalité via la méthode [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/).

## **Convertir le texte en colonnes à l'aide d'Aspose.Cells pour la bibliothèque Excel Python**

Le code d'exemple suivant explique l'utilisation de la méthode [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/). Le code ajoute d'abord quelques noms de personnes dans la colonne A de la première feuille de calcul. Le prénom et le nom de famille sont séparés par un espace. Ensuite, il applique la méthode [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) sur la colonne A et enregistre le fichier Excel de sortie. Si vous ouvrez le [fichier Excel de sortie](25395213.xlsx), vous verrez que les prénoms sont dans la colonne A tandis que les noms de famille sont dans la colonne B, comme indiqué dans cette capture d'écran.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-ConvertTextToColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}
