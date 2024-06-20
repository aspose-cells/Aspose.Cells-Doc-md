---
title: Définir comment croiser la chaîne dans le HTML de sortie en utilisant HtmlCrossType
type: docs
weight: 140
url: /fr/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Scénarios d'utilisation possibles**

Lorsque la cellule contient du texte ou une chaîne mais qu'elle est plus grande que la largeur de la cellule, alors la chaîne dépasse si la cellule suivante dans la colonne suivante est nulle ou vide. Lorsque vous enregistrez votre fichier Excel au format HTML, vous pouvez contrôler ce dépassement en spécifiant le type de croisement en utilisant l'énumération [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). Elle a les valeurs suivantes

- **HtmlCrossType.Default** : Affiche comme dans MS Excel, dépend de la cellule suivante. Si la prochaine cellule est nulle, la chaîne sera croisée ou elle sera tronquée.

- **HtmlCrossType.MSExport** : Affiche la chaîne comme dans MS Excel exportant HTML.

- **HtmlCrossType.Cross** : Affiche la chaîne HTML croisée, la performance pour la création de fichiers HTML volumineux sera plus de dix fois plus rapide que le réglage de la valeur sur Default ou FitToCell.

- **HtmlCrossType.FitToCell** : Affiche uniquement la chaîne dans la largeur de la cellule.

## **Spécifier comment croiser la chaîne dans le HTML de sortie en utilisant HtmlCrossType**

Le code d'exemple suivant charge le [fichier Excel d'exemple](51740732.xlsx) et l'enregistre au format HTML en spécifiant différents [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). Veuillez télécharger les [fichiers HTML de sortie](51740734.zip) générés avec ce code. Le fichier Excel d'exemple contient l'image bordée de couleur rouge comme indiqué dans cette capture d'écran qui montre l'effet des valeurs [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) sur le HTML de sortie.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
