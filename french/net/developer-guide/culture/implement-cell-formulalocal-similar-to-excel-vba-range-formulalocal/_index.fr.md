---
title: Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /fr/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **Scénarios d'utilisation possibles**

 Microsoft Les formules Excel peuvent avoir des noms différents selon les paramètres régionaux, les régions ou les langues. Par exemple,**SOMME**la fonction s'appelle**ÉTÉ** en allemand. Aspose.Cells ne peut pas fonctionner avec des noms de fonction non anglais. Dans Microsoft Excel VBA, il y a**Range.FormulaLocal**propriété qui renvoie le nom de la fonction selon sa langue ou sa région. Aspose.Cells fournit également[**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal)propriété à cet effet. Cependant, cette propriété ne fonctionnera que lorsque vous implémenterez[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)méthode.

## **Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal**

 L'exemple de code suivant explique comment implémenter[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) méthode. La méthode renvoie le nom local de la fonction standard. Si le nom de la fonction standard est**SOMME** , ça revient**UserFormulaLocal_SUM** Vous pouvez modifier le code selon vos besoins et renvoyer les noms de fonction locaux corrects, par exemple**SOMME** est**ÉTÉ** en allemand et**TEXTE** est**ТЕКСТ**en russe. Veuillez également consulter la sortie de la console de l'exemple de code ci-dessous pour référence.

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Sortie console**

{{< highlight "java" >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
