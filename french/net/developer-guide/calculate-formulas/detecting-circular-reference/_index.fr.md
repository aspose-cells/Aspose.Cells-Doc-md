---
title: Détection des références circulaires
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour détecter les références circulaires dans Microsoft Excel. En chargeant un fichier Excel existant ou en en créant un nouveau, nous pouvons utiliser la méthode fournie par Aspose.Cells pour détecter les références circulaires et obtenir les résultats. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, références circulaires, détection
type: docs
weight: 70
url: /fr/net/detecting-circular-reference/
---

## **Introduction**

Les classeurs peuvent comporter des références circulaires et parfois il est nécessaire de détecter si des références circulaires sont présentes ou non.

## **Concept derrière la détection de la référence circulaire**

Les références circulaires ne peuvent être détectées que lorsque la formule est calculée, car les références d'une formule dépendent généralement du résultat calculé d'autres parties ou d'autres formules. Nous fournissons donc de nouvelles API pour cette exigence (pour rassembler les cellules avec des références circulaires) dans le processus de calcul des formules :

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) : Représente le calcul des données pertinentes d'une cellule en cours de calcul

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) : sera invoquée par le moteur de calcul de formule lors de la détection de références circulaires, l'élément de l'énumérateur est des objets [**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) qui représentent toutes les cellules dans un cercle. La valeur retournée indique si le moteur de formule doit calculer ces cellules en cercle après cet appel.

L'utilisateur peut rassembler ces références circulaires dans la mise en œuvre de la méthode [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular).

Le fichier d'exemple source peut être téléchargé à partir du lien suivant :

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

La définition de la classe *CircularMonitor* qui est dérivée de la classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) est la suivante :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
