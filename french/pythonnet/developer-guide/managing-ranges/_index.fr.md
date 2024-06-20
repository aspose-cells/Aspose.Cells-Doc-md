---
title: Gestion des plages
linktitle: Plages
type: docs
weight: 105
url: /fr/python-net/managing-ranges/
description: Cet article montre comment gérer les plages avec l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Gérer les plages en Python, Créer une plage en Python, Mettre une valeur dans les cellules de la plage en Python, Définir le style des cellules de la plage en Python, Obtenir CurrentRegion de la plage en Python.
---

## **Introduction**

Dans Excel, vous pouvez sélectionner plusieurs cellules avec une sélection de zone à la souris, l'ensemble des cellules sélectionnées est appelé "Plage".

Par exemple, vous pouvez cliquer avec le bouton gauche de la souris dans la cellule "A1" d'Excel, puis faire glisser jusqu'à la cellule "C4". La zone rectangulaire que vous avez sélectionnée peut également être facilement créée en tant qu'objet en utilisant Aspose.Cells pour Python via .NET.

Voici comment créer une plage, mettre une valeur, définir un style et effectuer d'autres opérations sur l'objet "Plage".

## **Gestion des Plages en Utilisant la Bibliothèque Excel Aspose.Cells pour Python**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

## **Comment Créer une Plage**

Lorsque vous souhaitez créer une zone rectangulaire qui s'étend sur A1:C4, vous pouvez utiliser le code suivant :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Create.py" >}}

## **Comment Mettre une Valeur dans les Cellules de la Plage**

Supposons que vous avez une plage de cellules qui s'étend de A1 à C4. La matrice crée 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées séquentiellement.

L'exemple suivant montre comment saisir des valeurs dans les cellules de la plage.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-PutValue.py" >}}

## **Comment Définir le Style des Cellules de la Plage**

L'exemple suivant montre comment définir le style des cellules de la plage.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-SetStyle.py" >}}

## **Comment Obtenir la Région Actuelle de la Plage**

CurrentRegion est une propriété qui renvoie un objet Range qui représente la région actuelle. 

La région actuelle est une plage délimitée par une combinaison de lignes vierges et de colonnes vierges. En lecture seule.

Dans Excel, vous pouvez obtenir la région actuelle en :
1. Sélectionnez une zone (plage1) avec la boîte de souris.
2. Cliquez sur "Accueil - Modification - Recherche et sélection - Atteindre une spécificité - Région actuelle", ou utilisez "Ctrl+Maj+*", vous verrez qu'Excel vous aide automatiquement à sélectionner une zone (plage2), maintenant vous l'avez fait, la plage2 est la région actuelle de la plage1.

En utilisant Aspose.Cells pour Python via .NET, vous pouvez utiliser la propriété "Range.current_region" pour effectuer la même fonction.

Veuillez télécharger le fichier de test suivant, l'ouvrir dans Excel, utiliser la boîte de souris pour sélectionner une zone "A1:D7", puis cliquer sur "Ctrl+Maj+*", vous verrez que la zone "A1:C3" est sélectionnée.

[current_region.xlsx](current_region.xlsx)

Veuillez maintenant exécuter l'exemple suivant, voyez comment cela fonctionne dans Aspose.Cells pour Python via .NET :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CurrentRegion.py" >}}

## **Sujets avancés**
- [Plage AutoFill du fichier Excel](/cells/fr/python-net/autofill-ranges/)
- [Copier des plages de cellules d'Excel](/cells/fr/python-net/copy-ranges-of-excel/)
- [Copier uniquement les données de la plage](/cells/fr/python-net/copy-range-data-only/)
- [Copier les données de la plage avec le style](/cells/fr/python-net/copy-range-data-with-style/)
- [Copier uniquement le style de la plage](/cells/fr/python-net/copy-range-style-only/)
- [Créer l'union de la plage](/cells/fr/python-net/create-union-range/)
- [Couper et coller la plage](/cells/fr/python-net/cut-and-paste-cells/)
- [Supprimer les plages](/cells/fr/python-net/delete-ranges-from-excel/)
- [Obtenir le nombre de cellules, le décalage de la plage entière de colonne et de ligne entière](/cells/fr/python-net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insérer des plages](/cells/fr/python-net/insert-ranges-to-excel/)
- [Fusionner ou séparer la plage de cellules](/cells/fr/python-net/merge-or-unmerge-range-of-cells/)
- [Déplacer une plage de cellules dans une feuille de calcul](/cells/fr/python-net/move-range-of-cells-in-a-worksheet/)
- [Créer des plages nommées en fonction du classeur et de la feuille de calcul](/cells/fr/python-net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Rechercher et remplacer des données dans une plage](/cells/fr/python-net/search-and-replace-data-in-a-range/)

