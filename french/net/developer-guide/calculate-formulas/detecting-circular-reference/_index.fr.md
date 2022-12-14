---
title: Détection de référence circulaire
type: docs
weight: 70
url: /fr/net/detecting-circular-reference/
---
## **Introduction**

Les classeurs peuvent avoir des références circulaires et il est parfois nécessaire de détecter si des références circulaires sont présentes ou non.

## **Concept derrière la détection de la référence circulaire**

Les références circulaires ne peuvent être détectées que lorsque la formule est calculée car les références d'une formule dépendent généralement du résultat calculé d'autres parties ou d'autres formules. Nous fournissons donc de nouvelles API pour cette exigence (pour rassembler des cellules avec des références circulaires) dans le processus de calcul de la formule :

[**CelluleCalcul**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Représente le calcul des données pertinentes sur une cellule en cours de calcul

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): sera invoqué par le moteur de calcul de formule lors de la rencontre de références circulaires, l'élément dans l'énumérateur est[**CelluleCalcul**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) objets qui représentent toutes les cellules d'un cercle. La valeur renvoyée indique si le moteur de formule doit calculer ces cellules en circulaire après cet appel.

L'utilisateur peut rassembler ces références circulaires dans la mise en œuvre de[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) méthode.

Le fichier d'exemple source peut être téléchargé à partir du lien suivant :

[Formules circulaires.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

 Définition de*CirculaireMoniteur* classe dérivée de[**RésuméCalculMoniteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) classe est la suivante :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
