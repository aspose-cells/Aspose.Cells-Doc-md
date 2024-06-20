---
title: Calcul direct de fonction personnalisée sans l écrire dans une feuille de calcul
type: docs
weight: 650
url: /fr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

{{% alert color="primary" %}} 

Cet article explique comment vous pouvez calculer directement vos fonctions personnalisées sans les écrire d'abord dans une feuille de calcul. Veuillez utiliser la méthode [Worksheet.calculateFormula(string formula, CalculationOptions opts)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) à cette fin.

{{% /alert %}} 
## **Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul**
Veuillez consulter le code d'exemple suivant qui illustre l'utilisation de cette méthode. Nous avons utilisé une fonction personnalisée appelée *MyCompany.CustomFunction()* et nous calculons sa valeur comme "Aspose.Cells." nous-mêmes, puis cette valeur est automatiquement concaténée avec la valeur de la cellule A1, qui est "Bienvenue à " par le moteur de calcul, et la valeur calculée finale retourne comme "Bienvenue à Aspose.Cells.". Comme vous pouvez le voir dans le code, nous n'avons pas écrit notre fonction personnalisée n'importe où dans une feuille de calcul et elle est calculée directement par notre propre logique personnalisée.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **Sortie console**
Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **Article connexe**
{{% alert color="primary" %}} 

- [Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut d'Aspose.Cells](/cells/fr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
