---
title: Renvoi d'une plage de valeurs à l'aide de AbstractCalculationEngine
description: Cet article présente un moteur de calcul abstrait qui renvoie une plage de valeurs dans Excel Microsoft à l'aide de la bibliothèque Aspose.Cells. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour obtenir une plage de valeurs et renvoyer le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, an abstract calculation engine that returns a series of values
type: docs
weight: 55
url: /fr/net/returning-a-range-of-values-using-abstractcalculationengine/
---
{{% alert color="primary" %}}

 Aspose.Cells fournit[**RésuméCalculMoteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) classe utilisée pour implémenter des fonctions définies par l'utilisateur ou personnalisées qui ne sont pas prises en charge par Microsoft Excel en tant que fonctions intégrées.

 Cet article explique comment renvoyer la plage de valeurs de[**RésuméCalculMoteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

 Le code suivant illustre l'utilisation de[**RésuméCalculMoteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) classe et renvoie la plage de valeurs via sa méthode.

Créez une classe avec une fonction *CalculateCustomFunction*. Cette classe implémente[**RésuméCalculMoteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

Utilisez maintenant la fonction ci-dessus dans votre programme

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
