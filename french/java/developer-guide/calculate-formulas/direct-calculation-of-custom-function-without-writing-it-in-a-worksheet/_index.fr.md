---
title: Calcul direct de la fonction personnalisée sans l'écrire dans une feuille de calcul
type: docs
weight: 650
url: /fr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
{{% alert color="primary" %}} 

 Cet article explique comment calculer directement vos fonctions personnalisées sans les écrire au préalable dans une feuille de calcul. Veuillez utiliser le[Worksheet.calculateFormula (formule de chaîne, CalculationOptions opte)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) méthode à cet effet.

{{% /alert %}} 
## **Calcul direct de la fonction personnalisée sans l'écrire dans une feuille de calcul**
Veuillez consulter l'exemple de code suivant qui illustre l'utilisation de cette méthode. Nous avons utilisé une fonction personnalisée nommée*MyCompany.CustomFunction()*et nous calculons sa valeur comme "Aspose.Cells". par nous-mêmes, puis cette valeur est automatiquement concaténée avec la valeur de la cellule A1 qui est "Bienvenue à" par le moteur de calcul et la valeur calculée finale revient sous la forme "Bienvenue à Aspose.Cells.". Comme vous pouvez le voir dans un code, nous n'avons écrit notre fonction personnalisée nulle part dans une feuille de calcul et elle est calculée directement par notre propre logique personnalisée.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **Sortie console**
Vous trouverez ci-dessous la sortie de la console de l'exemple de code ci-dessus.

{{< highlight "java" >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **Article associé**
{{% alert color="primary" %}} 

- [Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut de Aspose.Cells](/cells/fr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
