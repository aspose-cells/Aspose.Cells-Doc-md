---
title: Renvoyer une plage de valeurs à l'aide de ICustomFunction
type: docs
weight: 50
url: /fr/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 La[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) est obsolète depuis la sortie de Aspose.Cells for Java 20.8. Veuillez utiliser le[**RésuméCalculMoteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) classer. L'utilisation de la[**RésuméCalculMoteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) classe est décrite dans l'article suivant.

[Retour d'une plage de valeurs à l'aide de AbstractCalculationEngine](/cells/fr/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells fournit[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)interface utilisée pour implémenter des fonctions définies par l'utilisateur ou personnalisées qui ne sont pas prises en charge par Microsoft Excel en tant que fonctions intégrées.

 Surtout lorsque vous implémentez le[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) méthode d'interface, vous devez renvoyer une seule valeur de cellule. Mais parfois, vous devez renvoyer une plage de valeurs. Cet article explique comment renvoyer la plage de valeurs de[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

 Le code suivant implémente[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)et renvoie la plage de valeurs via sa méthode.

 Créer une classe avec une fonction*CalculateCustomFunction*. Cette classe implémente[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Utilisez maintenant la fonction ci-dessus dans votre programme

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
