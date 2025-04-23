---
title: Utilisation de la fonction AbstractCalculationEngine
type: docs
weight: 20
url: /fr/cpp/using-abstractcalculationengine-feature/
---


## **Introduction**
Cet article fournit une compréhension de l'utilisation de la fonction [AbstractCalculationEngine](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) pour implémenter des fonctions personnalisées avec les API Aspose.Cells.

L'interface AbstractCalculationEngine vous permet d'ajouter des fonctions de calcul de formules personnalisées pour étendre le moteur de calcul de base d'Aspose.Cells afin de répondre à certaines exigences. Cette fonction est utile pour définir des fonctions personnalisées dans un fichier modèle ou dans un code où la fonction personnalisée peut être implémentée et évaluée à l'aide des API Aspose.Cells comme toute autre fonction par défaut de Microsoft Excel.

## **Utilisation de la fonction AbstractCalculationEngine - 1**

Le code d'échantillon suivant implémente l'interface AbstractCalculationEngine qui évalue et renvoie les valeurs des deux fonctions personnalisées, à savoir MySampleFunc() et YourSampleFunc(). Ces fonctions personnalisées se trouvent dans les cellules A1 et A2 respectivement. Ensuite, il appelle la méthode Workbook.CalculateFormula(const CalculationOptions& options) pour invoquer la mise en œuvre de la méthode .Calculate(CalculationData& data) de AbstractCalculationEngine. Ensuite, il affiche les valeurs de A1 et A2 sur la console. Veuillez consulter la sortie de la console du code d'échantillon ci-dessous pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingAbstractCalculationEngine.cpp" >}}


## **Sortie console**
{{< highlight java >}}

MySampleFunc-Test called successfully.
YourSampleFunc-Test called successfully.
Value of A1 is : 1
Value of A2 is : 2

{{< /highlight >}}

## **Utilisation de la fonction AbstractCalculationEngine - 2**

Le code d'exemple suivant lit une fonction personnalisée à partir d'un fichier d'exemple et appelle la méthode Workbook.CalculateFormula(const CalculationOptions& options) pour invoquer la méthode AbstractCalculationEngine .Calculate(CalculationData& data) pour un traitement ultérieur.

Fichier d'exemple :[sample-file.xlsx](sample-file.xlsx)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingAbstractCalculationEngine2.cpp" >}}
