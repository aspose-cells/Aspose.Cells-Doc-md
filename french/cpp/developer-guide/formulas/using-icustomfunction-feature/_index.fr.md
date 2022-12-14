---
title: Utilisation de la fonctionnalité ICustomFunction
type: docs
weight: 20
url: /fr/cpp/using-icustomfunction-feature/
---
## **Introduction**
Cet article explique comment utiliser la fonctionnalité ICustomFunction pour implémenter des fonctions personnalisées avec les API Aspose.Cells.

L'interface ICustomFunction vous permet d'ajouter des fonctions de calcul de formule personnalisées pour étendre le moteur de calcul de base Aspose.Cells afin de répondre à certaines exigences. Cette fonctionnalité est utile pour définir des fonctions personnalisées (définies par l'utilisateur) dans un fichier de modèle ou dans un code où la fonction personnalisée peut être implémentée et évaluée à l'aide des API Aspose.Cells comme toute autre fonction Excel Microsoft par défaut.
## **Utilisation de la fonctionnalité ICustomFunction**
L'exemple de code suivant implémente l'interface ICustomFunction qui évalue et renvoie les valeurs des deux fonctions personnalisées, à savoir MySampleFunc() et YourSampleFunc(). Ces fonctions personnalisées se trouvent respectivement dans les cellules A1 et A2. Ensuite, il appelle la méthode IWorkbook.CalculateFormula(false, ICustomFunction) pour appeler l'implémentation de la méthode ICustomFunction.CalculateCustomFunction(). Ensuite, il imprime les valeurs de A1 et A2 sur la console qui sont en fait les valeurs renvoyées par ICustomFunction.CalculateCustomFunction(). Veuillez consulter la sortie de la console de l'exemple de code ci-dessous pour plus d'aide.
## **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature.cpp" >}}


## **Sortie console**
{{< highlight "java" >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
