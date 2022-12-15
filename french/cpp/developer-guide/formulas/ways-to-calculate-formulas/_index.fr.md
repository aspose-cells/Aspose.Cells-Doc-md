---
title: Façons de calculer des formules
type: docs
weight: 30
url: /fr/cpp/ways-to-calculate-formulas/
---
## **Introduction**
Aspose.Cells dispose d'un moteur de calcul de formule intégré. Il peut non seulement recalculer les formules importées à partir de modèles de concepteur, mais prend également en charge le calcul des résultats des formules ajoutées au moment de l'exécution.
## **Ajout de formules et calcul des résultats**
Aspose.Cells prend en charge la plupart des formules ou fonctions qui font partie de Microsoft Excel. ils peuvent être utilisés via le API ou à l'aide de feuilles de calcul de concepteur. Aspose.Cells prend en charge un vaste ensemble de formules mathématiques, de chaîne, booléennes, de date/heure, statistiques, de recherche et de référence.

Utilisez la méthode Cell.Formula pour ajouter une formule à une cellule. Lorsque vous appliquez une formule à une cellule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel. Utilisez une virgule (,) pour délimiter les paramètres de la fonction.

Pour calculer les résultats des formules, appelez la méthode Workbook.CalculateFormula() qui traite toutes les formules incorporées dans un fichier Excel. Veuillez consulter l'exemple de code suivant qui ajoute la formule et calcule ses résultats. S'il vous plaît, vérifiez le[fichier excel de sortie](38109185.xlsx) généré avec ce code.

**Exemple de code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults.cpp" >}}
## **Calcul direct de la formule**
Parfois, vous devez calculer directement les résultats de la formule sans les ajouter dans une feuille de calcul. Les valeurs des cellules utilisées dans la formule existent déjà dans une feuille de calcul et tout ce dont vous avez besoin est de trouver le résultat de ces valeurs en fonction d'une formule Excel Microsoft sans ajouter la formule dans une feuille de calcul.

Vous pouvez utiliser la méthode Worksheet.CalculateFormula(String formula) pour calculer les résultats de ces formules sans les ajouter à la feuille de calcul.

Le code ci-dessous produit la sortie suivante.

{{< highlight "java" >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Exemple de code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}
## **Calculer des formules une seule fois**
Lorsque Workbook.CalculateFormula() est appelé pour calculer les valeurs des formules dans un modèle de classeur, Aspose.Cells crée une chaîne de calcul. Il augmente les performances lorsque les formules sont calculées pour la deuxième ou la troisième fois.

Cependant, si le modèle contient de nombreuses formules, la première fois que la formule est calculée peut consommer beaucoup de temps de traitement CPU et de mémoire.

Aspose.Cells vous permet de désactiver la création d'une chaîne de calcul, ce qui est utile lorsque vous souhaitez calculer des formules une seule fois.

 Veuillez appeler Workbook.GetISettings().SetCreateCalcChain() avec le paramètre false. Vous pouvez utiliser le[fichier excel fourni](38109186.xlsx) pour tester ce code.

**Exemple de code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly.cpp" >}}
