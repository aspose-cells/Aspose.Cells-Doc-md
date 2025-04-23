---
title: Calcul des formules
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour calculer des formules dans Microsoft Excel. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour calculer la formule et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, formules, calculs, Calcul direct de formule, Calcul des formules à plusieurs reprises, ajouter des formules.
type: docs
weight: 125
url: /fr/net/calculate-formulas/
---

## **Ajout de formules et calcul de résultats**

Aspose.Cells dispose d'un moteur de calcul de formules intégré. Non seulement il peut recalculer les formules importées à partir de modèles de concepteur, mais il prend également en charge le calcul des résultats des formules ajoutées à l'exécution.

Aspose.Cells prend en charge la plupart des fonctions ou formules qui font partie de Microsoft Excel (Lire [une liste des fonctions prises en charge par le moteur de calcul](/cells/fr/net/supported-formula-functions/)). Ces fonctions peuvent être utilisées via les API ou des feuilles de calcul de concepteur. Aspose.Cells prend en charge un large ensemble de formules mathématiques, de chaînes, booléennes, date/heure, statistiques, de base de données, de recherche et de référence.

Utilisez la propriété [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) ou les méthodes [**SetFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) pour ajouter une formule à une cellule. Lors de l'application d'une formule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel et utilisez une virgule (,) pour délimiter les paramètres de la fonction.

Pour calculer les résultats des formules, l'utilisateur peut appeler la méthode [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui traite toutes les formules intégrées dans un fichier Excel. Ou bien, l'utilisateur peut appeler la méthode [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) de la classe [**Worsheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) qui traite toutes les formules intégrées dans une feuille. Ou encore, l'utilisateur peut appeler la méthode [**Calculate**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) qui traite la formule d'une cellule :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **Important à savoir pour les formules**

{{% alert color="primary" %}}

La propriété **Formula** et les méthodes **SetFormula(...)** de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) fonctionnent différemment des méthodes **Calculate** des classes [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) et [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). La propriété **Formula** et les méthodes **SetFormula(...)** ajoutent simplement la formule à une cellule mais ne calculent pas le résultat à l'exécution. Pour obtenir le résultat des formules, veuillez appeler les méthodes **Calculate**.

{{% /alert %}}

## **Calcul direct de formule**

Aspose.Cells possède un moteur de calcul de formules intégré. En plus de calculer les formules importées à partir d'un fichier, Aspose.Cells peut calculer les résultats des formules directement.

Parfois, vous devez calculer directement les résultats des formules sans les ajouter à une feuille de calcul. Les valeurs des cellules utilisées dans la formule existent déjà dans une feuille de calcul et tout ce dont vous avez besoin est de trouver le résultat de ces valeurs en fonction d'une formule Microsoft Excel sans ajouter la formule dans une feuille de calcul.

Vous pouvez utiliser les API du moteur de calcul de formules Aspose.Cells pour [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) à [**calculate**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) les résultats de telles formules sans les ajouter à la feuille de calcul :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Le code ci-dessus produit la sortie suivante :
{{< highlight net >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Comment calculer des formules de manière répétée**

Lorsqu'il y a beaucoup de formules dans le classeur et que l'utilisateur doit les calculer de manière répétée en modifiant seulement une petite partie d'entre elles, il peut être utile pour les performances d'activer la chaîne de calcul des formules : [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **Important à savoir**

{{% alert color="primary" %}}

Par défaut, la chaîne de calcul est désactivée. Parce que la création de la chaîne nécessite également du temps supplémentaire, la première fois que les formules sont calculées ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)), cela peut prendre plus de temps de traitement CPU et de mémoire comparativement au calcul des formules sans chaîne. Si l'utilisateur n'a pas besoin de calculer les formules de manière répétée, le comportement par défaut (calcul de la formule directement sans création de la chaîne de calcul) devrait être la meilleure solution.

{{% /alert %}}


## **Sujets avancés**
- [Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel](/cells/fr/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calcul de la fonction SIERREUR en utilisant Aspose.Cells](/cells/fr/net/calculating-ifna-function-using-aspose-cells/)
- [Calcul de la formule de tableau de données](/cells/fr/net/calculation-of-array-formula-of-data-tables/)
- [Calcul des fonctions MINIFS et MAXIFS d'Excel 2016](/cells/fr/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Réduire le temps de calcul de la méthode Cell.Calculate](/cells/fr/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Détection des références circulaires](/cells/fr/net/detecting-circular-reference/)
- [Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut d'Aspose.Cells](/cells/fr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrompre ou annuler le calcul de formule du classeur](/cells/fr/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Retourner une plage de valeurs en utilisant AbstractCalculationEngine](/cells/fr/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [Retourner une plage de valeurs en utilisant ICustomFunction](/cells/fr/net/returning-a-range-of-values-using-icustomfunction/)
- [Définir le mode de calcul de formule du classeur](/cells/fr/net/setting-formula-calculation-mode-of-workbook/)
- [Utilisation de la fonction FormulaText dans Aspose.Cells](/cells/fr/net/using-formulatext-function-in-aspose-cells/)
- [Utiliser la fonctionnalité ICustomFunction](/cells/fr/net/using-icustomfunction-feature/)
{{< app/cells/assistant language="csharp" >}}
