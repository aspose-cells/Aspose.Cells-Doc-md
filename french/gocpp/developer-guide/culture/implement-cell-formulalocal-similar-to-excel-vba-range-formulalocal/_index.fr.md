---
title: Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal avec Golang via C++
linktitle: Implémenter Cell.FormulaLocal
type: docs
weight: 30
url: /fr/go-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Apprenez comment implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal en utilisant Aspose.Cells avec Golang via C++.
---

## **Scénarios d'utilisation possibles**

Les formules Microsoft Excel peuvent avoir des noms différents dans différentes langues ou régions. Par exemple, la fonction **SUM** est appelée **SUMME** en allemand. Aspose.Cells ne peut pas fonctionner avec des noms de fonction non anglais. En VBA Excel, il existe la propriété **Range.FormulaLocal** qui renvoie le nom de la fonction selon sa langue ou sa région. Aspose.Cells fournit également la propriété [**Cell.FormulaLocal**](https://reference.aspose.com/cells/go-cpp/cell/getformulalocal/) à cette fin. Cependant, cette propriété ne fonctionnera que si vous implémentez [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/) méthode.

## **Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal**

Le code d'exemple suivant explique comment implémenter la méthode [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getlocalfunctionname/). La méthode renvoie le nom local de la fonction standard. Si le nom de la fonction standard est **SUM**, elle renvoie **UserFormulaLocal_SUM**. Vous pouvez modifier le code selon vos besoins et renvoyer les noms de fonction locaux corrects, par exemple **SUM** est **SUMME** en allemand et **TEXT** est **ТЕКСТ** en russe. Veuillez également consulter la sortie console du code d'exemple ci-dessous pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCellFormulalocalSimilarToExcelVbaRangeFormulalocal.go" >}}
## **Sortie console**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
