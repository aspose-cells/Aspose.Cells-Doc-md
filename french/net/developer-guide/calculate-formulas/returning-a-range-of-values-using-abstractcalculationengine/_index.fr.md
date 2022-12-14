---
title: Retour d'une plage de valeurs à l'aide de AbstractCalculationEngine
type: docs
weight: 55
url: /fr/net/returning-a-range-of-values-using-abstractcalculationengine/
---
{{% alert color="primary" %}}

 Aspose.Cells fournit[**RésuméCalculMoteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) classe qui est utilisée pour implémenter des fonctions définies par l'utilisateur ou personnalisées qui ne sont pas prises en charge par Microsoft Excel en tant que fonctions intégrées.

 Cet article explique comment renvoyer la plage de valeurs de[**RésuméCalculMoteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

 Le code suivant illustre l'utilisation du[**RésuméCalculMoteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) classe et renvoie la plage de valeurs via sa méthode.

Créer une classe avec une fonction*CalculateCustomFunction*. Cette classe implémente[**RésuméCalculMoteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

Utilisez maintenant la fonction ci-dessus dans votre programme

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
