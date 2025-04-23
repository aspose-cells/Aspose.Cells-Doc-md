---
title: Détection des références circulaires
type: docs
weight: 70
url: /fr/java/detecting-circular-reference/
---

## **Introduction**

Les classeurs peuvent comporter des références circulaires et parfois il est nécessaire de détecter si des références circulaires sont présentes ou non.

## **Concept derrière la détection de la référence circulaire**

Les références circulaires ne peuvent être détectées que lorsque la formule est calculée, car les références d'une formule dépendent généralement du résultat calculé d'autres parties ou d'autres formules. Nous fournissons donc de nouvelles API pour cette exigence (pour rassembler les cellules avec des références circulaires) dans le processus de calcul des formules :

[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) : Représente le calcul des données pertinentes d'une cellule en cours de calcul

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-) : sera invoquée par le moteur de calcul de formule lors de la détection de références circulaires, l'élément de l'énumérateur est des objets [**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) qui représentent toutes les cellules dans un cercle. La valeur retournée indique si le moteur de formule doit calculer ces cellules en cercle après cet appel.

L'utilisateur peut rassembler ces références circulaires dans la mise en œuvre de la méthode [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-).

Le fichier d'exemple source peut être téléchargé à partir du lien suivant :

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

La définition de la classe *CircularMonitor* qui est dérivée de la classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) est la suivante :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
{{< app/cells/assistant language="java" >}}
