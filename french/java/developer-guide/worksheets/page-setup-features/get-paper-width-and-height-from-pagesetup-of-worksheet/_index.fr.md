---
title: Obtenir la largeur et la hauteur du papier à partir de la mise en page de la feuille de calcul
type: docs
weight: 300
url: /fr/java/get-paper-width-and-height-from-pagesetup-of-worksheet/
---

## **Scénarios d'utilisation possibles**

Parfois, vous avez besoin de connaître la largeur et la hauteur de la taille du papier telle qu'elle a été définie dans la mise en page de la feuille de calcul. Veuillez utiliser les propriétés [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperWidth) et [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperHeight) à cette fin.

## **Obtenir la largeur et la hauteur du papier à partir de la mise en page de la feuille de calcul**

Le code d'exemple suivant explique l'utilisation des propriétés [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperWidth) et [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperHeight). Il modifie d'abord la taille du papier en A2, puis trouve la largeur et la hauteur du papier, puis il le modifie en A3, A4, Letter et trouve respectivement la largeur et la hauteur du papier.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-GetPaperWidthHeight-GetPaperWidthHeight.java" >}}

## **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11.0

{{< /highlight >}}
