---
title: Réduire le temps de calcul de la méthode Cell.Calculate
type: docs
weight: 860
url: /fr/java/decrease-the-calculation-time-of-cell-calculate-method/
---


Scénarios d'utilisation possibles

Normalement, nous recommandons aux utilisateurs d'appeler la méthode [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) une seule fois, puis de récupérer les valeurs calculées des cellules individuelles. Mais parfois, les utilisateurs ne souhaitent pas calculer l'ensemble du classeur. Ils veulent simplement calculer une seule cellule. Aspose.Cells fournit la propriété [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) que vous pouvez régler sur **false** pour réduire considérablement le temps de calcul d'une cellule individuelle. Parce que lorsque la propriété récursive est réglée sur **true**, tous les dépendants des cellules sont recalculés à chaque appel. Mais lorsque la propriété récursive est réglée sur **false**, les cellules dépendantes ne sont calculées qu'une seule fois et ne le sont pas à nouveau lors des appels suivants.
## **Diminuer le temps de calcul de la méthode Cell.Calculate()**
Le code d'exemple suivant illustre l'utilisation de la propriété [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive). Veuillez exécuter ce code avec le fichier Excel d'exemple fourni (5472288.xlsx) et vérifier sa sortie console. Vous constaterez que le fait de définir la propriété récursive sur **false** a considérablement réduit le temps de calcul. Veuillez également lire les commentaires pour une meilleure compréhension de cette propriété.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Sortie console**
Il s'agit de la sortie console du code d'exemple ci-dessus lorsqu'il est exécuté avec le fichier Excel d'exemple fourni (5472288.xlsx) sur notre machine. Veuillez noter que votre sortie peut différer, mais le temps écoulé après avoir défini la propriété récursive sur **false** sera toujours inférieur à celui pour **true**.



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
