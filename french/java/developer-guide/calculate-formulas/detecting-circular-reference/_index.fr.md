---
title: Détection de référence circulaire
type: docs
weight: 70
url: /fr/java/detecting-circular-reference/
---
## **Introduction**

Les classeurs peuvent avoir des références circulaires et il est parfois nécessaire de détecter si des références circulaires sont présentes ou non.

## **Concept derrière la détection de la référence circulaire**

Les références circulaires ne peuvent être détectées que lorsque la formule est calculée car les références d'une formule dépendent généralement du résultat calculé d'autres parties ou d'autres formules. Nous fournissons donc de nouvelles API pour cette exigence (pour rassembler des cellules avec des références circulaires) dans le processus de calcul de la formule :

[**CelluleCalcul**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): Représente le calcul des données pertinentes sur une cellule en cours de calcul

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)) : sera invoqué par le moteur de calcul de formule lorsqu'il rencontrera des références circulaires, l'élément dans l'énumérateur est[**CelluleCalcul**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) objets qui représentent toutes les cellules d'un cercle. La valeur renvoyée indique si le moteur de formule doit calculer ces cellules en circulaire après cet appel.

 L'utilisateur peut rassembler ces références circulaires dans la mise en œuvre de[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)) méthode.

Le fichier d'exemple source peut être téléchargé à partir du lien suivant :

[Formules circulaires.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

Définition de*CirculaireMoniteur* classe dérivée de[**RésuméCalculMoniteur**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) classe est la suivante :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
