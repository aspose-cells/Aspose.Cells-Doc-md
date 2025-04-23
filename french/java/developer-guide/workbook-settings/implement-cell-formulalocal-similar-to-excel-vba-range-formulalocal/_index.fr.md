---
title: Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /fr/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Scénarios d'utilisation possibles**
Les formules Microsoft Excel peuvent avoir des noms différents selon la locale, la région ou la langue. Par exemple, la fonction *SUM* est appelée *SUMME* en *allemand*. Aspose.Cells ne peut pas fonctionner avec des noms de fonctions non anglais. En *VBA Microsoft Excel*, il existe une propriété *Range.FormulaLocal* qui renvoie le nom de la fonction selon sa langue ou région. Aspose.Cells offre également la propriété [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) à cette fin. Cependant, cette propriété ne fonctionnera que si vous implémentez la méthode [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-) 
## **Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal**
Le code suivant explique comment implémenter la méthode [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-). La méthode renvoie le nom local de la fonction standard. Si le nom de la fonction standard est *SUM*, elle renvoie *UserFormulaLocal_SUM*. Vous pouvez modifier le code selon vos besoins et renvoyer les noms de fonctions locaux corrects, par exemple, *SUM* est *SUMME* en *allemand* et *TEXT* est *ТЕКСТ* en *russe*. Veuillez également consulter la sortie console du code d'exemple ci-dessous à titre de référence.
## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Sortie console**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
