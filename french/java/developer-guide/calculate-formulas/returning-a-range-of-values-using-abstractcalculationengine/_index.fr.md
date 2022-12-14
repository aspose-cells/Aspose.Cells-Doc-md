---
title: Retour d'une plage de valeurs à l'aide de AbstractCalculationEngine
type: docs
weight: 275
url: /fr/java/returning-a-range-of-values-using-abstractcalculationengine/
---
{{% alert color="primary" %}}

 Aspose.Cells fournit[**RésuméCalculMoteur**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) classe qui est utilisée pour implémenter des fonctions définies par l'utilisateur ou personnalisées qui ne sont pas prises en charge par Microsoft Excel en tant que fonctions intégrées.

 Cet article explique comment renvoyer la plage de valeurs de[**RésuméCalculMoteur**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{% /alert %}}

 Le code suivant illustre l'utilisation du[**RésuméCalculMoteur**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)et renvoie la plage de valeurs via sa méthode.

Créer une classe avec une fonction*CalculateCustomFunction* . Cette classe s'étend[**RésuméCalculMoteur**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Utilisez maintenant la fonction ci-dessus dans votre programme.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ReturningRangeOfValues-1.java" >}}
