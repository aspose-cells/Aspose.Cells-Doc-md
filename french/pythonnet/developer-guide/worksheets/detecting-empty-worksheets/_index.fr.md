---
title: Détection de feuilles de calcul vides
type: docs
weight: 410
url: /fr/python-net/detecting-empty-worksheets/
description: Cet article vous présente du code expliquant comment détecter de manière programmatique si des feuilles Excel sont vides en utilisant la bibliothèque Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, détecter une feuille vide avec Python, trouver une feuille Excel vide en Python.
---

## **Vérifier les cellules peuplées**

Les feuilles de calcul peuvent avoir une ou plusieurs cellules peuplées de valeurs où une valeur peut être simple (texte, numérique, date/heure) ou une formule ou une valeur basée sur une formule. Dans ce cas, il est facile de détecter si une feuille de calcul donnée est vide ou non. Il suffit de vérifier les propriétés [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) ou [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/). Si les propriétés mentionnées retournent zéro ou des valeurs positives, cela signifie qu'une ou plusieurs cellules ont été peuplées, cependant, si l'une de ces propriétés retourne -1, cela indique que aucune des cellules n'a été peuplée dans la feuille de calcul donnée.

{{% alert color="primary" %}}

Les collections de lignes et de colonnes ont un index à base zéro, donc une cellule à la ligne 0 et à la colonne 0 signifie la première cellule dans la feuille de calcul, qui est A1.

{{% /alert %}}

## **Vérifier les cellules initialisées vides**

Toutes les cellules contenant des valeurs sont initialisées automatiquement, cependant il est possible qu'une feuille ait des cellules uniquement formatées. Dans ce cas, les propriétés [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) ou [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) renverront -1, indiquant l'absence de valeurs remplies, mais les cellules initialisées en raison du format de cellule ne peuvent pas être détectées avec cette approche. Pour vérifier si une feuille a des cellules initialisées vides, il est conseillé d'utiliser la méthode IEnumerator.MoveNext sur l'énumérateur acquis de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Si la méthode IEnumerator.MoveNext retourne **true**, cela signifie qu'il y a une ou plusieurs cellules initialisées dans la feuille donnée.

## **Vérifier les formes**

Il est possible qu'une feuille donnée ne contienne aucune cellule remplie, mais qu'elle puisse contenir des formes et objets tels que des contrôles, graphiques, images, etc. Si nous devons vérifier si une feuille contient des formes, nous pouvons le faire en inspectant les éléments [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection). Toute valeur positive indique la présence de formes dans la feuille.

## **Exemple de programmation**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
{{< app/cells/assistant language="python-net" >}}
