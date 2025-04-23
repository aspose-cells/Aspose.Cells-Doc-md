---
title: Calcul des formules
type: docs
weight: 110
url: /fr/java/calculate-formulas/
---

## **Ajout de formules et calcul de résultats**

Aspose.Cells dispose d'un moteur de calcul de formules intégré. Non seulement il peut recalculer les formules importées à partir de modèles de concepteur, mais il prend également en charge le calcul des résultats des formules ajoutées à l'exécution.

Aspose.Cells prend en charge la plupart des formules ou fonctions faisant partie de Microsoft Excel (Lire [une liste des fonctions prises en charge par le moteur de calcul](/cells/fr/java/supported-formula-functions/)). Ces fonctions peuvent être utilisées via les API ou les feuilles de calcul de concepteur. Aspose.Cells prend en charge un vaste ensemble de formules mathématiques, de chaînes de caractères, de booléens, de date/heure, statistiques, de base de données, de recherche et de référence.

Utilisez la propriété [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) ou les méthodes [**SetFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula-java.lang.String-com.aspose.cells.FormulaParseOptions-java.lang.Object-) de la classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) pour ajouter une formule à une cellule. Lors de l'application d'une formule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel et utilisez une virgule (,) pour délimiter les paramètres de la fonction.

Pour calculer les résultats des formules, l'utilisateur peut appeler la méthode [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--) de la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) qui traite toutes les formules intégrées dans un fichier Excel. Ou, l'utilisateur peut appeler la méthode [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-com.aspose.cells.CalculationOptions-boolean-) de la classe [**Worsheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) qui traite toutes les formules dans une feuille. Ou, l'utilisateur peut aussi appeler la méthode [**Calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate-com.aspose.cells.CalculationOptions-) de la classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) qui traite la formule d'une seule cellule :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Important à savoir**

{{% alert color="primary" %}}

La propriété **Formula** et les méthodes **SetFormula(...)** de la classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) fonctionnent différemment des méthodes **Calculate** des classes [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) et [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell). La propriété **Formula** et les méthodes **SetFormula(...)** ajoutent simplement la formule à une cellule mais ne calculent pas le résultat à l'exécution. Pour obtenir le résultat des formules, veuillez appeler les méthodes **Calculate**.

{{% /alert %}}

## **Calcul direct de formule**

Aspose.Cells possède un moteur de calcul de formules intégré. En plus de calculer les formules importées à partir d'un fichier, Aspose.Cells peut calculer les résultats des formules directement.

Parfois, vous devez calculer directement les résultats des formules sans les ajouter à une feuille de calcul. Les valeurs des cellules utilisées dans la formule existent déjà dans une feuille de calcul et tout ce dont vous avez besoin est de trouver le résultat de ces valeurs en fonction d'une formule Microsoft Excel sans ajouter la formule dans une feuille de calcul.

Vous pouvez utiliser les API du moteur de calcul de formules Aspose.Cells pour [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) à [**calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-java.lang.String-com.aspose.cells.CalculationOptions-) les résultats de telles formules sans les ajouter à la feuille de calcul :

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

Le code ci-dessus produit la sortie suivante :
{{< highlight java >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Calculer des formules de manière répétée**

Lorsqu'il y a beaucoup de formules dans le classeur et que l'utilisateur doit les calculer de manière répétée en modifiant seulement une petite partie d'entre elles, il peut être utile pour les performances d'activer la chaîne de calcul des formules : [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Important à savoir**

{{% alert color="primary" %}}

Par défaut, la chaîne de calcul est désactivée. La création de la chaîne nécessite également du temps supplémentaire, la première fois que des formules sont calculées ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--) peut consommer plus de temps CPU et de mémoire par rapport à un calcul sans chaîne. Si l'utilisateur n'a pas besoin de recalculer fréquemment des formules, le comportement par défaut (calculer la formule directement sans créer de chaîne de calcul) serait la meilleure méthode.

{{% /alert %}}

## **Sujets avancés**
- [Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel](/cells/fr/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Moteur de calcul de formule Aspose.Cells](/cells/fr/java/aspose-cells-formula-calculation-engine/)
- [Calcul de la fonction SIERREUR en utilisant Aspose.Cells](/cells/fr/java/calculating-ifna-function-using-aspose-cells/)
- [Calcul de la formule de tableau de données](/cells/fr/java/calculation-of-array-formula-of-data-tables/)
- [Calcul des fonctions MINIFS et MAXIFS d'Excel 2016](/cells/fr/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Réduire le temps de calcul de la méthode Cell.Calculate](/cells/fr/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Détection des références circulaires](/cells/fr/java/detecting-circular-reference/)
- [Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut d'Aspose.Cells](/cells/fr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrompre ou annuler le calcul de formule du classeur](/cells/fr/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Retourner une plage de valeurs en utilisant AbstractCalculationEngine](/cells/fr/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [Retourner une plage de valeurs en utilisant ICustomFunction](/cells/fr/java/returning-a-range-of-values-using-icustomfunction/)
- [Utiliser la fonctionnalité ICustomFunction](/cells/fr/java/using-icustomfunction-feature/)
{{< app/cells/assistant language="java" >}}
