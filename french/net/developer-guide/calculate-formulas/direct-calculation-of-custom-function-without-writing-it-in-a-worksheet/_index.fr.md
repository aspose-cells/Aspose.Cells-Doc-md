---
title: Calcul direct de fonction personnalisée sans l écrire dans une feuille de calcul
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour calculer directement des fonctions personnalisées dans Microsoft Excel sans écrire la fonction dans une feuille de calcul. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour calculer la fonction personnalisée et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, fonctions personnalisées, calculs directs, pas besoin d écrire sur les feuilles de calcul
type: docs
weight: 90
url: /fr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul**

Ce sujet explique comment vous pouvez calculer directement vos fonctions personnalisées sans les écrire d'abord dans une feuille de calcul. Veuillez utiliser la méthode [**Worksheet.CalculateFormula(string formula, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) à cette fin.

Veuillez consulter le code d'exemple suivant qui illustre l'utilisation de cette méthode. Nous avons utilisé une fonction personnalisée nommée MyCompany.CustomFunction() et nous calculons sa valeur comme "Aspose.Cells." par nous-mêmes, puis cette valeur est automatiquement concaténée avec la valeur de la cellule A1 qui est "Bienvenue à " par le moteur de calcul, et la valeur calculée finale retourne comme "Bienvenue à Aspose.Cells.". Comme vous pouvez le voir dans le code, nous n'avons pas écrit notre fonction personnalisée nulle part dans une feuille de calcul et elle est calculée directement par notre propre logique personnalisée.

### **Exemple de programmation**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Article connexe**

{{% alert color="primary" %}}

[Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut de Aspose.Cells](/cells/fr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
