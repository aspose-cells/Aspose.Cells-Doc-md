---
title: Calcul direct d une fonction personnalisée sans l écrire dans une feuille de calcul avec Golang via C++
linktitle: Calcul direct d une fonction personnalisée
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour calculer directement des fonctions personnalisées dans Microsoft Excel sans écrire la fonction dans une feuille de calcul. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour calculer la fonction personnalisée et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, fonctions personnalisées, calculs directs, pas besoin d écrire sur les feuilles de calcul
type: docs
weight: 90
url: /fr/go-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul**

Ce sujet explique comment vous pouvez calculer directement vos fonctions personnalisées sans les écrire d’abord dans une feuille de calcul. Veuillez utiliser la méthode [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula_string/) à cette fin.

Veuillez voir le code d'exemple suivant illustrant l'utilisation de cette méthode. Nous avons utilisé une fonction personnalisée nommée MyCompany::CustomFunction() et nous calculons sa valeur en "Aspose.Cells." nous-mêmes, puis cette valeur est automatiquement concaténée avec la valeur de la cellule A1 qui est "Welcome to " par le moteur de calcul. La valeur finale calculée renvoyée est "Welcome to Aspose.Cells.". Comme vous pouvez le voir dans le code, nous n'avons pas écrit notre fonction personnalisée n'importe où dans une feuille de calcul, elle est calculée directement par notre propre logique personnalisée.

### **Exemple de programmation**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DirectCalculationOfCustomFunctionWithoutWritingItInAWorksheet.go" >}}
### **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Article connexe**

{{% alert color="primary" %}}

[Mettre en œuvre un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut d'Aspose.Cells](/cells/fr/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
