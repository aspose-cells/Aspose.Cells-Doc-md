---
title: Obtenez tous les indices des lignes masquées après le rafraîchissement de l AutoFilter
type: docs
weight: 240
url: /fr/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---

## **Scénarios d'utilisation possibles**

Lorsque vous appliquez un filtre automatique sur les cellules de la feuille de calcul, certaines lignes se masquent automatiquement. Mais il se peut que certaines lignes soient déjà masquées manuellement par l'utilisateur final d'Excel et qu'elles ne soient pas masquées par le filtre automatique. Il est donc difficile de savoir quelles lignes sont masquées par le filtre automatique et lesquelles sont masquées manuellement par l'utilisateur final d'Excel. Aspose.Cells résout ce problème en utilisant la méthode int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)). Cette méthode renvoie les indices des lignes qui sont masquées par le filtre automatique et non manuellement par l'utilisateur final d'Excel.

## **Obtenir tous les indices des lignes masquées après le rafraîchissement de l'Autofiltre**

Veuillez consulter le code d'exemple suivant qui charge le [fichier Excel d'exemple](64716913.xlsx) qui contient certaines des lignes masquées manuellement par l'utilisateur final d'Excel. Le code applique le filtre automatique, le rafraîchit en utilisant la méthode int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)) qui renvoie les indices des lignes masquées par le filtre automatique. Il imprime ensuite les indices des lignes masquées sur la console avec les noms et valeurs des cellules.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

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
