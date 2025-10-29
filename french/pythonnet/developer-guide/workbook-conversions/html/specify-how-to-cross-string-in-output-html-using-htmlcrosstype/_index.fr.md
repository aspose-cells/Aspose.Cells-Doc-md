---
title: Définir comment croiser la chaîne dans le HTML de sortie en utilisant HtmlCrossType
type: docs
weight: 140
url: /fr/python-net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Scénarios d'utilisation possibles**

Lorsque la cellule contient du texte ou une chaîne mais qu'elle est plus grande que la largeur de la cellule, alors la chaîne dépasse si la cellule suivante dans la colonne suivante est nulle ou vide. Lorsque vous enregistrez votre fichier Excel au format HTML, vous pouvez contrôler ce dépassement en spécifiant le type de croisement en utilisant l'énumération [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype). Elle a les valeurs suivantes

- **HtmlCrossType.DEFAULT** : Affichage comme MS Excel, dépendant de la cellule suivante. Si la prochaine cellule est nulle, la chaîne sera croisée ou tronquée.

- **HtmlCrossType.MS_EXPORT** : Affichage de la chaîne comme lors de l’exportation HTML par MS Excel.

- **HtmlCrossType.CROSS** : Affichage de la chaîne croisée HTML, la performance pour créer de grands fichiers HTML sera plus de dix fois plus rapide qu’en réglant la valeur sur Default ou FitToCell.

- **HtmlCrossType.CROSS_HIDE_RIGHT** : Affichage de la chaîne croisée HTML et cache la chaîne de droite lorsque les textes se chevauchent.

- **HtmlCrossType.FIT_TO_CELL** : Affiche uniquement la chaîne à l’intérieur de la largeur de la cellule.

## **Spécifier comment croiser la chaîne dans le HTML de sortie en utilisant HtmlCrossType**

Le code d'exemple suivant charge le [fichier Excel d'exemple](51740732.xlsx) et l'enregistre au format HTML en spécifiant différents [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype). Veuillez télécharger les [fichiers HTML de sortie](51740734.zip) générés avec ce code. Le fichier Excel d'exemple contient l'image bordée de couleur rouge comme indiqué dans cette capture d'écran qui montre l'effet des valeurs [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype) sur le HTML de sortie.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SpecifyHtmlCrossTypeInOutputHTML.py" >}}
{{< app/cells/assistant language="python-net" >}}
