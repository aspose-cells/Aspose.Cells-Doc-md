---
title: Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /fr/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Scénarios d'utilisation possibles**

Les formules Microsoft Excel peuvent avoir des noms différents dans différentes langues ou régions. Par exemple, la fonction **SUM** est appelée **SUMME** en allemand. Aspose.Cells ne peut pas fonctionner avec des noms de fonction non anglais. En VBA Excel, il existe la propriété **Range.FormulaLocal** qui renvoie le nom de la fonction selon sa langue ou sa région. Aspose.Cells fournit également la propriété [**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal) à cette fin. Cependant, cette propriété ne fonctionnera que si vous implémentez [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) méthode.

## **Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal**

Le code d'exemple suivant explique comment implémenter la méthode [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname). La méthode renvoie le nom local de la fonction standard. Si le nom de la fonction standard est **SUM**, elle renvoie **UserFormulaLocal_SUM**. Vous pouvez modifier le code selon vos besoins et renvoyer les noms de fonction locaux corrects, par exemple **SUM** est **SUMME** en allemand et **TEXT** est **ТЕКСТ** en russe. Veuillez également consulter la sortie console du code d'exemple ci-dessous pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Sortie console**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
