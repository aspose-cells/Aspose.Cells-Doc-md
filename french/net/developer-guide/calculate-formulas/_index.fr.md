---
title: Calculer des formules
description: Cet article explique comment utiliser la bibliothèque Aspose.Cells pour calculer des formules dans Excel Microsoft. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour calculer la formule et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, formulas, calculations, Direct Calculation of Formula, Calculate Formulas repeatedly, add formulas.
type: docs
weight: 125
url: /fr/net/calculate-formulas/
---
##  **Ajout de formules et calcul des résultats**

Aspose.Cells dispose d'un moteur de calcul de formule intégré. Non seulement il peut recalculer les formules importées à partir de modèles de concepteur, mais il prend également en charge le calcul des résultats des formules ajoutées au moment de l'exécution.

 Aspose.Cells prend en charge la plupart des formules ou fonctions qui font partie de Microsoft Excel(Lire[une liste des fonctions supportées par le moteur de calcul](/cells/fr/net/supported-formula-functions/)). Ces fonctions peuvent être utilisées via les API ou les feuilles de calcul du concepteur. Aspose.Cells prend en charge un vaste ensemble de formules mathématiques, de chaîne, booléennes, de date/heure, statistiques, de base de données, de recherche et de référence.

 Utilisez le[**Formule**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) propriété ou[**DéfinirFormule(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) méthodes du[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe pour ajouter une formule à une cellule. Lorsque vous appliquez une formule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel et utilisez une virgule (,) pour délimiter les paramètres de la fonction.

 Pour calculer les résultats des formules, l'utilisateur peut appeler le[**CalculerFormule**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) méthode du[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe qui traite toutes les formules intégrées dans un fichier Excel. L'utilisateur peut également appeler le[**CalculerFormule**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) méthode du[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe qui traite toutes les formules intégrées dans une feuille. L'utilisateur peut également appeler le[**Calculer**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) méthode du[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe qui traite la formule de un Cell :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

###  **Important à savoir pour les formules**

{{% alert color="primary" %}}

 Le**Formule** la propriété et**DéfinirFormule(...)** méthodes du[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)travailler en classe différemment du**Calculer** méthodes du[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) et[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Des classes. Le**Formule** la propriété et**DéfinirFormule(...)** Les méthodes ajoutent simplement la formule à une cellule mais ne calculent pas le résultat au moment de l'exécution. Pour obtenir le résultat des formules, veuillez appeler**Calculer** méthodes.

{{% /alert %}}

##  **Calcul direct de la formule**

Aspose.Cells dispose d'un moteur de calcul de formule intégré. En plus de calculer des formules importées à partir d'un fichier de concepteur, Aspose.Cells peut calculer directement les résultats des formules.

Parfois, vous devez calculer directement les résultats d’une formule sans les ajouter dans une feuille de calcul. Les valeurs des cellules utilisées dans la formule existent déjà dans une feuille de calcul et tout ce dont vous avez besoin est de trouver le résultat de ces valeurs basé sur une formule Excel Microsoft sans ajouter la formule dans une feuille de calcul.

 Vous pouvez utiliser les API du moteur de calcul de formule Aspose.Cells pour[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) à[**calculer**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) les résultats de ces formules sans les ajouter à la feuille de calcul :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Le code ci-dessus produit le résultat suivant :
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

##  **Comment calculer des formules à plusieurs reprises**

Lorsqu'il y a beaucoup de formules dans le classeur et que l'utilisateur doit les calculer à plusieurs reprises en n'en modifiant qu'une petite partie, il peut être utile pour les performances d'activer la chaîne de calcul des formules :[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

###  **Important à savoir**

{{% alert color="primary" %}}

Par défaut la chaîne de calcul est désactivée. Parce que la création de la chaîne nécessite également du temps supplémentaire, la première fois que l'on calcule des formules ([**Classeur.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) peut consommer plus de temps de traitement CPU et de mémoire par rapport aux formules de calcul sans chaîne. Si l'utilisateur n'a pas besoin de calculer les formules à plusieurs reprises, le comportement par défaut (calcul direct de la formule sans créer de chaîne de calcul) devrait être le meilleur moyen.

{{% /alert %}}


##  **Sujets avancés**
- [Ajouter Cells à Microsoft Fenêtre de surveillance de formule Excel](/cells/fr/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calcul de la fonction IFNA à l'aide de Aspose.Cells](/cells/fr/net/calculating-ifna-function-using-aspose-cells/)
- [Calcul de la formule matricielle des tableaux de données](/cells/fr/net/calculation-of-array-formula-of-data-tables/)
- [Calcul des fonctions Excel 2016 MINIFS et MAXIFS](/cells/fr/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Diminuez le temps de calcul de Cell. Méthode de calcul](/cells/fr/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Détection d'une référence circulaire](/cells/fr/net/detecting-circular-reference/)
- [Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut de Aspose.Cells](/cells/fr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrompre ou annuler le calcul de la formule du classeur](/cells/fr/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Renvoi d'une plage de valeurs à l'aide de AbstractCalculationEngine](/cells/fr/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [Renvoyer une plage de valeurs à l'aide de ICustomFunction](/cells/fr/net/returning-a-range-of-values-using-icustomfunction/)
- [Définition du mode de calcul de formule du classeur](/cells/fr/net/setting-formula-calculation-mode-of-workbook/)
- [Utilisation de la fonction FormulaText dans Aspose.Cells](/cells/fr/net/using-formulatext-function-in-aspose-cells/)
- [Utilisation de la fonctionnalité ICustomFunction](/cells/fr/net/using-icustomfunction-feature/)
