---
title: Calculer des formules
type: docs
weight: 110
url: /fr/java/calculate-formulas/
---
## **Ajout de formules et calcul des résultats**

Aspose.Cells dispose d'un moteur de calcul de formule intégré. Non seulement il peut recalculer les formules importées à partir de modèles de concepteur, mais il prend également en charge le calcul des résultats des formules ajoutées au moment de l'exécution.

 Aspose.Cells prend en charge la plupart des formules ou fonctions qui font partie de Microsoft Excel (Lire[une liste des fonctions supportées par le moteur de calcul](/cells/fr/java/supported-formula-functions/)). Ces fonctions peuvent être utilisées via les API ou les feuilles de calcul du concepteur. Aspose.Cells prend en charge un vaste ensemble de formules mathématiques, de chaîne, booléennes, de date/heure, statistiques, de base de données, de recherche et de référence.

 Utilisez le[**Formule**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) propriété ou[**DéfinirFormule(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula(java.lang.String,%20com.aspose.cells.FormulaParseOptions,%20java.lang.Object) ) les méthodes de[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)classe pour ajouter une formule à une cellule. Lorsque vous appliquez une formule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel et utilisez une virgule (,) pour délimiter les paramètres de la fonction.

 Pour calculer les résultats des formules, l'utilisateur peut appeler le[**CalculerFormule**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) méthode de la[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)classe qui traite toutes les formules incorporées dans un fichier Excel. Ou, l'utilisateur peut appeler le[**CalculerFormule**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(com.aspose.cells.CalculationOptions,%20boolean)) méthode de la[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe qui traite toutes les formules incorporées dans une feuille. Ou, l'utilisateur peut également appeler le[**Calculer**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate(com.aspose.cells.CalculationOptions)) méthode de la[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)classe qui traite la formule d'un Cell :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Important à savoir**

{{% alert color="primary" %}}

 Le**Formule** propriété et**DéfinirFormule(...)** méthodes de la[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)le travail en classe différemment du**Calculer** méthodes de la[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) et[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) Des classes. Le**Formule** propriété et**DéfinirFormule(...)** Les méthodes ajoutent simplement la formule à une cellule mais ne calculent pas le résultat lors de l'exécution. Pour obtenir le résultat des formules, veuillez appeler**Calculer** méthodes.

{{% /alert %}}

## **Calcul direct de la formule**

Aspose.Cells dispose d'un moteur de calcul de formule intégré. En plus de calculer des formules importées à partir d'un fichier de concepteur, Aspose.Cells peut calculer directement les résultats des formules.

Parfois, vous devez calculer directement les résultats de la formule sans les ajouter dans une feuille de calcul. Les valeurs des cellules utilisées dans la formule existent déjà dans une feuille de calcul et tout ce dont vous avez besoin est de trouver le résultat de ces valeurs en fonction d'une formule Excel Microsoft sans ajouter la formule dans une feuille de calcul.

 Vous pouvez utiliser les API du moteur de calcul de formule Aspose.Cells pour[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) à[**calculer**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(java.lang.String,%20com.aspose.cells.CalculationOptions)) les résultats de ces formules sans les ajouter à la feuille de calcul :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

Le code ci-dessus produit la sortie suivante :
{{< highlight "java" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Calculer des formules à plusieurs reprises**

 Lorsqu'il y a beaucoup de formules dans le classeur et que l'utilisateur doit les calculer à plusieurs reprises en n'en modifiant qu'une petite partie, il peut être utile pour les performances d'activer la chaîne de calcul des formules :[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Important à savoir**

{{% alert color="primary" %}}

Par défaut la chaîne de calcul est désactivée. Parce que la création de la chaîne nécessite également du temps supplémentaire, la première fois que vous calculez des formules ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))) peut consommer plus de temps de traitement CPU et de mémoire lors de la comparaison avec le calcul de formules sans chaîne. Si l'utilisateur n'a pas besoin de calculer les formules à plusieurs reprises, le comportement par défaut (calcul direct de la formule sans créer de chaîne de calcul) devrait être le meilleur moyen.

{{% /alert %}}

## **Sujets avancés**
- [Ajouter Cells à Microsoft Fenêtre de surveillance des formules Excel](/cells/fr/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells Moteur de calcul de formule](/cells/fr/java/aspose-cells-formula-calculation-engine/)
- [Calcul de la fonction IFNA à l'aide de Aspose.Cells](/cells/fr/java/calculating-ifna-function-using-aspose-cells/)
- [Calcul de la formule matricielle des tableaux de données](/cells/fr/java/calculation-of-array-formula-of-data-tables/)
- [Calcul des fonctions Excel 2016 MINIFS et MAXIFS](/cells/fr/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Diminuez le temps de calcul de la méthode Cell.Calculate](/cells/fr/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Détection de référence circulaire](/cells/fr/java/detecting-circular-reference/)
- [Calcul direct de la fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut de Aspose.Cells](/cells/fr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrompre ou annuler le calcul de la formule du classeur](/cells/fr/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Retour d'une plage de valeurs à l'aide de AbstractCalculationEngine](/cells/fr/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [Renvoyer une plage de valeurs à l'aide de ICustomFunction](/cells/fr/java/returning-a-range-of-values-using-icustomfunction/)
- [Utilisation de la fonctionnalité ICustomFunction](/cells/fr/java/using-icustomfunction-feature/)
