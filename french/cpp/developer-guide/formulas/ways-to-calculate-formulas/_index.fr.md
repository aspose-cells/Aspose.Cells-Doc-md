---
title: Moyens de calculer les formules
type: docs
weight: 30
url: /fr/cpp/ways-to-calculate-formulas/
---

## **Introduction**
Aspose.Cells dispose d'un moteur de calcul de formules intégré. Il peut non seulement recalculer les formules importées à partir de modèles de concepteur, mais prend également en charge le calcul des résultats de formules ajoutées à l'exécution.
## **Ajout de formules et calcul de résultats**
Aspose.Cells prend en charge la plupart des formules ou fonctions qui font partie de Microsoft Excel. Ils peuvent être utilisés via l'API ou en utilisant des feuilles de calcul. Aspose.Cells prend en charge un vaste ensemble de formules mathématiques, de chaînes, booléennes, date/heure, statistiques, de recherche et de référence.

Utilisez la méthode Cell.SetFormula pour ajouter une formule à une cellule. Lors de l'application d'une formule à une cellule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel. Utilisez une virgule (,) pour délimiter les paramètres de la fonction.

Pour calculer les résultats des formules, appelez la méthode Workbook.CalculateFormula() qui traite toutes les formules intégrées dans un fichier Excel. Veuillez consulter le code d'exemple suivant qui ajoute la formule et calcule ses résultats. Veuillez vérifier le [fichier Excel de sortie](38109185.xlsx) généré avec ce code.

**Code d'exemple**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults-new.cpp" >}}
<!---## **Calcul direct de la formule**
Parfois, vous devez calculer directement les résultats des formules sans les ajouter à une feuille de calcul. Les valeurs des cellules utilisées dans la formule existent déjà dans une feuille de calcul et tout ce dont vous avez besoin est de trouver le résultat de ces valeurs en fonction d'une formule Microsoft Excel sans ajouter la formule dans une feuille de calcul.

Vous pouvez utiliser la méthode Worksheet.CalculateFormula(String formula) pour calculer les résultats de telles formules sans les ajouter à la feuille de calcul.

Le code ci-dessous produit la sortie suivante.

{{< highlight java >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Code d'exemple**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}   --->
## **Calcul des formules une seule fois**
Lorsque Workbook.CalculateFormula() est appelé pour calculer les valeurs des formules dans un modèle de classeur, Aspose.Cells crée une chaîne de calcul. Cela augmente les performances lorsque les formules sont calculées pour la deuxième ou la troisième fois.

Cependant, si le modèle contient beaucoup de formules, le calcul de la formule la première fois peut consommer beaucoup de temps de traitement CPU et de mémoire.

Aspose.Cells vous permet de désactiver la création d'une chaîne de calcul, ce qui est utile lorsque vous voulez calculer les formules une seule fois.

Veuillez appeler Workbook.GetISettings().SetCreateCalcChain() avec le paramètre false. Vous pouvez utiliser le [fichier Excel fourni](38109186.xlsx) pour tester ce code.

**Code d'exemple**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
