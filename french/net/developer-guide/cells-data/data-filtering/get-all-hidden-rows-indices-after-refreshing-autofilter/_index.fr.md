---
title: Obtenez tous les indices des lignes masquées après le rafraîchissement de l AutoFilter
type: docs
weight: 320
url: /fr/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Apprenez comment obtenir tous les indices des lignes masquées après le rafraîchissement de l AutoFilter en utilisant l API Aspose.Cells for .NET.
keywords: Obtenez tous les indices des lignes masquées après le rafraîchissement de l AutoFilter, Obtenez tous les indices des lignes masquées après le rafraîchissement de l AutoFilter, Récupérez tous les indices des lignes masquées après le rafraîchissement de l AutoFilter
---

## **Scénarios d'utilisation possibles**

Lorsque vous appliquez le filtre automatique sur les cellules de la feuille de calcul, certaines des lignes sont automatiquement masquées. Mais il se peut que certaines des lignes soient déjà masquées manuellement par l'utilisateur final d'Excel et qu'elles ne soient pas masquées par un filtre automatique. Il est donc difficile de savoir quelles sont les lignes masquées par le filtre automatique et lesquelles sont masquées manuellement par l'utilisateur final d'Excel. Aspose.Cells résout ce problème en utilisant la méthode int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1). Cette méthode renvoie les indices de lignes de toutes les lignes qui sont masquées par le filtre automatique et non manuellement par l'utilisateur final d'Excel.

## **Obtenir tous les indices des lignes masquées après le rafraîchissement de l'Autofiltre**

Veuillez consulter le code d'exemple suivant qui charge le [fichier Excel d'exemple](64716909.xlsx) contenant certaines des lignes masquées manuellement par l'utilisateur final d'Excel. Le code applique le filtre automatique et le rafraîchit à l'aide de la méthode int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1) qui renvoie les indices de lignes de toutes les lignes masquées par le filtre automatique. Il affiche ensuite les indices des lignes masquées sur la console avec les noms et les valeurs des cellules.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

## **Sortie console**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
