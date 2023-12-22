---
title: Façons de calculer des formules
type: docs
weight: 30
url: /fr/cpp/ways-to-calculate-formulas/
---
##  **Introduction**
Aspose.Cells dispose d'un moteur de calcul de formule intégré. Il peut non seulement recalculer les formules importées à partir de modèles de concepteur, mais prend également en charge le calcul des résultats des formules ajoutées lors de l'exécution.
##  **Ajout de formules et calcul des résultats**
Aspose.Cells prend en charge la plupart des formules ou fonctions qui font partie de Microsoft Excel. ils peuvent être utilisés via le API ou à l'aide de feuilles de calcul de concepteur. Aspose.Cells prend en charge un vaste ensemble de formules mathématiques, de chaîne, booléennes, de date/heure, statistiques, de recherche et de référence.

Utilisez la méthode Cell.SetFormula pour ajouter une formule à une cellule. Lorsque vous appliquez une formule à une cellule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel. Utilisez une virgule (,) pour délimiter les paramètres de fonction.

Pour calculer les résultats des formules, appelez la méthode Workbook.CalculateFormula() qui traite toutes les formules incorporées dans un fichier Excel. Veuillez consulter l'exemple de code suivant qui ajoute la formule et calcule ses résultats. S'il vous plaît, vérifiez le[sortie du fichier Excel](38109185.xlsx) généré avec ce code.

**Exemple de code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults-new.cpp" >}}
<!---## **Direct Calculation of Formula**
Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Worksheet.CalculateFormula(String formula) method to calculate the results of such formulas without adding them to worksheet.

The code below produces the following output.

{{< highlight java >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}   --->
##  **Calculer des formules une seule fois**
Lorsque Workbook.CalculateFormula() est appelé pour calculer les valeurs des formules dans un modèle de classeur, Aspose.Cells crée une chaîne de calcul. Cela augmente les performances lorsque les formules sont calculées pour la deuxième ou la troisième fois.

Cependant, si le modèle contient de nombreuses formules, le premier calcul de la formule peut consommer beaucoup de temps de traitement CPU et de mémoire.

Aspose.Cells vous permet de désactiver la création d'une chaîne de calcul, ce qui est utile lorsque vous souhaitez calculer des formules une seule fois.

 Veuillez appeler Workbook.GetISettings().SetCreateCalcChain() avec le paramètre false. Vous pouvez utiliser le[fichier excel fourni](38109186.xlsx) pour tester ce code.

**Exemple de code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly-new.cpp" >}}
