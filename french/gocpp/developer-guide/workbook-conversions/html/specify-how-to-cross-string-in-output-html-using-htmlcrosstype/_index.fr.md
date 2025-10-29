---
title: Spécifier comment croiser une chaîne dans le HTML de sortie en utilisant HtmlCrossType avec Golang via C++
linktitle: Spécifiez HtmlCrossType dans le HTML de sortie
type: docs
weight: 140
url: /fr/go-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Apprenez comment contrôler le débordement de chaîne dans le HTML de sortie en utilisant Aspose.Cells for C++ avec HtmlCrossType.
---

## **Scénarios d'utilisation possibles**

 Lorsqu'une cellule contient un texte ou une chaîne plus longue que la largeur de la cellule, la chaîne déborde si la cellule suivante dans la colonne suivante est nulle ou vide. Lors de l'enregistrement de votre fichier Excel en HTML, vous pouvez contrôler ce débordement en spécifiant le type de croisement avec l'énumération [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/). Elle a les valeurs suivantes :

- **HtmlCrossType.Default** : Affiche comme dans MS Excel, dépend de la cellule suivante. Si la prochaine cellule est nulle, la chaîne sera croisée ou elle sera tronquée.

- **HtmlCrossType.MSExport** : Affiche la chaîne comme dans MS Excel exportant HTML.

- **HtmlCrossType.Cross** : Affiche la chaîne HTML croisée, la performance pour la création de fichiers HTML volumineux sera plus de dix fois plus rapide que le réglage de la valeur sur Default ou FitToCell.

- **HtmlCrossType.FitToCell** : affiche uniquement la chaîne dans la largeur de la cellule.

## **Spécifier comment croiser la chaîne dans le HTML de sortie en utilisant HtmlCrossType**

 Le code exemple suivant charge le [fichier Excel d'exemple](51740732.xlsx) et le sauvegarde au format HTML en spécifiant différents [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/). Veuillez télécharger les [HTMLs de sortie](51740734.zip) générés avec ce code. Le fichier Excel exemple contient une image bordée en rouge comme montré dans cette capture d'écran, illustrant l'effet des valeurs [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/) sur le HTML de sortie.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputHtmlUsingHtmlcrosstype.go" >}}
