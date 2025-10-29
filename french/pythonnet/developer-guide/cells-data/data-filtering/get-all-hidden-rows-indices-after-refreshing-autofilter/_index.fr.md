---
title: Obtenez tous les indices des lignes masquées après le rafraîchissement de l AutoFilter
type: docs
weight: 320
url: /fr/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Apprenez à obtenir tous les indices des lignes masquées après l actualisation du filtre automatique à l aide de la bibliothèque Excel Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Python Obtenez tous les indices des lignes masquées après l actualisation du filtre automatique, Python Obtenir tous les indices des lignes masquées après l actualisation du filtre automatique, Python Récupérer tous les indices des lignes masquées après l actualisation du filtre automatique
---

## **Scénarios d'utilisation possibles**

Lorsque vous appliquez le filtre automatique sur les cellules de la feuille de calcul, certaines lignes sont automatiquement masquées. Cependant, il se peut que certaines lignes soient déjà masquées manuellement par l'utilisateur final d'Excel et qu'elles ne soient pas masquées par un filtre automatique. Il est donc difficile de savoir quelles lignes sont masquées par le filtre automatique et lesquelles sont masquées manuellement par l'utilisateur final d'Excel. Aspose.Cells pour Python via .NET gère ce problème à l'aide de la méthode [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool). Cette méthode renvoie les indices de ligne de toutes les lignes masquées par le filtre automatique et non manuellement par l'utilisateur final d'Excel.

## **Obtenir tous les indices des lignes masquées après le rafraîchissement de l'Autofiltre**

Veuillez consulter le code d'exemple suivant qui charge le [fichier Excel d'exemple](64716909.xlsx) contenant certaines des lignes masquées manuellement par l'utilisateur final d'Excel. Le code applique le filtre automatique et le rafraîchit en utilisant la méthode [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool) qui renvoie les indices de ligne de toutes les lignes masquées par le filtre automatique. Il imprime ensuite les indices des lignes masquées sur la console ainsi que les noms et valeurs des cellules.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
