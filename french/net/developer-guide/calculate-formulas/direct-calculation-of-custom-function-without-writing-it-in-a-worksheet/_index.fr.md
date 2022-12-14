---
title: Calcul direct de la fonction personnalisée sans l'écrire dans une feuille de calcul
type: docs
weight: 90
url: /fr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
## **Calcul direct de la fonction personnalisée sans l'écrire dans une feuille de calcul**

 Cette rubrique explique comment calculer directement vos fonctions personnalisées sans les écrire au préalable dans une feuille de calcul. Veuillez utiliser le[**Worksheet.CalculateFormula (formule de chaîne, CalculationOptions opte)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)méthode à cet effet.

Veuillez consulter l'exemple de code suivant qui illustre l'utilisation de cette méthode. Nous avons utilisé une fonction personnalisée nommée MyCompany.CustomFunction() et nous calculons sa valeur comme "Aspose.Cells". par nous-mêmes, puis cette valeur est automatiquement concaténée avec la valeur de la cellule A1 qui est "Bienvenue à" par le moteur de calcul et la valeur calculée finale revient sous la forme "Bienvenue à Aspose.Cells."". Comme vous pouvez le voir dans un code que nous avons pas écrit notre fonction personnalisée n'importe où dans une feuille de calcul et elle est calculée directement par notre propre logique personnalisée.

### **Exemple de programmation**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Sortie console**

Vous trouverez ci-dessous la sortie de la console de l'exemple de code ci-dessus.

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Article associé**

{{% alert color="primary" %}}

[Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut de Aspose.Cells](/cells/fr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
